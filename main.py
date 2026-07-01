import asyncio
import io
import json
import os

import httpx
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pypdf import PdfReader

app = FastAPI(title="Reeds Jobs API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

GREENHOUSE_BOARDS = [
    "riskified",
    "fireblocks",
    "pagayais",
    "gongio",
    "lightricks",
    "similarweb",
    "melio",
    "wizinc",
    "yotpo",
    "catonetworks",
]
GREENHOUSE_URL = "https://boards-api.greenhouse.io/v1/boards/{token}/jobs?content=true"

GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
)
RANK_BATCH_SIZE = 30
RANK_MAX_CONCURRENCY = 5


async def fetch_board(client: httpx.AsyncClient, token: str) -> list[dict]:
    """Fetch all jobs for a single Greenhouse board and tag them with the company."""
    response = await client.get(GREENHOUSE_URL.format(token=token))
    response.raise_for_status()
    data = response.json()
    jobs = []
    for job in data.get("jobs", []):
        location = job.get("location") or {}
        jobs.append(
            {
                "title": job.get("title"),
                "location": location.get("name"),
                "apply_url": job.get("absolute_url"),
                "company": token,
            }
        )
    return jobs


async def fetch_all_jobs(client: httpx.AsyncClient) -> list[dict]:
    results = await asyncio.gather(
        *(fetch_board(client, token) for token in GREENHOUSE_BOARDS),
        return_exceptions=True,
    )
    jobs: list[dict] = []
    for token, result in zip(GREENHOUSE_BOARDS, results):
        if isinstance(result, Exception):
            raise HTTPException(
                status_code=502,
                detail=f"Failed to fetch jobs for board '{token}': {result}",
            )
        jobs.extend(result)
    return jobs


@app.get("/jobs")
async def get_jobs() -> dict:
    """Fetch jobs from all configured Greenhouse boards concurrently and combine them."""
    async with httpx.AsyncClient(timeout=30.0) as client:
        jobs = await fetch_all_jobs(client)
    return {"count": len(jobs), "jobs": jobs}


async def score_batch(
    client: httpx.AsyncClient,
    api_key: str,
    cv: str,
    role: str,
    batch: list[dict],
    start_idx: int,
    semaphore: asyncio.Semaphore,
) -> list[dict]:
    """Ask Gemini to score a batch of jobs against the CV + target role."""
    jobs_desc = "\n".join(
        f"{start_idx + i}. [{j['company']}] {j['title']} — {j['location'] or 'N/A'}"
        for i, j in enumerate(batch)
    )
    prompt = (
        "You are a career-fit scoring assistant. Given a candidate CV and a target role, "
        "score each listed job 0-100 for how well it fits the candidate and target role, "
        "and write a one-sentence reason grounded in the CV.\n\n"
        f"Candidate CV:\n{cv}\n\n"
        f"Target role: {role}\n\n"
        f"Jobs:\n{jobs_desc}\n\n"
        'Return ONLY a JSON array. Each element must be '
        '{"index": <int>, "score": <int 0-100>, "reason": "<one short sentence>"}. '
        "Include every listed index exactly once."
    )
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseMimeType": "application/json",
            "temperature": 0.2,
        },
    }
    async with semaphore:
        response = await client.post(
            GEMINI_URL.format(model=GEMINI_MODEL),
            params={"key": api_key},
            json=payload,
        )
    response.raise_for_status()
    data = response.json()
    text = data["candidates"][0]["content"]["parts"][0]["text"]
    parsed = json.loads(text)
    if not isinstance(parsed, list):
        raise ValueError("Gemini response is not a JSON array")
    return parsed


def extract_cv_text(filename: str, data: bytes) -> str:
    """Extract plain text from an uploaded CV; supports PDF and plain text."""
    name = (filename or "").lower()
    if name.endswith(".pdf") or data[:4] == b"%PDF":
        try:
            reader = PdfReader(io.BytesIO(data))
            parts = [page.extract_text() or "" for page in reader.pages]
            text = "\n".join(parts).strip()
        except Exception as exc:
            raise HTTPException(status_code=400, detail=f"Failed to parse PDF: {exc}")
        if not text:
            raise HTTPException(status_code=400, detail="Could not extract text from PDF.")
        return text
    try:
        return data.decode("utf-8", errors="ignore").strip()
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Failed to read CV: {exc}")


@app.post("/rank")
async def rank_jobs(
    cv: UploadFile = File(...),
    role: str = Form(...),
) -> dict:
    """Rank every job by fit against the uploaded CV (PDF or text) and target role."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="GEMINI_API_KEY environment variable is not set.",
        )

    cv_bytes = await cv.read()
    if not cv_bytes:
        raise HTTPException(status_code=400, detail="CV file is empty.")
    cv_text = extract_cv_text(cv.filename or "", cv_bytes)

    async with httpx.AsyncClient(timeout=120.0) as client:
        jobs = await fetch_all_jobs(client)

        semaphore = asyncio.Semaphore(RANK_MAX_CONCURRENCY)
        batch_tasks = [
            score_batch(
                client, api_key, cv_text, role, jobs[i : i + RANK_BATCH_SIZE], i, semaphore
            )
            for i in range(0, len(jobs), RANK_BATCH_SIZE)
        ]
        batch_results = await asyncio.gather(*batch_tasks, return_exceptions=True)

    scores: dict[int, tuple[int, str]] = {}
    errors: list[str] = []
    for res in batch_results:
        if isinstance(res, Exception):
            errors.append(str(res))
            continue
        for item in res:
            idx = item.get("index")
            if not isinstance(idx, int) or idx < 0 or idx >= len(jobs):
                continue
            try:
                score = int(item.get("score", 0))
            except (TypeError, ValueError):
                score = 0
            score = max(0, min(100, score))
            reason = str(item.get("reason", "")).strip()
            scores[idx] = (score, reason)

    if not scores:
        raise HTTPException(
            status_code=502,
            detail=f"Ranking failed: {errors[0] if errors else 'no scores returned'}",
        )

    ranked = []
    for i, job in enumerate(jobs):
        score, reason = scores.get(i, (0, "Not scored"))
        ranked.append(
            {
                "title": job["title"],
                "company": job["company"],
                "location": job["location"],
                "apply_url": job["apply_url"],
                "score": score,
                "reason": reason,
            }
        )
    ranked.sort(key=lambda j: j["score"], reverse=True)

    return {"count": len(ranked), "jobs": ranked}
