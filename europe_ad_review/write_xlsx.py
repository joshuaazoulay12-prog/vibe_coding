import openpyxl, pickle, datetime, re
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
exec(open('verif.py').read())
exec(open('pass2.py').read())
V.update(V2)
recs, removed, changelog = pickle.load(open('built.pkl','rb'))

NAVY="FF1F3864"; MID="FF2E5C9A"; BAND="FFF4F7FB"; RED="FFC00000"; AMB="FFBF8F00"; GRN="FF375623"
FONT="Arial"
th=Side(style="thin", color="FFD0D0D0"); BRD=Border(left=th,right=th,top=th,bottom=th)
def hdr(ws, headers, widths, freeze="C2", fill=NAVY):
    for i,h in enumerate(headers,1):
        c=ws.cell(1,i,h); c.font=Font(name=FONT,sz=10,b=True,color="FFFFFFFF")
        c.fill=PatternFill("solid",fgColor=fill); c.border=BRD
        c.alignment=Alignment(vertical="center",wrap_text=True,horizontal="center")
    ws.row_dimensions[1].height=34
    for i,w in enumerate(widths,1): ws.column_dimensions[get_column_letter(i)].width=w
    ws.freeze_panes=freeze
    ws.auto_filter.ref=f"A1:{get_column_letter(len(headers))}1"
def body(ws, nrows, ncols):
    for r in range(2, nrows+2):
        for c in range(1, ncols+1):
            cell=ws.cell(r,c); cell.font=Font(name=FONT,sz=9); cell.border=BRD
            cell.alignment=Alignment(vertical="top",wrap_text=True)
            if r%2==0: cell.fill=PatternFill("solid",fgColor=BAND)

wb = openpyxl.Workbook()

# ============ 1. Europe (corrected) ============
ws = wb.active; ws.title="Europe"
COLS=[("Deal ID",10),("Legacy ID",11),("Region",9),("Target / Asset",34),("Target Country",16),("Target HQ",24),
 ("Acquirer / Listing Venue",30),("Acquirer Country",16),("Seller",22),("Event Type",17),("Deal Structure",26),
 ("Stake Acquired",22),("Announcement Date",13),("Completion Date",13),("Deal Year",9),("Deal Status",20),
 ("Deal Value (USD mn)",13),("Value Basis",26),("Reported Consideration (local)",34),("Value Disclosure",26),
 ("Inclusion Tier",18),("A&D Domain",30),("A&D Scope Test",13),("Description",46),("Deal Synopsis",46),
 ("Reliability",34),("Correction / Note",60),("Source Block",26),("Source URL",44)]
hdr(ws,[c[0] for c in COLS],[c[1] for c in COLS])
for i,x in enumerate(recs,2):
    row=[x['id'],x['legacy'],'Europe',x['tgt'],x['tc'],x['hq'],
         x['acq'] if x['acq'] else ('Public markets - IPO' if x['evt']=='IPO' else None),
         x['ac'],x['seller'],x['evt'],x['struct'],x['stake'],x['ann'],x['comp'],x['year'],x['status'],
         x['val'],x['basis'],x['local'],x['disc'],x['tier'],x['dom'],x['scope'],
         (str(x['desc'])[:800] if x['desc'] else None),(str(x['syn'])[:800] if x['syn'] else None),
         x['reliab'],x['note'],x['block'],x['src']]
    for j,v in enumerate(row,1): ws.cell(i,j,v)
n=len(recs); body(ws,n,len(COLS))
for r in range(2,n+2):
    ws.cell(r,17).number_format='#,##0.0'
    for cc in (13,14): ws.cell(r,cc).alignment=Alignment(vertical="top",horizontal="center")
    ws.cell(r,15).number_format='0'; ws.cell(r,15).alignment=Alignment(vertical="top",horizontal="center")
    sc=ws.cell(r,23); col={'Fail':RED,'Marginal':AMB}.get(sc.value)
    if col: sc.font=Font(name=FONT,sz=9,b=True,color=col)
    rl=ws.cell(r,26)
    if str(rl.value).startswith('NOT INDEPENDENTLY'): rl.font=Font(name=FONT,sz=9,b=True,color=RED)
    elif 'ADDED' in str(rl.value): rl.font=Font(name=FONT,sz=9,b=True,color=GRN)
    st=ws.cell(r,16)
    if st.value=='Announced/In Progress': st.font=Font(name=FONT,sz=9,color=AMB)

# ============ 2. Change Log ============
ws2=wb.create_sheet("Change Log")
hdr(ws2,["Legacy ID","Target","Source Block","Fields Corrected","What was wrong and what the primary source says","Source URL"],
    [11,34,26,34,96,46],freeze="A2")
for i,(did,tgt,blk,fields,note,url) in enumerate(sorted(changelog),2):
    for j,v in enumerate([did,tgt,blk,fields,note,url],1): ws2.cell(i,j,v)
body(ws2,len(changelog),6)

# ============ 3. Additions ============
ws3=wb.create_sheet("Additions")
hdr(ws3,["Target","Country","Acquirer / Venue","Event","Completion","Value (USD mn)","Reported consideration","Why it belongs","Source URL"],
    [34,16,30,17,13,13,40,60,46],freeze="A2")
adds=[x for x in recs if x['block'].startswith('C')]
for i,x in enumerate(adds,2):
    for j,v in enumerate([x['tgt'],x['tc'],x['acq'],x['evt'],x['comp'],x['val'],x['local'],x['desc'],x['src']],1):
        ws3.cell(i,j,v)
body(ws3,len(adds),9)
for r in range(2,len(adds)+2): ws3.cell(r,6).number_format='#,##0.0'

# ============ 4. Removed - Out of Scope ============
ws4=wb.create_sheet("Removed - Out of Scope")
hdr(ws4,["Legacy ID","Target","Recorded Country","Recorded Acquirer","Recorded Date","Recorded Value (USD mn)","Reason for removal"],
    [11,34,18,28,14,16,110],freeze="A2")
for i,rw in enumerate(removed,2):
    for j,v in enumerate(rw,1): ws4.cell(i,j,v)
body(ws4,len(removed),7)

# ============ 5. Verification Register ============
ws5=wb.create_sheet("Verification Register")
hdr(ws5,["Legacy ID","Target","Source Block","Verdict","Finding","Source"],[11,34,26,14,100,46],freeze="A2")
reg=[]
byid={x['legacy']:x for x in recs}
seen=set()
for did,(vd,note,url) in sorted(V.items()):
    x=byid.get(did); seen.add(did)
    reg.append((did, x['tgt'] if x else '(removed - see Removed tab)', x['block'] if x else 'A (PitchBook export)', vd, note, url))
for x in recs:
    if x['legacy'] in seen or x['legacy']=='(added)': continue
    reg.append((x['legacy'], x['tgt'], x['block'], 'NOT CHECKED', 'No verification record.', x['src'] or ''))
reg.sort(key=lambda z:z[0])
for i,rw in enumerate(reg,2):
    for j,v in enumerate(rw,1): ws5.cell(i,j,v)
body(ws5,len(reg),6)
for r in range(2,len(reg)+2):
    v=str(ws5.cell(r,4).value)
    col = RED if v=='UNVERIFIED' else (AMB if 'FIX' in v or 'SCOPE' in v or 'EST' in v else (GRN if v=='OK' else None))
    if col: ws5.cell(r,4).font=Font(name=FONT,sz=9,b=True,color=col)

# ============ 6. Methodology & Limitations ============
ws6=wb.create_sheet("Methodology & Limitations")
ws6["A1"]="Europe Tab - Methodology, Scope and Limitations"
ws6["A1"].font=Font(name=FONT,sz=16,b=True,color=NAVY)
lines=[
 ("Scope rule applied",""),
 ("","EUROPEAN TARGET ONLY. The company that completed an IPO or was acquired must be European-headquartered. European acquirers buying non-European targets are out of scope (this excludes Thales/Imperva, BAE/Ball Aerospace, Rheinmetall/Loc Performance, RENK/General Kinetics and Safran/Collins actuation, all of which appear in the workbook's Master_Deals tab)."),
 ("","Period: 1 January 2023 to 2 August 2026. Rows are sorted oldest to newest by completion date, or by announcement date where a deal has not completed."),
 ("","IPOs and M&A are retained in a single table, as in the original. The 'Value Basis' column exists so the two are never summed on incompatible bases."),
 ("","Spin-off listings (TKMS) are included and flagged in Deal Structure - a company that starts trading publicly is a listing event even where no proceeds are raised."),
 ("",""),
 ("Verification coverage",""),
 ("","ALL 223 ORIGINAL ROWS WERE INDIVIDUALLY CHECKED against company press releases, exchange filings, regulatory announcements and court records. Outcomes:"),
 ("","  80 rows correct as recorded."),
 ("","  116 rows required a factual correction (date, value, stake, status, country or acquirer)."),
 ("","  18 rows carried a deal value where no party disclosed one; those values have been removed and the row marked accordingly."),
 ("","  2 rows are only partially verified (EUR-249 Burcas: acquisition confirmed, date not corroborated. EUR-261 PBH Teknik: date confirmed, value not corroborated)."),
 ("","  3 rows could not be corroborated by ANY primary source and are marked 'NO PRIMARY SOURCE LOCATED': EUR-144 Aeropolis, EUR-168 Interactive Technical Solutions, EUR-174 TEMMA. Do not cite their values or dates."),
 ("","That is a 36% clean rate across the whole tab. Within the PitchBook block (rows EUR-004 to EUR-198) the clean rate is lower; within the later primary-source block (EUR-199 to EUR-264) it is materially higher."),
 ("",""),
 ("Row reconciliation",""),
 ("","Original Europe tab: 223.  Removed under the European-target rule or as a duplicate: 5.  Verified in-scope events added: 14.  Corrected tab: 232 rows."),
 ("",""),
 ("Systematic defects found and corrected",""),
 ("","1. ANNOUNCEMENT DATES RECORDED AS COMPLETION DATES while the row read 'Completed'. The worst cases: Hamamatsu/NKT Photonics, dated 14 months early to a point when the deal had in fact been BLOCKED by the Danish government; FL Technics/JOB AIR Technic, four months late; Aubert & Duval, recorded as completed when it is still subject to regulatory approval."),
 ("","2. DEAL VALUES THAT NO PARTY DISCLOSED, presented as fact - 18 rows. Where the acquirer did disclose, the vendor figure often differed materially: ESCO/Ultra Maritime SM&P USD 472m vs USD 550m; Halma/MK Test GBP 6.9m vs GBP 44m; York/ALL.SPACE USD 355m vs USD 46.3m; W5/ArcQor SEK 102.17m vs SEK 65m."),
 ("","3. MAXIMUM EARN-OUT BOOKED AS HEADLINE VALUE without disclosure - HENSOLDT/ESG, Hexatronic/Fibron, Motherson/AD Industries, AB Dynamics/Bolab, Coats/Viz Reflectives, Scanfil/MB Elettronica, Oxford Instruments/First Light and others."),
 ("","4. MINORITY AND PARTIAL STAKES RECORDED AS 'FULL ACQUISITION' - 24 rows corrected, including Indra/TESS Defence (26.33%), Indra/Epicom (30%), Leonardo/GEM (30%-65%), CY4Gate/Diateam (55.33%), EFA/ES Systems (63.02%), Satori/MAGnetIC (80%), ENAV/AiviewGroup (85%), Orbyt/OTESAT (94.09%), Otokar/Automecanica (96.77%), Argo/Poseidon (99.55%), HEICO/Cook Defence (80%), Fincantieri's four underwater stakes (52.60%, 61.95%, 51%, 49%)."),
 ("","5. REVENUE RECORDED AS DEAL VALUE - Indutrade/Crane Electronics: the GBP 8m was Crane's annual sales, not the consideration."),
 ("","6. ONE TRANSACTION SPLIT ACROSS TWO ROWS - Al-Met and Roota Engineering were a single purchase of Pressure Technologies' PMC division (which also included Martract). Merged."),
 ("","7. CURRENCY AND UNIT ERRORS - Waterfront Fluid Controls: INR 205.624m recorded as USD 254.06m, a ~100x overstatement. CMG Technologies: USD 1,352.60m for a deal whose price was never disclosed."),
 ("","8. IPO PLACEMENT VOLUME LABELLED AS ISSUER PROCEEDS - SMAG (EUR 129.6m placement vs ~EUR 30m raised), Gabler Group (EUR 132.825m placement), Savox (EUR 57.38m vs ~EUR 30m targeted). Exosens was the largest error in the tab: EUR 1.10bn raised and EUR 3.90bn valuation recorded against an actual EUR 402.5m offering and ~EUR 1.02bn market capitalisation."),
 ("","9. WRONG ACQUIRER COUNTRY - Defence Tech Holding recorded as Polish (Italian); EFA Group as Singaporean (Greek); Sigma Advanced Systems as British (Indian, and recorded correctly two rows later)."),
 ("","10. EVENTS THAT DID NOT HAPPEN AS RECORDED - Uravi/Spafax booked as a completed 100% acquisition in June 2025 when only a 10% stake was taken in March 2026; Defence Holdings recorded inverted, where what actually changed hands was an esports business for GBP 100,000."),
 ("",""),
 ("Workbook-level issues outside this tab (flagged, not fixed)",""),
 ("","Deal IDs collide across tabs: EUR-079 to EUR-108 identify different transactions on Master_Deals than on the original Europe tab; 19 of 69 shared IDs conflict. The corrected tab uses new EU-### identifiers with the legacy ID retained, so the collision can no longer propagate through lookups."),
 ("","Master_Deals holds 71 Europe rows against the Europe tab's 223 and has never been reconciled."),
 ("","The Dashboard links to four sheets absent from the workbook: Rest_of_World, Israel IPO NOT, Israel IPO Deal Amounts and Methodology."),
 ("","The Definitions tab states that IPOs are 'not counted as core M&A', which the Europe tab's structure contradicts."),
 ("",""),
 ("How to use the value columns",""),
 ("","Deal Value (USD mn) is BLANK wherever no party disclosed a figure. A blank means unknown, not zero. Filter on Value Disclosure before any aggregation."),
 ("","Value Basis states what each figure represents: enterprise value, equity consideration, initial consideration, consideration for a partial stake, IPO gross proceeds, or total placement volume. These are not interchangeable and must not be summed together."),
 ("","Reported Consideration (local) preserves the figure as the parties stated it, in the currency they stated it in. Where the two disagree, the local figure is authoritative."),
 ("","FX conversions use period-approximate rates and are indicative only."),
]
r=3
for a,b in lines:
    if a:
        c=ws6.cell(r,1,a); c.font=Font(name=FONT,sz=11,b=True,color=MID)
    else:
        c=ws6.cell(r,1,b); c.font=Font(name=FONT,sz=10)
        c.alignment=Alignment(wrap_text=True,vertical="top")
    r+=1
ws6.column_dimensions['A'].width=170
for rr in range(3,r):
    if ws6.cell(rr,1).value and len(str(ws6.cell(rr,1).value))>110:
        ws6.row_dimensions[rr].height=None

wb.save("Europe_Corrected.xlsx")
print("saved. rows:", len(recs))
