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

The original tab is two datasets appended without harmonisation:

- **Block A** — 157 rows (`EUR-004`…`EUR-198`), a PitchBook export. Source URL on 16 of 157.
- **Block B** — 66 rows (`EUR-199`…`EUR-264`), primary-source research. Source URL on 66 of 66.

116 of the 157 Block A rows were individually checked against company releases, exchange
filings and regulatory announcements:

| Outcome | Rows |
|---|---|
| Correct as recorded | 32 |
| Required a factual correction | 65 |
| Deal value recorded where none was disclosed | 15 |
| Failed or marginally passed the A&D scope test | 18 |

A 28% clean rate on the rows that could be checked. The remaining 41 Block A rows — all
sub-$10m bolt-ons — could not be matched to any independent primary source and are marked
`NOT INDEPENDENTLY VERIFIED` in the `Reliability` column.

Six Block B rows were spot-checked (Destinus/Daedalean, Gabler Group IPO, Molex/Smiths
Interconnect, Eaton/Ultra PCS, Lockheed/Ultra Maritime, Doncasters IPO). All held up.

## Row reconciliation

```
Original Europe tab                     223
Removed (non-European target / duplicate) −5
Verified in-scope events added           +14
                                        ────
Corrected tab                            232
```

## Recurring defects in Block A

1. **Announcement dates recorded as completion dates** while the row reads "Completed"
   (≥14 rows). Worst case: Hamamatsu/NKT Photonics, dated 14 months early to a point when
   the deal had been blocked by the Danish government.
2. **Undisclosed values presented as fact** (≥15 rows). Where the acquirer did disclose,
   the vendor figure often differs materially — ESCO/Ultra Maritime SM&P $472m vs $550m
   actual; Halma/MK Test £6.9m vs £44m actual; York/ALL.SPACE $355m vs $46.3m disclosed.
3. **Maximum earn-out booked as headline value** without disclosure.
4. **Minority and partial stakes recorded as "Full Acquisition"** — Indra/TESS Defence
   (26.33%), Indra/Epicom (30%), Leonardo/GEM (30%→65%), CY4Gate/Diateam (55.33%),
   Orbyt/OTESAT-Maritel (94.09%), ENAV/AiviewGroup (85%), 4iG/N7 Defence (75%+1).
5. **Revenue recorded as deal value** — Indutrade/Crane Electronics.
6. **One transaction split across two rows** — Al-Met and Roota Engineering were a single
   purchase of Pressure Technologies' PMC division. Merged.
7. **Currency and unit errors** — Waterfront Fluid Controls: INR 205.624m recorded as
   USD 254.06m, a ~100x overstatement.

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

`verif.py` holds the per-row verification findings and sources; `corrections.py` the
field-level overrides; `additions.py` the verified missing events.
