import geopandas as gpd

boundary = gpd.read_file(
    "uyo_lga_boundary_utm32n.gpkg", layer="uyo_lga_boundary_utm32n"
)
boundary = boundary[boundary.geom_type == "Polygon"]
rivers = gpd.read_file("data/processed/uyo_hydrorivers.gpkg", layer="uyo_hydrorivers")

print("Boundary CRS:", boundary.crs)
print("Rivers CRS:", rivers.crs)
print("Suggested UTM:", boundary.estimate_utm_crs())

boundary_utm = boundary.to_crs(epsg=32632)
rivers_utm = rivers.to_crs(epsg=32632)

area_km2 = boundary_utm.area.sum() / 1_000_000
length_km = rivers_utm.length.sum() / 1000
print("Uyo LGA area:", round(area_km2, 1), "km2")
print("River reaches:", len(rivers_utm))
print("River length inside Uyo LGA:", round(length_km, 1), "km")
