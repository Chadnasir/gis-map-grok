# Commercial-grade land development reference maps

Do NOT train on homemade buffer-circle maps. These are the sheets professionals actually stamp, file, and finance against.

## A. Due-diligence / entitlement maps (first look)

| Map | Why it is commercial-grade | Open this |
|---|---|---|
| City of Irvine General Plan Land Use (36x36) | Official adopted land-use polygons, planning areas, intensity codes | https://gis.cityofirvine.org/pdf/Map%20Gallery/Land-Use_Color_36x36_2023.pdf |
| City of Irvine Zoning Map (36x36) | Geocode + zoning district polygons. This is the regulatory base. | http://gis.cityofirvine.org/pdf/Map%20Gallery/Zoning-Map_36x36_20190401.pdf |
| Irvine Planning Areas | Master-planned community districts (PA 1–51) | http://gis.cityofirvine.org/pdf/Map%20Gallery/Planning%20Areas_11x17_landscape.pdf |
| Irvine PA aerial | Same districts on imagery | http://gis.cityofirvine.org/pdf/Map%20Gallery/AerialIrvine2016.pdf |
| Irvine PA 38 Westpark II tract & parcel map | Recorded tract numbers, lot lines, parks, wash | https://gis.cityofirvine.org/pdf/PA%20Tract%20Maps/PA38_20220822.pdf |
| Irvine GIS map gallery | Full official set | http://gis.cityofirvine.org/irvinegis/pdfmaps.html |
| FEMA Flood Map Service Center | Effective FIRM panels — Zone A/AE/VE/X, floodway, BFE | https://msc.fema.gov/portal/home |
| FEMA NFHL | Seamless digital FIRM for GIS | https://hazards.fema.gov/femaportal/NFHL/searchResult/ |
| USFWS NWI Wetlands Mapper | Cowardin wetland polygons | https://fws.gov/wetlands/data/mapper.html |
| USGS The National Map / US Topo | Contours, hydro, NAIP | https://www.usgs.gov/tools/national-map-viewer |
| USDA Web Soil Survey (SSURGO) | Map-unit soils, hydric, hydrologic group | https://websoilsurvey.sc.egov.usda.gov/ |
| Esri developable-land map | Land-to-improvement value choropleth | https://www.esri.com/en-us/arcgis/products/arcgis-online/developable-land |

## B. Survey and civil plan-set sheets (what gets stamped)

Standard US commercial set follows National CAD Standard:

| Sheet | What it shows | Live example |
|---|---|---|
| Cover / G-000 | Title, vicinity, sheet index, zoning table, seals | Chipotle Maple Grove plan set: http://maplegrovemn.gov/AgendaCenter/ViewFile/Item/4865?fileID=17886 |
| ALTA/NSPS Land Title Survey | Bearings/distances, monuments, easements, improvements, Table A | 2026 standards: https://altalandsurvey.com/wp-content/uploads/2026/05/2026-ALTA-NSPS-Standards.pdf |
| Existing conditions / demolition | What stays, what is removed | Same Chipotle set, C1.1 |
| Site plan C-2 | Boundary, setbacks, building footprint, parking, driveways, fire access | Longview TX official template: https://www.longviewtexas.gov/DocumentCenter/View/13808/Development-Site-Plan-Template |
| Grading & drainage C-3 | Existing/proposed contours, spots, slopes, basins | Brylee North Eagle Mountain: https://www.utah.gov/pmn/files/1042783.pdf |
| Utility plan C-4 | Water, sewer, storm, gas, electric, easements | Denton Plaza II McCrone: https://dentonmaryland.com/wp-content/uploads/2023/04/Web-Site-Plan.pdf |
| SWPPP / erosion control | Construction BMPs, stabilized entrance | Chipotle set C5 |
| Landscape L-1 | Planting, irrigation, buffers | Chipotle set L1 |
| Tentative tract map | Proposed lots, streets, open space stats | OC Ranch Plan packet: https://ocds.ocpublicworks.com/sites/ocpwocds/files/2021-06/TT%20Checklist%20Package%20(Ranch)%206-9-2021.pdf |
| PUD master concept plan | Tracts, lakes, buffers, land-use table | Fort Myers 662-acre MCP: https://images1.showcase.com/d2/SHcGUs90iNDHGl91jGMHtbwLg8drRCfFXrJyyxilYPA/document.pdf |
| Constraints exhibit | Wetland line, floodplain, slopes, easements overlaid on one sheet | New Berlin WI set with delineated wetland: https://www.newberlinwi.gov/DocumentCenter/View/15925/PLN-Revised-Plan-Set---2021_04_29- |
| SLO County opportunities & constraints checklist | Required map of high spots, low spots, 20% slopes, hydrology | https://www.slocounty.ca.gov/departments/public-works/forms-documents/stormwater/appendix-b_opportunities-and-constraints-analysis_finaldraft |

## C. What commercial maps look like (visual language)

1. **Title block** — project, APN, legal, owner, PE/PLS seal, scale bar, north arrow, revision deltas.
2. **Heavy boundary** — surveyed property line is the darkest line on the sheet.
3. **Dashed easements** labeled with width + recording reference.
4. **Setback lines** dimensioned to the building, not guessed.
5. **Contours** at 1' or 2' with spot elevations at FF, TC, grate, invert.
6. **Irregular constraint polygons** — wetland drip-line, floodway, slope >20%, drip-line of protected trees. Never a circle around a pin.
7. **Zoning compliance table** — required vs provided for height, FAR, coverage, parking, open space.
8. **Vicinity map** inset, not the whole story.
9. **Line weights** follow NCS: C-PROP, C-BLDG, C-TOPO, C-STRM, C-WATR, C-SSWR, C-ESMT.

## D. Books / specs the industry trains on

- Dewberry, *Land Development Handbook* (McGraw-Hill) — the civil standard.
- Colley, *Practical Manual of Land Development*.
- LaGro, *Site Analysis* — opportunity/constraint synthesis.
- ALTA/NSPS Minimum Standard Detail Requirements (current year).
- US National CAD Standard v6 sheet series.
- Orange County Subdivision Manual + Irvine Subdivision Manual.
- Cindy Brewer, *Designing Better Maps* + ColorBrewer.

## E. Rules for the bot

When asked for a land-development map:
- Start from an official parcel / zoning / FIRM / NWI / soils / topo source above.
- Draw **irregular** constraint polygons and recorded lines, not radius rings.
- Label every overlay with its official source and date.
- If the connector cannot pull FEMA/NWI geometry, say so and point the user at MSC / NWI Mapper instead of faking a disk.
