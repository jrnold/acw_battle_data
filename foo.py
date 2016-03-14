import yaml
import csv

def process_cwsac(x):
    battle = x['battle']
    description = '%s (%s-%s)' % (x['battle_name'], x['start_date'], x['end_date'])
    return (battle, {'id': battle, 'description': description})

with open('rawdata/clodfelter2008/clodfelter.yaml', 'r') as f:
    data = yaml.load(f)

with open('data/cwsac_battles.csv', 'r') as f:
    reader = csv.DictReader(f)
    cwsac = dict(process_cwsac(x) for x in reader)

cwsac_links = []
for battle in data:
    if 'end_date' not in battle:
        battle['end_date'] = battle['start_date']
    if 'cwsac' in battle:
        links = battle['cwsac']
        relation = links[0]['relation']
        if relation == "<":
            relation == "lt"
        elif relation == ">":
            relation == "gt"
        battles_cwsac = [cwsac[x['id']] for x in battle['cwsac']]
        cwsac_links.append({'battles_from': [{'id': battle['battle_id'],
                                               'description': '%s to %s' % (battle['start_date'], battle['end_date'])}],
                             'battles_cwsac': battles_cwsac,
                              'relation': relation})
        del battle['cwsac']

dbpedia_links = []
for battle in data:
    if 'end_date' not in battle:
        battle['end_date'] = battle['start_date']
    if 'dbpedia' in battle:
        links = battle['dbpedia']
        relation = links[0]['relation']
        if relation == "<":
            relation == "lt"
        elif relation == ">":
            relation == "gt"
        battles_dbpedia = [x['url'] for x in battle['dbpedia']]
        dbpedia_links.append({'battles_from': [{'url': battle['battle_id'],
                                               'description': '%s to %s' % (battle['start_date'], battle['end_date'])}],
                             'battles_dbpedia': battles_dbpedia,
                              'relation': relation})
        del battle['dbpedia']


with open('clodfelter.yaml', 'w') as f:
    yaml.dump(data, f, default_flow_style = False, Dumper = yaml.SafeDumper)
with open('clodfelter_to_cwsac.yaml', 'w') as f:
    yaml.dump(cwsac_links, f, default_flow_style = False, Dumper = yaml.SafeDumper)
with open('clodfelter_to_dbpedia.yaml', 'w') as f:
    yaml.dump(dbpedia_links, f, default_flow_style = False, Dumper = yaml.SafeDumper)
