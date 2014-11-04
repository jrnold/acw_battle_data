#!/bin/env python3
""" Data from Phister """
import csv
import sys
import yaml
from datetime import datetime as datetime_
from os import path

import sqlalchemy as sa

from acwbdb import model

def _todate(x):
    return datetime_.strptime(x, "%Y-%m-%d").date()

def _calc_losses(x, disagg):
    """ Return total from killed + wounded + losses unless missing,
    in which case return the original total
    """
    newx = 0
    isany = False
    for d in disagg:
        if d :
            newx += int(d)
            isany = True
    if isany:
        return newx
    else:
        return x

def load_data(src, miscsrc):
    session = model.Session()
    reader = csv.DictReader(src, delimiter = '\t')
    misc = yaml.load(miscsrc)
    for row in reader:
        battleid = int(row['battle'])
        del row['page']
        row['start_date'] = _todate(row['start_date'])
        if row['end_date']:
            row['end_date'] = _todate(row['end_date'])
        else:
            row['end_date'] = row['start_date']
        casualties = [row[k] for k in ('us_killed', 'us_wounded', 'us_missing')]
        row['us_losses'] = _calc_losses(row['us_losses'], casualties)
        surrender = battleid in misc['surrender']
        if surrender:
            for k in ('us_killed', 'us_wounded', 'us_missing', 'us_losses'):
                row[k] = 0
        session.add(model.PhiForce(battle = battleid,
                          combatant = "CS",
                          losses = row['cs_losses']))
        session.add(model.PhiForce(battle = battleid,
                          combatant = "US",
                          killed = row['us_killed'],
                          wounded = row['us_wounded'],
                          missing = row['us_missing'],
                          losses = row['us_losses']))
        session.add(model.PhiBattle(battle = battleid,
                           battle_name = row['battle_name'],
                           start_date = row['start_date'],
                           end_date = row['end_date'],
                           campaign = battleid in misc['campaigns'],
                           surrender = battleid in misc['surrender']))
    session.commit()

def load_phi_forces_2():
    """ Create phi_forces_2 table from phi_forces

    See documentation of PhiForce2 for changes made.

    """
    session = model.Session()
    b2354_US_losses = session.query(model.PhiForce.losses).\
                      filter(model.PhiForce.battle == 2354).\
                      filter(model.PhiForce.combatant == "US").one()[0]
    ## Use the relative proportions of K/W/M from b2345
    ## to fill in K/W/M in 2354
    b2354_US_killed = round((1370. / 8670) * b2354_US_losses)
    b2354_US_wounded = round((6500. / 8670) * b2354_US_losses)
    b2354_US_missing = round((800. / 8670) * b2354_US_losses)
    b2354_CS = session.query(model.PhiForce.losses).\
               filter(model.PhiForce.battle == 2354).\
               filter(model.PhiForce.combatant == "CS").one()[0]
    phi_forces = (session.query(model.PhiForce).\
                  filter(model.PhiForce.battle != 2372).all())
    for x in phi_forces:
        phi_force_2 = model.PhiForce2.from_phi_force(x)
        if phi_force_2.battle == 2345:
            if phi_force_2.combatant == "US":
                phi_force_2.losses -= b2354_US_losses
                phi_force_2.killed -= b2354_US_killed
                phi_force_2.wounded -= b2354_US_wounded
                phi_force_2.missing -= b2354_US_missing
            else:
                phi_force_2.losses -= b2354_CS
                ## CS only has aggregate losses
        elif phi_force_2.battle == 2354:
            if phi_force_2.combatant  == "US":
                phi_force_2.killed = b2354_US_killed
                phi_force_2.wounded = b2354_US_wounded
                phi_force_2.missing = b2354_US_missing
        session.add(phi_force_2)
    session.commit()

def load_phi_to_cwsac_2():
    session = model.Session()
    ## Account for adjustments to battles 2345 and 2354 in phi_forces_2
    q = session.query(model.PhiToCwsac).\
        filter(sa.or_(model.PhiToCwsac.battle != 2345,
                      model.PhiToCwsac.cwsac != "GA015")).\
        filter(model.PhiToCwsac.battle != 2372)
    for btl in q:
        session.add(model.PhiToCwsac2.from_phi_to_cwsac(btl))
    session.commit()
    

# def load_links(filename):
#     model.PhiToDbpedia.load_from_file(filename)
#     model.PhiToCwsac.load_from_file(filename)
                
def load(datadir):
    print("loading phi_*")
    load_data(open(path.join(datadir, 'phister',
                             'Loss_In_Engagement.tsv'), 'r'),
              open(path.join(datadir, 'phister',
                             'misc.yaml'), 'r'))
    #load_links(path.join(datadir, 'phister', 'phi_links.yaml'))
    load_phi_forces_2()
    #load_phi_to_cwsac_2()

def main():
    engine, datadir = sys.argv[1:3]
    model.Session.configure(bind = sa.create_engine(engine))
    load(datadir)

if __name__ == '__main__':
    main()
