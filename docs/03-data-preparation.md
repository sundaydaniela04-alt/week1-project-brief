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
| Uyo LGA boundary | EPSG:4326 | EPSG:32632 | Reprojected |

## 2. Clipping to the study area

**Revision note:** An earlier version of this file clipped to a fixed bounding box (4.95–5.10°N, 7.85–8.05°E) as an approximation of Uyo LGA. Following review feedback, this was corrected to clip against the actual Uyo LGA administrative boundary polygon, retrieved from OpenStreetMap (relation 3715390, admin_level=6) via Overpass API.

- **Boundary used:** Real Uyo LGA polygon (1 feature), reprojected to EPSG:32632
- **Features before clipping:** 1 (river)
- **Features after clipping:** 0

## 3. The five quality checks

| Check | Result | Action taken |
|---|---|---|
| Is the CRS what I think it is? | Yes — confirmed projected (metric) CRS after reprojection | None needed |
| Are there nulls in the fields I need? | 0 nulls in the source waterway data | None needed |
| Are there duplicate features? | No duplicates | None needed |
| Is the geometry valid? | 0 invalid geometries in the source data | None needed |
| Does coverage span the whole study area? | **No — the single mapped river falls entirely outside the true Uyo LGA boundary**, approximately 1,924 metres away | Flagged as a critical data limitation, not fixed |

## 4. Problems found, and what I did

**The waterway does not actually fall within Uyo LGA.** When clipped against the true administrative boundary (rather than the earlier bounding-box approximation), the one waterway feature returned by OpenStreetMap for this area sits about 1.9 km outside Uyo LGA — most likely nearer Idu, a neighbouring settlement. This means the analysis-ready dataset for Uyo LGA currently contains **zero waterway features**.

This is a genuine and significant data gap, not a processing error. I verified it using `geopandas.distance()` against the true boundary polygon rather than assuming the earlier bounding-box result was correct. I am flagging this honestly: the current OSM data cannot support the Week 1 flood-proximity question as originally scoped, and a future step will need to source additional hydrology data (e.g. digitising from satellite imagery, or a national dataset such as HydroSHEDS) to make the analysis meaningful.

## 5. The analysis-ready output

- **File:** `uyo_waterways_analysis_ready.gpkg`
- **Format:** GeoPackage
- **CRS:** EPSG:32632
- **Features:** 0 (see problems above)
- **Also included:** `uyo_lga_boundary_utm32n.gpkg` — the verified Uyo LGA boundary, reprojected and saved for use in future weeks
- **Produced by:** Python script (geopandas) run in Google Colab, used as a substitute for desktop QGIS

---

**Status:** Week 3 complete, with an honestly flagged data gap. Waterway
sourcing needs revisiting before further spatial analysis in Week 4.
