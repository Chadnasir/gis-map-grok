# Spark / Muse autonomy pack — Riverside APN exhibit job

Goal: Muse Spark 1.3 in Spark Line (or Bill GIS in Grok) runs a vacant-land due-diligence exhibit **without a human fetching rings**.

The attached sample set (`Example_Site_GIS_Exhibit_Set`) is the sheet language. Live geometry must come from RivCo REST, not from Muse imagination.

## Tools the app must own

| Tool | What it does | Endpoint / impl |
|---|---|---|
| `rivco_apn` | 9-digit APN → acres, class, TRA, mail, WGS84 rings | `tools/rivco_apn.py` → Assessor/40 + CREST/50 |
| `rivco_identify` | Envelope → zoning, GP, SKR fee, BUOW, liquefaction | Planning/0-1, Species_Habitats/2+11, Hazards/3 |
| `arcgis_map_with_overlay` | Official rings on imagery + streets | Existing ArcGIS connector |
| `arcgis_elevation` | Spot heights MSL on corners + centroid | Existing connector |
| `arcgis_reverse_geocode` | Situs-style street name | Existing connector |
| `google_map` | Static + embed fallback | Spark Line google.server |
| `muse_measured_image` | Title-block site diagram **using the rings JSON** | Meta Responses API image |
| `site_brief_pdf` | G-001 findings + map embeds | Spark Line pdf.server |
| `geo_reason` | Compass, miles, Plus Code | Spark Line locate.server |

## Required Spark Line function tools (add if missing)

```json
{
  "type": "function",
  "name": "rivco_apn",
  "description": "Look up Riverside County assessor parcels by 9-digit APN. Returns acres, class, TRA, mail, WGS84 rings.",
  "parameters": {
    "type": "object",
    "properties": {
      "apns": {
        "type": "array",
        "items": { "type": "string" },
        "description": "One or more APNs, dashed or 9-digit"
      }
    },
    "required": ["apns"]
  }
}
```

Wire `rivco_apn` to `python tools/rivco_apn.py ...` or the same REST calls in `arcgis.server.ts`.

After rings return, Muse **must** call `arcgis_map_with_overlay` with those rings before it draws a pretty picture. If the Meta key is invalid, still attach the ArcGIS PNG.

## Autonomous run (this job)

User: `map APN 394-060-001 and 394-050-001 Riverside County`

1. Normalize to `394060001`, `394050001`.
2. `rivco_apn` both.
3. `rivco_identify` on combined envelope.
4. `elevation_at_locations` on centroid + four corners.
5. `reverse_geocode` centroid.
6. `map_with_overlay` imagery + streets with official rings (2-char pins `50` / `60`).
7. `muse_measured_image` with the `muse_prompt` string from the script (rings included).
8. `site_brief_pdf` G-001 table: utilities pending, MSHCP/SKR/BUOW, liquefaction, GP/zoning, drainage toward I-15 / Temescal Wash.
9. Disclaimer on every sheet.

## Keys

- Muse: full `LLM|...` string in Spark Line → Connection. Last test (2026-09-17) returned `invalid_api_key`.
- ArcGIS Location Services: Grok connector (already connected).
- Google Static Maps: optional, embed fallback if Static Maps API is off.

## What Muse must not do

- Invent a rectangle instead of assessor rings.
- Call a circle a floodplain or MSHCP cell.
- Print an image caption with no PNG attached.
- Treat MLS copy (electric / no water) as a will-serve.
