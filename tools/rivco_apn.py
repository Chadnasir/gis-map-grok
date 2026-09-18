#!/usr/bin/env python3
"""Riverside County APN exhibit runner.

Queries official RCIT OpenData REST layers and prints a JSON brief plus
WGS84 rings ready for ArcGIS map_with_overlay / Muse measured-site prompts.

Usage:
  python tools/rivco_apn.py 394-060-001 394-050-001
  python tools/rivco_apn.py 394060001
"""
from __future__ import annotations

import json
import sys
import urllib.parse
import urllib.request
from typing import Any

BASE = "https://gis.countyofriverside.us/arcgis_mapping/rest/services"

LAYERS = {
    "parcels": f"{BASE}/OpenData/Assessor/MapServer/40",
    "crest": f"{BASE}/OpenData/Assessor/MapServer/50",
    "zoning": f"{BASE}/OpenData/Planning/MapServer/1",
    "gp": f"{BASE}/OpenData/Planning/MapServer/0",
    "skr_fee": f"{BASE}/OpenData/Species_Habitats/MapServer/2",
    "buow": f"{BASE}/OpenData/Species_Habitats/MapServer/11",
    "liquefaction": f"{BASE}/OpenData/NaturalFeatureAndHazards/MapServer/3",
}

ASSESSOR = "https://ca-riverside-acr.publicaccessnow.com/PropertySearch/Valuation.aspx"
MMC = "https://gis1.countyofriverside.us/Html5Viewer/index.html?viewer=MMC_Public"
RCA = "https://experience.arcgis.com/experience/379b037fb33b4cc0ad8849c5dca76db6"
FLOOD = "https://content.rcflood.org/floodplainmap"
FEMANFHL = "https://hazards.fema.gov/arcgis/rest/services/public/NFHL/MapServer/28"


def normalize_apn(raw: str) -> str:
    digits = "".join(ch for ch in raw if ch.isdigit())
    if len(digits) != 9:
        raise SystemExit(f"APN must be 9 digits, got {raw!r}")
    return digits


def dashed(apn: str) -> str:
    return f"{apn[:3]}-{apn[3:6]}-{apn[6:]}"


def query(url: str, params: dict[str, Any]) -> dict[str, Any]:
    qs = urllib.parse.urlencode(params, safe="(),:'")
    req = urllib.request.Request(f"{url}/query?{qs}", headers={"User-Agent": "bill-gis/1.0"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return json.loads(resp.read().decode())


def parcel_query(apn: str) -> dict[str, Any]:
    where = f"APN='{apn}'"
    crest = query(
        LAYERS["crest"],
        {
            "where": where,
            "outFields": "*",
            "returnGeometry": "true",
            "outSR": 4326,
            "f": "json",
        },
    )
    feats = crest.get("features") or []
    if not feats:
        raw = query(
            LAYERS["parcels"],
            {
                "where": where,
                "outFields": "*",
                "returnGeometry": "true",
                "outSR": 4326,
                "f": "json",
            },
        )
        feats = raw.get("features") or []
    if not feats:
        return {"apn": apn, "found": False}
    feat = feats[0]
    attrs = feat.get("attributes") or {}
    geom = feat.get("geometry") or {}
    rings = geom.get("rings") or []
    xs = [pt[0] for ring in rings for pt in ring]
    ys = [pt[1] for ring in rings for pt in ring]
    cx = sum(xs) / len(xs) if xs else None
    cy = sum(ys) / len(ys) if ys else None
    return {
        "found": True,
        "apn": apn,
        "apn_dashed": dashed(apn),
        "acreage": attrs.get("ACREAGE") or attrs.get("ACRE"),
        "class_code": attrs.get("CLASS_CODE"),
        "subdivision": attrs.get("SUBDIVISION_NAME"),
        "map_book_page": attrs.get("MAP_BOOK_PAGE"),
        "tra": attrs.get("TAX_RATE_AREA") or attrs.get("TRA"),
        "land": attrs.get("LAND"),
        "structures": attrs.get("STRUCTURES") or attrs.get("STRUCTURE"),
        "situs_street": attrs.get("SITUS_STREET"),
        "situs_city": attrs.get("SITUS_CITY"),
        "mail_street": attrs.get("MAIL_STREET") or attrs.get("MAIL_TO_STREET"),
        "mail_city": attrs.get("MAIL_CITY") or attrs.get("MAIL_TO_CITY"),
        "centroid": {"x": cx, "y": cy},
        "envelope": {
            "xmin": min(xs) if xs else None,
            "ymin": min(ys) if ys else None,
            "xmax": max(xs) if xs else None,
            "ymax": max(ys) if ys else None,
        },
        "rings_wgs84": rings,
        "assessor_url": f"{ASSESSOR}?a={apn}&p={apn}",
    }


def envelope_identify(env: dict[str, float]) -> dict[str, Any]:
    geom = f"{env['xmin']},{env['ymin']},{env['xmax']},{env['ymax']}"
    common = {
        "geometry": geom,
        "geometryType": "esriGeometryEnvelope",
        "inSR": 4326,
        "spatialRel": "esriSpatialRelIntersects",
        "outFields": "*",
        "returnGeometry": "false",
        "f": "json",
    }
    out: dict[str, Any] = {}
    for key in ("zoning", "gp", "skr_fee", "buow", "liquefaction"):
        try:
            data = query(LAYERS[key], common)
            out[key] = [f.get("attributes") for f in data.get("features") or []]
        except Exception as exc:  # noqa: BLE001
            out[key] = {"error": str(exc)}
    return out


def muse_prompt(parcels: list[dict[str, Any]]) -> str:
    lines = [
        "Draw a north-up measured vacant-land site exhibit.",
        "Use the official Riverside County assessor rings below. Do not invent a rectangle.",
        "Title: Vacant Land Due Diligence | Riverside County, CA",
        "Sheets: EX-1 existing conditions on aerial, EX-2 frontage utilities callouts.",
        "Show Concordia Ranch Rd / I-15 if those roads appear in context.",
        "Scale bar, north arrow, APN labels, combined acreage.",
        "Preliminary — not for construction.",
        "",
    ]
    total = 0.0
    for p in parcels:
        if not p.get("found"):
            continue
        ac = p.get("acreage") or 0
        try:
            total += float(ac)
        except (TypeError, ValueError):
            pass
        lines.append(f"APN {p['apn_dashed']} | {p.get('acreage')} ac | {p.get('class_code')} | centroid {p.get('centroid')}")
        lines.append(f"rings_wgs84={json.dumps(p.get('rings_wgs84'))}")
    lines.append(f"Combined assessed acres: {total:.2f}")
    return "\n".join(lines)


def main(argv: list[str]) -> None:
    if len(argv) < 2:
        raise SystemExit("usage: rivco_apn.py APN [APN...]")
    apns = [normalize_apn(a) for a in argv[1:]]
    parcels = [parcel_query(a) for a in apns]
    envs = [p["envelope"] for p in parcels if p.get("found") and p.get("envelope", {}).get("xmin") is not None]
    ident = {}
    if envs:
        env = {
            "xmin": min(e["xmin"] for e in envs),
            "ymin": min(e["ymin"] for e in envs),
            "xmax": max(e["xmax"] for e in envs),
            "ymax": max(e["ymax"] for e in envs),
        }
        ident = envelope_identify(env)
    brief = {
        "county": "Riverside",
        "viewers": {"mmc": MMC, "rca": RCA, "flood": FLOOD, "fema_nfhl": FEMANFHL},
        "parcels": parcels,
        "constraints": ident,
        "muse_prompt": muse_prompt(parcels),
        "disclaimer": "Desktop GIS compilation. Not a survey, will-serve, delineation, Phase I, or CEQA determination.",
    }
    print(json.dumps(brief, indent=2))


if __name__ == "__main__":
    main(sys.argv)
