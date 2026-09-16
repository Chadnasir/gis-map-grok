# Bill GIS

Commercial-grade land-development GIS agent for Grok.
Home turf: Riverside County and the Inland Empire.

## Install (2 minutes)

1. Open Grok → **Settings → Customize → Create Agent**.
2. Name: **Bill GIS**
3. Paste [`BILL_GIS_AGENT.txt`](./BILL_GIS_AGENT.txt) into Instructions.
4. Confirm the **ArcGIS Location Services** connector is connected (pay-as-you-go Location Platform).
5. First test: `Map APN 365-030-015 — assessor plat, MSHCP cell, truck route. No circles.`

Repo: https://github.com/Chadnasir/gis-map-grok

## What this is (and is not)

- **Is:** a reusable specialist prompt + tool handbook + the published County / consultant GIS catalogs Bill opens first.
- **Is not:** a fine-tuned model. Grok cannot train new weights from these files. Bill behaves like a specialist because the prompt + tools + reference maps constrain him.
- **Is not** already sitting in your Grok agent slots. You have to paste the prompt once.

## Files

| File | Purpose |
|---|---|
| [BILL_GIS_AGENT.txt](./BILL_GIS_AGENT.txt) | Paste-ready agent prompt |
| [TOOLS.md](./TOOLS.md) | ArcGIS + public GIS tools, limits, workflow |
| [RIVERSIDE.md](./RIVERSIDE.md) | County viewers (MMC, RivCoView, RCA, Flood, PLUS) |
| [STUDIES.md](./STUDIES.md) | Stamped consultant GIS (GLA, Cadre, Urban Crossroads, WLC) |
| [THEMES.md](./THEMES.md) | Vegetation, biological, traffic TIA, population density |
| [MORE_THEMES.md](./MORE_THEMES.md) | Assessor, travel, industrial truck routes, CEQA figures |
| [LANDDEV.md](./LANDDEV.md) | Land-development sheet stack |
| [REFERENCES.md](./REFERENCES.md) | Basemaps and cartography |
