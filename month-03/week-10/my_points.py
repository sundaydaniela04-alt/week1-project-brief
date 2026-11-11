import pandas as pd

facilities = pd.read_csv("data/raw/health_facilities.csv")
print("Before cleaning:")
print(facilities["type"].value_counts())

facilities["type"] = facilities["type"].str.strip().replace(
    {"PHC": "Primary Health Centre"}
)
print("After cleaning:")
print(facilities["type"].value_counts())
