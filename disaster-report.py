import csv

with open("global_disasters.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    filtered = []
    for row in reader:
        if row["magnitude"].strip() == "" or row["location"].strip() == "":
            continue
        row["magnitude"] = float(row["magnitude"])
        filtered.append(row)

top_10 = sorted(filtered,key=lambda row: row["magnitude"],reverse=True)[:10]

with open("top_10.csv", "w",newline="",encoding="utf-8") as file:
    fieldnames = top_10[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(top_10)