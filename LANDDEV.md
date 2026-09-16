# Commercial-grade land-development maps (training corpus)

Do **not** train on homemade buffer/circle maps. Study these official and consultant sheets instead. They are the maps lenders, cities, civil engineers, and title companies actually stamp.

## 1. ALTA/NSPS Land Title Survey — commercial closing standard

Standard (effective 23 Feb 2026): https://nsps.us.com/page/2026ALTA

What the plat must show: record boundary, monuments, improvements, easements from the title commitment, encroachments, observed utilities, north arrow, graphic scale, Table A items, unaltered certification.

Public sealed examples:
- Partner ESI sample city-block ALTA (2021 standards, topo sheet): https://www.partneresi.com/wp-content/uploads/2024/04/3.Partner-SAMPLE-ALTA-Survey-City-Block.pdf
- AZ State Land / Wood Patel ALTA, 74.44 ac tract: https://land.az.gov/sites/default/files/media/53-121237_alta.pdf
- BKF Engineers ALTA, 20540 Broadway, Sonoma, CA (FIRM Zone X noted): https://storage.googleapis.com/proudcity/sonomaca/2025/09/Land-Title-Survey.pdf
- Green International ALTA, Gillette site, Andover, MA: https://www.andoverma.gov/DocumentCenter/View/14643/ALTA_NSPS-Land-Title-Survey
- Colliers ALTA, Union Township, NJ: https://uniontwp-hcnj.gov/vertical/sites/%7B45967581-AB8B-4219-9A83-39FE1CF6DFB8%7D/uploads/14_20211111_-_15001164E_ALTA_Survey_Signed.pdf
- Boulder Land Consultants school campus ALTA: https://blcsurveyors.com/wp-content/uploads/2020/05/84018_ALTA.pdf

Handbook for ALTA + zoning report + Phase I ESA: NV5 2026 CRE Due Diligence Handbook https://www.nv5.com/wp-content/uploads/2026/04/NV5_Handbook_2026-04.14.2026.pdf

## 2. Vesting Tentative Tract Map + grading / utilities exhibit — CA entitlement set

These are the maps a Planning Commission votes on.

Fuscoe Engineering — Harbor City mixed-use, LA County VTTM 73203:
- Tentative map (lots, easements, zoning, sewer/water notes): https://case.planning.lacounty.gov/assets/upl/case/tr073203_tentative-map.pdf
- Exhibit A site plan / open space / parking / coverage: https://case.planning.lacounty.gov/assets/upl/case/tr073203_exhibit-map.pdf
- Grading + utilities exhibit: https://case.planning.lacounty.gov/assets/upl/case/tr073203_exhibit-map-20160224.pdf

LA County VTTM 83311 (existing-to-remain vs remove, sewer laterals, PUEs): https://case.planning.lacounty.gov/assets/upl/case/tr083311_tentiative-tract-map-20210708.pdf

City of Irvine recorded tract index (Planning Area 10): http://gis.cityofirvine.org/pdf/PA%20Tract%20Maps/PA10_20220822.pdf
Irvine GIS map library: http://gis.cityofirvine.org/irvinegis/pdfmaps.html
Irvine VTTM format rules: https://legacy.cityofirvine.org/civica/filebank/blobdload.asp?BlobID=13797
Orange County tentative map checklist (contours, flood, cut/fill): https://ocds.ocpublicworks.com/sites/ocpwocds/files/import/data/files/8539.pdf
Irvine civil title-sheet CAD/PDF templates: https://cityofirvine.org/development-engineering/standard-city-irvine-title-sheets

## 3. Official land-use / zoning (entitlement base)

- Irvine 2045 General Plan (Land Use Element + maps): https://cityofirvine.gov/community-development/current-general-plan
- Irvine Zoning Ordinance: https://library.municode.com/ca/irvine/codes/zoning
- City GIS land-use / zoning / aerial planning-area PDFs: http://gis.cityofirvine.org/irvinegis/pdfmaps.html

A land-dev map is useless if it does not name the zone district, overlays (airport, hillside, coastal, fire), FAR/density, and setbacks.

## 4. Flood — FEMA FIRM / FIRMette, not a buffer disk

- Map Service Center: https://msc.fema.gov
- How to print a FIRMette: https://www.fema.gov/sites/default/files/documents/fema_how-find-your-firm-make-firmette.pdf
- NFHL REST (Flood Hazard Zones layer 28): https://hazards.fema.gov/arcgis/rest/services/public/NFHL/MapServer

ALTA Table A item 2 is the flood-zone callout lenders expect. Copy FIRM panel number + zone letter, never invent a circle.

## 5. Opportunities & constraints / site-suitability exhibits

- EPA Revitalization Ready due-diligence guide (ALTA, flood, wetlands checklist): https://www.epa.gov/system/files/documents/2021-12/revitalization-ready-guide-final-508compliant-12-10-21.pdf
- Glenn County Opportunities & Constraints Report: https://static1.squarespace.com/static/5c8a73469b7d1510bee16785/t/5e6969a05fb89076ac11cfba/1583966629919/Opportunities-Constraints-Report-Final1.pdf
- Portland Buildable Lands constraint layers (floodway, 25% slope, landslide, noise, greenway): https://efiles.portlandoregon.gov/record/16560152/file/document/
- Esri Business Analyst suitability walkthrough (fulfillment-center siting): https://pro.arcgis.com/en/pro-app/3.5/help/analysis/business-analyst/suitability-analysis-walkthrough.htm
- Esri Suitability Modeler workflow: https://pro.arcgis.com/en/pro-app/latest/help/analysis/spatial-analyst/suitability-modeler/the-general-suitability-modeling-workflow.htm

Constraint layers developers actually overlay: zoning + overlays, FEMA SFHA, NWI wetlands, 3DEP slope >15–25%, fault/landslide, airport influence, fire hazard severity, sewer/water will-serve, recorded easements from the ALTA.

## 6. What a commercial sheet looks like (copy these conventions)

- Title block: project name, tract/parcel number, owner, civil firm, PE/PLS seal, date, sheet index
- North arrow + graphic scale + engineering scale in words (1" = 40')
- Heavy property line vs light easement vs dashed utility
- Matchlines on multi-sheet ALTA sets
- Tables: lot area, coverage %, parking required vs provided, earthwork cut/fill, open-space %
- Typical sections for streets and pads
- Notes citing title report number, FIRM panel, zone, benchmark
- No decorative circles. Geometry is the lot, the easement, the flood zone, the pad.
