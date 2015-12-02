import yaml
import nameparser

src = "bodart.yaml"
with open(src, 'r') as f:
    data = yaml.load(f)

def parse_names(d):
    parsed_name = nameparser.HumanName(d['name']).as_dict()
    # if only one name given, it is treated as a first name
    if parsed_name['last'] == '':
        d['first_name'] = ''
        d['last_name'] = parsed_name['first']
    else:
        d['first_name'] = parsed_name['first']
        d['last_name'] = parsed_name['last']
    d['middle_name'] = parsed_name['middle']
    d['suffix'] = parsed_name['suffix']

for battle in data:
    for side in ('loser', 'victor'):
        try:
            for cdr in data[battle][side]['commanders']:
                parse_names(cdr)
        except KeyError:
            print(battle)
            pass
        try:
            for cdr in data[battle][side]['generals_killed']:
                parse_names(cdr)
        except KeyError:
            pass

with open("bodart2.yaml", 'w') as f:
    yaml.dump(data, f, default_flow_style = False)
