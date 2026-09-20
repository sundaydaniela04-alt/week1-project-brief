# Project brief

**Week 1 deliverable.** GeoDev Lab Africa, Cohort One.
Author: Daniela

---

## 1. The question

> Which wards in Uyo LGA, Akwa Ibom State, fall within 500 metres of a mapped river or stream, and how does each ward's exposed area compare — to identify which wards should be prioritised for flood mitigation planning?

## 2. Why this question

Uyo LGA experiences seasonal flooding linked to its proximity to river tributaries and poor drainage in low-lying wards. Communities near watercourses face repeated property damage and displacement during the rainy season, yet there is no published ward-level ranking of flood exposure to guide local planning. As a Geosciences student from this region, I want to build a tool that could genuinely inform local flood mitigation decisions.

## 3. Study area

Uyo Local Government Area, Akwa Ibom State, Nigeria. The boundary will be defined using ward-level administrative boundary data from GRID3 Nigeria.

## 4. What I mean by the terms

"High risk of flooding" is measured as any ward area falling within a 500-metre buffer of a mapped river or stream. This is a proximity-based proxy, not a hydrological flood model.

## 5. Datasets

No link, no dataset. Every row below has a source I have opened myself.

| # | Dataset | What it gives me | Source |
|---|---|---|---|
| 1 | Administrative boundaries (Uyo LGA ward boundaries) | Ward geometries to overlay the buffer on | https://grid3.gov.ng |
| 2 | Rivers and streams (hydrology layer) | The waterways to buffer around | https://download.geofabrik.de/africa/nigeria.html |
| 3 | Settlements and population data | Estimate of people affected per ward | https://data.humdata.org/group/nga |
| 4 | Roads and built-up areas | Context/reference for interpreting exposure | https://download.geofabrik.de/africa/nigeria.html |

OSM waterway coverage for Uyo LGA is very sparse (confirmed in Week 2) — this is a known limitation and is addressed as a risk below.

## 6. What "done" looks like

A ranked table and map showing each ward's flood exposure (% area within 500m of a river or stream), reproducible by anyone with the linked datasets and this repository's scripts.

## 7. Known risks

**Sparse waterway data.** OpenStreetMap has very limited waterway coverage for Uyo LGA — only one mapped river was found in initial data collection. This may under-represent true flood exposure. Fallback: supplement with visual digitising from satellite imagery if time allows.

**No consistent computer access.** I do not have reliable laptop/desktop access this term, so QGIS-based workflows have been substituted with Python (geopandas) in Google Colab, which runs in-browser on mobile. This is documented in each week's notes.

---

**Status:** Week 1 complete. Data acquisition in Week 2, see
[02-data-notes.md](02-data-notes.md).
