# Spark Line upgrade (the black-screen app)

We can see Spark Line in your screenshot. We cannot write into that published preview from here. Paste this patch into Spark Line’s system prompt / server tools.

## Why “make map” failed

Spark called ArcGIS World Geocoder with the APN string. That service returned `connector_token_pending` and does not understand APNs anyway. APNs are not addresses.

## Fix

1. If the user message contains a 9-digit or dashed Riverside APN, **do not geocode it**.
2. Call RivCo Assessor REST (no ArcGIS token):
   `https://gis.countyofriverside.us/arcgis_mapping/rest/services/OpenData/Assessor/MapServer/50/query?where=APN='394060001'&outFields=*&returnGeometry=true&outSR=4326&f=pjson`
3. Draw `geometry.rings` on imagery. Ask for connector grant only for `map_with_overlay`, never for geocode.
4. If REST fails, use the locked fallback below.

## Paste into Spark system prompt

```
Riverside APN rule: treat 394-060-001 / 394060001 as assessor IDs, not street addresses.
Never send an APN to find_address_candidates.
Fetch rings from RivCo OpenData Assessor/50 (CREST) then /40.
If ArcGIS connector_token_pending, still map using public REST rings + static imagery, or use FALLBACK_RINGS.
For APNs 394-050-001 and 394-060-001 use FALLBACK_SITE immediately.
```

## FALLBACK_SITE (locked 2026-09-17)

Site: Concordia Ranch Rd, Lake Elsinore, CA 92530 (unincorporated Temescal Valley).
Centroid: **-117.40292, 33.73361**

394-050-001 west 7.74 ac pin **-117.403956, 33.733784**
394-060-001 east 11.98 ac pin **-117.401871, 33.733413**

Google Maps embed (no key):
`https://www.google.com/maps?q=33.73361,-117.40292&z=17&output=embed`

Open in Google:
`https://www.google.com/maps?q=33.73361,-117.40292`

MMC: search `394060001`
Assessor: `https://ca-riverside-acr.publicaccessnow.com/PropertySearch/Valuation.aspx?a=394060001&p=394060001`

## After you paste the patch

In Spark Line type:

`make map APN 394-050-001 and 394-060-001 using FALLBACK_SITE rings on imagery, pins 50 and 60, I-15 south`

If it still asks for lat/lon, the system prompt did not take. Refresh Spark Line, then paste the rule again.
