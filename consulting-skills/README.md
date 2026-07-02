# The Definitive Guide to Consulting-Grade AI Skills (SKILL.md)

**Curated & verified: July 2026.** Every repository below was individually verified — existence, star count, release recency, file structure, and (for the top picks) the actual `SKILL.md` content was read and assessed for methodological depth (MECE, hypothesis-driven problem solving, Pyramid Principle, evidence discipline). Marketing claims in READMEs were **not** taken at face value.

**Who this is for:** consulting professionals who want Claude (Opus / Claude Code / Claude.ai), ChatGPT, or Codex to work at the level of a senior MBB analyst across **market research, market analysis, strategy consulting, management consulting, and financial consulting**.

---

## How rankings were done

| Criterion | What was checked |
|---|---|
| Depth | Actual SKILL.md content read — word count, routing logic, output contracts, worked examples |
| Methodology | MECE, issue trees, hypothesis trees, Pyramid Principle/SCQA, 80/20, evidence labeling, triangulated market sizing |
| Maintenance | Last release/commit, versioning, open issues |
| Deliverables | Can it produce client-ready output (PPTX decks, Excel models, memos)? |
| Provenance | Author credentials, official vs. community, license |
| Portability | Claude.ai upload, Claude Code plugin, Codex/ChatGPT adaptability |

---

## TIER 1 — Install these first (the backbone)

### 1. `anthropics/financial-services` — **the single best financial-consulting asset on GitHub**
- **Link:** https://github.com/anthropics/financial-services
- **Verified:** 32.9k ★ · Apache 2.0 · official Anthropic · actively maintained
- **What it is:** Anthropic's reference implementation for financial-services agents. This is what banks actually deploy.
- **Contents:**
  - **Core skill bundle `financial-analysis`:** `/comps` (trading comps), `/dcf` (DCF with WACC + sensitivities), `/lbo`, `/3-statement-model`, `/debug-model` (Excel formula audit, hardcode detection), deck-refresh, `ib-check-deck` (presentation QC)
  - **Investment banking:** `/one-pager`, `/cim`, `/teaser`, `/buyer-list`, `/merger-model` (accretion/dilution), `/process-letter`, `/deal-tracker`
  - **Equity research:** `/earnings`, `/earnings-preview`, `/initiate`, `/model-update`, `/sector`, `/thesis`
  - **Private equity:** `/source`, `/screen-deal`, `/dd-checklist`, `/ic-memo`, `/portfolio`, `/value-creation` (100-day plans), `/ai-readiness`
  - **Named agents:** Pitch Agent, Market Researcher (industry overviews, competitive landscape, peer comps), Earnings Reviewer, Model Builder, Meeting Prep Agent
  - **11 real-data MCP connectors:** FactSet, S&P Global, Morningstar, PitchBook, LSEG, Moody's, Daloopa, MT Newswires, Aiera, Chronograph, Egnyte/Box — **this is the anti-hallucination layer** (see §Accuracy below)
- **Install (Claude Code):**
  ```bash
  claude plugin marketplace add anthropics/financial-services
  claude plugin install financial-analysis@claude-for-financial-services
  claude plugin install investment-banking@claude-for-financial-services
  claude plugin install equity-research@claude-for-financial-services
  claude plugin install private-equity@claude-for-financial-services
  claude plugin install market-researcher@claude-for-financial-services
  ```
- **Install (Cowork/Claude.ai plugins):** Settings → Plugins → Add plugin → paste the repo URL.

### 2. `anthropics/skills` — the deliverables engine (PPTX / XLSX / DOCX / PDF)
- **Link:** https://github.com/anthropics/skills
- **Verified:** 158k ★ · document skills are the same reference implementations that power Claude's own document features
- **Why a consultant needs it:** every engagement ends in a deck or a model. These skills make Claude produce real `.pptx` decks and `.xlsx` models, not markdown approximations. Also contains the official Agent Skills **spec** and template — the standard the other repos follow.
- **Install (Claude Code):**
  ```bash
  /plugin marketplace add anthropics/skills
  /plugin install document-skills@anthropic-agent-skills
  ```

---

## TIER 2 — Senior-consultant reasoning layer (strategy & management consulting)

### 3. `DogInfantry/claude-skill-management-consultant-B1` — the deepest MBB-style skill verified
- **Link:** https://github.com/DogInfantry/claude-skill-management-consultant-B1
- **Verified:** v1.2.1 (April 2026) · **118 reference modules** across 5 knowledge pillars · SKILL.md is ~8–9k words with a 40+ row conditional routing matrix
- **First-hand content assessment:** hierarchical 7-step engagement workflow (problem statement → structure → analysis → synthesis → quantification → action → negotiation); prescriptive Pyramid-Principle communication rules; 9 industry vertical files (healthcare, fintech, energy, tech, CPG, industrial, public sector, real estate, hospitality); specialist modules for due diligence, post-merger integration, pricing, org design; M&A case library; full MBB case-interview coaching (McKinsey interviewer-led, BCG candidate-led, Bain collaborative). Explicitly built from public sources only — no proprietary firm material.
- **Weaknesses (honest):** depends on its reference files being loaded alongside SKILL.md; its "demand archetypes" are tuned to 2025–26 market conditions; light on uncertainty quantification.
- **Install:** download `skill/SKILL.md` **and the entire `skill/references/` folder** (the skill is a routing hub — without references it degrades). Copy to `~/.claude/skills/management-consultant/` or zip and upload to Claude.ai.
- Note: a near-identical mirror (`charlie989898/-mbb-management-consultant-claude-skill`) appears in search results but was unreachable when verified — use the DogInfantry repo.

### 4. `gcamilo/management-consulting` — the most disciplined single-file skill (eval-backed)
- **Link:** https://github.com/gcamilo/management-consulting
- **Verified:** 37 ★ · 22 files, ~5,700 lines · `SKILL.md` at repo **root**, default branch **master**
- **Why it stands out:** the only consulting skill found with **published evaluations** (+1.5 pt average over baseline across standard/ambiguous/adversarial prompts; +2.2 on process discipline). 42 frameworks across 7 categories (Five Forces, VRIO, Wardley Mapping, RAPID, JTBD, profit trees, TAM/SAM/SOM, unit economics…). Three response modes — **Quick Structure**, **Full Case**, **Client Deliverable**. Enforces **evidence labeling (Fact / Inference / Assumption / Estimate)**, devil's-advocate + pre-mortem steps, and a 9-point output contract. This evidence-labeling discipline is the best hallucination control in any community skill reviewed.
- **Install:**
  ```bash
  npx skills add gcamilo/management-consulting
  # or: git clone https://github.com/gcamilo/management-consulting && cp -r management-consulting ~/.claude/skills/
  ```

### 5. `sruthir28/enterprise-ai-skills` — ex-McKinsey consultant's toolkit (best deck pipeline)
- **Link:** https://github.com/sruthir28/enterprise-ai-skills
- **Verified:** 94 ★ · MIT · updated May 2026 · author Sruthi Chintakunta, former McKinsey consultant
- **Contents (verified paths, root-level folders):** `scpr-framework/`, `issue-tree-builder/`, `hypothesis-tree/`, `synthesis/`, `prioritization/`, `ai-use-case-scorer/`, `data-insights-simple/`, `decision-memo-builder/`, `top-down-memo/`, `storyline-builder/`, `meeting-prep-kit/`, `stakeholder-map/`, `workshop-designer/` — plus `mckinsey-charts/` (waterfall/marimekko-style charting), `deck-pipeline/` (storyline → full PPTX via python-pptx), `mckinsey-critic/` (QC agent that red-teams your output).
- **Killer feature:** skills **compose**: Issue Tree → Hypothesis Tree → Synthesis → Decision Memo → Deck Pipeline → McKinsey Critic is a complete engagement production line. Ships ready-made `.skill` files for direct Claude.ai upload.
- **Install:** clone into a Claude Code project (auto-loads), or upload the `.skill` files at claude.ai → Settings → Capabilities → Skills. Deck generation needs Python 3.9+ with `python-pptx`.

### 6. `aapersh/strategy-skills-for-claude` — broadest strategy coverage (21 skills, 6 domains)
- **Link:** https://github.com/aapersh/strategy-skills-for-claude
- **Verified:** 224 ★ · 21 skills in `skills/01…06` folders (diagnosis & framing; market & competitive intelligence; strategic choice & economics; operating model & execution; risk/performance/value governance; alignment & executive communication)
- **First-hand content assessment (honest):** each skill is a **compact template (~250 words)** — clean workflow, enforced output tables, MECE standards ("separate market attractiveness from right to win"), requires ≥2 sizing approaches with cross-checks. But: no worked examples, no data-source guidance, thin on TAM/SAM/SOM mechanics. **Use it for breadth and output structure, paired with Tier-1/Tier-2 skills for depth.** Standouts: `profit-pool-analysis`, `war-gaming`, `competitive-intel`, `decision-memo`, `assumption-audit`.
- **Install:** copy any file to a folder as `SKILL.md`, upload to Claude.ai, or drop folders into `~/.claude/skills/`.

### 7. `yoichiojima-2/consultant` — framework library + case-interview trainer
- **Link:** https://github.com/yoichiojima-2/consultant
- **Verified:** 28 ★ · MIT · v1.1.0 (June 2026) · 50+ frameworks (MECE, Pyramid, 7S, Five Forces, BCG Matrix, Blue Ocean, market sizing, M&A, NPV/IRR, Lean/Six Sigma) · commands `/consult`, `/analyze`, `/case-practice`
- **Install:** `/plugin marketplace add yoichiojima-2/consultant` → `/plugin install consulting@consultant`

---

## TIER 3 — Market research & market analysis specialists

### 8. `alirezarezvani/claude-skills` — the enterprise mega-library (354 skills)
- **Link:** https://github.com/alirezarezvani/claude-skills
- **Verified:** 19.7k ★ · MIT · v2.9.0 (May 28, 2026) · 593 stdlib-only Python CLI tools · security-audited skills
- **Relevant bundles:** **Research Operations** (market-research, product-research, research-finance), **C-Level Advisory** (68 skills incl. `c-level-advisor/skills/competitive-intel/`), **Finance** (DCF analysis, SaaS metrics, investment advisory), **Commercial** (pricing strategy, deal desk, channel economics, RFP responses).
- **Why it matters for you:** ships **conversion scripts for 13 platforms including Codex, Cursor, and Gemini CLI** — the cleanest path to reusing SKILL.md files outside Claude.
- **Install:** `/plugin marketplace add alirezarezvani/claude-skills` then install the bundles you need (e.g. `c-level-skills@claude-code-skills`).

### 9. `ishwarjha/claude-marketing-research-skill` — customer/competitor research system
- **Link:** https://github.com/ishwarjha/claude-marketing-research-skill
- **Verified:** 32 ★ · Apache 2.0 · v1.0.0 (March 2026)
- **Contents:** 6 modules — competitor landscape mapping & gap analysis, product feature-benefit analysis, avatar profiling (desires/problems/conflict), market-awareness staging, 4 value propositions with usage matrices, psychological mental models. Runs an intake interview, then executes modules automatically; outputs ~300-line research documents.
- **Install:** upload `.skill` file to Claude.ai, or clone into Claude Code, or paste SKILL.md contents into any LLM.

### 10. `OctagonAI/skills` — real-data financial & market research (anti-hallucination pick)
- **Link:** https://github.com/OctagonAI/skills
- **Verified:** 124 ★ · MIT · requires **free** Octagon API key (octagonai.co)
- **Contents:** master skills (financial-analyst, earnings-analyst, sec-analyst, market-analyst) over live data: SEC 10-K/10-Q risk-factor & MD&A extraction, earnings-call transcript parsing + guidance extraction, analyst estimates, price targets, sector P/E — **grounded in retrieved filings, not model memory**.
- **Install:** `npx skills add OctagonAI/skills`

### 11. `birne-sk/claude-skills` — MBB-style market research with PPTX output
- **Link:** https://github.com/birne-sk/claude-skills
- **Verified:** 16 ★ · single-commit, early-stage · 4-level pyramid analysis + PPTX generation under `.claude/skills/market-research/`
- **Verdict:** promising methodology, immature repo. Watch, don't depend on.

---

## TIER 4 — Financial consulting depth

### 12. `JoelLewis/finance_skills` — 81 skills across 7 financial-services domains
- **Link:** https://github.com/JoelLewis/finance_skills
- **Verified:** 145 ★ · MIT · plugins: core (returns, TVM, statistics), wealth-management, compliance (KYC/AML/fiduciary/suitability), advisory-practice, trading-operations, client-operations, data-integration
- **Install:** `npx skills add JoelLewis/finance_skills` or `./install.sh --plugin wealth-management`

### 13. `anthropics/claude-cookbooks` → `skills/custom_skills/creating-financial-models/SKILL.md`
- **Link:** https://github.com/anthropics/claude-cookbooks/blob/main/skills/custom_skills/creating-financial-models/SKILL.md
- Official Anthropic worked example of a financial-modeling skill — also the best template for writing your own firm-specific skills.

---

## Directories for ongoing discovery
- https://github.com/VoltAgent/awesome-agent-skills — 1,000+ skills incl. official ones from Anthropic, Vercel, Stripe, Cloudflare; cross-agent (Claude Code, Codex, Gemini CLI, Cursor)
- https://github.com/ComposioHQ/awesome-claude-skills and https://github.com/travisvn/awesome-claude-skills — curated lists
- https://github.com/VoltAgent/awesome-claude-code-subagents — `market-researcher.md`, `competitive-analyst.md` subagent definitions

---

## Platform compatibility matrix

| Platform | How to attach skills |
|---|---|
| **Claude Opus 4.8 (claude.ai)** | Settings → Capabilities → Skills → upload folder/zip containing `SKILL.md` (paid plans). `.skill` files upload directly. |
| **Claude Code** | `/plugin marketplace add <repo>` + `/plugin install`, or copy folders into `~/.claude/skills/` (global) / `.claude/skills/` (project). Auto-triggers on matching tasks. |
| **Claude API / Agent SDK** | Skills API (see anthropics/skills → spec/) |
| **ChatGPT (incl. Thinking models)** | No native SKILL.md support. Paste SKILL.md body into a **Project's custom instructions** or a Custom GPT's instructions. One skill per project works best; strip the YAML frontmatter. |
| **Codex** | Supports agent-skill folders; the `npx skills add` CLI and `alirezarezvani/claude-skills` conversion scripts target Codex/Cursor/Gemini CLI directly. Alternatively paste into `AGENTS.md`. |

---

## Accuracy & hallucination control (read this — it's the part that actually matters)

No SKILL.md can make any model hallucination-free. What the best ones do is force **process discipline** so errors become visible and checkable. To operate at true senior-analyst accuracy:

1. **Ground numbers in retrieved data, never model memory.** Market sizes, multiples, growth rates → require live sources: web search on Claude.ai, the 11 MCP data connectors in `anthropics/financial-services` (FactSet, S&P, PitchBook, LSEG…), or Octagon's SEC/earnings retrieval. If a number can't be sourced, it must be labeled an **Estimate** with stated methodology.
2. **Require evidence labeling.** `gcamilo/management-consulting` enforces Fact / Inference / Assumption / Estimate tagging natively; add it to every other skill via the Universal Operating Prompt in `PROMPT_PLAYBOOK.md`.
3. **Triangulate all market sizing** — top-down and bottom-up must be computed independently and reconciled; a >30% divergence gets flagged, not averaged away.
4. **Red-team every deliverable** with `mckinsey-critic` (enterprise-ai-skills) or a pre-mortem pass before it goes to a client.
5. **Human sign-off** — Anthropic's own financial-services repo ships with this disclaimer for a reason: agents draft work product; a professional signs it.

---

## Files in this folder
- `PROMPT_PLAYBOOK.md` — the optimal prompts for every skill above, plus chained engagement workflows (market entry study, commercial due diligence, board deck production)
- `download-skills.sh` — one-shot script to download all recommended skills to your machine (run locally, requires git + internet)
