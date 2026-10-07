# Loretta OUTPUT LOOK — HARD RULE (Chad 2026-10-06)

**Status:** NON-NEGOTIABLE for every future vacant-land GIS screening deliverable.
**Authority:** Chad Nasir direct (via Derek Route + Chief of Staff), 2026-10-06. Supersedes any softer “default / prefer / optional 3D” language.
**Canonical content provenance (Eve v1):** `templates/LORETTA-GIS-REPORT-TEMPLATE.md` @ git `29956765fc17352c7f760b8dbe5ffdf0e287f99d` (raw SHA `6385b96904c9ed69908f5391fefd757cd7a79a8e92ef2901aa6ed62efb2197bb`).
**GIS structure + audit adds:** `templates/LORETTA-GIS-REPORT-TEMPLATE-v2.md` (FEMA↔HELIX checklist, EX-2, GT-1, QA) — **on top of** this look, never replacing it.
**CoS lane:** desk brief/tools/training, broker-side companions, Gate-1 HELD discipline. Bill GIS does **not** own those commits.

---

## HARD RULE — two parts (both required)

### (A) Nine-sheet OUTPUT LOOK — match Loretta exactly

Every vacant-land screening packet **must** deliver these nine sheets **in this order**. No skip. No merge. No “optional 3D.” Deviate = **HELD** for Chad (FAIL, not a soft miss).

| # | Sheet | Required content |
|---|---|---|
| 1 | **G-001** | Cover / audited findings — flood overlay, parcel index, consolidated findings sidebar, acreage bases, title block |
| 2 | **EX-1** | Existing topography — DEM, contours, sampled high/low, terrain summary |
| 3 | **GR-1** | Illustrative earthwork — depth classes, quantities, **slope-sign reversal audit** |
| 4 | **HELIX Fig. 5** | Jurisdictional features (or site-equivalent JD figure) — waters/wetlands/riparian; HELIX caveat when third-party |
| 5 | **SO-1** | Soils — SSURGO units, acres, HSG, drainage/farmland |
| 6 | **HELIX Fig. 4** | Vegetation / land use (or site-equivalent) — sensitive community flags |
| 7 | **3D-1** | 3D existing conditions / dimensions — perspective, frontage, notes |
| 8 | **3D-2** | 3D topographic model — elev tint + hillshade, FEMA AE overlay, VE 3× |
| 9 | **3D-3** | 3D topo + grading — finish-grade surface, cut/fill labels |

**G-001 cover AND all three 3D sheets are mandatory.** Chad approved the 3D design. Do not argue against 3D. Opinions against 3D are out of scope.

**Chrome (every sheet):**
- Map left (~2/3); sidebar tables / legend / notes right
- Full title block: project, APNs, area, CRS, datum, date, prepared-for, sheet #
- North arrow + scale bar (2D sheets); 3D sheets: perspective labeled **NOT TO SCALE**, vertical exaggeration **3×** stated
- Footer every sheet: **PRELIMINARY — NOT FOR CONSTRUCTION** plus desktop-screening disclaimer
- Gold-look styling (see `/home/box/skills/bill-gis-gold/` craft 04–09 / 13 / 14)

**Content rules still mandatory (from Loretta / v2):**
- Three acreage bases labeled (recorded / GIS analysis / tract)
- Earthwork slope-sign reversal check when volumes reported
- FEMA AE (or applicable zone) + BFE stated or “no BFE”
- HELIX / third-party JD+veg caveat (not field-verified / no agency concurrence)
- HSG / drainage / farmland interpretations with FMMP caveat
- Sensitive veg flags per CDFW Natural Community List

Companion sheets (EX-2 utilities, GT-1 geotech) may be **added** after the nine; they never replace a core sheet.

---

### (B) Four-tool 3D pipeline — MANDATORY (order + ownership)

Chad: use these tools or there will be a huge gap. Template way required.

**3D-1 / 3D-2 / 3D-3 must use the full pipeline in order.** QGIS alone is **not** enough.

| Stage | Tool | Ownership / what it produces |
|---|---|---|
| 1 | **QGIS** | Real geometries only: parcels, elevation tint, hillshade, contours, FEMA AE, finish-grade surface, cut/fill rasters/vectors. Source of truth for geometry and elevation. |
| 2 | **Blender** | 3D render: tint+hillshade draped, **3×** vertical exaggeration, perspective camera. |
| 3 | **Higgsfield** | Polish on Blender 3D renders. |
| 4 | **Grok image generator** | Final polish / composite into sheet chrome. |

**Skip any stage = FAIL / HELD.** Do not deliver the packet.

**Fallback (document explicitly, never silent):**
- If **Higgsfield** is unavailable: record the outage, substitute **Grok image generator** for polish stage 3+4, and still require **QGIS + Blender**.
- QGIS + Blender are **never** optional.
- Never drop a stage silently. Missing evidence stays **HELD**.

---

## QA gate — 3D provenance (before delivery)

For **each** of 3D-1, 3D-2, 3D-3, verify and record:

| Check | Pass criteria |
|---|---|
| QGIS source | Path or export ID for geometry / elev tint / hillshade / FEMA / FG as applicable |
| Blender | Render file / frame for that sheet |
| Higgsfield | Run/job ID **or** documented unavailable + Grok-substitute note |
| Grok image gen | Final composite used on the sheet |

Missing any stage for any 3D sheet → **do not deliver**; flag HELD with the missing stage named.

Also fail delivery if:
- Any of the nine sheets missing or reordered
- Chrome missing title block / PRELIMINARY footer
- Acreage bases unlabeled, earthwork without slope-sign audit (when CY reported), inventing FEMA/NWI/AP/FHSZ buffers
- API keys in output; auto-email or auto-post of maps

---

## Skill pointers

- `.grok/skills/bill-gis/SKILL.md`
- `skills/bill-gis/SKILL.md`
- Box mirror: `/home/box/skills/bill-gis/SKILL.md`
- This file: `templates/LORETTA-OUTPUT-LOOK-HARD-RULE.md`

---

## Change log

- 2026-10-06 — Chad HARD RULE: nine-sheet look + G/3D mandatory; 3D design approved; four-tool pipeline QGIS→Blender→Higgsfield→Grok; QA provenance; Higgsfield fallback documented.
