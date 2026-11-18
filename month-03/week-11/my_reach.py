import geopandas as gpd
import matplotlib.pyplot as plt

boundary = gpd.read_file("uyo_lga_boundary_utm32n.gpkg", layer="uyo_lga_boundary_utm32n")
boundary = boundary[boundary.geom_type == "Polygon"].to_crs(epsg=32632)
rivers = gpd.read_file("data/processed/uyo_hydrorivers.gpkg", layer="uyo_hydrorivers").to_crs(epsg=32632)
grid = gpd.read_file("data/processed/uyo_grid_counts.gpkg", layer="grid").to_crs(epsg=32632)

cells = gpd.clip(grid, boundary)
cells = cells[cells.geom_type.isin(["Polygon", "MultiPolygon"])].copy()
cells["cell_km2"] = cells.area / 1_000_000

reach = gpd.GeoDataFrame(geometry=rivers.buffer(500), crs=rivers.crs).dissolve()
near = gpd.overlay(cells, reach, how="intersection")
near["near_km2"] = near.area / 1_000_000

gaps = near[["cell_id", "near_km2"]].groupby("cell_id").sum().reset_index()
result = cells.merge(gaps, on="cell_id", how="left")
result["near_km2"] = result["near_km2"].fillna(0)
result["near_pct"] = (result["near_km2"] / result["cell_km2"] * 100).round(1)
print(result[["cell_id", "cell_km2", "near_km2", "near_pct"]].round(2))
print("Within 500 m of a river:", round(result["near_km2"].sum(), 1), "km2 of", round(result["cell_km2"].sum(), 1), "km2")
result.to_file("data/processed/uyo_reach_500m.gpkg", layer="uyo_reach_500m", driver="GPKG")

fig, ax = plt.subplots(figsize=(8, 8))
result.plot(ax=ax, column="near_pct", cmap="Blues", edgecolor="grey", legend=True, legend_kwds={"label": "% of cell within 500 m of a river"})
rivers.plot(ax=ax, color="darkblue", linewidth=1)
boundary.boundary.plot(ax=ax, color="black", linewidth=1.5)
ax.set_title("Uyo LGA: share of each 5 km grid cell within 500 m of a river")
ax.set_xlabel("Easting (m, EPSG:32632)")
ax.set_ylabel("Northing (m, EPSG:32632)")
plt.savefig("month-03/week-11/my_reach_map.png", dpi=150, bbox_inches="tight")
print("Map saved")
