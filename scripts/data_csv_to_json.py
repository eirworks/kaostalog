import csv
import json
import os


data_csv = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.csv')
target = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.json')

# configs
product_title = "Kaos Pria/Wanita Distro Cotton Combed 24s Holyshirt Industries {}" 
product_material = "Cotton Combed 24s"
product_description = """HOLYINDUSTRY 100% ORIGINAL GUARANTEE

*WAJIB TANYAKAN KETERSEDIAAN SIZE (UKURAN) SEBELUM CHECKOUT!

Material : Premium 24s Reactive. (baca deskripsi di bawah ini tentang spesifikasi)
Ink / Sablon : Direct Print High Quality (Kuat dan Awet)

Keunggulan :
*Lebih mudah menyerap keringat & Adem.
*Sablon Kuat & Tahan Lama.

Premium 24s Reactive.
1.Tidak kaku , Lembut & nyaman.
2.Menyerap Keringat & Tidak Gerah.
3.Ringan.
4.Tidak kasar.
5.Bila Di pakai terasa adem.

Barang akan di proses paling lambat 2X24 jam setelah pembayaran,

Dianjurkan untuk chat dahulu untuk mengetahui ketersediaan barang/ukuran yang di inginkan karena barang bisa sewaktu-waktu habis.

Happy shopping!!

#kaosdistro #kaosdistrocowok #bajukaosdistro #kaoswanitalenganpendek #kaosdistrooriginal
#kaosdistrowanita #kaoslenganpendek #kaoslenganpendekpria #kaospendek #kaospendekwanita
#kaosceweklenganpendek #bajukaoswanitalenganpendek #kaospendek #kaospendekwanita
#kaospendekpria #tshirt #kaostshirt #kaostshirtpria #kaostshirtwanita #tshirtdistro #kaospriadistron #bajukaospriadistro
"""

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