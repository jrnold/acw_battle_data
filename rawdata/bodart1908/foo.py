import csv
import yaml

with open("bodart.yaml", "r") as f:
    data = yaml.load(f)

with open("bodart1908_battles.csv", "r") as f:
    reader = csv.DictReader(f)
    ids = [row for row in reader]

for row in ids:
    data[row['battle_id']]['id'] = row['number']

with open("bodart2.yaml", "w") as f:
    foo =  sorted(data.values(), key = lambda x: x['id'])
    for x in foo:
        del x['id']
    yaml.dump(foo, f)
        
    
