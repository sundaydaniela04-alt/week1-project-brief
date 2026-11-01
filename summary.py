import csv

def read_rows(filename):
    with open(filename, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def clean_values(rows, column):
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return values

def summarise(values):
    return {"count": len(values), "smallest": min(values), "largest": max(values), "average": round(sum(values) / len(values), 2)}
def summarise_all(filename, columns):
    rows = read_rows(filename)
    for column in columns:
        print(column, summarise(clean_values(rows, column)))

summarise_all("uyo_rivers.csv", ["LENGTH_KM", "CATCH_SKM"])
