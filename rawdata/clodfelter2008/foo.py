import yaml
import os
from os import path
import re

def rename_key(d, key_from, key_to):
    try:
        d[key_to] = d.pop(key_from)
    except KeyError:
        pass

with open('clodfelter.yaml.old', 'r') as f:
    data = yaml.load(f)

for theater in data:
    for battle in data[theater]:
        for lnk in battle['links']:
            if len(lnk) == 1:
                lnk.append("=")
            if re.search(r"en\.wikipedia\.org", lnk[0]):
                if 'wikipedia' not in battle:
                    battle['wikipedia'] = []
                battle['wikipedia'].append({'url': lnk[0], 'relation': lnk[1]})
            else:
                if 'cwsac' not in battle:
                    battle['cwsac'] = []
                battle['cwsac'].append({'id': lnk[0], 'relation': lnk[1]})
        del battle['links']
        for belligerent in ("US", "Confederate"):
            rename_key(battle[belligerent], "p", "captured")
            rename_key(battle[belligerent], "w", "wounded")
            rename_key(battle[belligerent], "wm", "wounded_missing")
            rename_key(battle[belligerent], "s", "strength")
            rename_key(battle[belligerent], "c", "casualties")
            rename_key(battle[belligerent], "cm", "missing_captured")
            rename_key(battle[belligerent], "m", "missing")
            rename_key(battle[belligerent], "k", "killed")
            rename_key(battle[belligerent], "kw", "killed_wounded")
            rename_key(battle[belligerent], "km", "killed_missing")
        rename_key(battle, "start", "start_date")
        rename_key(battle, "end", "end_date")
        rename_key(battle, "p", "page")        
        battle['forces'] = {}
        battle['forces']['US'] = battle.pop('US')
        battle['forces']['Confederate'] = battle.pop('Confederate')        

with open('clodfelter.yaml', 'w') as f:
    yaml.dump(data, f, default_flow_style = False)
