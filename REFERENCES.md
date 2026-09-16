# Real-world reference maps GIS developers use

Study these the way a junior cartographer studies a wall of printed maps. They are the professional defaults — not decoration.

## Basemaps (open these first)

| Reference | Why developers use it | URL |
|---|---|---|
| ArcGIS Basemap Styles | Streets / navigation / imagery / light-gray / human-geography. Same family as `map_with_overlay`. | https://developers.arcgis.com/documentation/mapping-and-location-services/mapping/basemaps/arcgis-styles/ |
| ArcGIS Living Atlas | Curated global layers: imagery, elevation, people, infrastructure. | https://www.esri.com/en-us/arcgis/products/living-atlas |
| Esri World Imagery | Operational satellite/aerial base. | Living Atlas → World Imagery |
| Esri Human / Physical Geography | Monochrome base + transparent detail + labels. Best under thematic overlays. | Esri blog: layered physical geography basemap |
| USGS The National Map | US topo, NAIP imagery, hydro, contours, shaded relief. | https://www.usgs.gov/core-science-systems/ngp/tnm-corps/closer-look-layers-list |
| USGS US Topo / 3DEP hillshade | Lidar-derived landform. 1 m / 10 m / 30 m DEMs. | https://basemap.nationalmap.gov/arcgis/rest/services/USGSShadedReliefOnly/MapServer |
| OpenStreetMap Carto | Default osm.org style. Study `CARTOGRAPHY.md` + `roads.mss` / `landcover.mss`. | https://github.com/openstreetmap-carto/openstreetmap-carto |
| Natural Earth | Public-domain coastlines, admin, populated places at 1:10m / 50m / 110m. | https://www.naturalearthdata.com/ |
| Light Gray Canvas | Neutral thematic background. | Esri Living Atlas |

## Thematic layers (what “real” maps use instead of circles)

| Theme | Official source | Notes |
|---|---|---|
| Elevation / terrain | USGS 3DEP + Living Atlas World Elevation / Terrain / TopoBathy | Quarterly lidar updates. Hillshade + DEM, not a buffer. |
| Flood | FEMA NFHL / Map Service Center | https://hazards.fema.gov/femaportal/NFHL/searchResult/ — Zone A/AE/VE/X polygons. |
| Wetlands / habitat | USFWS National Wetlands Inventory | Cowardin classes. Mapper colors: PFO/PSS green, PEM lime, estuarine teal. https://www.fws.gov/node/268025 |
| Land cover | NLCD (USGS/MRLC), ESA WorldCover | Raster classes, not pins. |
| Imagery / change | NAIP (USDA), Landsat, Sentinel-2 | Living Atlas Landsat Explorer. |
| People | Esri GeoEnrichment / ACS / Census TIGER tracts | `POPDENS_CY`, `DPOPDENSCY` are samples, not tract polygons. |
| Noise (airports) | Airport 14 CFR Part 150 / AEDT CNEL or DNL contours | Elongated along runways. Never a ring around the terminal pin. |
| Traffic | ArcGIS routing + local DOT AADT | Use `solve_route` polylines here; official counts live at State DOT / HPMS. |
| Soils | USDA NRCS SSURGO / Web Soil Survey | Map units, not circles. |
| Hydro | NHD / NHDPlus HR (USGS) | Flowlines + waterbodies. |

## Color and design (non-negotiable)

| Resource | Use |
|---|---|
| ColorBrewer 2.0 | https://colorbrewer2.org — sequential / diverging / qualitative, colorblind-safe, photocopy-safe. |
| ColorBrewer source | https://github.com/axismaps/colorbrewer |
| Cindy Brewer, *Designing Better Maps* | Standard GIS cartography text. |
| Wong colorblind-safe set | `#0072B2` `#009E73` `#E69F00` `#D55E00` `#CC79A7` `#F0E442` `#56B4E9` `#000000` |
| ICA / Esri cartographic style guides | Hierarchy, contrast, label collision. |

## Developer style specs

| Spec | URL |
|---|---|
| Mapbox Style Spec | https://docs.mapbox.com/style-spec/ |
| ArcGIS Basemap Styles service | Esri Developer docs (50+ styles from one service) |
| Leaflet + QGIS print layout | Open-source composition references |
| Geofabrik OSM extracts | https://download.geofabrik.de |

## How the agent should “train” on these

When a user names a theme, look up the matching official layer above, say what that layer actually looks like (irregular polygons, rasters, contours), then render the closest honest proxy this connector can produce. Never pretend a circular buffer is a FIRM, a CNEL lobe, or a wetland class.
