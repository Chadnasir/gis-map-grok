# Job card — Concordia Ranch APNs (worked example)

Locked 2026-09-17 against RivCo Assessor CREST + OpenData/40.

| APN | Side | Assessed ac | Class | TRA |
|---|---|---|---|---|
| 394-050-001 | West | 7.74 | Vacant Residential Land – Other | 065030 |
| 394-060-001 | East | 11.98 | Homesite / 10–49.9 ac | 065030 |

Combined 19.72 ac. Shared line ≈ −117.40291. No situs. Mail 13743 Desert Ridge, Corona 92883. Clayton MB 13/6. T5S R5W Sec 16.

Frontage: Concordia Ranch Rd, Lake Elsinore 92530, immediately north of I-15 / Temescal Canyon Rd.

Elev MSL: high ~1399 ft (east interior), low ~1232 ft (SE at road). Relief ~167 ft.

Identify envelope: zoning N-A / M-SC / I-P nearby; GP OS-RUR / LI / RR / FWY; SKR fee+plan Y; BUOW survey 1; liquefaction Low and Moderate.

MLS (not county): each listed $1,350,000; electric at street; water none.

Run:

```bash
python tools/rivco_apn.py 394-050-001 394-060-001
```

Then overlay the printed `rings_wgs84` on ArcGIS imagery.
