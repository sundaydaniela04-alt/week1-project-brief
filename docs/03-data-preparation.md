# Data preparation

**Week 3 deliverable.** GeoDev Lab Africa, Cohort One.
Author: Daniela

What I reprojected, what I clipped, what I checked, and what I fixed.

---

## 1. Coordinate system decisions

**Working CRS:** EPSG:32632 (WGS 84 / UTM Zone 32N)

**Why this one:** The Week 1 question requires measuring distance (a 500m buffer around rivers/streams), and distance calculations are not accurate in a geographic CRS like EPSG:4326, which is in degrees. Nigeria spans three UTM zones (31N, 32N, 33N), split roughly at 6°E and 12°E. Uyo LGA's coordinates (~8.0°E, 5.1°N) fall clearly within the 6°E–12°E range, confirming it belongs to **Zone 32N**, not 31N. EPSG:32632 (WGS 84 / UTM Zone 32N) was therefore chosen as it correctly covers Uyo LGA and Akwa Ibom State with minimal distortion, rather than assumed by default. 

| Dataset | CRS as downloaded | CRS after | Operation |
|---|---|---|---|
| Uyo waterways | EPSG:4326 | EPSG:32632 | Reprojected |

> Reprojecting recalculates every coordinate. Assigning a CRS only
> relabels the data. I reprojected using `geopandas.to_crs()`, which
> recalculates coordinates rather than just relabelling them.

## 2. Clipping to the study area

- **Boundary used:** A fixed bounding box covering Uyo LGA (4.95–5.10°N, 7.85–8.05°E), reprojected to EPSG:32632
- **Features before clipping:** 1
- **Features after clipping:** 1

The single waterway feature fell fully within the study area bounding box, so no features were lost or partially cut during clipping.

## 3. The five quality checks

| Check | Result | Action taken |
|---|---|---|
| Is the CRS what I think it is? | Yes — confirmed projected (metric) CRS after reprojection | None needed |
| Are there nulls in the fields I need? | 0 nulls across all columns | None needed |
| Are there duplicate features? | No duplicates (only 1 feature total) | None needed |
| Is the geometry valid? | 0 invalid geometries | None needed |
| Does coverage span the whole study area? | No — only 1 of an expected many waterways is mapped | Flagged as a known data limitation, not fixed (source data gap, not a processing error) |

## 4. Problems found, and what I did

**Sparse source coverage.** Only one waterway feature exists in OpenStreetMap for the entire Uyo LGA study area. This is not something I can fix through data processing — it reflects a genuine gap in the underlying OSM data for this region. I am flagging this honestly rather than treating the dataset as complete; any later analysis using this data will understate true flood exposure.

## 5. The analysis-ready output

- **File:** `uyo_waterways_analysis_ready.gpkg`
- **Format:** GeoPackage
- **CRS:** EPSG:32632
- **Features:** 1
- **Produced by:** Python script (geopandas) run in Google Colab, used as a substitute for desktop QGIS

---

**Status:** Week 3 complete. First spatial analysis in Week 4.
