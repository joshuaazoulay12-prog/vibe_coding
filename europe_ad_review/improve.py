import openpyxl, datetime, copy
from openpyxl.styles import Font, PatternFill, Alignment, Border
from openpyxl.utils import get_column_letter

wb = openpyxl.load_workbook('codex.xlsx')
ws = wb['Europe']
H = [ws.cell(1,c).value for c in range(1,29)]
IDX = {h:i for i,h in enumerate(H)}
def blank_row(): return [None]*28

# ---------- read existing 129 rows ----------
rows = []
for r in range(2, 131):
    rows.append([ws.cell(r,c).value for c in range(1,29)])

def setf(row, key, val): row[IDX[key]] = val
def getf(row, key): return row[IDX[key]]
def find(did):
    for x in rows:
        if x[0] == did: return x
    raise KeyError(did)

CH = []   # change log

# ================= CORRECTIONS =================
# 1. Milectria - HANZA's own release: EUR 17.1m / ~SEK 190m at completion
x = find('EUR-066')
setf(x,'Native Deal Value (mn)', 190)
setf(x,'Value Basis', "Completion consideration of EUR 17.1m, stated by HANZA as approximately SEK 190m; contingent earn-out of up to EUR 18m if turnover more than doubles over 2025-2027.")
setf(x,'Audit Notes', (getf(x,'Audit Notes') or '') + " CORRECTED 2026-08-02: native value was SEK 266m with a SEK 77m earn-out; HANZA's completion release and headline state EUR 17.1m (~SEK 190m) with an earn-out of up to EUR 18m.")
setf(x,'Secondary Source URL', "https://evertiq.com/news/2025-10-01-hanza-completes-acquisition-of-milectria")
CH.append(('EUR-066','Milectria Group','Native deal value SEK 266m -> SEK 190m (EUR 17.1m); earn-out restated to EUR 18m',
           "HANZA completion release: 'HANZA completes acquisition of Milectria for EUR 17.1 million, equivalent to approximately SEK 190 million'; additional consideration up to EUR 18m.",
           'https://hanza.com/investor/pressreleases/hanza-completes-acquisition-and-expands-capacity-for-the-defense-industry/'))

# 2. ALL.SPACE - $355m was the announcement headline; completion release gives ~$46.3m initial consideration
x = find('EUR-125')
setf(x,'Native Deal Value (mn)', 46.3)
setf(x,'Deal Value (USD mn)', 46.3)
setf(x,'Value Basis', "Initial total consideration at completion of approximately USD 46.3m (approx. USD 17.9m cash plus 1,240,148 York shares valued at York's 7 July 2026 close), rising to approximately USD 54.4m if all escrow and holdback amounts are released. The USD 355m figure was the headline cash-and-stock value announced on 30 April 2026.")
setf(x,'Audit Notes', (getf(x,'Audit Notes') or '') + " CORRECTED 2026-08-02: the row paired the 30 April 2026 announcement headline (USD 355m) with the 8 July 2026 completion date. York's completion release states initial consideration of ~USD 46.3m; both figures are now recorded with their bases.")
CH.append(('EUR-125','ALL.SPACE','Deal value USD 355m -> USD 46.3m initial consideration at completion (USD 355m retained as the announced headline)',
           "York Space Systems completion release: initial cash ~USD 17.9m plus 1,240,148 York shares, ~USD 46.3m total, up to ~USD 54.4m with escrow release.",
           'https://www.businesswire.com/news/home/20260707941488/en/York-Space-Systems-Completes-Acquisition-of-ALL.SPACE-Delivering-Assured-Communications-and-Positioning-in-Contested-Environments'))

# 3. Sky-Hero - exact completion date is public
x = find('EUR-010')
setf(x,'Completion / IPO Date', datetime.datetime(2023,7,14))
setf(x,'Audit Notes', (getf(x,'Audit Notes') or '') + " CORRECTED 2026-08-02: date was held as the text string '2023-06 (estimated)'. Axon's own announcement and transaction records date the acquisition 14 July 2023, so an exact date replaces the month estimate.")
setf(x,'Secondary Source URL', "https://www.axon.com/blog/our-next-step-in-robotics-sky-hero-joins-forces-with-axon")
CH.append(('EUR-010','Sky-Hero','Completion date text "2023-06 (estimated)" -> 2023-07-14 (real date value)',
           "Axon announcement and transaction record date the Sky-Hero acquisition 14 July 2023.",
           'https://www.axon.com/blog/our-next-step-in-robotics-sky-hero-joins-forces-with-axon'))

# 4. Tethys - exact date is public
x = find('EUR-114')
setf(x,'Completion / IPO Date', datetime.datetime(2026,5,4))
setf(x,'Ownership Acquired', "Majority stake, alongside management and Bpifrance")
setf(x,'Audit Notes', (getf(x,'Audit Notes') or '') + " CORRECTED 2026-08-02: date was held as the text string '2026-05 (estimated)'. Abenex announced the transaction on 4 May 2026; it is a majority-stake LBO taken alongside management and Bpifrance, which reinvested.")
setf(x,'Secondary Source URL', "https://largilliere-finance.com/en/tethys-welcomes-abenex-as-its-new-majority-shareholder/")
CH.append(('EUR-114','Tethys','Completion date text "2026-05 (estimated)" -> 2026-05-04 (real date value); ownership restated as majority stake',
           "Abenex publication dated 4 May 2026: Abenex becomes majority shareholder alongside management and Bpifrance.",
           'https://www.abenex.com/en/publications/abenex-acquires-tethys'))

# 5. Ultra Maritime SM&P - ESCO's completion release is dated 28 April 2025
x = find('EUR-054')
setf(x,'Completion / IPO Date', datetime.datetime(2025,4,28))
setf(x,'Audit Notes', (getf(x,'Audit Notes') or '') + " CORRECTED 2026-08-02: completion date 25 April 2025 replaced with 28 April 2025, the date of ESCO's completion release.")
CH.append(('EUR-054','Ultra Maritime Signature Management & Power business','Completion date 2025-04-25 -> 2025-04-28',
           "ESCO Technologies release 'ESCO Completes Acquisition of SM&P' is dated 28 April 2025.",
           'https://investor.escotechnologies.com/news-releases/news-release-details/esco-completes-acquisition-smp'))

# 6. VoltAero - AURA AERO acquired the assets on 29 June 2026
x = find('EUR-121')
setf(x,'Completion / IPO Date', datetime.datetime(2026,6,29))
setf(x,'Audit Notes', (getf(x,'Audit Notes') or '') + " CORRECTED 2026-08-02: completion date 23 June 2026 replaced with 29 June 2026 per contemporaneous trade reporting of the asset transfer.")
CH.append(('EUR-121','VoltAero assets and operations','Completion date 2026-06-23 -> 2026-06-29',
           "AURA AERO acquired the Cassio demonstrator and other VoltAero assets on 29 June 2026.",
           'https://www.aerotime.aero/articles/french-electric-aviation-set-to-consolidate-after-aura-aero-acquires-voltaero'))

# ================= ADDITIONS =================
def mk(tc, tgt, acq, acqc, seller, ann, comp, ttype, struct, own, native, cur, usd, basis,
       hss, dom, evid, syn, web, purl, surl, note):
    row = blank_row()
    row[IDX['Deal ID']] = 'NEW'
    row[IDX['Region']] = 'Europe'
    row[IDX['Target Country']] = tc
    row[IDX['Target / Business']] = tgt
    row[IDX['Acquirer']] = acq
    row[IDX['Acquirer Country']] = acqc
    row[IDX['Seller']] = seller
    row[IDX['Announcement Date']] = ann
    row[IDX['Completion / IPO Date']] = comp
    row[IDX['Transaction Type']] = ttype
    row[IDX['Deal Structure']] = struct
    row[IDX['Ownership Acquired']] = own
    row[IDX['Deal Status']] = 'Completed'
    row[IDX['Native Deal Value (mn)']] = native
    row[IDX['Currency']] = cur
    row[IDX['Deal Value (USD mn)']] = usd
    row[IDX['Value Basis']] = basis
    row[IDX['Hardware / Software / Services']] = hss
    row[IDX['A&D Domain']] = dom
    row[IDX['Inclusion Tier']] = 'Core A&D'
    row[IDX['Scope Evidence']] = evid
    row[IDX['Deal Synopsis']] = syn
    row[IDX['Company Website']] = web
    row[IDX['Verification Status']] = 'Verified — primary source'
    row[IDX['Primary Source URL']] = purl
    row[IDX['Secondary Source URL']] = surl
    row[IDX['Audit Notes']] = note
    return row

ADDED = [
mk('Estonia','Milrem Robotics','EDGE Group PJSC','United Arab Emirates','Founders, employees and Estonian private investors',
   datetime.datetime(2023,2,15), datetime.datetime(2023,2,15),'M&A','Majority stake','Majority (KNDS/KMW retained ~24.9%; founder and employees retained minority holdings)',
   'Not disclosed','Not disclosed','Not disclosed',
   'Consideration not publicly disclosed by either party.',
   'Hardware / Software','UAVs & Autonomous Systems',
   'Unmanned Ground Systems. Milrem develops and manufactures the THeMIS and Type-X robotic combat and support vehicles for NATO and allied armed forces; defence robotics is its sole business.',
   'EDGE Group acquired a majority stake in Milrem Robotics, announced 2023-02-15 at IDEX. Described by both parties as the largest foreign investment in Estonia’s defence industry. Consideration not disclosed.',
   'https://milremrobotics.com','https://edgegroup.ae/news/edge-acquires-majority-stake-milrem-robotics-europes-leading-developer-robotics-and-autonomous',
   'https://milremrobotics.com/edge-acquires-majority-stake-in-milrem-robotics-europes-leading-developer-of-robotics-and-autonomous-systems/',
   'ADDED 2026-08-02: absent from the original workbook and from the audit log. Passes the strict tests — Estonian target, defence robotics as sole business, change of control. Neither party disclosed a separate legal completion date; the announcement date is used and flagged.'),

mk('France','CS Group','Sopra Steria Group SE','France','Yazid Sabeg, Eric Blanc-Garin, Duna & Cie, Cira Holding and the founders of Novidy’s',
   datetime.datetime(2022,11,18), datetime.datetime(2023,2,28),'M&A','Majority stake','75.06% of share capital and 76.21% of voting rights',
   11.50,'EUR','Not disclosed',
   'Price per share of EUR 11.50 paid for the acquired blocks; Sopra Steria did not publish an aggregate transaction value.',
   'Software / Services','Cyber & Digital Defence',
   'Digital services and critical systems for defence and security, space and energy. CS Group is a French defence and security prime contractor with approximately 2,500 employees.',
   'Sopra Steria finalised its acquisition of a majority stake in CS Group on 2023-02-28, taking it to 75.06% of share capital and 76.21% of voting rights at EUR 11.50 per share. CS Group was consolidated from 1 March 2023.',
   'https://www.cs-soprasteria.com','https://www.soprasteria.com/newsroom/press-releases/details/sopra-steria-finalises-its-acquisition-of-a-majority-stake-in-the-share-capital-of-cs-group',
   'https://www.cs-soprasteria.com/en/news/sopra-steria-finalises-its-acquisition-of-a-majority-stake-in-the-share-capital-of-cs-group/',
   'ADDED 2026-08-02: absent from the original workbook and from the audit log, although CS Group appears in the sheet as an acquirer. Passes the strict tests — French target, defence and security critical systems as primary business, change of control completed inside the window.'),

mk('Germany','TKMS AG & Co. KGaA','Frankfurt Stock Exchange (Prime Standard) — admission to trading','N/A — listing','thyssenkrupp AG (49% distributed to its shareholders; 51% retained)',
   datetime.datetime(2025,8,13), datetime.datetime(2025,10,20),'IPO','Spin-off admission to trading (no public offering; no proceeds raised)','49% of shares distributed to thyssenkrupp shareholders; thyssenkrupp retained 51%',
   'Not applicable','Not applicable','Not applicable',
   'No public offering and no proceeds were raised. Shares were distributed to thyssenkrupp shareholders at a ratio of 1:20. Market capitalisation reached approximately EUR 6.8bn on the debut day.',
   'Hardware / Services','Naval & Underwater Systems',
   'Submarines, frigates and maritime defence systems. TKMS is one of Europe’s largest pure-play naval defence companies, with an order backlog of approximately EUR 18.6bn at listing.',
   'TKMS AG & Co. KGaA was admitted to trading in the Prime Standard of the Frankfurt Stock Exchange on 2025-10-20 following the spin-off approved by thyssenkrupp shareholders on 2025-08-13. Shares opened at EUR 60 and reached as high as EUR 107, valuing the company at up to approximately EUR 6.8bn.',
   'https://www.tkmsgroup.com','https://www.tkmsgroup.com/news/article/tkms-lists-on-the-frankfurt-stock-exchange-successful-market-debut-for-maritime-defense-provider',
   'https://www.thyssenkrupp.com/en/newsroom/press-releases/pressdetailpage/thyssenkrupp-ag-announces-planned-date-for-stock-market-listing-of-tkms-308582',
   'ADDED 2026-08-02: absent from the original workbook and from the audit log. This is the largest European pure-play naval defence listing of the review period. NOTE ON SCOPE: it is a spin-off admission, not a public offering, so it does not meet the workbook’s strict "Completed IPO" definition. It is included and explicitly flagged in Deal Structure so it can be filtered out if the strict offering test is preferred.'),

mk('United Kingdom','Spirit AeroSystems Belfast and Prestwick operations','Airbus SE','Netherlands','Spirit AeroSystems Holdings, Inc.',
   datetime.datetime(2025,4,28), datetime.datetime(2025,12,8),'M&A','Carve-out','100% of the acquired European sites',
   'Not disclosed','Not disclosed','Not disclosed',
   'No purchase price was paid by Airbus. Airbus received compensation of USD 439m from Spirit AeroSystems, subject to purchase price adjustments and customary post-closing review.',
   'Hardware','Aerospace Platforms & Components',
   'Aerostructures. Belfast produces A220 wings and mid-fuselage sections; Prestwick produces wing components for the A320 and A350. Both sites work exclusively on Airbus commercial aircraft programmes.',
   'Airbus completed the acquisition of Spirit AeroSystems’ Belfast (A220 wings and mid-fuselage) and Prestwick (A320/A350 wing components) operations on 2025-12-08, alongside the Kinston, North Carolina site. Over 4,000 employees transferred across the acquired sites. Airbus received compensation of USD 439m.',
   'https://www.airbus.com','https://www.airbus.com/en/newsroom/press-releases/2025-12-airbus-completes-acquisition-of-spirit-aerosystems-sites',
   'https://www.airbus.com/en/newsroom/press-releases/2025-04-airbus-signs-definitive-agreement-with-spirit-aerosystems',
   'ADDED 2026-08-02: absent from the original workbook and from the audit log. Passes the strict tests — UK operating sites, aerostructures as sole business, carve-out of an identifiable operating business completed inside the window. Only the European sites are recorded; the Kinston, NC site is out of scope.'),
]
rows.extend(ADDED)

# ================= SORT + RENUMBER =================
def keydate(x):
    d = getf(x,'Completion / IPO Date')
    return d if isinstance(d, datetime.datetime) else datetime.datetime(2099,1,1)
rows.sort(key=keydate)
idmap = {}
for i, x in enumerate(rows, 1):
    old = x[0]; new = f"EUR-{i:03d}"
    if old != 'NEW': idmap[old] = new
    x[0] = new

# ================= WRITE BACK =================
tpl_font  = ws.cell(2,1).font
tpl_align = ws.cell(2,1).alignment
tpl_bord  = ws.cell(2,1).border
for r in range(2, ws.max_row+1):
    for c in range(1, 40):
        ws.cell(r,c).value = None
for i, x in enumerate(rows):
    r = i + 2
    for c in range(1, 29):
        cell = ws.cell(r,c)
        cell.value = x[c-1]
        cell.font = copy.copy(tpl_font)
        cell.alignment = copy.copy(tpl_align)
        cell.border = copy.copy(tpl_bord)
    ws.cell(r, IDX['Deal Year']+1).value = f'=IFERROR(YEAR(I{r}),IFERROR(VALUE(LEFT(I{r},4)),""))'
    ws.cell(r, IDX['Completion / IPO Date']+1).number_format = 'yyyy-mm-dd'
    ws.cell(r, IDX['Announcement Date']+1).number_format = 'yyyy-mm-dd'
N = len(rows); LAST = N + 1
ws.delete_rows(LAST+1, ws.max_row - LAST)
print(f"Europe: {N} rows (was 129); trailing blanks removed")
import pickle; pickle.dump((rows, ADDED, CH, idmap, N), open('improve.pkl','wb'))
wb.save('Europe_Improved.xlsx')
