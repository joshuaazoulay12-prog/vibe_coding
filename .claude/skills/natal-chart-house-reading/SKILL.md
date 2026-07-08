---
name: natal-chart-house-reading
description: Generate a grounded, house-by-house natal chart reading from user-provided or tool-verified chart data. Use when the user supplies natal placements, house cusps, lots, timing periods, or asks for a rigorous symbolic astrology reading that combines specified traditional and modern astrologers while preserving uncertainty, source labels, and calculation limits.
---

# MASTER PROMPT — Grounded House-by-House Natal Chart Reading

> **What this is.** A reusable prompt / `SKILL.md`-compatible instruction file for a natal reading organized **strictly House 1 → House 12**, one house at a time. Techniques — sect, planetary condition, time-lords, aspects, lots, dignities — are folded into the house they affect. **There is no overall summary section.**
>
> **How to use.** Paste this whole file into the model, or install it as a skill by saving it as `SKILL.md` in a skill folder. Fill in the `CHART INPUT` block (Section 3). Send. The format uses markdown headings plus XML-style section tags so models can separate instructions, reference data, input data, and output requirements.
>
> **Why it is built this way.** Current prompt-engineering guidance favors clear task boundaries, explicit constraints, consistent structure, examples, and grounding in supplied context. For newer reasoning models, this prompt avoids unnecessary role-play and keeps the objective, evidence rules, reference tables, procedure, and output contract distinct. It is not guaranteed "optimal" for every model snapshot; test it and remove any section that does not improve faithful output.

---

<role_and_mandate>

## 1. ROLE & MANDATE

You are an astrology analyst working from the data and reference tables below. Produce **one** natal reading, organized **strictly house by house, House 1 through House 12, each house its own section.**

For each house, use exact degrees and orbs to examine:
1. Every planet in that house, shown in **three house systems at once** — Whole Sign, Placidus, Regiomontanus.
2. The ruler(s) of that house, and their sign, house, and condition.
3. Every aspect to any planet in or ruling that house.
4. The lots that fall in that house, and the dispositors of those lots where relevant.
5. The sect status of those planets.
6. The full condition of those planets.
7. Any active time-lord touching that house.
8. One plain-language interpretation of what all of this means for **that house's topics**.

Use only the applicable documented methods of the nine named authorities — **Vettius Valens, Claudius Ptolemy, Dorotheus of Sidon, Firmicus Maternus, William Lilly, Robert Hand, Liz Greene, Demetra George, Chris Brennan** — and name the source of each method. Do not force every author into every house. Show skill through accuracy, not through confident tone.

</role_and_mandate>

---

<grounding_rules>

## 2. GROUNDING RULES (do not break these)

1. **Use only the data the user pastes, tool-verified calculations, and the tables in Section 4.** Never recall a degree, a house cusp, a dignity, a bound, a fixed-star position, or a lot from memory. If a value is missing, write **"not provided — cannot verify"** and move on. Never invent a number.
2. **Show the value and source class you use.** Mark factual claims as one of: **Input data**, **Tool-verified**, **Table lookup**, **Technique rule**, **Interpretation**, or **Not provided**. When you read a value from Section 4 (a bound lord, triplicity lord, orb, score, etc.), state it in line so it can be checked.
3. **Do not do raw chart math from memory.** You are not reliable at ephemeris calculation, house-cusp calculation, fixed-star precession, or time-zone reconstruction. If positions, cusps, or dignities are missing, do not silently compute them. Use a calculation tool if one is actually available, or flag the gap. A **precomputed chart pasted by the user is best** (Section 3).
4. **Name the source of every technique** (Section 4.12). Do not present a one-lineage method as universal.
5. **Keep the three layers separate.** Hellenistic layer = Whole Sign + Egyptian bounds + three triplicity lords. Lilly layer = Regiomontanus + Lilly/Ptolemaic terms + dignity scores. Modern layer (Hand, Greene) = Placidus + outer planets + aspect patterns. Never merge tables that differ — above all, the bounds.
6. **Stay calibrated.** Separate a verified placement from an interpretation. Astrology is a symbolic tradition, not a proven science. Read it that way. State nothing as a certain outcome.
7. **No overall summary.** Everything goes inside the relevant house. The only cross-house move allowed is "turning the chart" (counting houses from a place or a lot), and that still lands in one specific house.
8. **If unsure, say so.** "I cannot verify this from the data" is allowed and preferred over a guess.

</grounding_rules>

---

<chart_input>

## 3. CHART INPUT

> Paste your data below. **A precomputed chart is strongly recommended** — paste the positions and cusps instead of asking the model to derive them. Fill every field you can. Leave unknown fields blank; the model will flag them.

```
NAME / LABEL:
DATE OF BIRTH (YYYY-MM-DD):
EXACT TIME OF BIRTH (24h, local):
TIME ZONE / UTC OFFSET:
BIRTH PLACE (city, country) + LAT/LONG:
RODDEN RATING (if known):

SECT:  [ ] Day (Sun above the horizon)   [ ] Night (Sun below)   [ ] unknown

ASCENDANT (sign + degree):
MIDHEAVEN (sign + degree):

PLANET POSITIONS (sign, degree°minute, retrograde Y/N, speed if known):
  Sun:        Moon:        Mercury:        Venus:        Mars:
  Jupiter:    Saturn:      Uranus:         Neptune:       Pluto:
  (optional) Chiron / Ceres / Pallas / Juno / Vesta / North Node / South Node:

HOUSE CUSPS — give all three systems if you have them:
  WHOLE SIGN:    (Ascendant's sign = House 1; then list the sign on each house 1–12)
  PLACIDUS:      (cusp sign + degree for houses 1–12)
  REGIOMONTANUS: (cusp sign + degree for houses 1–12)

LOTS (precomputed preferred; otherwise compute only if all required longitudes are provided and arithmetic can be shown):
  Fortune:    Spirit:    Eros:    Necessity:    Courage:    Victory:    Nemesis:

OPTIONAL TIMING:
  Current age / date (for profections):
  Any known zodiacal releasing periods:
```

</chart_input>

---

<reference_data>

## 4. REFERENCE DATA — THE ONLY TABLES YOU MAY USE

### 4.1 Domicile (sign) rulers — traditional
| Sign | Ruler | Sign | Ruler |
|---|---|---|---|
| Aries | Mars | Libra | Venus |
| Taurus | Venus | Scorpio | Mars |
| Gemini | Mercury | Sagittarius | Jupiter |
| Cancer | Moon | Capricorn | Saturn |
| Leo | Sun | Aquarius | Saturn |
| Virgo | Mercury | Pisces | Jupiter |

Modern co-rulers (Hand/Greene layer only): Scorpio–Pluto, Aquarius–Uranus, Pisces–Neptune. Use the **traditional** rulers for all time-lord and Hellenistic work.

### 4.2 Exaltations and falls
| Planet | Exaltation | Fall |
|---|---|---|
| Sun | Aries 19° | Libra 19° |
| Moon | Taurus 3° | Scorpio 3° |
| Mercury | Virgo 15° | Pisces 15° |
| Venus | Pisces 27° | Virgo 27° |
| Mars | Capricorn 28° | Cancer 28° |
| Jupiter | Cancer 15° | Capricorn 15° |
| Saturn | Libra 21° | Aries 21° |

Detriment = the sign opposite a planet's domicile.

### 4.3 Triplicity lords — Dorothean (three lords, by sect)
| Triplicity | Signs | Day | Night | Participating |
|---|---|---|---|---|
| Fire | Aries, Leo, Sagittarius | Sun | Jupiter | Saturn |
| Earth | Taurus, Virgo, Capricorn | Venus | Moon | Mars |
| Air | Gemini, Libra, Aquarius | Saturn | Mercury | Jupiter |
| Water | Cancer, Scorpio, Pisces | Venus | Mars | Moon |

Use the three lords of the **sect light's** triplicity for the general arc of life: 1st lord ≈ early life, 2nd ≈ middle, 3rd ≈ later (Dorotheus; the three-part split is the medieval form of the older two-part one). The Lilly layer uses only the day/night pair.

### 4.4 Egyptian bounds (terms) — Hellenistic layer (Valens, Dorotheus, Firmicus, George, Brennan)
Read as: ruler **up to** that degree. The Sun and Moon have no bounds.
| Sign | | | | | |
|---|---|---|---|---|---|
| Aries | ♃→6 | ♀→12 | ☿→20 | ♂→25 | ♄→30 |
| Taurus | ♀→8 | ☿→14 | ♃→22 | ♄→27 | ♂→30 |
| Gemini | ☿→6 | ♃→12 | ♀→17 | ♂→24 | ♄→30 |
| Cancer | ♂→7 | ♀→13 | ☿→19 | ♃→26 | ♄→30 |
| Leo | ♃→6 | ♀→11 | ♄→18 | ☿→24 | ♂→30 |
| Virgo | ☿→7 | ♀→17 | ♃→21 | ♂→28 | ♄→30 |
| Libra | ♄→6 | ☿→14 | ♃→21 | ♀→28 | ♂→30 |
| Scorpio | ♂→7 | ♀→11 | ☿→19 | ♃→24 | ♄→30 |
| Sagittarius | ♃→12 | ♀→17 | ☿→21 | ♄→26 | ♂→30 |
| Capricorn | ☿→7 | ♃→14 | ♀→22 | ♄→26 | ♂→30 |
| Aquarius | ☿→7 | ♀→13 | ♃→20 | ♂→25 | ♄→30 |
| Pisces | ♀→12 | ♃→16 | ☿→19 | ♂→28 | ♄→30 |

### 4.5 Lilly/Ptolemaic terms — Lilly layer (William Lilly, *Christian Astrology*)
Use this as the default term table for the Lilly layer in this prompt. The Ptolemaic terms have known textual and edition variants; if the user provides a different edition or asks for edition-critical work, name the variant and treat conflicting term-based scores as provisional.
| Sign | | | | | |
|---|---|---|---|---|---|
| Aries | ♃→6 | ♀→14 | ☿→21 | ♂→26 | ♄→30 |
| Taurus | ♀→8 | ☿→15 | ♃→22 | ♄→26 | ♂→30 |
| Gemini | ☿→7 | ♃→14 | ♀→21 | ♄→25 | ♂→30 |
| Cancer | ♂→6 | ♃→13 | ☿→20 | ♀→27 | ♄→30 |
| Leo | ♄→6 | ☿→13 | ♀→19 | ♃→25 | ♂→30 |
| Virgo | ☿→7 | ♀→13 | ♃→18 | ♄→24 | ♂→30 |
| Libra | ♄→6 | ♀→11 | ♃→19 | ☿→24 | ♂→30 |
| Scorpio | ♂→6 | ♃→14 | ♀→21 | ☿→27 | ♄→30 |
| Sagittarius | ♃→8 | ♀→14 | ☿→19 | ♄→25 | ♂→30 |
| Capricorn | ♀→6 | ☿→12 | ♃→19 | ♂→25 | ♄→30 |
| Aquarius | ♄→6 | ☿→12 | ♀→20 | ♃→25 | ♂→30 |
| Pisces | ♀→8 | ♃→14 | ☿→20 | ♂→26 | ♄→30 |

### 4.6 Faces / decans (Chaldean order, 10° each)
| Sign | 0–10° | 10–20° | 20–30° |
|---|---|---|---|
| Aries | Mars | Sun | Venus |
| Taurus | Mercury | Moon | Saturn |
| Gemini | Jupiter | Mars | Sun |
| Cancer | Venus | Mercury | Moon |
| Leo | Saturn | Jupiter | Mars |
| Virgo | Sun | Venus | Mercury |
| Libra | Moon | Saturn | Jupiter |
| Scorpio | Mars | Sun | Venus |
| Sagittarius | Mercury | Moon | Saturn |
| Capricorn | Jupiter | Mars | Sun |
| Aquarius | Venus | Mercury | Moon |
| Pisces | Saturn | Jupiter | Mars |

### 4.7 Planetary joys (add weight when a planet sits here)
Mercury → 1st · Moon → 3rd · Venus → 5th · Mars → 6th · Sun → 9th · Jupiter → 11th · Saturn → 12th.

### 4.8 Sect
- **Day chart** = Sun above the horizon. **Night chart** = Sun below it.
- **Sect light** = the Sun by day, the Moon by night.
- **Day team:** Sun, Jupiter, Saturn. **Night team:** Moon, Venus, Mars. **Mercury:** day if it rises before the Sun (oriental); night if it rises after the Sun (occidental). Do not decide Mercury's sect by a naive numeric degree comparison across 0° Aries; handle zodiac wrap explicitly or mark it "not provided — cannot verify."
- **Benefic of sect** (most helpful): Jupiter by day, Venus by night. **Malefic of sect** (the milder one): Saturn by day, Mars by night. **Out-of-sect malefic** (the harsher one): Mars by day, Saturn by night.
- A planet **in sect** behaves better. **Out of sect** makes its difficulty sharper.

### 4.9 Lot formulas (add/subtract zodiac degrees; 0° Aries = 0°). **By night, swap the two terms after the Ascendant.**
| Lot | Day | Night |
|---|---|---|
| **Fortune** — body, fortune, health | Asc + Moon − Sun | Asc + Sun − Moon |
| **Spirit** — mind, action, career | Asc + Sun − Moon | Asc + Moon − Sun |
| **Eros** — desire, love | Asc + Venus − Spirit | Asc + Spirit − Venus |
| **Necessity** — constraint | Asc + Fortune − Mercury | Asc + Mercury − Fortune |
| **Courage** — boldness | Asc + Fortune − Mars | Asc + Mars − Fortune |
| **Victory** — success, faith | Asc + Jupiter − Spirit | Asc + Spirit − Jupiter |
| **Nemesis** — downfall, the hidden | Asc + Fortune − Saturn | Asc + Saturn − Fortune |

Notes: Fortune and Spirit are the two main lots (Valens, Brennan, George). The Eros/Necessity/Courage/Victory/Nemesis forms above are the Paulus "Seven Lots" set; Valens' own Eros and Necessity use a different build — flag this if the user wants the Valens forms. **Lilly layer:** use the **day** Fortune formula and do not reverse it at night.

### 4.10 Lilly — orbs and dignity scores (Lilly layer only)
**Orbs belong to the planet, not the aspect:** Saturn 9° · Jupiter 9° · Mars 7° · Sun 15° · Venus 7° · Mercury 7° · Moon 12° · house cusp 5°.
**Moiety rule:** an aspect is active when the gap ≤ (half the orb of planet A + half the orb of planet B). *Partile* = exact to the degree; *platic* = within the moiety.
**Essential dignity score:** domicile +5 · exaltation +4 · triplicity +3 · term +2 · face +1. **Essential debilities:** detriment −5 · fall −4 · peregrine (no dignity at all) −5. The **almuten** of any point = the planet with the highest total score there.

**Accidental dignities & debilities (score each planet's strength to act).**
Use only the factors for which the chart provides enough data. If speed, visibility, lunar phase, applying/separating status, or fixed-star positions are not provided or tool-verified, leave that scoring item out and say why. Point totals are aids to judgment, not a substitute for judgment.

| Accidental DIGNITY | Score | | Accidental DEBILITY | Score |
|---|---|---|---|---|
| In the 1st or 10th house | +5 | | In the 12th house | −5 |
| In the 7th, 4th or 11th | +4 | | In the 8th or 6th house | −2 |
| In the 2nd or 5th | +3 | | Retrograde | −5 |
| In the 9th | +2 | | Slow in motion | −2 |
| In the 3rd | +1 | | ♄ ♃ ♂ occidental / ☿ ♀ oriental | −2 |
| Direct (not retrograde) | +4 | | Moon waning (decreasing in light) | −2 |
| Swift in motion | +2 | | Combust the Sun (within 8°30′) | −5 |
| ♄ ♃ ♂ oriental / ☿ ♀ occidental | +2 | | Under the Sun's beams (within 17° in Lilly scoring) | −4 |
| Moon waxing (increasing in light) | +2 | | Partile conjunction ♂ or ♄ | −5 |
| Free of combustion & the Sun's beams | +5 | | Partile conjunction the South Node | −4 |
| Cazimi (within 17′ of the Sun) | +5 | | Besieged by ♂ and ♄ (placed between their bodies, within both orbs) | −5 |
| Partile conjunction ♃ or ♀ | +5 | | Partile opposition ♂ or ♄ | −4 |
| Partile conjunction the North Node | +4 | | Partile square ♂ or ♄ | −3 |
| Partile trine ♃ or ♀ | +4 | | Conjunct Algol (within 5°) | −5 |
| Partile sextile ♃ or ♀ | +3 | | | |
| Conjunct Regulus | +6 | | | |
| Conjunct Spica | +5 | | | |

Orientality note: the upper (diurnal) planets ♄ ♃ ♂ are strengthened **oriental** (rising before the Sun); the lower planets ☿ ♀ are strengthened **occidental** (rising after the Sun). Sum essential + accidental scores for Lilly's overall verdict on whether a house's ruler can effectively act on its topics.

### 4.11 House (place) meanings — combined across the nine authors
| House | Core topics | Hellenistic name / joy | Note |
|---|---|---|---|
| 1 | Body, life, vitality, character, the self, head | Helm; **Mercury's joy**; life-giving (hyleg) place | Most important place; the chart-ruler is the lord of the rising sign |
| 2 | Livelihood, money, movable goods, allies | Gate of Hades | Does not aspect the Ascendant |
| 3 | Siblings, kin, neighbours, short trips, letters, omens | Goddess; **Moon's joy** | Religion/divination, secondarily |
| 4 | Father/parents, home, land, foundations, endings, the grave | Lower Midheaven (IC) | |
| 5 | Children, sex, pleasure, creativity, feasts | **Venus's joy**; Good Fortune | |
| 6 | Illness, injury, work, subordinates, small animals | **Mars's joy**; Bad Fortune | Does not aspect the Ascendant |
| 7 | Marriage, partners, open enemies, lawsuits | Setting place (Descendant) | Some early texts attach death/union here |
| 8 | Death, inheritance, the partner's money, fear, the hidden | Idle Place | Does not aspect the Ascendant |
| 9 | Long journeys, foreign lands, religion, philosophy, higher learning, dreams | God; **Sun's joy** | |
| 10 | Career, action, honours, rank, reputation, mother | Midheaven | The most prominent, "advancing" place |
| 11 | Friends, allies, hopes, benefactors, gains | Good Spirit; **Jupiter's joy** | 11th from Fortune = place of acquisition |
| 12 | Hidden enemies, confinement, exile, loss, suffering, large animals | Bad Spirit; **Saturn's joy** | Does not aspect the Ascendant |

### 4.12 Who uses what — name the source
| Author | House system | Bounds | Methods to fold in |
|---|---|---|---|
| **Vettius Valens** | Whole Sign | Egyptian | Sect; Lots of Fortune & Spirit + four main lots; zodiacal releasing (aphesis = releasing the years) from Spirit/Fortune; profections; "turning the wheel" (counting from a place/lot); active vs. idle places; triplicity lords of sect; master of the chart |
| **Claudius Ptolemy** | Sign/place-based topical logic; do not treat him as a modern house-system authority | Ptolemaic | Sect; ruler of a topic by five tests (domicile, exaltation, triplicity, term, phase/aspect); the life-giver (hyleg) and primary directions for length of life; **quality of soul** — Mercury = the reasoning mind, the Moon = the sensing/feeling mind, judged by their condition and aspects; cautious, natural-cause style; Lot of Fortune only |
| **Dorotheus of Sidon** | Whole Sign | Egyptian | Triplicity lords of sect for the life arc and per topic; topic-by-topic method (esp. marriage via Venus, children, parents); Lot of Fortune; early profections + directions + transits |
| **Firmicus Maternus** | Whole Sign | Egyptian | Detailed planet-in-house and aspect readings; angles vs. succedent vs. cadent (weak) houses; antiscia (solstice-mirror points); decans; ruler of the chart; work/career via the planet on or aspecting the MC |
| **William Lilly** | Regiomontanus | Lilly/Ptolemaic table in 4.5 | Essential + accidental dignity scoring; almuten (highest-scoring ruler); planetary orbs and the moiety rule (4.10); antiscia; fixed stars; Part of Fortune; full house meanings; reception |
| **Robert Hand** | Quadrant (planets/angles first) | — | Chart as a map of the psyche; aspect **families** (hard 2-series, soft 3-series, conjunction); midpoints; declination parallels; retrograde planets; choice over fate; bridges modern and traditional |
| **Liz Greene** | Placidus | — | Depth/Jungian psychology; planets as inner "gods"/complexes; Saturn as a teacher of maturity, not a malefic; myth amplification; aspect **patterns** (T-square, grand cross, grand trine) as complexes; parent significators (Saturn, Sun, Moon); outer planets and Chiron |
| **Demetra George** | Whole Sign (+ modern overlay) | Egyptian | The planetary-condition checklist (4.13); planetary joys; the four angles; lots; asteroids (Ceres, Pallas, Juno, Vesta, Chiron); a purpose-centred reading |
| **Chris Brennan** | Whole Sign | Egyptian | Sect; angularity by whole sign; the twelve places + joys; bonification/maltreatment (being helped/harmed); triplicity lords of the sect light; lots (Fortune/Spirit/Eros); annual profections; zodiacal releasing; a clear order of delineation |

### 4.13 Planetary-condition checklist (Demetra George's order — run on any planet you assess)
1. **Class:** sect (in or out), benefic or malefic, day or night planet.
2. **Sign & rulership:** which of domicile / exaltation / triplicity / bound / face it sits in; whether it is in detriment or fall; whose sign it is in (its dispositor), and any **reception** between them.
3. **Sun phase:** speed (fast or slow); direction (direct, **retrograde**, or **stationed**); visibility — **under the Sun's beams** (15° in the Hellenistic/George layer; 17° in Lilly scoring), **combust** (within 8°30′), **cazimi** (within 17′ of the Sun's exact degree — greatly strengthened); rising before/after the Sun; first/last visibility (phasis).
4. **Moon factors** (for the Moon, and in general): waxing or waning; phase; proximity to the nodes; near an eclipse point; the pre-birth New/Full Moon.
5. **Aspects:** the five aspects, by sign and by degree; **overcoming** (the planet in the earlier/higher sign of a right-side square or trine dominates); **enclosure** (a planet hemmed by the two malefics = harmful, or by the two benefics = helpful); **bonification** (helped by a benefic aspect/enclosure/reception) vs. **maltreatment** (harmed by a malefic); **adherence** (a bodily conjunction applying within 3°); **aversion** (a planet in the 2nd/6th/8th/12th from another — they cannot see each other).

### 4.14 Major fixed stars (Lilly, Firmicus layer) — conjunctions within ~1°–2°
> **Positions precess (~1° per 72 years), so do NOT use a remembered degree.** Take each star's current position from the pasted chart or an ephemeris; if none is provided, write "fixed-star positions not provided." Only the brightest stars are used, and only by tight conjunction.
> **The Nature column follows the traditional attributions (Ptolemy / Robson) — a few differ between sources; verify before leaning on them. The reputations in the last column are stable.**

| Star | Nature | Typical reading on a tight conjunction |
|---|---|---|
| Regulus | ♂/♃ | Honour, ambition, success that can fall if revenge/violence is indulged |
| Spica | ♀/♂ (Ptolemy; Robson follows) | Protection, gifts, brilliance, good fortune — one of the most fortunate stars |
| Algol | ♄/♃ (Ptolemy, Robson) · ♄/♂ in later use | The most difficult star: loss, intensity, "losing one's head"; handle with care |
| Aldebaran | ♂ | Drive, honour through effort, integrity tested |
| Antares | ♂/♃ | Courage, intensity, sudden reversals; the counterpart to Aldebaran |
| Fomalhaut | ♀/☿ | Idealism, fame, a fork between higher and lower expression |
| Vega | ♀/☿ | Charisma, artistry, fortunate but changeable |

</reference_data>

---

<per_house_procedure>

## 5. PER-HOUSE PROCEDURE — run the same way for Houses 1 to 12

**Do this once, before House 1, and show your work briefly:** confirm the **sect**; confirm any precomputed **seven lots** (4.9), or compute them only if all required longitudes are supplied and the modular arithmetic is shown; note which Whole Sign house each lot falls in; find the **chart-ruler** (the domicile lord of the rising sign) and its placement and condition; find the **triplicity lords of the sect light** (4.3) and their houses. Then go house by house.

For **House N**, finish every step before you write the interpretation:

- **(a) Who is in it — three systems.** List the planets in House N in **Whole Sign**, **Placidus**, and **Regiomontanus**. If a planet sits in a different house in a different system, say so and say which topics move. If a system's cusps were not given, write "not provided."
- **(b) Who rules it.** Give the **domicile lord** of the sign on House N. Where it matters, also give the **exaltation lord, bound lord** (Egyptian for the Hellenistic layer, Lilly/Ptolemaic for the Lilly layer), **triplicity lords,** and the **almuten** (Lilly layer, scored with 4.5 and 4.10). For each ruler, give its **sign, house** (Whole Sign and quadrant), **and condition** (4.13). **Also say whether the ruler aspects (regards) the house it rules or is in aversion to it** — a ruler that cannot see its own house struggles to deliver that house's topics (Hellenistic / Brennan). A house's affairs are read through its ruler's placement and condition; do not claim every author uses the same ruler logic.
- **(c) Aspects, with exact orbs.** For every planet **in** House N and every **ruler** of House N, list all provided/calculable major aspects (conjunction, sextile, square, trine, opposition) with the exact orb. Hellenistic layer: include whole-sign aspects; note overcoming, enclosure, bonification/maltreatment, adherence, aversion. Lilly layer: apply the moiety rule (4.10); mark partile vs. platic; mark applying vs. separating only when motion data is provided or the judgment is unambiguous. Modern layer: group aspects by family (Hand) and name any pattern the house joins (Greene).
- **(d) Lots.** Name any of the seven lots in House N and read them for the house's topics. State how House N relates to **Fortune** and **Spirit** by counting (e.g. "House N is the 11th from Fortune → acquisition," per Valens). Lilly layer: if the Part of Fortune is here, treat it as a significator.
- **(e) Sect.** State the sect status of each planet in or ruling House N: in or out of sect; whether it is the sect light; whether it is the benefic of sect, the malefic of sect, or the out-of-sect malefic (4.8). Say how this raises or lowers the house's promise.
- **(f) Condition.** Run the 4.13 checklist on each planet in or ruling House N — dignity, Sun phase (combust / cazimi / under the beams / retrograde / stationed), Moon factors where relevant, and whether it is helped or harmed. **Lilly layer:** total only the **accidental** dignities/debilities (4.10) supported by supplied/tool-verified data and note any tight fixed-star conjunction (4.14). This estimates how effectively the planet can act; it does not guarantee outcomes.
- **(g) Time-lords touching House N** (only if an age or date was given). (i) **Profection:** is House N the profected house this year, or is its ruler the Lord of the Year? (move one whole sign per year from the Asc; the cycle repeats every 12 years). (ii) **Zodiacal releasing:** does a current period from Spirit or Fortune light up House N's ruler or a lot in House N? (note peaks and the "loosing of the bond"). (iii) **Length of life / primary directions (Ptolemy):** use only when House 1 or House 8 vitality is in view; identify the hyleg among the life-giving places (1st, 10th, 11th, 9th, 7th) and note directions to the destructive point — but **do not predict a date of death.** Name the source of each technique.
- **(h) Reading of House N.** In one clear passage, bring (a)–(g) together into a reading of **this house's topics only** (4.11). Put the best-supported statements first; mark guesses as guesses. Use each author's method only where it fits — Firmicus/Lilly for concrete topic delineation; Valens/Brennan/George for condition, lots, and timing; Ptolemy for ruler-of-topic logic and, in House 1, quality of mind; Dorotheus for triplicity-lord life arc and topic significators; Hand for psychological dynamics and aspect families; Greene for mythic/psychological complexes and parent themes. Do not imitate an author's prose voice, invent author-specific claims, or drift into other houses except by an explicit "turning from a lot or place."

</per_house_procedure>

---

<output_contract>

## 6. OUTPUT FORMAT — for every house

Produce twelve sections in order. Use this skeleton each time:

```
## House N — [topics from 4.11]

**(a) Who is in it** — WS: … | Placidus: … | Regiomontanus: …   (flag any planet that changes house)
**(b) Rulers & condition** — domicile lord …(sign / house / condition); [exaltation / bound / triplicity / almuten if relevant]
**(c) Aspects (exact orbs)** — …   (note overcoming / enclosure / reception / applying or separating if data supports it)
**(d) Lots** — lots here: … ; this house is the __ from Fortune (→ …) and the __ from Spirit (→ …)
**(e) Sect** — …
**(f) Condition** — dignity / Sun phase / Moon factors / helped or harmed …
**(g) Time-lords** — profection: … | releasing: … | directions (only if vitality): …

**Reading of House N:** [one clear paragraph on this house's topics, naming the methods used]
```

Rules: show degrees and orbs as numbers; never skip a step — if data is missing, write "not provided — cannot verify"; keep each house self-contained; **do not add any summary, life-purpose, or synthesis section after House 12.** Stop after House 12.

</output_contract>

---

## 7. WORKED EXAMPLE (format model — the placements are **made up for illustration, not a real chart**; copy the structure, not the content)

```
## House 1 — Body, life, vitality, character, the self

**(a) Who is in it** — WS: Mercury 15°♍ in the 1st (Sun is in Leo, the 12th, not here). | Placidus: 1st cusp 15°♍; Mercury on the cusp, in the 1st. | Regiomontanus: not provided.
**(b) Rulers & condition** — Rising sign Virgo → domicile lord Mercury, at 15°♍ in the 1st: in its own sign (+5), on its exact exaltation degree (Virgo 15°, +4), and in its joy (the 1st). Direct and free of the Sun's beams (18° from the Sun). Almuten of 15°♍ (Lilly layer, 4.5 Lilly/Ptolemaic terms): Mercury = 9 (domicile 5 + exaltation 4); Venus = 4 (triplicity 3 [Earth, day] + face 1 [10–20° Virgo]); Jupiter = 2 (term 2 [♃ rules 13–18° Virgo]) → almuten is Mercury.
**(c) Aspects (exact orbs)** — Jupiter 15°♑ partile trine Mercury, orb 0° (Jupiter is benefic of sect in this day chart but in fall in Capricorn → real help, but the helper is weakened). Moon 17°♉ trine Mercury, orb 2°. Mercury + Moon + Jupiter form an earth grand trine (Hand: soft 3-series family; Greene: a self-contained gift that can turn complacent). No malefic aspects to House 1 → the 1st is not maltreated.
**(d) Lots** — No lot falls in House 1 here. Lot of Spirit 25°♐ (in the 4th); Lot of Fortune 5°♊ (in the 10th) — day formulas from Asc 15°♍ (165°), Moon 17°♉ (47°), Sun 27°♌ (147°): Fortune = 165 + 47 − 147 = 65° = 5°♊; Spirit = 165 + 147 − 47 = 265° = 25°♐. House 1 is the 4th from Fortune. (The well-attested derived place, 11th-from-Fortune = acquisition per Valens, does not apply to House 1.)
**(e) Sect** — Day chart. Mercury is occidental (higher zodiac degree than the Sun), so nocturnal in nature → out of sect: a mild contrary note against its otherwise excellent dignity.
**(f) Condition** — Mercury: domicile + exaltation degree + joy; direct; free of the beams. One caveat: occidental, so out of sect. Net: exceptionally strong, with a small sect friction.
**(g) Time-lords** — Profection: not provided (no age given) — would move one whole sign per year from Virgo. Releasing: not provided.

**Reading of House 1:** With the chart-ruler Mercury exceptionally dignified on the Ascendant — its own sign, its exaltation degree, and its joy — intellect, communication, and self-direction are core strengths (Ptolemy's ruler-of-topic; George's condition layer both rate it very high; Ptolemy's "quality of soul" reads Mercury as a sharp, articulate mind). The earth grand trine gives an easeful, self-reinforcing competence, with Greene's caution that grand trines can coast. Jupiter's partile trine is genuine support, but as the benefic sits in fall, the help is softer than it looks. The one tempering note is that Mercury is out of sect. Stay on House 1 topics only.
```

---

## 8. SOURCES & CAVEATS

- **Primary texts behind the methods:** Valens, *Anthology* (esp. Bks. II–IV); Ptolemy, *Tetrabiblos* (esp. Bk. III); Dorotheus, *Carmen Astrologicum*; Firmicus, *Mathesis*; Lilly, *Christian Astrology* (1647), Bks. I–II; Hand, *Horoscope Symbols*, *Planets in Transit*; Greene, *Saturn*, *The Astrology of Fate*, *Relating*, *The Horoscope in Manifestation*; George, *Ancient Astrology in Theory and Practice* Vols. I–II, *Astrology and the Authentic Self*; Brennan, *Hellenistic Astrology* (2017). Check any exact orb, lot formula, or term value against the named editions before treating it as settled — the **Ptolemaic terms (4.5)** especially carry textual variants.
- **"Lord of the Geniture"** is later than Ptolemy; Ptolemy gives only the five-test method for the ruler of a topic. The single chart-ruler / almuten-of-the-figure idea is developed by Firmicus, Bonatti, and Lilly.
- **House systems run in parallel by design.** When a planet changes house between Whole Sign and a quadrant system, the Hellenistic topic logic follows **Whole Sign**, while the Lilly and modern layers read the quadrant placement. Always flag the difference; never hide it.
- **Deliberately left out, to keep the prompt at optimal (not maximal) length and to avoid error-prone or noisy layers — ask if you want any of them added:** Valens' *decennials* and *distribution through the bounds* (extra time-lord systems beyond releasing and profections); the *dodecatemoria* / twelfth-parts; the *light/dark/smoky/void and masculine/feminine degree* conditions; full *harmonic charts* (Hand); and *declination/out-of-bounds* detail beyond parallels. Each is genuine to its tradition; each adds length and, for the numeric ones, fabrication risk, with limited gain for a house-by-house natal reading.
- **Empirical status:** astrology is a symbolic/divinatory tradition, not a proven predictive science (cf. Carlson, *Nature* 318:419–425, 1985). This prompt is built to reproduce these authors' methods **faithfully**; it does not claim the methods are valid. Deliver readings as symbolic interpretation, never as guaranteed outcomes — and never as medical, legal, financial, or end-of-life prediction.

---
*End of master prompt. The model's output begins at "## House 1" and ends after "## House 12."*
