#CSV
import csv
with open("marks.csv","r") as f:
    reader=csv.DictReader(f)
    for row in reader:
        print(row)
#json
import json
with open("student.json","r") as f:
    s=json.load(f)
    print(s["name"],s["course"])