import geopandas as gpd

files = [
    "uyo_lga_boundary_utm32n.gpkg",
    "uyo_waterways_analysis_ready.gpkg",
]

for path in files:
    layers = gpd.list_layers(path)
    print("FILE:", path)
    print(layers)
    name = layers["name"].iloc[0]
    gdf = gpd.read_file(path, layer=name)
    print("Shape:", gdf.shape)
    print("Geometry types:", list(gdf.geom_type.unique()))
    print("CRS:", gdf.crs)
    print("Bounds:", gdf.total_bounds)
    print()
