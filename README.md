# Uyo Flood Exposure Mapping

A ward-level analysis of flood risk in Uyo LGA, Akwa Ibom State, based on proximity to rivers and streams.

**GeoDev Lab Africa, Cohort One.** Daniela

---

## The question

> Which wards in Uyo LGA, Akwa Ibom State, fall within 500 metres of a mapped river or stream, and how does each ward's exposed area compare — to identify which wards should be prioritised for flood mitigation planning?

## What's in here

- [docs/01-project-brief.md](docs/01-project-brief.md) — Week 1: the question, study area, and datasets with source links
- [docs/02-data-notes.md](docs/02-data-notes.md) — Week 2: what was downloaded, feature count, columns, and gaps found
- [docs/03-data-preparation.md](docs/03-data-preparation.md) — Week 3: CRS reprojection, clipping to the real Uyo LGA boundary, and the five quality checks
- [month-1-summary.md](month-1-summary.md) — Week 4: the spatial analysis (500m buffer + intersection), what I expected vs. what I got, and what data is still needed
- `uyo_waterways_analysis_ready.gpkg` — the analysis-ready waterway data
- `uyo_lga_boundary_utm32n.gpkg` — the verified Uyo LGA boundary
- `river_buffer_map.png` — the map from Week 4's analysis

## The answer, in one line

The single mapped river in OpenStreetMap for this area falls entirely outside Uyo LGA (~1,924m away), so a 500m buffer does not reach the boundary. This means current OSM data cannot answer the flood-proximity question for Uyo LGA — a genuine data gap, documented in month-1-summary.md.

---

Daniela · GeoDev Lab Africa
Learn. Build. Collaborate. Transform.
