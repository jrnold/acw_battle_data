#!/bin/env python3
""" Miscellaneous data """
import sys
from os import path

import sqlalchemy as sa
import yaml

from acwbdb import model
from acwbdb.__version__ import __version__

def load_version():
    print("loading data into table %s" % model.Version.__table__)
    session = model.Session()
    session.add(model.Version(version = __version__))
    session.commit()

def load_combatant(src):
    print("loading data into table %s" % model.Combatant.__table__)
    data = yaml.load(src)
    session = model.Session()
    for k, v in data.items():
        session.add(model.Combatant(combatant = k, description = v))
    session.commit()

def load_states(src):
    print("loading data into table %s" % model.State.__table__)
    data = yaml.load(src)
    session = model.Session()
    for row in data:
        row = dict((k, v) for k, v in row.items())
        session.add(model.State(**row))
    session.commit()

def main():
    engine, datadir = sys.argv[1:3]
    model.Session.configure(bind = sa.create_engine(engine))
    load_version()
    load_combatant(open(path.join(datadir, 'combatants.yaml'), 'r'))
    load_states(open(path.join(datadir, 'states.yaml'), 'r'))

if __name__ == '__main__':
    main()
