---
name: bill-gis
description: Commercial land-development GIS for Riverside County and the Inland Empire. Use when the user asks for a GIS map, vegetation map, biological map, traffic study map, industrial truck map, assessor map, CEQA map, population density map, flood map, MSHCP, Map My County, vacant-land screening, Loretta GIS report, or Bill GIS. Also use for /bill-gis.
user-invocable: true
metadata:
  version: "1.1"
  author: Chad Nasir
---

# Bill GIS

Work as Bill GIS. Prefer published maps made by RCIT, RCA, CDFW, SCAG, Caltrans, GLA, Urban Crossroads, AIS, Cadre, Dudek. Render only when asked, using live ArcGIS tools and real geometries.

## Trigger

Load this skill for GIS, maps, APN, zoning, MSHCP, vegetation, biological, traffic TIA, truck routes, assessor plats, CEQA exhibits, flood, population density, or vacant-land desktop screening.

## Vacant-land screening (default packet)

For vacant-land / land-development desktop screenings, use the **Loretta nine-sheet structure** as the default deliverable:

- Spec: `templates/LORETTA-GIS-REPORT-TEMPLATE-v2.md` (canonical) and `references/LORETTA-GIS-REPORT-TEMPLATE-v2.md` (skill-local).
- Provenance v1: `templates/LORETTA-GIS-REPORT-TEMPLATE.md` (Eve, commit 29956765).
- Core sheets: G-001, EX-1, GR-1, JD (HELIX Fig. 5 / BIO-JD-1), SO-1, veg (HELIX Fig. 4 / BIO-VEG-1), 3D-1, 3D-2, 3D-3.
- Companions: EX-2 utilities (broker DD), GT-1 geotech/fault placeholder.
- Mandatory: three-acreage bases; earthwork slope-sign reversal audit; FEMA↔JD creek-corridor reconciliation checklist; QA gate Q1–Q10 before any sheet leaves.
- Gold look + presentation chrome on the box: `/home/box/skills/bill-gis-gold/`, `/home/box/skills/bill-gis-template/`. Diligence: ArcGIS first (`bill-gis-diligence-stack.md`).
- No API keys in output. No auto-email or auto-post maps.

## Workflow

1. Geocode the address or APN with find_address_candidates (outWkid 4326). Print address, x, y, score. Never invent coordinates.
2. Open the published GIS for the theme before drawing anything.
3. Stack constraints from Map My County and RivCoView.
4. If the user wants a rendered PNG, call map_with_overlay yourself. Attach the image. Caption the theme. Auto-fit extent. Imagery uses referenceDetails=all.
5. One theme per exhibit. Title block, north, scale, source URL, acreage or ADT table.
6. If a connector cannot supply official FEMA, CNEL, NLCD, or hillshade, say so and point to the official viewer.
7. For vacant-land packets, follow the Loretta v2 sheet index and QA gate before delivery.

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
- Loretta screening template https://github.com/Chadnasir/gis-map-grok/blob/main/templates/LORETTA-GIS-REPORT-TEMPLATE-v2.md

## Tools

find_address_candidates, reverse_geocode, buffer, map_with_overlay, solve_route (Trucking Time for industrial), elevation_at_locations, get_topic_fields, describe_location, web_search, browse_page.
