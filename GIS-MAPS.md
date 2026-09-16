# GIS maps made by others (not us)

Study these published GIS maps. Do not train on homemade ArcGIS connector posters.

## Municipal / county GIS (site due diligence)

| Map | Who made it | Open it |
|---|---|---|
| OC Land Insights | Orange County Public Works / OC Survey | https://webapps.ocgis.com/oclandinsights |
| Irvine parcel / zoning / GP / flood GIS | City of Irvine | https://gis.cityofirvine.org/irvinegis/pdfmaps.html and Parcel_Pro https://gis.cityofirvine.org/arcgis/rest/services/Parcel_Pro/MapServer |
| Irvine Community Profile | City of Irvine | https://experience.arcgis.com/experience/8c2e1b3d9d1c47758be65bdb69d49692 |
| LA County Z-NET (zoning + land use lookup) | LA County Regional Planning | https://experience.arcgis.com/experience/0eecc2d2d0b944a787f282420c8b290c |
| LA County GIS-NET Public | LA County Regional Planning | https://planning.lacounty.gov/maps-and-gis/gis-net-public/ |
| LA County A-NET (airport influence, RPZ, noise) | LA County ALUC | https://experience.arcgis.com/experience/7cc141ac27f34ab29da31be36e5d5c93 |
| LA County HOUSING-NET (SB 330 layers) | LA County Regional Planning | https://experience.arcgis.com/experience/aebeb8d0f62a4e23b98f7efc2d353fb0 |
| Orange County Open Data Hub | County of Orange GIS | https://data-orangecountygis.hub.arcgis.com/ |
| CA statewide zoning (south) | CA OPR | https://gis.data.ca.gov/datasets/Gov-OPR::california-statewide-zoning-south |

Irvine Parcel_Pro layers a developer actually clicks: Parcel, Zoning, General Plan, HOA, Flood Zone, Fire Ordinance Zone, Building.

## Federal constraint GIS

| Map | Who made it | Open it |
|---|---|---|
| FEMA NFHL Viewer | FEMA | https://experience.arcgis.com/experience/9d22cdae8b7542b88e0d555a3eb92949 |
| FEMA Map Service Center | FEMA | https://msc.fema.gov |
| FWS Wetlands Mapper | USFWS National Wetlands Inventory | https://www.fws.gov/program/national-wetlands-inventory/wetlands-mapper |
| USGS National Map Viewer | USGS | https://apps.nationalmap.gov/viewer/ |
| USGS 3DEP elevation ImageServer | USGS | https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer |

## Living Atlas / Esri production GIS

| Map | Who made it | Open it |
|---|---|---|
| Sentinel-2 10 m Land Cover Explorer (2017–2025) | Esri + Impact Observatory + Microsoft | https://livingatlas.arcgis.com/landcoverexplorer |
| Esri Land Cover product page | Esri | https://livingatlas.arcgis.com/landcover/ |
| Living Atlas home | Esri + GIS community | https://livingatlas.arcgis.com |
| Esri Land Use Inquiry template | Esri | https://www.arcgis.com/apps/instant/lookup/index.html?appid=ac9622ea51844642ae8f50e1c6d009c9 |
| ArcGIS Urban planning / zoning digital twin | Esri | https://www.esri.com/en-us/industries/urban-community-planning/initiatives/planning-design |
| Suitability Analysis walkthrough | Esri | https://pro.arcgis.com/en/pro-app/3.5/help/analysis/business-analyst/suitability-analysis-walkthrough.htm |

## Commercial parcel / site-selection GIS others sell

These are the maps CRE and land-dev teams pay for:

- LandVision (Digital Map Products) — parcel + zoning + flood overlays for underwriting
- Regrid + Esri Living Atlas parcels — https://regrid.com/esri
- ArcGIS Urban — 3D zoning scenarios
- UrbanFootprint — land-use + climate-risk scenario GIS
- Placer.ai / StreetLight — activity GIS, not cadastral
- Shovels GIS — building permits as hosted feature layers on parcels

## How the bot should copy these maps

1. Parcel polygon first, not a pin-in-a-circle.
2. Separate toggleable layers: zoning, general plan, flood, wetlands, slope, airport, fire.
3. Identify-on-click returns attributes (zone code, FIRM panel, APN).
4. Legend, scale bar, north, source citation in the chrome.
5. Official geometry from the agency that owns the layer.
