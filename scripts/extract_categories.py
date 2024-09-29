import csv
import json
import os


data_csv = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.csv')
target = os.path.join(os.path.dirname(__file__), '..', 'data', 'categories.json')

if not os.path.exists(data_csv):
    print("File data.csv not found!")
    exit(1)

categories = []

with open(data_csv, 'r', newline='') as f:
    reader = csv.reader(f, delimiter=";")

    for row in reader:
        categories.append(row[6])

categories = list(set(categories))

with open(target, 'w') as f:
    f.write(json.dumps(categories))

print("File categories telah dibuat di {}".format(target))