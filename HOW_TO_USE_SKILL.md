# Use Bill GIS as a skill in chat

A SKILL.md does not appear in the Bots sidebar. It loads when Grok matches the description, or when you type `/bill-gis`.

## Fastest path on grok.com

In a new chat (or this one) send:

```
Save Bill GIS as a custom skill. Use the file at https://github.com/Chadnasir/gis-map-grok/blob/main/.grok/skills/bill-gis/SKILL.md
Name it bill-gis. Auto-use it whenever I ask for GIS maps, vegetation, biological, traffic, assessor, CEQA, flood, truck routes, or population density.
```

Then test:

```
/bill-gis Map APN 365-030-015 — MSHCP cell and assessor plat. No circles.
```

## Project path (stays on for every chat in that project)

1. Left sidebar → Projects → New project → name it Land Dev GIS.
2. Project instructions — paste BILL_GIS_AGENT.txt.
3. Attach or link https://github.com/Chadnasir/gis-map-grok
4. Do map work inside that project.

## Grok Build / Grok Bot desktop

Clone the repo. The skill lives at `.grok/skills/bill-gis/SKILL.md` so Grok loads it from the repo root. Slash command `/bill-gis`.
