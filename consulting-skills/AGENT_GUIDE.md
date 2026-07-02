# Senior Consultant Agent — Deployment & Usage Guide

One agent, three packagings, already in this repo:

| File | Use on |
|---|---|
| `.claude/agents/senior-consultant.md` | **Claude Code** (subagent — active in this repo now) |
| `consulting-skills/senior-consultant/SKILL.md` | **Claude.ai / Claude Opus** (upload as a Skill), **ChatGPT**, **Codex** |
| `consulting-skills/PROMPT_PLAYBOOK.md` §0 | Universal operating prompt if you can't install anything |

What it is: a single system prompt that hard-codes the full MBB operating system — SCQA framing, MECE issue trees, Day-1 hypotheses, 80/20 analysis planning, triangulated market sizing, valuation discipline (WACC build, terminal cross-checks, returns bridges), synthesis-not-summary, Pyramid-Principle delivery, red-team/pre-mortem passes — plus hard anti-error rules: evidence tagging ([FACT]/[INFERENCE]/[ASSUMPTION]/[ESTIMATE]/[MEMORY]), no unsourced numbers, no fabricated citations, all multi-step math executed in code, sanity checks against base rates, and mandatory confidence + kill conditions on every recommendation.

---

## 1. Deploy

### Claude Code (best experience — it can compute, search, and build files)
Already live in this repo. To make it available in every project:
```bash
cp .claude/agents/senior-consultant.md ~/.claude/agents/
```
Invoke explicitly: *"Use the senior-consultant agent to …"* — or let Claude auto-delegate when a task matches its description. For maximum power, also install the Tier-1 skills (see `README.md`): the agent is written to route to `/dcf`, `/comps`, `/lbo`, `/ic-memo`, document/PPTX skills, and web search when they're installed.

### Claude.ai / Claude Opus (paid plans)
Zip the folder and upload:
```bash
cd consulting-skills && zip -r senior-consultant.zip senior-consultant/
```
Settings → Capabilities → Skills → upload. Enable web search in the conversation — the agent's fact protocol depends on retrieval for time-sensitive numbers.

### ChatGPT
Create a **Project** (or Custom GPT) → paste the body of `senior-consultant/SKILL.md` (everything below the second `---`) into its instructions. Turn web browsing on. Note: ChatGPT can't run this repo's tool-routing lines; they degrade gracefully (the agent falls back to its built-in methodology).

### Codex
Paste the SKILL.md body into `AGENTS.md` at your repo root, or install as a skill folder if your Codex version supports agent skills (`npx skills add` targets Codex/Cursor/Gemini CLI too).

---

## 2. How to instruct it — the Task Brief

The agent is built so that **your only job is a clear brief**. Use this template (fields you skip become stated assumptions):

```
TASK: [what you want done — one sentence]
CLIENT/CONTEXT: [company or situation, size, geography, ownership]
DECISION: [what decision this work informs, and who makes it]
DELIVERABLE: [Quick Structure | Working Analysis | Client Deliverable: memo / deck storyline / model]
AUDIENCE: [board / CEO / IC / internal team]
DEPTH/DEADLINE: [quick take vs. full workup]
DATA: [attach files, paste numbers, or say "search for it" / "none — structure only"]
CONSTRAINTS: [scope limits, things already decided, politics]
HOW I WANT IT: [any format/style specifics]
```

### Worked examples

**Market sizing:**
```
TASK: Size the market for at-home diagnostic testing kits.
CLIENT/CONTEXT: PE fund evaluating a platform acquisition; targets are US + UK.
DECISION: Whether the market supports a 3x revenue underwriting case by 2030.
DELIVERABLE: Working Analysis. AUDIENCE: deal team.
DATA: Search for it; cite everything.
HOW I WANT IT: TAM/SAM/SOM with both sizing methods reconciled, sensitivity on the 3 weakest assumptions.
```

**Strategy:**
```
TASK: Should we enter the SMB segment with a self-serve tier?
CLIENT/CONTEXT: $80M ARR B2B SaaS, enterprise sales-led, flat NRR, EU-based.
DECISION: Go/no-go at next month's exec offsite. DELIVERABLE: Client Deliverable — decision memo.
CONSTRAINTS: No M&A; engineering capacity capped at 2 squads.
```

**Financial:**
```
TASK: DCF and comps valuation of [TICKER].
DECISION: Initiate a position or pass. DELIVERABLE: Working Analysis.
DATA: Pull the latest filings/figures via available tools; flag anything you had to take from memory.
HOW I WANT IT: WACC build shown, terminal value both ways, football field vs. 8-10 justified peers.
```

**Due diligence:**
```
TASK: Commercial DD red-flag screen on the attached CIM.
DECISION: Proceed to full diligence or drop. DELIVERABLE: Working Analysis, then /ic-memo format summary.
DATA: [attach CIM] + search for market/competitor validation.
```

**Deck production:**
```
TASK: Turn the attached analysis into a 12-slide steering-committee deck storyline.
AUDIENCE: CFO + COO, skeptical of the initiative.
DELIVERABLE: Client Deliverable — deck storyline, then generate the PPTX.
HOW I WANT IT: Action titles carry the full argument; every slide has an exhibit spec.
```

**Pressure-testing (use it against your own work):**
```
TASK: Red-team this strategy document as a skeptical senior partner. [attach]
DELIVERABLE: Working Analysis — the 5 weakest points ranked by (impact if wrong × likelihood wrong),
the cheapest test for each, and the pre-mortem: it's 18 months later and this failed — why?
```

---

## 3. Getting maximum accuracy out of it

1. **Give it retrieval.** The agent's no-unsourced-numbers rule needs somewhere to get numbers: web search on Claude.ai/ChatGPT; the financial-services data connectors or Octagon skills in Claude Code. With no retrieval, it will still work — but it will (correctly) mark the fact base as unverified memory and tell you what to verify. That's by design.
2. **Run it on a top reasoning model** (Opus-class or equivalent). The protocol assumes a model strong enough to follow 10 simultaneous disciplines; on weak models you get well-formatted mediocrity.
3. **Trust the tags.** [FACT] items carry citations you can click and check. [MEMORY] and [ESTIMATE] items are the ones to verify before a client sees them — the agent surfaces exactly where checking effort should go.
4. **Use the kill conditions.** Every recommendation ends with "this flips if…". Those are your diligence checklist.
5. **Keep a human signature.** No agent — this one included — can guarantee zero errors; what this one guarantees is that every claim is *checkable*: tagged, sourced, or derived, with the weakest link flagged. Final work product still gets a professional's sign-off before it goes to a client. That is also exactly how MBB firms operate: analysis by the team, signature by the partner.
