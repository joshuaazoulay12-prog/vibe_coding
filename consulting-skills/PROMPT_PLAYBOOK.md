# Prompt Playbook — Consulting Skills at Senior-MBB Level

Optimal prompts for each recommended skill, when to use which, and full chained-engagement workflows. Prompts are written for Claude (Opus 4.8 / Claude Code); §6 covers adapting them for ChatGPT and Codex.

---

## 0. The Universal Operating Prompt (use with EVERY skill)

Paste this once at the start of any consulting session (or into project instructions). It layers evidence discipline on top of whatever skill is active — this is what separates senior-analyst output from confident nonsense:

```
Operating standards for this engagement:
1. EVIDENCE DISCIPLINE — Tag every material claim as [FACT] (sourced, cite it),
   [INFERENCE] (derived, show the logic), [ASSUMPTION] (state basis and
   sensitivity), or [ESTIMATE] (show the calculation). Never present an
   estimate as a fact.
2. NO UNSOURCED NUMBERS — Market sizes, growth rates, multiples, and shares
   must come from retrieved sources or explicit bottom-up calculation. If you
   cannot source or derive a number, say so and propose how we would get it.
3. TRIANGULATE SIZING — Any market sizing needs independent top-down AND
   bottom-up builds. Reconcile them; if they diverge >30%, flag it and explain
   which is more reliable and why. Do not average away the gap.
4. MECE OR DIE — Every decomposition must be mutually exclusive, collectively
   exhaustive. State the cut logic (by customer, by product, by value chain…).
5. ANSWER FIRST — Pyramid Principle: governing thought up front, 2–4 MECE
   supporting arguments, evidence beneath. SCQA for framing.
6. SO WHAT — Every exhibit and section ends with the implication for the
   client's decision, not a restatement of the data.
7. CONFIDENCE + KILL CONDITIONS — End every recommendation with a confidence
   level (H/M/L + why) and the 2–3 findings that would reverse it.
8. PRE-MORTEM — Before finalizing, spend one pass attacking your own answer:
   what would a skeptical partner tear apart?
```

---

## 1. Strategy & management consulting prompts

### 1.1 `DogInfantry/claude-skill-management-consultant-B1` (MBB consultant, 118 modules)
**Activate with:** `Act as my management consultant.` (its documented trigger)

**When:** full ambiguous business problems; anything you'd staff an engagement team on; case-interview prep.

**Optimal prompt — profitability / diagnostic:**
```
Act as my management consultant.

Client: [company, ~revenue, geography, ownership]
Situation: EBITDA margin fell from [X]% to [Y]% over [period] while revenue
grew [Z]%. Board wants a diagnostic and turnaround options in 6 weeks.
Data available: [P&L by segment / pricing files / none yet].

Run your full workflow: problem statement, MECE issue tree with your Day-1
hypothesis marked, the 5 analyses you'd run first (80/20), data requests,
and a straw-man SCQA storyline for the week-2 steering committee.
Load your relevant industry reference for [sector].
```

**Optimal prompt — market entry:**
```
Act as my management consultant. Engagement: should [client] enter the
[market] in [geography]?
Structure as: market attractiveness (size via two independent methods,
growth, profit pools) | right to win (assets, capabilities vs. incumbents)
| entry modes (build/buy/partner with economics of each) | risks and kill
conditions. End with a recommendation at 70% confidence and what you'd
need to reach 90%.
```

**Optimal prompt — case interview practice:**
```
Act as my management consultant. Run me through a McKinsey-style
interviewer-led case on [topic]. Give me the prompt, wait for my structure,
push back like a real interviewer, include a quant section, and score me at
the end on structure, hypothesis, quant, synthesis, and recommendation.
```

### 1.2 `gcamilo/management-consulting` (42 frameworks, 3 modes)
**When:** you want speed control. It has three explicit modes — invoke them by name.

- **Exploring an idea (fast):** `Quick Structure: how should I think about [problem]?`
- **Real analysis:** `Full Case: [problem + context + data]. Label all evidence.`
- **Client-ready output:** `Client Deliverable: turn this analysis into a stakeholder-ready
  recommendation for [audience]. Apply your full output contract.`

**Optimal prompt:**
```
Full Case. Client context: [2–3 sentences]. Question: [decision to make].
Constraints: [budget/time/politics]. Pick the 2–3 most appropriate
frameworks from your library and say why you rejected the obvious
alternatives. Run evidence labeling throughout, then the devil's-advocate
and pre-mortem passes before your final recommendation.
```

### 1.3 `sruthir28/enterprise-ai-skills` (ex-McKinsey production line)
**When:** producing actual work product — memos, storylines, decks. Chain the skills explicitly:

```
Step 1 — Use issue-tree-builder: decompose "[client question]" into a MECE
issue tree, 3 levels deep, with the killer branch flagged.
Step 2 — Use hypothesis-tree: convert the priority branches into testable
hypotheses with data requirements and pass/fail criteria.
Step 3 — [after analysis] Use synthesis: turn these findings into insights
(so-whats), not summaries.
Step 4 — Use storyline-builder: build the SCQA deck storyline, one
governing thought per slide, action titles only.
Step 5 — Use deck-pipeline: generate the PPTX.
Step 6 — Use mckinsey-critic: red-team the deck. Fix everything it flags.
```

**Decision memo (fastest high-value single skill):**
```
Use decision-memo-builder. Decision: [X vs Y by date]. Audience: [CEO/board].
Context: [1 paragraph]. Constraints: [...]. Write the memo top-down:
recommendation first, then the case, then risks with mitigations, then the
ask. One page.
```

### 1.4 `aapersh/strategy-skills-for-claude` (21 skills — invoke one per task)
**When:** you know exactly which module of an engagement you're in. Name the skill:

- `Use the profit-pool-analysis skill on the [industry] value chain in [geo]. Where is margin concentrated today and where is it migrating?`
- `Use the war-gaming skill: we launch [move]; simulate [competitor A] and [B] responses over 3 rounds, with our counter-moves.`
- `Use the assumption-audit skill on this strategy: [paste]. Rank assumptions by (impact if wrong × probability of being wrong) and design the cheapest test for the top 3.`
- `Use the decision-memo skill to convert this analysis into a one-page written decision for the exec committee.`

*(These are compact templates — pair with the Universal Operating Prompt and web search for depth.)*

---

## 2. Market research & market analysis prompts

### 2.1 Gold-standard market sizing (works with any of the above)
```
Market sizing request: [product/category] in [geography], [year].
Method requirements:
- TOP-DOWN: start from a sourced macro anchor (industry reports, census,
  regulator data — search for and cite them), apply explicit filter chain
  with a stated rationale per filter.
- BOTTOM-UP: units × frequency × price, built from named proxy data.
- Reconcile the two. Divergence >30% → investigate, don't average.
- Output TAM / SAM / SOM with the boundary definition of each, a
  sensitivity table on the 3 weakest assumptions, and a one-line
  "how much would I bet on this number" confidence statement.
```

### 2.2 `anthropics/financial-services` → Market Researcher agent
**When:** industry overviews, competitive landscapes, peer comps — grounded in connector data.
```
/market-researcher (or invoke the market-researcher agent)
Build an industry primer on [sector]: market structure and size, top 8
players with share and positioning, 3-year demand drivers, disruption
vectors, and a peer comp table (EV/EBITDA, growth, margin). Cite every
number to its source. Flag any figure that came from memory rather than
a retrieved source.
```

### 2.3 `ishwarjha/claude-marketing-research-skill`
**When:** customer/competitor research for positioning, GTM, or copy — not for market sizing.
```
Run a full marketing research on [product]. Focus modules: competitor
landscape + gap analysis, avatar profiling, and value propositions.
Interview me first for what you need.
```

### 2.4 `alirezarezvani/claude-skills` → competitive-intel
```
Use the competitive-intel skill. Target: [competitor]. Build: company
snapshot, product/pricing teardown, GTM motion, recent strategic moves
(search for the last 12 months and cite), predicted next moves, and a
battlecard: how we win against them, where we lose, landmines to plant.
```

### 2.5 `OctagonAI/skills` (real filings — highest factual accuracy)
```
Using the sec-analyst and earnings-analyst skills: analyze [TICKER]'s last
10-K and two most recent earnings calls. Extract: revenue by segment with
YoY, stated guidance vs. delivery, top 5 risk factors ranked by novelty
vs. prior year, and management-tone shift. Every claim cited to the filing
or transcript.
```

---

## 3. Financial consulting prompts (`anthropics/financial-services`)

| Task | Prompt |
|---|---|
| Trading comps | `/comps [TICKER] — peer set of 8–10, justify each inclusion/exclusion, EV/EBITDA, EV/Revenue, P/E, growth-adjusted; flag outliers and where [TICKER] should trade and why.` |
| DCF | `/dcf [TICKER] — 5-year explicit period, WACC build shown line by line, terminal via both Gordon and exit multiple, sensitivity grid on WACC × terminal growth, football field vs. comps.` |
| LBO | `/lbo [target] — entry at [X]× EBITDA, [structure], base/upside/downside operating cases, returns bridge (leverage vs. multiple expansion vs. operations), min IRR covenant headroom check.` |
| 3-statement | `/3-statement-model for [company] from these financials: [attach]. Fully linked, drivers tab, no hardcodes in formula cells.` |
| Model audit | `/debug-model [attach .xlsx] — trace formula errors, find hardcodes, broken links, sign-convention inconsistencies. Report by severity.` |
| Deck QC | `ib-check-deck on [attach deck] — numbers vs. source consistency, footnote integrity, title-says-what-chart-shows check.` |
| IC memo | `/ic-memo for [target]: thesis, market, moat, financial summary, returns math, key diligence findings, risks with mitigants, recommendation with conditions.` |
| DD checklist | `/dd-checklist for a [sector] target at [size] — commercial, financial, legal, tech, HR workstreams with priority tiers and data-room requests.` |

---

## 4. Chained engagement workflows (the real senior-consultant move)

### Workflow A — Market entry study (2–3 sessions)
1. **Frame:** MBB skill → `Act as my management consultant` + market-entry prompt (§1.1) → issue tree + hypotheses
2. **Size:** Gold-standard sizing prompt (§2.1) with web search ON
3. **Competitive field:** competitive-intel prompt (§2.4) per key incumbent + `profit-pool-analysis` (§1.4)
4. **Economics:** `/dcf`-style business case on the entry option; sensitivity on the 3 weakest assumptions
5. **Pressure-test:** `war-gaming` skill (§1.4) — incumbents respond
6. **Deliver:** enterprise-ai-skills chain (§1.3) storyline → deck → mckinsey-critic

### Workflow B — Commercial due diligence (buy-side)
1. `/screen-deal` on the CIM → red flags + first-pass thesis
2. `/dd-checklist` → workstream plan
3. Octagon sec/earnings analysis (§2.5) on target + public comps
4. Market sizing (§2.1) + competitive-intel (§2.4) → market and moat validation
5. `/comps` + `/lbo` → valuation and returns
6. `/ic-memo` → committee-ready output; mckinsey-critic pass before submission

### Workflow C — Board/steering-committee deck in one day
1. `decision-memo-builder` → get the argument right in prose FIRST
2. `storyline-builder` → SCQA slide storyline, action titles
3. `mckinsey-charts` → waterfall/marimekko exhibits from your data
4. `deck-pipeline` + `document-skills (pptx)` → real .pptx
5. `mckinsey-critic` + `ib-check-deck` → double QC pass, then human review

---

## 5. Which skill when — decision table

| You need… | Use |
|---|---|
| Structure an ambiguous business problem | DogInfantry MBB skill or gcamilo (Quick Structure) |
| Full engagement-grade analysis | DogInfantry MBB + Universal Operating Prompt |
| Market size with defensible numbers | §2.1 prompt + web search / data connectors |
| Competitor deep-dive / battlecard | alirezarezvani competitive-intel |
| Customer/avatar/positioning research | ishwarjha marketing-research |
| Public-company facts (zero-hallucination) | OctagonAI skills or financial-services connectors |
| Valuation (DCF/comps/LBO/merger) | anthropics/financial-services |
| Due diligence / IC memo | anthropics/financial-services PE bundle |
| Memo or deck production | enterprise-ai-skills chain + anthropics document skills |
| QC before the client sees it | mckinsey-critic + ib-check-deck |
| Case interview prep | DogInfantry MBB or yoichiojima `/case-practice` |

---

## 6. Adapting for ChatGPT and Codex

- **ChatGPT:** create a **Project** per skill; paste the SKILL.md body (minus YAML frontmatter) into the project's custom instructions; put the Universal Operating Prompt at the top. Best candidates for this treatment: gcamilo's SKILL.md (self-contained single file) and any single aapersh skill. Multi-file skills (DogInfantry's 118 references) degrade — attach the reference files to the project as knowledge files.
- **Codex:** skills folders work via the `npx skills add <repo>` CLI (targets Claude Code/Codex/Cursor/Gemini CLI), or use `alirezarezvani/claude-skills` conversion scripts; otherwise paste the skill body into `AGENTS.md` at repo root.
- **Everything else:** SKILL.md is just markdown — pasting the body as the first message of a conversation works on any frontier model, at the cost of auto-triggering.

**Model note:** these skills assume a strong reasoning model. On Claude, use Opus-class models for engagement work; skills + weak models produce well-formatted wrong answers.
