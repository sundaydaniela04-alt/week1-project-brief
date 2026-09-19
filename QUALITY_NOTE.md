# Data Preparation & Quality Note — Week 3

## Tool Used
Data preparation was carried out using Python (geopandas) in Google Colab, as a substitute for desktop QGIS, which was not accessible during this period. All operations performed (reprojection, clipping, export to GeoPackage) are standard GIS operations equivalent to what QGIS would perform.

## CRS Chosen and Why
The data was reprojected from its original CRS (EPSG:4326, WGS 84 — geographic coordinates in degrees) to **EPSG:32632 (WGS 84 / UTM Zone 32N)**. This zone covers Uyo LGA and Akwa Ibom State. A projected, metric CRS was necessary because the Week 1 spatial question requires measuring distance (a 500m buffer around rivers/streams), and distance calculations are not accurate in a geographic (degree-based) CRS like EPSG:4326.

## What Was Reprojected and Clipped
The waterway dataset from Week 2 (1 river feature, sourced from OpenStreetMap via Overpass API) was reprojected to EPSG:32632, then clipped to a bounding box covering Uyo LGA (approx. 4.95–5.10°N, 7.85–8.05°E in the original coordinates).

## Quality Checks and Results
1. **Geometry validity** — 0 invalid geometries found. All geometries are valid.
2. **CRS confirmation** — Confirmed the layer's CRS is projected (metric), verifying the reprojection to EPSG:32632 was successful.
3. **Missing/null values** — 0 missing values across all columns (id, name, waterway, source, GNS reference fields, geometry).
4. **Geometry type consistency** — Only LineString geometries present, consistent with the original dataset (no mixed or unexpected geometry types).
5. **Coordinate range sanity check** — The clipped layer's bounding box falls within expected UTM Zone 32N coordinate ranges for the Uyo area, confirming the clip operation worked correctly.

## Problems Found
None. The dataset passed all five quality checks cleanly — no invalid geometries, no missing values, and consistent geometry type.

## Where the Analysis-Ready File Lives
The reprojected, clipped, analysis-ready file is saved as `uyo_waterways_analysis_ready.gpkg` in this repository.
