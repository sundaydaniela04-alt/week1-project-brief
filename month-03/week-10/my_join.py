import pandas as pd
import geopandas as gpd

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards")
table = pd.read_csv("wards.csv")

first_try = wards.merge(table, left_on="ward_name", right_on="ward", how="left")
matched = first_try["area_km2"].notna().sum()
print("Matched on first try:", matched, "of", len(wards))


def clean_name(name):
    return name.strip().upper().replace("-", " ")


wards["join_key"] = wards["ward_name"].apply(clean_name)
table["join_key"] = table["ward"].apply(clean_name)

joined = wards.merge(table, on="join_key", how="left")
matched = joined["area_km2"].notna().sum()
print("Matched after cleaning:", matched, "of", len(wards))
print(joined[["ward_name", "area_km2"]])
