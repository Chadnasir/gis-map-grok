# Commercial-grade GIS maps from STUDIES

Only consultant / CEQA / CRE analytics products. No municipal wall posters. No homemade buffers.

## 1. Industrial master-plan + EIR GIS (Riverside County logistics)

**World Logistics Center Specific Plan** — Moreno Valley / eastern RivCo, ~2,610 ac, 40.6M sf logistics. Stamped plan-set GIS exhibits:
- Regional map, SP area, surrounding land use, fault zones, land-use plan, fire station, edge treatments, circulation, street sections
- PDF: https://www.moval.org/cdd/specificplans/wlc.pdf
- Status GIS (approved / under construction / occupied) compiled from County + City GIS: https://morenovalleybusiness.com/wp-content/uploads/2017/04/WLCIndustrial2016_102016.pdf
- CEQA: SCH 2012021045 https://ceqanet.lci.ca.gov/2012021045/5

**Majestic Freeway Business Center SP 341 / EIR 466** — Mead Valley, unincorporated RivCo. Albert A. Webb Associates land-use plan + plot-plan site GIS:
- Phase II site plans (bldg 11/12/20) with GP LI, zoning M-SC, APNs, AASHTO truck courts: https://www.majesticrealty.com/brochures/MFBC_PhaseII_3_Bldgs.pdf
- Building 19 addendum (347,672 sf warehouse study): https://planning.rctlma.org/majestic-freeway-business-center-building-19-eir-addendum
- Phase II Final EIR (AQ, HRA, biology, traffic appendices): https://planning.rctlma.org/notice-availability-final-eir-majestic-freeway-business-center-phase-ii
- Webb land-use color plan in Board packet: https://media.rivcocob.org/proceeds/2014/p2014_07_29_files/16-01001part2.pdf

**Villages of Lakeview SP 00342 EIR** — 2,883 ac County specific plan. Study stack is CEQA figures + technical appendices (bio, hydro, traffic), not a zoning wall map.
- Project page: https://planning.rctlma.org/villages-lakeview-specific-plan-sp00342
- CEQANet SCH 2006071095: https://ceqanet.lci.ca.gov/2006071095/5

Typical commercial EIR GIS figure set (copy this list):
regional location · vicinity · existing land use · proposed land use / planning areas · vegetation / jurisdictional waters · soils / faults / liquefaction · floodplain · noise receivers · traffic distribution · cumulative projects.

## 2. Published warehouse-impact GIS study (Inland Empire)

**Warehouse CITY** — Phillips & McCarthy, *Environment and Planning B* (2024). Assessor-derived warehouse polygons + truck / DPM / NOx / CO2 / jobs for LA, Orange, Riverside, San Bernardino.
- Paper: https://journals.sagepub.com/doi/10.1177/23998083241262553
- Code + data: https://github.com/RadicalResearchLLC/WarehouseMap
- Used in later GIS studies: Freight Burdens StoryMap https://storymaps.arcgis.com/stories/063eead608d246349a57468beaecb87d

This is a study product, not a city poster. Polygons are building footprints, not circles.

## 3. Commercial real estate site-selection GIS studies

These are the maps brokers and capital partners actually buy:

| Study / product | Firm | What the GIS shows | Link |
|---|---|---|---|
| Site selection with Business Analyst | Mid-America Real Estate + Esri | Customer-derived trade areas, 75k-pop threshold rings as *drive-time*, void analysis | https://www.esri.com/en-us/landing-page/industry/real-estate/2020/mid-america-real-estate-group-case-study |
| Future housing pipeline maps | Colliers Utah GIS (Esri case study) | Graduated symbols by project size + status | https://www.colliers.com/en/news/salt-lake-city/esri-gis-case-study |
| Dimension location intelligence | CBRE | HQ commute optimizer, tenant mix, site stories | https://www.esri.com/about/newsroom/publications/wherenext/the-world-leader-in-commercial-real-estate-tells-a-new-story |
| Amazon warehouse animated GIS | Goodman + Esri Australia | Drive-time + GeoEnrichment for industrial marketing | https://esriaustralia.com.au/industries/commercial-real-estate |
| Fulfillment-center suitability | Esri Business Analyst tutorial | County-level scored markets then sites | https://pro.arcgis.com/en/pro-app/3.5/help/analysis/business-analyst/suitability-analysis-walkthrough.htm |
| Industrial snapshot StoryMap | City of Riverside ED (CoStar-style GIS) | Business-park polygons + available SF | https://storymaps.arcgis.com/stories/5ffd32fd9c7d447bb26f0c47845f9428 |

## 4. What “commercial grade” means on a study map

A study map that would survive a Planning Commission / lender package has:
- Title block: project name, SP/PPT/SCH number, consultant, date, north, scale
- Source footer: County GIS / assessor / FEMA / field survey date
- Classified **polygons** (land use, vegetation, flood, warehouse footprint)
- Tables tied to the geometry (acreage, SF, DU, trips, emissions)
- Separate figures per topic (do not dump 12 themes on one basemap)
- No decorative circles. Drive-time isochrones are OK only when the study method is network travel time.
