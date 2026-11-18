import geopandas as gpd
from shapely.geometry import box

boundary = gpd.read_file("uyo_lga_boundary_utm32n.gpkg", layer="uyo_lga_boundary_utm32n")
boundary = boundary[boundary.geom_type == "Polygon"].to_crs(epsg=32632)
rivers = gpd.read_file("data/processed/uyo_hydrorivers.gpkg", layer="uyo_hydrorivers").to_crs(epsg=32632)

minx, miny, maxx, maxy = boundary.total_bounds
size = 5000
cells = []
x = minx
while x < maxx:
    y = miny
    while y < maxy:
        cells.append(box(x, y, x + size, y + size))
        y += size
    x += size
grid = gpd.GeoDataFrame({"geometry": cells}, crs="EPSG:32632")
grid = grid[grid.intersects(boundary.union_all())].reset_index(drop=True)
grid["cell_id"] = grid.index + 1

points = rivers.copy()
points["geometry"] = rivers.representative_point()
joined = gpd.sjoin(points, grid[["cell_id", "geometry"]], how="inner", predicate="within")
counts = joined.groupby("cell_id").size().rename("reach_count").reset_index()
grid = grid.merge(counts, on="cell_id", how="left")
grid["reach_count"] = grid["reach_count"].fillna(0).astype(int)
print(grid[["cell_id", "reach_count"]])
print("Total counted:", grid["reach_count"].sum(), "of", len(points))
grid.to_file("data/processed/uyo_grid_counts.gpkg", layer="grid", driver="GPKG")
