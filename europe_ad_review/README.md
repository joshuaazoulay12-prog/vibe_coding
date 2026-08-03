# Europe A&D IPO / M&A dataset — audit and repair

Review of the Europe tab of `Final Spreadsheet Updated_v2 (0128529)`, covering European
aerospace & defence companies that completed an IPO or were acquired between
1 January 2023 and 2 August 2026.

## Deliverables

| File | Contents |
|---|---|
| `Europe_Improved.xlsx` | **Current deliverable.** The stricter competing build with 4 additions and 6 corrections applied (133 completed rows + 14 pending) |
| `Europe_Tab_Audit.xlsx` | 15 findings across factual errors, omissions, scope exceptions and format defects |
| `Europe_Corrected.xlsx` | Earlier standalone Europe rebuild (232 rows) — superseded, retained for its verification register |

## Second-review outcome (2026-08-02)

A competing build was assessed against this one and judged **better on balance**: it preserves the
full workbook, applies a stricter and consistently documented "A&D is the target's primary
business" test with a retain/exclude/correct decision for every original row, separates pending
deals, carries two source URLs per row, and includes ~20 in-scope deals this repo had missed
(WASS Submarine Systems/Fincantieri €287m, Marshall Land Systems, Sofisport/FN Browning,
Paul Boyé/NFM, Summa Defence, Hirtenberger/4iG, Harder Digital/THEON, MADES/Cicor and others).

It was therefore adopted and improved rather than replaced. Changes applied:

**Added (4)** — absent from that build *and* from its audit log, all passing its own stated policy:

| Target | Event | Date |
|---|---|---|
| Milrem Robotics | EDGE Group majority stake | 2023-02-15 |
| CS Group | Sopra Steria 75.06% | 2023-02-28 |
| TKMS AG & Co. KGaA | Frankfurt Prime Standard admission | 2025-10-20 |
| Spirit AeroSystems Belfast + Prestwick | Airbus carve-out | 2025-12-08 |

TKMS is flagged in Deal Structure as a spin-off admission with no offering and no proceeds, so it
can be filtered out under a strict "public offering" reading.

**Corrected (6)**

| Row | Was | Now |
|---|---|---|
| Milectria Group | SEK 266m + SEK 77m earn-out | **SEK 190m (€17.1m)** + €18m earn-out |
| ALL.SPACE | $355m "transaction value" | **$46.3m** initial consideration at completion; $355m retained as the announced headline |
| Sky-Hero | text `2023-06 (estimated)` | **2023-07-14** |
| Tethys | text `2026-05 (estimated)` | **2026-05-04** |
| Ultra Maritime SM&P | 2025-04-25 | **2025-04-28** |
| VoltAero | 2026-06-23 | **2026-06-29** |

Also removed 94 trailing blank rows, re-sorted and renumbered `EUR-001`…`EUR-133`, reconciled
`Master_Deals`, remapped every audit-log ID, and appended all changes to `Europe_Audit_Log`,
`Sources_Audit` and `Checks`.

## Scope rule applied

**European target only** — the company that completed an IPO or was acquired must be
European-headquartered. European acquirers buying non-European targets are out of scope.

## Verification coverage

**All 223 original rows were individually checked** against company press releases, exchange
filings, regulatory announcements and court records.

| Outcome | Rows |
|---|---|
| Correct as recorded | 80 |
| Required a factual correction | 116 |
| Deal value recorded where none was disclosed | 18 |
| Partially verified | 2 |
| No primary source located | 3 |

A 36% clean rate. Three rows could not be corroborated at all and are marked
`NO PRIMARY SOURCE LOCATED`: **EUR-144** Aeropolis (recorded acquirer appears wrong —
sources point to Infracorp, not Mareterra/Sophrance), **EUR-168** Interactive Technical
Solutions, **EUR-174** TEMMA. Two are partially verified: **EUR-249** Burcas (acquisition
confirmed, date not corroborated) and **EUR-261** PBH Teknik (date confirmed, value not
corroborated).

The original tab was two datasets appended without harmonisation — a PitchBook export
(`EUR-004`…`EUR-198`, source URL on 16 of 157) and a later primary-source pass
(`EUR-199`…`EUR-264`, source URL on all 66). The error rate is concentrated in the first.

## Row reconciliation

```
Original Europe tab                     223
Removed (non-European target / duplicate) −5
Verified in-scope events added           +14
                                        ────
Corrected tab                            232
```

## Systematic defects found

1. **Announcement dates recorded as completion dates** while the row reads "Completed"
   (≥14 rows). Worst case: Hamamatsu/NKT Photonics, dated 14 months early to a point when
   the deal had been blocked by the Danish government.
2. **Undisclosed values presented as fact** (≥15 rows). Where the acquirer did disclose,
   the vendor figure often differs materially — ESCO/Ultra Maritime SM&P $472m vs $550m
   actual; Halma/MK Test £6.9m vs £44m actual; York/ALL.SPACE $355m vs $46.3m disclosed.
3. **Maximum earn-out booked as headline value** without disclosure.
4. **Minority and partial stakes recorded as "Full Acquisition"** — 24 rows corrected,
   including Indra/TESS Defence (26.33%), Indra/Epicom (30%), Leonardo/GEM (30%→65%),
   CY4Gate/Diateam (55.33%), EFA/ES Systems (63.02%), Satori/MAGnetIC (80%),
   ENAV/AiviewGroup (85%), Orbyt/OTESAT (94.09%), Otokar/Automecanica (96.77%),
   Argo/Poseidon (99.55%), HEICO/Cook Defence (80%), and Fincantieri's four underwater
   stakes (52.60%, 61.95%, 51%, 49%).
5. **Revenue recorded as deal value** — Indutrade/Crane Electronics.
6. **One transaction split across two rows** — Al-Met and Roota Engineering were a single
   purchase of Pressure Technologies' PMC division. Merged.
7. **Currency and unit errors** — Waterfront Fluid Controls: INR 205.624m recorded as
   USD 254.06m, a ~100x overstatement.
8. **IPO placement volume labelled as issuer proceeds** — SMAG (€129.6m placed vs ~€30m
   raised), Gabler Group, Savox. Exosens was the largest single error in the tab: €1.10bn
   raised and a €3.90bn valuation recorded against an actual €402.5m offering and ~€1.02bn
   market capitalisation.
9. **Wrong acquirer country** — Defence Tech Holding recorded as Polish (Italian); EFA Group
   as Singaporean (Greek); Sigma Advanced Systems as British (Indian — and recorded
   correctly two rows later).
10. **Events that did not happen as recorded** — Uravi/Spafax booked as a completed 100%
   acquisition in June 2025 when only a 10% stake was taken in March 2026; Aubert & Duval
   booked as completed when it remains subject to regulatory approval; Defence Holdings
   recorded inverted, where what actually changed hands was an esports business for £100,000.

## Workbook-level issues outside this tab (flagged, not fixed)

- Deal IDs collide across tabs: `EUR-079`…`EUR-108` identify different transactions on
  `Master_Deals` than on `Europe`; 19 of 69 shared IDs conflict. The corrected tab uses new
  `EU-###` identifiers with the legacy ID retained in its own column.
- `Master_Deals` holds 71 Europe rows against the Europe tab's 223, never reconciled.
- The Dashboard links to four sheets absent from the workbook.
- The Definitions tab states IPOs are "not counted as core M&A", which the Europe tab
  contradicts.

## Reproducing

```
pip install openpyxl
python build.py        # applies corrections + additions, writes built.pkl
python write_xlsx.py   # renders Europe_Corrected.xlsx
```

`verif.py` and `pass2.py` hold the per-row verification findings and sources; `corrections.py` the
field-level overrides; `additions.py` the verified missing events.
