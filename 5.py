import json

with open('0.json') as f:
    data = json.load(f)

for each, value in data['titles'].items():
    if not value['popularity']:
        del value['popularity']
    else:
        value['popularity'] = round(value['popularity'], 4)


with open('5.json', 'w') as f:
    json.dump(data, f, indent=2)
