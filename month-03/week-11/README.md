# Week 11: CRS and spatial operations

## What is in this folder
- Eight guided scripts: area_wrong_and_right.py, set_vs_to.py, one_point.py, spatial_ops.py, coverage_gap.py, nearest.py, clip_dissolve.py and fix_geometry.py. They use the Ibadan North teaching data in EPSG:32631.
- Four challenge scripts on my own Uyo LGA data in EPSG:32632: my_crs.py, my_count.py, my_reach.py and my_validity.py.
- my_reach_map.png is my map of the results.
- Results saved in data/processed: uyo_grid_counts.gpkg and uyo_reach_500m.gpkg.

## How to run
From the repository root, run each script with uv run, for example: uv run month-03/week-11/my_crs.py
Run my_count.py before my_reach.py and my_validity.py, because it creates the grid file they read.

## What I found
- Uyo LGA covers 186.5 km2. I reprojected to EPSG:32632 (UTM zone 32N) because Uyo is at about 7.9 E, inside the 6 E to 12 E strip.
- 40 HydroRIVERS river reaches lie inside the LGA, 61.2 km in total.
- my_count.py counted the river reaches per 5 km grid cell, and all 40 were counted.
- About 60.6 km2 of the LGA (32.5%) lies within 500 m of a river. I chose 500 m because my project question asks about land within 500 metres of a river.
- my_validity.py checked 1 boundary polygon and 19 grid cells: 0 invalid before make_valid and 0 invalid after.

## What went wrong
- My first area calculation printed 0.0004 because the layer was still in degrees (EPSG:4326). After to_crs it gave square kilometres.
- clip_dissolve.py needed roads.gpkg, which I had not uploaded yet. I added it from the starter data.

## Limitation of my method
HydroRIVERS only maps rivers with a catchment of at least 10 km2, so smaller streams are missing and the 500 m share is a minimum. Also, there are no open ward boundaries for Uyo, so I used 5 km grid cells instead of wards. The results are per square cell, not per community.
