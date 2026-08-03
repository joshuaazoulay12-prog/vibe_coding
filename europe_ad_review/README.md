# Europe A&D IPO / M&A dataset — audit and repair

Review of the Europe tab of `Final Spreadsheet Updated_v2 (0128529)`, covering European
aerospace & defence companies that completed an IPO or were acquired between
1 January 2023 and 2 August 2026.

## Deliverables

| File | Contents |
|---|---|
| `Europe_Tab_Audit.xlsx` | 15 findings across factual errors, omissions, scope exceptions and format defects |
| `Europe_Corrected.xlsx` | Repaired dataset (232 rows), change log, additions, removals, per-row verification register, methodology |

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
