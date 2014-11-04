from os import path
import sys
import os

import sqlalchemy as sa

from acward import util
from acward import model

def parse_ranges(x):
    if x:
        y = x.split('-')
        if len(y) > 1:
            data = [int(i) for i in y]
        else:
            data = [int(y[0])] * 2
    else:
        data = [None] * 2
    return tuple(data)

def load_wiki(src):
    session = model.Session()
    for row in csv2.DictReader(src, delimiter='\t'):
        uri = row['uri']
        c1 = {'battle': uri, 'combatant': row['combatant1']}
        c1['strength_min'], c1['strength_max'] = parse_ranges(row['strength1'])
        c1['casualties_min'], c1['casualties_max'] = parse_ranges(row['casualties1'])
        c2 = {'battle': uri, 'combatant': row['combatant2']}
        c2['strength_min'], c2['strength_max'] = parse_ranges(row['strength2'])
        c2['casualties_min'], c2['casualties_max'] = parse_ranges(row['casualties2'])
        session.add(model.WikiForces(**c1))
        session.add(model.WikiForces(**c2))
    session.commit()
    
def load(datadir):
    print("load wiki_*")
    load_wiki(open(path.join(datadir, 'wiki_casualties.tsv'), 'r'))
