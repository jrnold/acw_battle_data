import yaml
import csv

with open("forces.yaml", "r") as f:
    data = yaml.load(f)

allkeys = set()
for k, v in data.items():
    for combatant in ('CS', 'US', 'I'):
        if combatant in v:
            for j in v[combatant].keys():
                allkeys.add(j)

varnames = sorted(list(allkeys))
varnames = [x for x in varnames if x != 'description']

with open('forces.csv', 'w') as f:
    writer = csv.DictWriter(f, ['cwsac', 'combatant', 'forces_text', 'description'] + varnames)
    print(writer.fieldnames)
    writer.writeheader()
    for k, v in data.items():
        for combatant in ('CS', 'US', 'I'):
            if combatant in v:
                row = v[combatant]
                row['cwsac'] = k
                row['combatant'] = combatant
                row['forces_text'] = v['forces_text']
                writer.writerow(row)

