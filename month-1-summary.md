# Month 1 Summary

**GeoDev Lab Africa, Cohort One.** Daniela

---

## My question, restated

Which wards in Uyo LGA, Akwa Ibom State, fall within 500 metres of a mapped river or stream, and how does each ward's exposed area compare — to identify which wards should be prioritised for flood mitigation planning?

## What I ran, and why

I buffered the single mapped river (from OpenStreetMap) by 500 metres, then intersected that buffer with the true Uyo LGA administrative boundary polygon. I chose intersection because it directly answers the "within 500m" part of my question — it tells me exactly which parts of the study area, if any, fall inside the buffer zone.

## What I expected

Based on my Week 3 finding that the river sits approximately 1,924 metres outside the Uyo LGA boundary, I expected the 500m buffer to fall short of reaching the boundary by roughly 1,424 metres. I expected the intersection to return **empty geometry** — zero overlap.

## What I got

The intersection was confirmed empty (`is_empty: True`, area: 0.0 sq metres). I checked this four ways:
1. **Map** — visually confirms the buffer and boundary don't touch, with clear separation
2. **Row count** — the buffer feature exists correctly, as expected
3. **Verified by hand** — comparing bounding boxes confirms the buffer's coordinate range doesn't overlap the boundary's
4. **Empty geometry check** — confirmed empty, but a valid Polygon type (not a broken/error result)

My expectation was correct.

## What surprised me

Not the outcome itself — I already suspected this from Week 3 — but how *decisively* empty it was. I expected the gap might be close, perhaps a partial edge overlap. Instead there's a clean, unambiguous 1.9km gap with no overlap at any point. This makes it clear the issue isn't marginal or a coordinate-precision quirk; it's a genuine, significant data coverage gap.

## What data I still need

I need a more complete waterway/hydrology dataset for Uyo LGA. OpenStreetMap currently has only one mapped river for the entire LGA, and it doesn't even fall inside the boundary. Options going forward:
- A national or regional hydrology dataset (e.g. HydroSHEDS, or a Nigerian government source if one becomes accessible)
- Manually digitising streams from satellite imagery for the study area
- Contacting NIHSA (Nigeria Hydrological Services Agency) or a similar body for authoritative data

Without this, the original flood-proximity question cannot be meaningfully answered — the analysis pipeline (buffer, clip, intersect) is built and tested correctly, but the input data doesn't yet support real conclusions for Uyo LGA specifically.

---

**Tools used throughout:** Google Colab (Python, geopandas) as a
substitute for desktop QGIS, since a computer was not accessible this
month. Overpass Turbo for querying OpenStreetMap data.
