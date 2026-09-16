# GIS Map Grok

Specialist Grok agent that makes real GIS maps from live tools — not descriptions of maps.

## Install (2 minutes)

1. Open Grok → Settings → Customize → Create Agent (or Custom Instructions / a Project).
2. Paste [`AGENT.md`](./AGENT.md) as the agent instructions.
3. Confirm the **ArcGIS Location Services** connector is connected (pay-as-you-go Location Platform).
4. Ask: `Map 1 World Way, Los Angeles, CA — elevation grid, no circles.`

Repo: https://github.com/Chadnasir/gis-map-grok

## What this is (and is not)

- **Is:** a reusable specialist prompt + tool handbook + the same reference catalogs GIS developers actually open.
- **Is not:** a fine-tuned model. Grok cannot train new weights from these files. The agent behaves like a specialist because the prompt + tools constrain it.

## Files

| File | Purpose |
|---|---|
| [AGENT.md](./AGENT.md) | Paste-ready agent prompt |
| [TOOLS.md](./TOOLS.md) | Exact connector tools, limits, workflow |
| [REFERENCES.md](./REFERENCES.md) | Real-world basemaps, layers, and cartography references |
