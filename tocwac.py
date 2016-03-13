# -*- coding: utf-8 -*-
import pandas as pd
import yaml
import json

fox_forces2_to_cwsac = pd.read_csv('data/fox_forces2_to_cwsac.csv')
fox_forces2 = pd.read_csv('data/fox_forces2.csv')
cwsac_battles = pd.read_csv('data/nps_battles.csv')

for x in fox_forces2_to_cwsac.iterrows():
    print(x)