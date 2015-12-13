import yaml

with open("battleunits.yaml", "r") as f:
    data = yaml.load(f)

for battle_id, battle_data in data['battles'].items():
    US_units = []
    for k, v in battle_data['US']['units'].items():
        US_units.append({'code': k,
                         'name': v})
    battle_data['US']['units'] = US_units
    Confederate_units = []
    for k, v in battle_data['Confederate']['units'].items():
        Confederate_units.append({'unit_code': k,
                         'unit_name': v})
    battle_data['Confederate']['units'] = Confederate_units

with open("battleunits.yaml.new", "w") as f:
    yaml.dump(data, f, default_flow_style = False)
