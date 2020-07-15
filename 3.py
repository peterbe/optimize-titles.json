import json

with open('0.json') as f:
    data = json.load(f)

new = {'titles': {}}
for each, value in data['titles'].items():
    new['titles'][each.replace('/en-US/docs/', '')] = value

with open('3.json', 'w') as f:
    json.dump(new, f, indent=2)
