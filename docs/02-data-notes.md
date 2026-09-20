# Data notes

**Week 2 deliverable.** GeoDev Lab Africa, Cohort One.
Author: Daniela

What I downloaded, where it came from, what is in it, and what is wrong
with it.

---

## Summary

| # | Dataset | Type | Retrieved | Status |
|---|---|---|---|---|
| 1 | Uyo waterways (rivers/streams) | Vector | 12 September 2026 | Partial |

---

## 1. Uyo waterways (rivers/streams)

- **Source:** https://overpass-turbo.eu (Overpass API query against OpenStreetMap)
- **Retrieved:** 12 September 2026
- **File:** `export.geojson`
- **Format:** GeoJSON
- **Geometry type:** LineString
- **Feature count:** 1
- **CRS as downloaded:** EPSG:4326

**Key columns**

| Column | What it holds | Nulls |
|---|---|---|
| `waterway` | Feature type (e.g. "river") | 0 |
| `name` | Name of the watercourse | 0 |
| `source` | Data provenance (GNS) | 0 |
| `is_in:country` | Country | 0 |
| `GNS:dsg_code`, `GNS:dsg_string`, `GNS:id` | Reference codes from the GEOnet Names Server | 0 |

**What I noticed**

Only one waterway feature (a single river named "Isong Inyurig") was returned for the entire Uyo LGA bounding box, despite testing several query strategies (area-name match, visible-map bounds, and a fixed coordinate box). This indicates OpenStreetMap's waterway coverage for Uyo LGA is very sparse — most smaller streams and rivers are likely unmapped or untagged. This is a significant limitation for the flood-proximity analysis, since a 500m buffer method depends on a reasonably complete river/stream network. A more complete analysis would need to supplement this with digitising
