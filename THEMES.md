# Vegetation / biological / traffic / population GIS (commercial-grade, made by others)

## 1. Vegetation GIS

| Map | Who made it | URL |
|---|---|---|
| BIOS 6 public viewer | CDFW VegCAMP | https://apps.wildlife.ca.gov/bios6/ |
| BIOS home | CDFW | https://www.wildlife.ca.gov/Data/BIOS |
| Western Riverside vegetation 2005 [ds170] | CNPS + AIS for CDFW / MSHCP | https://filelib.wildlife.ca.gov/public/BDB/GIS/BIOS/metadata/DS0170.html |
| Western Riverside vegetation update 2012 [ds1196] | AIS for RCA | https://www.arcgis.com/home/item.html?id=93bf8bf746214d2d96c26d6fe418cacf |
| Coachella Valley Floor vegetation [ds2898] | UCR CCB / CVCC / VegCAMP | https://map.dfg.ca.gov/metadata/ds2898.html |
| GLA DBESP Exhibit 4 vegetation | Glenn Lukos Associates | https://planning.rctlma.org/sites/g/files/aldnop416/files/2023-08/Appendix%20C5%20-%20DBESP%20(Building%2013).pdf |

How to use BIOS: Add BIOS Layers → search `ds1196` or `Western Riverside vegetation` → turn layer on. Alliance-level polygons, not land-cover wash.

## 2. Biological GIS

| Map | Who | URL |
|---|---|---|
| RCA MSHCP Information Map 3.0 | Western Riverside RCA | https://experience.arcgis.com/experience/379b037fb33b4cc0ad8849c5dca76db6 |
| WR-MSHCP program | TLMA | https://planning.rctlma.org/epd/wr-mshcp |
| CDFW Habitat Connectivity Viewer | CDFW | https://wildlife.ca.gov/Data/Analysis/Connectivity |
| Biodiversity Explorer (ACE) | CDFW | https://storymaps.arcgis.com/stories/1585bd91b41e413b96259baafd5d8089 |
| GLA DBESP exhibits 3/5/8 | Glenn Lukos | same Building 13 PDF — site/impact, soils, MSHCP riverine |
| NWI wetlands mapper | USFWS | https://fwsprimary.wim.usgs.gov/wetlands/apps/wetlands-mapper/ |

Biological study language: criteria cells, survey hatches, vegetation alliances, jurisdictional drainages, CNDDB occurrences. Not a green circle.

## 3. Traffic studies (GIS figures inside TIA/TA PDFs)

Commercial traffic maps are **exhibits** in Urban Crossroads / Trames / similar sealed reports:

| Study | Firm | What the maps show | URL |
|---|---|---|---|
| Arroyo Vista TA (Woodcrest, RivCo) | Urban Crossroads 14577-04 | Location, site plan, study area, existing ADT, project-only volumes, cumulative locations | https://planning.rctlma.org/sites/g/files/aldnop416/files/2025-08/Appendix%20K2%20-%20Traffic%20Analysis.pdf |
| Cajalco Commerce Center VMT | Urban Crossroads for T&B | Warehouse trip gen + VMT | CEQANet attachment / County case PPT220050 |
| Palmyrita warehouse TIA | Urban Crossroads for FirstCarbon | PCE vs actual vehicles, existing vs proposed | https://riversideca.gov/cedd/sites/riversideca.gov.cedd/files/pdf/planning/2023/Palmyrita/Appendix%20H%20-%20Transportation%20Supporting%20Information%20COMBINED.pdf |
| 7-11 Arlington/Monroe TIA | Trames Solutions | Existing / EACP / cumulative turning-movement diagrams | https://riversideca.gov/cedd/sites/riversideca.gov.cedd/files/ceqa/Appendix%20F%20-%20Traffic%20Impact%20Analysis.pdf |
| County traffic counts | RivCo Transportation | 24-hr ADT census | https://trans.rctlma.org/traffic-counts |
| County TA guidelines | RivCo Trans | Required exhibit list + LOS tables | Desert Hot Springs host of County guidelines PDF |

Standard TIA GIS figure stack: location · site plan · study-area intersections · existing volumes · trip distribution % on network · project-only volumes · existing+project · cumulative locations · with-project volumes. Trucks and cars often split on industrial sites.

## 4. Population density GIS

| Map | Who | URL |
|---|---|---|
| ACS Population Density (CA, tract/BG) | Census ACS 2020–2024 | https://experience.arcgis.com/experience/125fbe5709234f90b891d3523fb5cc56 |
| 2026 USA pop density / sq mi | Esri Demographics Living Atlas | https://www.arcgis.com/apps/mapviewer/index.html?webmap=9b20f96749c143f4b050753aa9f5fe4e |
| 2020 Census pop density | Esri / Census DHC | https://www.arcgis.com/home/item.html?id=982187601fdb4d6792477330ff43d39a |
| Urban vs rural dot density 2020 | Esri | https://www.arcgis.com/home/item.html?id=558cefa38c31422cb6ed527d98b19279 |
| SCAG SoCal Atlas | SCAG | https://hub.scag.ca.gov/ |
| SCAG population-centers map | SCAG RDP | https://hub.scag.ca.gov/maps/9df4a45a3f5e46f6aae5af57988d45fa |
| CalEnviroScreen 4.0 (pop characteristics by tract) | OEHHA | https://experience.arcgis.com/experience/11d2f52282a54ceebcac7428e6184203 |

Population density on a land-dev study is **census tract or block-group choropleth or dots**, never a ring around a pin. SCAG TAZ forecasts feed traffic models; that is the commercial link between pop density and TIA.
