# LORETTA GIS Desk Companion v1

**Lane:** Chief of Staff / broker desk (not Bill GIS sheet work)  
**Pairs with:** `LORETTA-GIS-REPORT-TEMPLATE.md` (template v1 = commit `29956765fc17352c7f760b8dbe5ffdf0e287f99d`)  
**Canonical template:** https://github.com/Chadnasir/gis-map-grok/blob/main/templates/LORETTA-GIS-REPORT-TEMPLATE.md  
**Desk mirror:** `/home/box/agent-data/workflows/cre-desk-library/gis-screening/`  
**Companion version:** v1 (versions independently of the nine-sheet template)  
**Adopted:** 2026-10-06 PT  
**Bill GIS agent:** `1f3440d5-08b9-42d1-a6ec-13a0986e039d` (owns GIS skill / sheet production / `LORETTA-OUTPUT-LOOK-HARD-RULE.md`)  
**Limits:** No CRM writes. No Chad approvals. Missing mandatory evidence = HELD. Do not duplicate Bill GIS skill or hard-rule commits.

---

## HARD RULE (CHAD AMENDMENT 2026-10-06 — supersedes prior; non-negotiable)

All future vacant-land GIS screening deliverables on the CRE desk **MUST MATCH the Loretta report OUTPUT LOOK exactly**.

- **Mandatory default = Loretta look.** Nine sheets required, no skipping:
  1. G-001 cover (G-prefix cover required)
  2. EX-1 topo
  3. GR-1 earthwork
  4. HELIX Fig. 5 jurisdictional
  5. SO-1 soils
  6. HELIX Fig. 4 vegetation
  7. 3D-1
  8. 3D-2
  9. 3D-3
- **G-prefix cover AND all three 3D sheets required** — no skipping.
- **3D design is APPROVED.** Do not propose dropping or redesigning 3D.
- **Any proposal to deviate** (fewer sheets, no 3D, different chrome) = **HELD** pending Chad's explicit approval.
- Bill GIS owns `templates/LORETTA-OUTPUT-LOOK-HARD-RULE.md` and the bill-gis skill. CoS wires desk pointers only; do not duplicate those commits.

### HARD RULE 2 — TOOL PIPELINE (CHAD URGENT FOLLOW-UP 2026-10-06)

Mandatory for **all 3D sheets**. All four tools required; skip any = huge gap = **HELD for Chad**:

1. **QGIS** — geometry, elevation tint, hillshade, contours, FEMA overlay, finish-grade surface
2. **Blender** — 3D render (3x vertical exaggeration, perspective)
3. **Higgsfield** — image generation / polish on 3D renders
4. **Grok image generator** — final polish / composite

Any GIS screening task must specify this four-tool pipeline. Proposal to skip a tool (e.g. "just QGIS") = **HELD** pending Chad's explicit approval.

Both hard rules sit **above** the three broker improvements below.

---

## Improvement 1 — One-page buyer-diligence checklist (what this template does NOT cover)

Screening PASS ≠ production start. Items below stay **HELD** until named evidence exists. Do not imply they were cleared by the nine-sheet GIS screen.

| Gap (not covered by screening template) | HELD until evidence |
|-----------------------------------------|---------------------|
| Utilities capacity / will-serve (EX-2 and beyond) | Written utility will-serve / capacity letters (or documented N/A with source) |
| Geotech / fault / liquefaction | Licensed geotech report or jurisdiction fault/liquefaction study on file |
| BFE / CLOMR-LOMR / flood map change | FEMA BFE determination and any CLOMR-LOMR package, or documented N/A |
| Formal wetland / waters delineation concurrence | Agency concurrence (or verified negative with source date) |
| Written entitlement confirmation | Jurisdiction written confirmation of zoning / entitlement path (not GIS layer alone) |
| Engineered grading takeoff | Engineer-stamped grading / earthwork takeoff (screening slope/cut-fill is not a takeoff) |

**Rule:** Screening PASS does not authorize production, pricing as shovel-ready, or buyer assurance that the gaps above are closed. Missing any mandatory evidence row for the deal scope → **HELD**.

---

## Improvement 2 — Standard acreage-quote script (buyer calls)

Always state **recorded**, **GIS analysis**, and **tract-map gross/net** separately. Never mix unlabeled acres on a call or in a brief.

**Spoken lines a broker can use:**

1. "We quote three acreage bases separately — recorded deed acres, GIS analysis acres, and tract-map gross versus net — and we never blend them without labels."
2. "The recorded figure is what the deed/assessor shows; the GIS figure is our analysis polygon; tract-map gross/net comes from the recorded map, not from the GIS screen alone."
3. "If any of those three is missing or unlabeled on the sheet, we treat acreage as HELD for buyer quotes until the basis box is complete."

**Broker risk:** Unlabeled mixing of recorded vs GIS vs tract-map acres is a Gate 1 / diligence fail. Acreage-basis box required on land screening packs.

---

## Improvement 3 — Template versioning + Gate 1 evidence rule

| Item | Rule |
|------|------|
| Template v1 | Eve commit `29956765fc17352c7f760b8dbe5ffdf0e287f99d` (nine-sheet Loretta look) |
| Sheet-structure change | Any change to the nine-sheet set / structure / chrome **bumps template version** and is **HELD for Chad** under the HARD RULE until approved. CoS does not silently edit Eve’s / Bill’s template. |
| Desk companion | Versions **independently** (this file = companion v1). Companion improvements do not rewrite Bill’s sheets. |
| Gate 1 (land / vacant-land GIS screening) | Requires **named template version** + **acreage-basis box** + **earthwork audit-correction box** present, or each marked **explicitly N/A with reason**, **and** pack matches Loretta OUTPUT LOOK (nine sheets including G-001 + 3D-1/2/3). Otherwise **HELD**. |

Gate 1 still requires Chad’s explicit approval of property, research, and scope. This companion only defines desk evidence minimums; it does not grant approval.

---

## Ownership reminder

- **Bill GIS** (`1f3440d5-08b9-42d1-a6ec-13a0986e039d`): GIS-side skill, sheet production, output-look hard rule, template sheet structure.  
- **Chief of Staff:** This companion, desk workflow pointers, Gate 1 coordination evidence checks.  
- Loretta vacant-land project row: NOT FOUND in Notion (2026-10-06). Do not invent a page. Do not conflate APN 394 assemblage with Loretta 466-220.
