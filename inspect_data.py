import csv

# with open("uyo_rivers.csv", encoding="utf-8-sig") as f:
#    reader = csv.DictReader(f)
#    rows = list(reader)

# values = []
# for row in rows:
#    raw = row["LENGTH_KM"].strip()
#    if raw == "":
#        continue
#    values.append(float(raw))

# print("Smallest:", min(values))
# print("Largest:", max(values))
# print("Count:", len(values)) 


def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw)) 
    return {"smallest": min(values), "largest": max(values), "count": len(values)}
result = inspect_column("uyo_rivers.csv", "LENGTH_KM")
print(result)
result = inspect_column("uyo_rivers.csv", "CATCH_SKM")
print(result)