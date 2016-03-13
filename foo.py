# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

import json
import csv
import yaml

#fox2cwsac = pd.read_csv("data/fox_forces2_to_cwsac.csv") 
#
#fox = pd.read_csv("data/fox_forces2.csv")

bod2cwsac = pd.read_csv("data/bodart1908_to_cwsac.csv")
bod = pd.read_csv("data/bodart1908_battles.csv")
cwsac = pd.read_csv("data/nps_battles.csv")


results = []
for row in bod2cwsac.itertuples():
    _id = int(row[1])
    cwsac_id = row[2]
    cwsac_battle = cwsac[cwsac.cwsac_id == cwsac_id].iloc[0]
    cwsac_description = ('%s , %s (%s - %s)' % (cwsac_battle['battle_name'],
                                                cwsac_battle['state'],
                                                cwsac_battle['start_date'],
                                                cwsac_battle['end_date'],))
    battle = bod[bod.battle_id == _id]
    description = ('%s (%s - %s)' % (battle.iloc[0,:]['name'],
                                                battle.iloc[0,:]['start_date'],
                                                battle.iloc[0,:]['end_date'],))                                               
    results.append({'cwsac': [{'id': cwsac_id, 'description': cwsac_description}],
                    'phisterer': [{'id': _id, 'description': description}],
                    'start_date': cwsac_battle['start_date'],
                    'relation': row[3]})
                  
results.sort(key = lambda x: x['start_date'])
with open('cwsac_to_bodart.csv', 'w') as f:
    yaml.dump(results, f, default_flow_style = False)