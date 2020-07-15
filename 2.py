import json
import csv

with open('0.json') as f:
    data = json.load(f)


import csv
with open('2.csv', 'w') as f:
    writer = csv.writer(f, delimiter="|")
    for each, value in data['titles'].items():
        writer.writerow([each, value['title'], value['popularity']])
