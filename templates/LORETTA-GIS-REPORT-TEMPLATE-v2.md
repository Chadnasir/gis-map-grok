# Loretta GIS Report — Desktop Screening Template (v2)

**Version:** 2.0 — Bill GIS adoption pass (2026-10-06)
**Source v1:** Eve template from GIS report *Loretta development_compressed (2).pdf* — Leon/Scott Road four-parcel site, Riverside County (APNs 466-220-013, -014, -015, -016), prepared 09/22/2026 for Chad Nasir. Upstream: `templates/LORETTA-GIS-REPORT-TEMPLATE.md` @ commit 29956765.
**Status:** DEFAULT vacant-land / land-development desktop screening packet for Bill GIS.
**Rule:** Adapt site-specific numbers; keep sheet structure, acreage discipline, earthwork audit, disclaimers, and QA gates. No API keys in sheets or notes. Do not auto-email or auto-post maps.

---

## 1. What this packet is

- **Core nine GIS sheets** (G-001 → 3D-3) plus, when the site needs them, **companion sheets** EX-2 (utilities), GT-1 (geotech/fault screen), and a FEMA↔HELIX reconciliation memo on G-001 or as a DataSources addendum.
- Separate Tentative Tract Map (when one exists) and third-party bio/JD figures (e.g. HELIX) are companions — reproduce unchanged; never redraw as if field-verified.
- **Every GIS sheet carries the same limit:** desktop screening only — NOT a survey, geotechnical investigation, or engineered grading/drainage plan.

### Default sheet order (vacant-land screen)

| # | Sheet | Content |
|---|---|---|
| 1 | G-001 | Cover / audited findings — flood overlay, parcel index, consolidated findings, acreage bases, reconciliation flags |
| 2 | EX-1 | Existing topography — USGS 3DEP DEM, contours, sampled high/low, terrain summary |
| 3 | GR-1 | Illustrative earthwork — scenario depths, rounded CY, **slope-sign reversal audit**, yield assumption |
| 4 | HELIX Fig. 5 *(or BIO-JD-1)* | Jurisdictional features — USACE/RWQCB waters & wetlands, CDFW/MSHCP riparian riverine, pools, culverts, ditches |
| 5 | SO-1 | Soils — SSURGO map units, acres, HSG, drainage/farmland interpretations |
| 6 | HELIX Fig. 4 *(or BIO-VEG-1)* | Vegetation and land use — sensitive communities per CDFW Natural Community List |
| 7 | 3D-1 | 3D existing conditions / dimensions — perspective, frontage, notes/sources |
| 8 | 3D-2 | 3D topographic model — elevation tint + hillshade, flood overlay, vertical exaggeration stated |
| 9 | 3D-3 | 3D topo + grading — finish-grade scenario, cut/fill labels, frontage |

**Companion sheets (add when data exists; do not invent):**

| Sheet | When |
|---|---|
| EX-2 | Utilities / POCs — default companion for broker DD; QL disclosed |
| GT-1 | Fault / liquefaction / landslide / proposed borings placeholder |
| E-1 / C-1 | CEQA vicinity or constraints composite when Chad asks beyond the nine-sheet core |

Gold look: match `/home/box/skills/bill-gis-gold/` entitlement craft (04–09) and utilities craft (13). Presentation chrome: `/home/box/skills/bill-gis-template/PRESENTATION.md`. Data priority: ArcGIS first; agency sites fallback only (`bill-gis-diligence-stack.md`).

---

## 2. Cover sheet (G-001) — required elements

- **Title block:** project name, location (cross streets / area plan), APNs, area, CRS, datum, date, prepared-for, sheet number.
- **Flood callout:** zone (A/AE/X/…), acres and % of GIS analysis area, fill clipped to parcels, BFE assigned or **explicitly “no BFE”**. Cite NFHL/MSC pull date.
- **Consolidated findings sidebar:** terrain (elev range, relief, mean slope), earthwork audit status, flood/JD reconciliation flag, soils summary, planning status (zoning, GPA, yield), third-party figure note, sheet index, EX-2 / GT-1 companion note.
- **Acreage bases box:** recorded vs GIS analysis vs tract-map gross/net — label each (§5).
- **Disclaimer footer:** DESKTOP GIS SCREENING — NOT A SURVEY, GEOTECHNICAL INVESTIGATION OR ENGINEERED GRADING / DRAINAGE PLAN. Also: PRELIMINARY — NOT FOR CONSTRUCTION.

---

## 3. Terrain (EX-1) — required elements

- USGS 3DEP 1 m DEM (or better), acquisition + publication dates.
- Contours: state interval; index vs intermediate; sampled high/low with locations.
- Terrain summary: analysis area, min/max/mean elev, total relief, mean slope (Horn 3×3), area slope >15%, >25%.
- Method/data-date + interpretation: DEM is a terrain screen — not runoff, flow-routing, outlet capacity, or engineered drainage.
- Contour interval is **not** a vertical-accuracy statement.
- Craft bar: gold #14 (2D contours + hydrology); EX-1 sample in `bill-gis-template/`.

---

## 4. Earthwork (GR-1) — required elements

- Illustrative earthwork map: horizontal comparison plane; fill/cut depth classes (fill >8, >2, >0.5; near zero; cut 0.5–2, 2–8, >8); black dashed zero-cut/fill; subject outline.
- **Audit correction box (mandatory when volumes are reported):** recompute cut/fill on the **opposite** drainage direction. Near-identical volume on the reversed slope = **slope sign reversal**, not a real volume — flag and publish the corrected figure. (v1 caught ~259,000 CY on Loretta.)
- Quantities table: geometric cut, geometric fill, geometric fill space, shrink shortfall (state %), import (BCY) — yield assumption stated (e.g. 0.88 bank-to-compacted, **unverified**) and source (DEM + assessor geometry, fractional boundary-cell weights).
- Whole-site sensitivity: no environmental exclusions or engineered grading tie-ins; map does not establish a feasible grading footprint.
- Max geometric cut/fill depths labeled; engineering review required.

---

## 5. Acreage discipline (mandatory)

Always present three numbers when they differ:

1. **Recorded acres** (assessor geometry).
2. **GIS analysis acres** (fractional boundary cells).
3. **Tract-map gross / net acres** (if a TTM exists).

State which basis each quoted figure uses. Never mix bases in one sentence without labels.

---

## 6. Jurisdictional + vegetation (third-party or desktop)

**JD (HELIX Fig. 5 / BIO-JD-1):** USACE/RWQCB waters (blue) and wetlands (orange); CDFW/MSHCP riparian riverine (green); presumed connections (dashed); culverts; potential pools; man-made ditch/outfall callouts; aerial source + date. Explicit: desktop audit ≠ agency concurrence; formal delineation required before yield.

**Veg (HELIX Fig. 4 / BIO-VEG-1):** classes with sensitive communities flagged per CDFW Natural Community List (*). Source + date. On-parcel vs wider-AOI classes must not be conflated.

Gold craft: #07 JD, #08 veg, #05 alliances.

---

## 7. Soils (SO-1)

- SSURGO map units: code, name, slope range, acres, dominant HSG.
- Drainage/farmland: HSG D totals, poorly drained acreage, NRCS farmland ratings with caveat (not FMMP / Williamson Act).
- Source: USDA NRCS Soil Data Access query date.
- Gold craft: #01 soil-report density when labeling map units.

---

## 8. 3D exhibits (3D-1 / 3D-2 / 3D-3)

- Perspective labeled NOT TO SCALE; vertical exaggeration stated (3× typical).
- Frontage/dimensions from GIS geometry — not a survey.
- 3D-2: elevation tint + hillshade, flood overlay, elev-range legend.
- 3D-3: finish-grade surface for chosen scenario; cut/fill at extrema; FG formula disclosed; max cut/fill callouts.
- Notes/sources: DEM, imagery, datum, exaggeration, desktop-screening disclaimer.
- **Craft note:** Prefer gold 2D topo (#14) for primary decision sheets. 3D sheets are perspective exhibits only — never substitute for EX-1 / GR-1. No ArcGIS Urban as the deliverable bar.

---

## 9. Companion EX-2 — utilities & POCs (required companion for broker DD)

Match `bill-gis-template` EX-2 samples and gold #13 multi-utility legend.

**Required elements:**
- Map (~2/3): imagery, site boundary, wet/dry utility lines by status color, POC callout boxes with distance (ft).
- Sidebar: Legend · UtilitySummary (Utility, Provider, Nearest Main, Dist FT, Status, ASCE 38 QL, Will-Serve) · DataSources (Layer, Source, Type, Date, Native CRS).
- Title block: project, APN(s), jurisdiction, H/V datum (e.g. NAD83 CA SP VI + NAVD88), scale, sheet #, date, PRELIMINARY.
- Every feature: SOURCE / SOURCE_TYPE / SOURCE_DATE; **QL disclosed** (QL-D = records only).
- If will-serve letters are missing: state MISSING — do not invent provider concurrence.
- If no utility layer available from ArcGIS: say so, use agency/provider fallback, cite URL + date.

---

## 10. Companion GT-1 — geotech / fault screening placeholder

Desktop screen only — not a geotechnical investigation.

**Required elements when sheet is included:**
- County fault zones / Alquist-Priolo query result (count + distance to nearest mapped trace if off-site).
- Liquefaction / landslide susceptibility classes intersecting the **parcel footprints** (not centroid-only when polygons straddle classes).
- Proposed boring / perc program placeholder table (ID, purpose, approx location) — labeled PROPOSED / NOT DRILLED.
- Explicit gaps: State CGS AP polygons, sealed OSFM FHSZ, or other token-gated layers — **UNSEALED** until live extract succeeds; never invent AP/FHSZ polygons from buffers.
- DataSources + pull dates. Diligence stack: ArcGIS first; EQ Zapp / OSFM fallback with URL + date.

If Chad skips GT-1 for a given job: note “GT-1 not in this packet” on G-001 findings sidebar.

---

## 11. FEMA AE ↔ HELIX / JD creek-corridor reconciliation (mandatory checklist)

Run before G-001 flood callout is briefed as final. Record PASS / FAIL / N/A on G-001 or a one-page memo.

1. **Pull dates:** FEMA NFHL/MSC (or County REST flood) date; HELIX (or desktop NWI/NHD) figure date; imagery date if used.
2. **Geometries:** FEMA AE (or A/floodway) clipped to parcels — acres + % of GIS analysis acres. HELIX/NWI waters+wetlands+riparian acres on-parcel vs vicinity-only.
3. **Overlap test:** Does the FEMA AE polygon follow the same corridor as the JD water/wetland/riparian features? Note coincident, offset, or AE-without-JD / JD-without-AE.
4. **BFE:** Assigned or none. If none, state it. Do not invent a BFE from DEM.
5. **NHD vs JD:** On-parcel NHD count vs HELIX linework. Vicinity named washes stay **vicinity only** — never brief as “stream on property” unless on-parcel geometry proves it.
6. **Sources cited:** ArcGIS layer IDs or fallback MSC + Wetlands Mapper URLs + dates. Never invent FEMA/NWI polys with buffers.
7. **Briefing language:** One sentence for brokers: reconciled / conflict flagged / incomplete (name the gap).

---

## 12. Disclaimers (every sheet)

- DESKTOP GIS SCREENING — NOT A SURVEY, GEOTECHNICAL INVESTIGATION OR ENGINEERED GRADING / DRAINAGE PLAN.
- PRELIMINARY — NOT FOR CONSTRUCTION.
- Third-party bio/JD figures retain original content; this desktop audit does not independently verify field delineations or establish agency concurrence.
- 3D views are perspective, not to scale; vertical exaggeration applies.
- Frontage/dimensions from GIS geometry — not a survey.

---

## 13. Layout / color / legend (gold-look)

- **One theme per map pane.** No nested second parcel map inside a theme sheet.
- **Colorblind-safe** (Okabe-Ito) for fill classes; flood = blue hatch/fill consistent across G-001 / 3D-2; JD waters blue, wetlands orange, riparian green (match HELIX when reproducing).
- **Legend:** every mapped class; depth classes for GR-1; elev range for 3D-2; utility status for EX-2.
- **Chrome:** title block, north arrow, scale bar, date, DataSources, PRELIMINARY stamp.
- **Basemap:** fresh imagery or hillshade for the theme — never paste chrome onto a prior finished sheet (nested-map failure mode).
- **Labels:** short; APN last-3 or lot IDs; avoid clutter over flood spine.

---

## 14. QA gate (before any sheet leaves Bill GIS)

Packet fails QA if any item is true:

| # | Fail condition |
|---|---|
| Q1 | Any acreage quoted without basis label (recorded / GIS / tract) |
| Q2 | Earthwork volumes reported without slope-sign reversal audit box |
| Q3 | FEMA or JD acres briefed without reconciliation checklist result |
| Q4 | Invented FEMA / NWI / AP / FHSZ polygons or buffer stand-ins |
| Q5 | EX-2 present without ASCE 38 QL disclosure (or EX-2 skipped with no G-001 note) |
| Q6 | Sealed claim for a layer that returned empty, 400, or token error |
| Q7 | Nested map / chrome-on-finished-sheet |
| Q8 | Missing desktop-screening + PRELIMINARY disclaimers on any sheet |
| Q9 | API keys, tokens, or credentials in sheet text, DataSources, or commit |
| Q10 | Auto-email or auto-post of maps (forbidden) |

**PASS** = all Q1–Q10 clear. Stamp DRAFT until CoS/Chad accept. Hold client posts until asked.

---

## 15. What this template still does not replace

- Flood study with BFE; CLOMR/LOMR path.
- Formal jurisdictional delineation concurrence.
- Entitlement status beyond written County confirmation.
- Grading takeoff including strip, shrink, walls, and the flood spine as engineered quantities.
- Will-serve letters (EX-2 records status only).

---

## 16. Adoption / paths

| Location | Role |
|---|---|
| `templates/LORETTA-GIS-REPORT-TEMPLATE.md` | v1 (Eve) — keep as provenance |
| `templates/LORETTA-GIS-REPORT-TEMPLATE-v2.md` | **This file — default vacant-land screening** |
| `.grok/skills/bill-gis/SKILL.md` | Points here for nine-sheet default |
| `skills/bill-gis/SKILL.md` | Same |
| `.grok/skills/bill-gis/references/LORETTA-GIS-REPORT-TEMPLATE-v2.md` | Symlink-equivalent copy for skill-local resolve |
| `/home/box/skills/bill-gis-template/LORETTA-GIS-REPORT-TEMPLATE-v2.md` | Box presentation kit |
| `/home/box/skills/bill-gis/LORETTA-GIS-REPORT-TEMPLATE-v2.md` | Box skill mirror |

---

## 17. Change log (v1 → v2)

- Added FEMA AE ↔ HELIX/JD creek-corridor reconciliation checklist (§11).
- Promoted EX-2 utilities companion to required broker-DD companion (§9).
- Added GT-1 geotech/fault screening placeholder (§10).
- Tightened QA gate to fail/pass table (§14).
- Locked gold-look layout/color/legend rules (§13); nested-map ban.
- Clarified 3D as perspective-only; 2D EX-1/GR-1 remain decision sheets.
- Wired as default vacant-land packet in bill-gis SKILL.md (both trees).
