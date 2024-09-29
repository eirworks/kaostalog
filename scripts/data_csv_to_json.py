import csv
import json
import os


description_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'description.txt')
data_csv = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.csv')
target = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.json')

# configs
product_title = "Kaos Pria/Wanita Distro Cotton Combed 24s Holyshirt Industries {}" 
product_material = "Cotton Combed 24s"

with open(description_file, 'r') as f:
    product_description = f.read()

if not os.path.exists(data_csv):
    print("File data.csv not found!")
    exit(1)

new_data = []

with open(data_csv, 'r', newline='') as f:
    reader = csv.reader(f, delimiter=";")

    for row in reader:
        new_data.append({
            "id": row[0],
            "title": product_title.format(row[1]),
            "name": row[1],
            "images": [n+1 for n in range(int(row[2]))],
            "image_urls": ["/products/{}/{}.jpg".format(row[0], n+1) for n in range(int(row[2]))],
            "sizes": row[3].split(","),
            "material": product_material,
            "colors": [n for n in row[5].split(",")],
            "description": product_description,
        })

with open(target, "w") as f:
    f.write(json.dumps(new_data))

print("JSON created in {}".format(target))