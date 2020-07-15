import json

with open('0.json') as f:
    data = json.load(f)

for each, value in data['titles'].items():
    if value['popularity'] > 0:
        #if value['popularity'] < 0.0001:
        #    print(value['popularity'])
        value['popularity'] = round(value['popularity'], 4)

with open('4.json', 'w') as f:
    json.dump(data, f, indent=2)
