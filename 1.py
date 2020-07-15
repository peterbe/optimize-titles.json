import json

with open('0.json') as f:
    data = json.load(f)

for each, value in data['titles'].items():
    if not value['popularity']:
        del value['popularity']

with open('1.json', 'w') as f:
    json.dump(data, f, indent=2)
