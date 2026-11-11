import geopandas as gpd
import matplotlib.pyplot as plt

boundary = gpd.read_file(
    "uyo_lga_boundary_utm32n.gpkg", layer="uyo_lga_boundary_utm32n"
)

fig, ax = plt.subplots(figsize=(7, 8))
boundary.plot(ax=ax, color="#E6F2F3", edgecolor="#037E8E")
ax.set_title("Uyo LGA boundary, Akwa Ibom State")
ax.set_axis_off()

fig.savefig("month-03/week-10/my_map.png", dpi=150, bbox_inches="tight")
print("Map saved")
