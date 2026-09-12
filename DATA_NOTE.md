# Data Note

## Source
Waterway data for Uyo LGA was retrieved from OpenStreetMap using the Overpass API, queried via overpass-turbo.eu. The query searched a bounding box covering Uyo LGA (coordinates: 4.95–5.10°N, 7.85–8.05°E) for all features tagged `waterway`.

Source link: https://overpass-turbo.eu
Underlying data: https://www.openstreetmap.org

## Feature Count
The query returned 1 way (line feature) representing a single river, built from 216 individual nodes (coordinate points).

## Key Columns (Tags)
- `waterway` — feature type (value: "river")
- `name` — name of the watercourse (value: "Isong Inyurig")
- `source` — data provenance (value: "GNS")
- `is_in:country` — country (value: "Nigeria")
- `GNS:dsg_code`, `GNS:dsg_string`, `GNS:id` — reference codes linking to the GEOnet Names Server

## Geometry Type
LineString (a single connected line made of 216 nodes).

## Gaps / Observations
Only one waterway feature was returned for the entire Uyo LGA bounding box. This suggests OpenStreetMap's waterway coverage for this area is very sparse — many smaller streams and rivers in Uyo are likely unmapped or untagged. This is a significant limitation for a flood-proximity analysis, since the 500m buffer method from the Week 1 brief depends on having a reasonably complete river/stream network. A more complete analysis would need to supplement this with additional sources (e.g., digitising from satellite imagery, or national hydrology datasets if available).
