# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

import json
import csv
import yaml

#fox2cwsac = pd.read_csv("data/fox_forces2_to_cwsac.csv") 
#
#fox = pd.read_csv("data/fox_forces2.csv")

to_cwsac = pd.read_csv("data/livermore_to_cwsac.csv")
btl = pd.read_csv("data/livermore_battles.csv")
cwsac = pd.read_csv("data/nps_battles.csv")


results = []
for row in to_cwsac.itertuples():
    print(row)
    _id = row[1]
    cwsac_id = row[2]
    cwsac_battle = cwsac[cwsac.cwsac_id == cwsac_id].iloc[0]
    cwsac_description = ('%s , %s (%s - %s)' % (cwsac_battle['battle_name'],
                                                cwsac_battle['state'],
                                                cwsac_battle['start_date'],
                                                cwsac_battle['end_date'],))
    battle = btl[btl.par_id == _id]
    description = ('%s, %s (%s - %s)' % (battle.iloc[0,:]['battle_name'],
                                                battle.iloc[0,:]['state'],
                                                battle.iloc[0,:]['start_date'],
                                                battle.iloc[0,:]['end_date'],))                                               
    results.append({'cwsac': [{'id': cwsac_id, 'description': cwsac_description}],
                    'phisterer': [{'id': int(_id), 'description': description}],
                    'start_date': cwsac_battle['start_date'],
                    'relation': row[3]})
                  
results.sort(key = lambda x: x['start_date'])
with open('cwsac_to_livermore.csv', 'w') as f:
    yaml.dump(results, f, default_flow_style = False)