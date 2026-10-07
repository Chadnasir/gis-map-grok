# Loretta OUTPUT LOOK — HARD RULE (Chad 2026-10-06)

**Status:** NON-NEGOTIABLE for every future vacant-land GIS screening deliverable.
**Authority:** Chad Nasir direct (via Derek Route + Chief of Staff), 2026-10-06. Supersedes any softer “default / prefer / optional 3D” language.
**Canonical content provenance (Eve v1):** `templates/LORETTA-GIS-REPORT-TEMPLATE.md` @ git `29956765fc17352c7f760b8dbe5ffdf0e287f99d` (raw SHA `6385b96904c9ed69908f5391fefd757cd7a79a8e92ef2901aa6ed62efb2197bb`).
**GIS structure + audit adds:** `templates/LORETTA-GIS-REPORT-TEMPLATE-v2.md` (FEMA↔HELIX checklist, EX-2, GT-1, QA) — **on top of** this look, never replacing it.
**CoS lane:** desk brief/tools/training, broker-side companions, Gate-1 HELD discipline. Bill GIS does **not** own those commits.

---

## HARD RULE — four parts (all required)

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

### (B) 3D pipeline — FINAL HARD ORDER (Chad 2026-10-06)

**Order is locked:** **QGIS → Blender → Higgsfield → ReRender**.

| Stage | Tool | Ownership / what it produces |
|---|---|---|
| 1 | **QGIS** | Real geometries only: parcels, elevation tint, hillshade, contours, FEMA AE, finish-grade surface, cut/fill rasters/vectors. Source of truth for geometry and elevation (LiDAR DEM when available — see §C). |
| 2 | **Blender** | 3D render: tint+hillshade draped, **3×** vertical exaggeration, perspective camera. **NON-SUBSTITUTABLE.** |
| 3 | **Higgsfield** | First polish on Blender 3D renders. **Mandatory before ReRender. Do not drop.** |
| 4 | **ReRender** | Second polish **after** Higgsfield. Required on **client deliverables**. |

**Skip any stage = FAIL / HELD.** Do not deliver the packet.

**Rules:**
- **Blender is NON-SUBSTITUTABLE.** No 3D sheet without a Blender render in provenance. Do **not** replace Blender with QGIS 2D/3D exports, Higgsfield alone, ReRender alone, Grok image gen alone, ArcGIS Urban, or any other tool. Missing Blender = **FAIL / HELD**.
- **Higgsfield is mandatory before ReRender.** Do not skip or remove Higgsfield. ReRender does **not** replace Higgsfield, QGIS, or Blender.
- **ReRender goes AFTER Higgsfield** — never before, never instead of.
- On **client deliverables**, missing ReRender provenance = **FAIL**.
- Optional final composite into sheet chrome may still use Grok image generator **after** ReRender; it never replaces stages 1–4.
- Never drop a stage silently. Missing evidence stays **HELD**.

**ReRender plan tier (TBD — Chad):**
- Free vs Pro **not yet confirmed**.
- If **Pro with commercial rights** confirmed → note here; allow client-facing ReRender outputs.
- If **free tier only** → watermarked frames are **internal-draft only**; **Pro required for client deliverables**. Flag HELD on client packets that rely on free-tier watermarked ReRender.

---

### (C) USGS 3DEP LiDAR POINT CLOUD — MANDATORY data source (Chad 2026-10-06)

**Same weight as (A) nine-sheet structure and (B) 3D pipeline.**

#### Source (public domain — US Government, no license cost)
- Registry: https://registry.opendata.aws/usgs-lidar/
- Public EPT (no AWS account): `s3://usgs-lidar-public` (us-west-2) — `aws s3 ls --no-sign-request s3://usgs-lidar-public/`
- Requester-pays raw LAZ: `s3://usgs-lidar` — only if public EPT lacks tiles
- STAC: https://usgs-lidar-stac.s3-us-west-2.amazonaws.com/ept/catalog.json
- Tools: PDAL / QGIS read LAZ; PDAL reads EPT; LidarExplorer https://www.usgs.gov/tools/lidarexplorer

#### Rules
1. **Download LAZ (or EPT crop) covering the site AOI** before EX-1 / GR-1 / 3D terrain work. Store under `/workspace/lidar/<site>/` (or repo `lidar/`) with README: project name, survey date, point density, CRS, download command, file list + sizes + SHA256.
2. **Authoritative elevation where available:** generate LiDAR-derived DEM (PDAL or QGIS Processing). Compare to USGS 3DEP 1 m DEM. Report vertical Δ at sampled high/low. If material change to earthwork (GR-1) or Scenario B slope numbers → recompute and **flag**.
3. **3D concept / 3D-1/2/3:** Blender terrain must use LiDAR-derived surface when LiDAR covers the site. Document LiDAR provenance in the 3d-concept README (alongside design-source provenance).
4. **DataSources row on EVERY sheet** (title block / DataSources table): include USGS 3DEP LiDAR project name, survey year, density, CRS, and tile/path citation.
5. **QA gate:** any deliverable missing the LiDAR DataSources row = **FAIL / HELD**.

#### Riverside County coverage note (verified 2026-10-06)
- Named `USGS_LPC_CA_Riverside_B1_2019` / `B2_2019` cover **eastern** RivCo only — do **not** assume they cover western city / Menifee sites.
- Indiana Avenue (−117.50, 33.88) and Scott/Leon Menifee (~−117.12, 33.64) fall in **`USGS_LPC_CA_SoCal_Wildfires_B1_2018_LAS_2019`** (STAC geometry verified). Always confirm with STAC/LidarExplorer per site.

---

## QA gate — 3D provenance (before delivery)

For **each** of 3D-1, 3D-2, 3D-3, verify and record **in order**:

| Check | Pass criteria |
|---|---|
| QGIS source | Path or export ID for geometry / elev tint / hillshade / FEMA / FG as applicable |
| Blender | Render file / frame for that sheet — **required; no substitute** |
| Higgsfield | Run/job ID — **mandatory before ReRender; do not drop** |
| ReRender | Run/job ID — **required on client deliverables** (missing = FAIL) |
| LiDAR | DataSources row citing USGS 3DEP LiDAR project + path (when site covered) |

Missing any stage for any 3D sheet → **do not deliver**; flag HELD with the missing stage named.

Also fail delivery if:
- Any of the nine sheets missing or reordered
- Chrome missing title block / PRELIMINARY footer
- Acreage bases unlabeled, earthwork without slope-sign audit (when CY reported), inventing FEMA/NWI/AP/FHSZ buffers
- API keys in output; auto-email or auto-post of maps
- Missing USGS 3DEP LiDAR DataSources row on any sheet
- LiDAR available for site but EX-1/GR-1/3D terrain ignores it without documented HELD
- Missing Higgsfield provenance before ReRender
- Missing ReRender provenance on a client deliverable
- Pipeline order violated (ReRender before Higgsfield, or either before Blender)

---

## Blender (non-substitutable)

Chad (2026-10-06): "make sure Blender is also used."

- Every **3D-1 / 3D-2 / 3D-3** sheet must include a **Blender** render in provenance (tint+hillshade draped on real QGIS geometry, **3×** VE, perspective).
- **No fallback skips Blender.** Higgsfield and ReRender are polish stages only; they never replace Blender.
- Forbidden substitutes for Blender: QGIS renders alone, Grok/Higgsfield/ReRender image gen alone, ArcGIS Urban/3D, screenshots of other viewers.
- QA: missing Blender render for any 3D sheet = **FAIL / HELD**.

## Skill pointers

- `.grok/skills/bill-gis/SKILL.md`
- `skills/bill-gis/SKILL.md`
- Box mirror: `/home/box/skills/bill-gis/SKILL.md`
- This file: `templates/LORETTA-OUTPUT-LOOK-HARD-RULE.md`

---

## Change log

- 2026-10-06 — Chad HARD RULE: nine-sheet look + G/3D mandatory; 3D design approved; pipeline QGIS→Blender→Higgsfield→Grok; QA provenance; Higgsfield fallback documented.
- 2026-10-06 follow-up — Blender NON-SUBSTITUTABLE for 3D-1/2/3; no Blender skip; polish-only fallback for Higgsfield.
- 2026-10-06 — Chad HARD RULE: USGS 3DEP LiDAR point cloud mandatory data source; LiDAR DEM authoritative where available; DataSources LiDAR row QA = FAIL if missing.
- 2026-10-06 — Chad: ReRender added as post-Higgsfield polish; pipeline FINAL ORDER = QGIS→Blender→Higgsfield→ReRender; both polish stages required in provenance; missing ReRender on client deliverable = FAIL; Higgsfield mandatory before ReRender; tier TBD (free = draft-only / Pro for client).
