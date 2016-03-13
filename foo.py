# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

import json
import csv
import yaml

#fox2cwsac = pd.read_csv("data/fox_forces2_to_cwsac.csv") 
#
#fox = pd.read_csv("data/fox_forces2.csv")

liv2cwsac = pd.read_csv("data/livermore_to_cwsac.csv")
liv = pd.read_csv("data/livermore_battles.csv")
cwsac = pd.read_csv("data/nps_battles.csv")


results = []
for row in liv2cwsac.itertuples():
    print(row)
    liv_id = int(row[1])
    cwsac_id = row[2]
    cwsac_battle = cwsac[cwsac.cwsac_id == cwsac_id].iloc[0]
    cwsac_description = ('%s , %s (%s - %s)' % (cwsac_battle['battle_name'],
                                                cwsac_battle['state'],
                                                cwsac_battle['start_date'],
                                                cwsac_battle['end_date'],))
    liv_battle = liv[liv.par_id == liv_id].iloc[0]
    liv_description = ('%s , %s (%s - %s)' % (liv_battle['battle_name'],
                                                liv_battle['state'],
                                                liv_battle['start_date'],
                                                liv_battle['end_date'],))
                                                
    results.append({'cwsac': [{'id': cwsac_id, 'description': cwsac_description}],
                    'livermore': [{'id': liv_id, 'description': liv_description}],
                    'start_date': cwsac_battle['start_date'],
                    'relation': row[3]})
                  
results.sort(key = lambda x: x['start_date'])
with open('cwsac_to_livermore.csv', 'w') as f:
    yaml.dump(results, f, default_flow_style = False)