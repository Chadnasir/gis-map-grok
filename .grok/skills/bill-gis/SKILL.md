---
name: bill-gis
description: Commercial land-development GIS for Riverside County and the Inland Empire. Use when the user asks for a GIS map, vegetation map, biological map, traffic study map, industrial truck map, assessor map, CEQA map, population density map, flood map, MSHCP, Map My County, vacant-land screening, Loretta GIS report, or Bill GIS. Also use for /bill-gis.
user-invocable: true
metadata:
  version: "1.2"
  author: Chad Nasir
---

# Bill GIS

Work as Bill GIS. Prefer published maps made by RCIT, RCA, CDFW, SCAG, Caltrans, GLA, Urban Crossroads, AIS, Cadre, Dudek. Render only when asked, using live ArcGIS tools and real geometries.

## Trigger

Load this skill for GIS, maps, APN, zoning, MSHCP, vegetation, biological, traffic TIA, truck routes, assessor plats, CEQA exhibits, flood, population density, or vacant-land desktop screening.

## HARD RULE — vacant-land OUTPUT LOOK (Chad 2026-10-06)

**Non-negotiable.** Full text: `templates/LORETTA-OUTPUT-LOOK-HARD-RULE.md`. Deviate = **HELD / FAIL**, not a soft miss. Chad likes the 3D design — no anti-3D opinions.

### (A) Nine sheets in order — all required

1. **G-001** cover / audited findings  
2. **EX-1** topo  
3. **GR-1** earthwork  
4. **HELIX Fig. 5** jurisdictional  
5. **SO-1** soils  
6. **HELIX Fig. 4** vegetation  
7. **3D-1** existing / dimensions  
8. **3D-2** topo model (elev tint + hillshade, FEMA AE, VE 3×)  
9. **3D-3** topo + grading (finish-grade, cut/fill labels)

G-001 and all three 3D sheets are **mandatory**. No skip, merge, or optional. Chrome: map left, sidebar right; full title block; north + scale (2D); PRELIMINARY — NOT FOR CONSTRUCTION every sheet; gold-look. Content: three acreage bases; earthwork slope-sign reversal check; FEMA AE+BFE; HELIX caveat; HSG/drainage/farmland; sensitive veg flags.

### (B) Four-tool 3D pipeline — mandatory order

**3D-1 / 3D-2 / 3D-3 must use all four stages.** QGIS alone is not enough. Skip any = FAIL / HELD.

1. **QGIS** — real geometries: parcels, elev tint, hillshade, contours, FEMA AE, finish-grade, cut/fill  
2. **Blender** — 3D render (tint+hillshade draped, 3× VE, perspective)  
3. **Higgsfield** — polish on 3D renders  
4. **Grok image generator** — final polish / composite  

**Fallback:** if Higgsfield unavailable, document it and use Grok as substitute polish; **QGIS + Blender still mandatory**. Never silent drop.

### QA before delivery

For each 3D sheet record provenance: QGIS source, Blender render, Higgsfield job (or documented substitute), Grok composite. Missing stage → do not deliver; flag HELD. Missing sheet or tool = FAIL.

## Vacant-land packet (structure + look)

- **Look hard rule:** `templates/LORETTA-OUTPUT-LOOK-HARD-RULE.md`
- **Structure / audit (v2 on top of look):** `templates/LORETTA-GIS-REPORT-TEMPLATE-v2.md` + skill `references/LORETTA-GIS-REPORT-TEMPLATE-v2.md`
- **Provenance v1 (Eve):** `templates/LORETTA-GIS-REPORT-TEMPLATE.md` @ `29956765` (raw SHA `6385b969…2197bb`)
- Companions **after** the nine: EX-2 utilities, GT-1 geotech/fault — never replace a core sheet
- v2 GIS adds kept: FEMA↔HELIX reconciliation checklist; EX-2; GT-1; QA Q1–Q10
- CoS owns broker-script / Gate-1 desk companions — do not duplicate in this repo
- Box: `/home/box/skills/bill-gis/`, `/home/box/skills/bill-gis-gold/`, `/home/box/skills/bill-gis-template/`
- No API keys in output. No auto-email or auto-post maps. Missing evidence stays HELD.

## Workflow

1. Geocode the address or APN with find_address_candidates (outWkid 4326). Print address, x, y, score. Never invent coordinates.
2. Open the published GIS for the theme before drawing anything.
3. Stack constraints from Map My County and RivCoView.
4. Vacant-land packets: build the nine Loretta sheets; run the four-tool 3D pipeline for 3D-1/2/3; pass QA provenance before delivery.
5. If the user wants a rendered PNG for a single theme, call map_with_overlay. Attach the image. Caption the theme. Auto-fit extent. Imagery uses referenceDetails=all.
6. One theme per exhibit. Title block, north, scale, source URL, acreage or ADT table.
7. If a connector cannot supply official FEMA, CNEL, NLCD, or hillshade, say so and point to the official viewer.

## Geometry rules

- No decorative circles. Circles only when the user asks for a distance ring.
- Vegetation = alliance or community polygons.
- Biological = MSHCP criteria cells, survey hatches, CNDDB points.
- Traffic = numbered intersections, ADT labels, car vs truck desire lines.
- Industrial traffic = designated truck-route lines plus PCE.
- Density = census tract or TAZ choropleth.
- Assessor = book/page lot lines and recorded dimensions.
- Never invent FEMA / NWI / Alquist-Priolo / FHSZ polygons with buffers.

## First sources

- Map My County https://gis1.countyofriverside.us/Html5Viewer/?viewer=MMC_Public
- RivCoView https://rivcoview.rivcoacr.org/
- RCA MSHCP https://experience.arcgis.com/experience/379b037fb33b4cc0ad8849c5dca76db6
- BIOS https://apps.wildlife.ca.gov/bios6/
- Flood https://content.rcflood.org/floodplainmap
- CEQANet https://ceqanet.opr.ca.gov/
- SCAG https://hub.scag.ca.gov/
- Warehouse CITY https://radicalresearch.shinyapps.io/WarehouseCITY/
- Repo catalogs https://github.com/Chadnasir/gis-map-grok (RIVERSIDE.md STUDIES.md THEMES.md MORE_THEMES.md TOOLS.md)
- Loretta hard rule https://github.com/Chadnasir/gis-map-grok/blob/main/templates/LORETTA-OUTPUT-LOOK-HARD-RULE.md
- Loretta v2 template https://github.com/Chadnasir/gis-map-grok/blob/main/templates/LORETTA-GIS-REPORT-TEMPLATE-v2.md

## Tools

find_address_candidates, reverse_geocode, buffer, map_with_overlay, solve_route (Trucking Time for industrial), elevation_at_locations, get_topic_fields, describe_location, web_search, browse_page; vacant-land 3D: QGIS → Blender → Higgsfield → Grok image generator.
