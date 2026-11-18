import geopandas as gpd

boundary = gpd.read_file("uyo_lga_boundary_utm32n.gpkg", layer="uyo_lga_boundary_utm32n")
boundary = boundary[boundary.geom_type == "Polygon"].to_crs(epsg=32632)
grid = gpd.read_file("data/processed/uyo_grid_counts.gpkg", layer="grid")

for name, layer in [("boundary", boundary), ("grid", grid)]:
    before = int((~layer.is_valid).sum())
    fixed = layer.copy()
    fixed["geometry"] = fixed.make_valid()
    after = int((~fixed.is_valid).sum())
    print(name, "- polygons:", len(layer), "| invalid before:", before, "| invalid after:", after)
