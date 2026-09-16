# Riverside County project GIS maps (made by others)

County of Riverside TLMA / RCIT / Flood Control / RCA maps used on live land-development projects. Not city of Irvine boards.

## County research viewers (open these first)

| Map | Who | URL | What a developer uses it for |
|---|---|---|---|
| **Map My County (MMC) Public** | RCIT GIS | https://gis1.countyofriverside.us/Html5Viewer/index.html?viewer=MMC_Public | Parcel → zoning, GP land use, specific plan, MSHCP, airport, fire, flood, PLUS case # |
| RCIT GIS Hub | RCIT | https://rcitgis-countyofriverside.hub.arcgis.com/ | Open data + app index |
| What’s My Zoning | TLMA Planning | https://planning.rctlma.org/whats-my-zoning | How to run MMC |
| My Survey Research | County Surveyor | https://www.arcgis.com/apps/webappviewer/index.html?id=26ab70d308c349dd934b1b65378c6544 | Recorded maps, tract maps, ROS, hanging files, ROW |
| Survey GIS tools index | RivCo Transportation | https://trans.rctlma.org/frequently-asked-questions/gis-research-tools-web-maps | Road Book, geodetic control, hanging-file mosaic |
| RivCoView assessor maps | Assessor | https://www.rivcoacr.org/AssessorMaps | 21,000+ assessor plat PDFs |
| PLUS Activities download | RCIT | https://rcitgis-countyofriverside.hub.arcgis.com/pages/data-distribution | Live planning cases / developments |

MMC search keys a project GIS needs: APN, address, **LMS case number**, specific plan, township/range.

## Constraints GIS that every RivCo project hits

| Map | Who | URL |
|---|---|---|
| Floodplain Viewer (FEMA + DWR + RCFC Ordinance 458) | Riverside County Flood Control | https://content.rcflood.org/floodplainmap |
| Flood Control GIS page | RCFCWCD | https://rcflood.org/geographic-information-systems |
| RCA MSHCP Information Tool | Western Riverside County RCA | https://experience.arcgis.com/experience/379b037fb33b4cc0ad8849c5dca76db6 |
| RCA maps index | WRC-RCA | https://www.wrc-rca.org/rcamaps/ |
| WR-MSHCP program | TLMA | https://planning.rctlma.org/epd/wr-mshcp |
| General Plan Land Use layer | RCIT Open Data | https://gis.countyofriverside.us/arcgis_mapping/rest/services/OpenData/General/MapServer/230 |
| Parcels | RCIT | https://gis.countyofriverside.us/arcgis_mapping/rest/services/OpenData/Assessor/MapServer/40 |

Static download pack also includes: Specific Plan polygons, Zoning, Airport Influence / Compatibility, Fire Hazard Severity, Liquefaction, Faults, Farmland, Criteria Area / Narrow Endemic Plants, Burrowing Owl cells, Desert Tortoise, RCA conserved lands.

## Named County projects (study their plan maps, then verify in MMC)

| Project | What it is | Official page |
|---|---|---|
| Villages of Lakeview SP00342 | 2,883 ac, up to 8,725 DU + 1.38M sf commercial, 1,106 ac conservation | https://planning.rctlma.org/villages-lakeview-specific-plan-sp00342 |
| Specific Plan 380 (French Valley) | ~200 ac master plan; EIR upheld *Residents Against SP 380 v. County of Riverside* | County case files / CEQA Chronicles writeup |
| County Planning project list | Current + advance planning cases | https://planning.rctlma.org/projects |
| County General Plan + Area Plans | Blueprint maps (use MMC for parcel truth) | https://planning.rctlma.org/riverside-county-general-plan |

City-in-county examples often confused with County cases (still RivCo geography):
- Goodman Commerce Center, Eastvale (WEBB) — 200 ac warehouses + retail: https://webbassociates.com/projects/goodman-commerce-center/
- City of Riverside cumulative projects GIS: https://riversideca.gov/cedd/planning/development-projects-and-ceqa-documents

## How the bot should copy RivCo project GIS

1. Start in MMC on the project APN / LMS case.
2. Draw the **parcel + specific-plan planning areas**, not a radius.
3. Overlay MSHCP criteria cells / conserved lands, Ordinance 458 floodplain, airport compatibility, fire hazard.
4. Cite PLUS case number and SP number in the title block.
5. Conservation acreage is a polygon from RCA, not a green wash.
