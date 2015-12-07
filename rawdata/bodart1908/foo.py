import yaml

with open("bodart.yaml", "r") as f:
    data = yaml.load(f)

for battle in data:
    battle['result'] = battle['victor']['belligerent']
    battle['forces'] = {}
    battle['forces'][battle['victor']['belligerent']] = battle['victor']
    battle['forces'][battle['loser']['belligerent']] = battle['loser']
    battle['forces']['US'] = battle['forces']['Union']
    battle['forces']['Confederate'] = battle['forces']['Confederacy']
    if battle['result'] == "Confederacy":
        battle['result'] = "Confederate"
    del battle['forces']['Union']
    del battle['forces']['Confederacy']
    del battle['victor']
    del battle['loser']

with open("bodart-new.yaml", "w") as f:
    yaml.dump(data, f, default_flow_style = False)

