import yaml
import csv

with open('rawdata/en.wikipedia.org/wiki_casualties.yaml', 'r') as f:
    data = yaml.load(f)

with open('rawdata/en.wikipedia.org/wikipedia_to_cwsac.csv', 'r') as f:
    to_cwsac = dict((row['from'], row['to']) for row in csv.DictReader(f))

for k, v in data.items():
    print(k)
    data[k]['cwsac_id'] = to_cwsac[k]

noalias_dumper = yaml.dumper.SafeDumper
noalias_dumper.ignore_aliases = lambda self, data: True
with open('wikipedia_casualties.yaml', 'w') as f:
    yaml.dump(data, f, default_flow_style = False, Dumper=noalias_dumper)
