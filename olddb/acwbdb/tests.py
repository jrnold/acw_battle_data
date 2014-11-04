import sys

import sqlalchemy as sa

from acwbdb import model

def test_cwsac_forces():
    """ Test that all battles have two and only two combatant entries """
    session = model.Session()
    for btl in session.query(model.CwsacBattle):
        ## Check indian force
        q = session.query(model.CwsacForce).\
            filter(model.CwsacForce.battle == btl.battle)

        n_indian = q.filter(model.CwsacForce.combatant == u"I").count()
        n_us = q.filter(model.CwsacForce.combatant == u"US").count()
        n_cs = q.filter(model.CwsacForce.combatant == u"CS").count()
           
        if int(btl.indian) != n_indian:
            print("cwsac_forces %s%s: %d observations is incorrect" %
                  (btl.battle, "I", n_indian))
        if int(btl.us) != n_us:
            print("cwsac_forces %s%s: %d observations is incorrect" %
                  (btl.battle, "US", n_us))
        if int(btl.cs) != n_cs:
            print("cwsac_forces %s%s: %d observations is incorrect" %
                  (btl.battle, "CS", n_cs))
    session.close()

def test_cwsac_casualties_1():
    """ cwsac_battles.casualties test 1

    If cwsac_battles.casualties is NULL then there must exists a null value in
    cwsac_forces.casualties for that battle.
    
    """
    session = model.Session()
    for btl in session.query(model.CwsacBattle).\
            filter(model.CwsacBattle.casualties == None):
        if session.query(model.CwsacForce).\
               filter(model.CwsacForce.battle == btl.battle).\
               filter(model.CwsacForce.casualties == None).count() == 0:
            print(''.join(["cwsac_forces, cwsac_battles: %s missing total casualties ",
                           "and no missing force casualties"]) % btl.battle)
    session.close()

def test_cwsac_casualties_2():
    """ cwsac_battles.casualties test 2

    If all cwsac_forces.casualties are not null, then cwsac_battles.casualties must equal the
    sum of cwsac_forces.casualties for that battle.

    """
    session = model.Session()
    stmt = session.query(model.CwsacForce.battle.label("battle"),
                         sa.func.sum(model.CwsacForce.casualties).label("casualties_tot")).\
                         filter(model.CwsacForce.casualties != None).\
                         group_by(model.CwsacForce.battle).\
                         having(sa.func.count(model.CwsacForce.casualties) > 1L).subquery()
    q = session.query(model.CwsacBattle, stmt.c.casualties_tot).\
        join((stmt, stmt.c.battle == model.CwsacBattle.battle)).\
        filter(model.CwsacBattle.casualties != stmt.c.casualties_tot)
    for btl, casualties in q:
        print(''.join(["cwsac_battles %s: casualties does not match aggregation of",
                       "casualties in cwsac_forces"]) % btl.battle)
    session.close()

def test_cwsac_casualties_3():
    """ cwsac_battles.casualties test 3

    If cwsac_battles.casualties is not NULL then there must be either 0 or 2
    null entries in cwsac_forces.casualties.
    
    """
    session = model.Session()
    for btl in session.query(model.CwsacBattle).\
            filter(model.CwsacBattle.casualties != None):
        if session.query(model.CwsacForce).\
               filter(model.CwsacForce.battle == btl.battle).\
               filter(model.CwsacForce.casualties == None).count() not in (0, 2):
            print(''.join(["cwsac_forces, cwsac_battles: %s non-null total casualties",
                           "but 1 non-null cwsac_forces.casualties value"]) % btl.battle)
    session.close()

def test_kennedy_forces():
    """ Test that battles in ken_battles have the correct forces in ken_forces """
    session = model.Session()
    for btl in session.query(model.KenBattle):
        ## Check indian force
        q = session.query(model.KenForce).\
            filter(model.KenForce.battle == btl.battle)

        n_indian = q.filter(model.KenForce.combatant == u"I").count()
        n_us = q.filter(model.KenForce.combatant == u"US").count()
        n_cs = q.filter(model.KenForce.combatant == u"CS").count()
           
        if int(btl.indian) != n_indian:
            print("ken_forces %s%s: %d observations is incorrect" %
                  (btl.battle, "I", n_indian))
        if int(btl.us) != n_us:
            print("ken_forces %s%s: %d observations is incorrect" %
                  (btl.battle, "US", n_us))
        if int(btl.cs) != n_cs:
            print("ken_forces %s%s: %d observations is incorrect" %
                  (btl.battle, "CS", n_cs))
    session.close()

def test_ken_casualties_1():
    """ If ken_battles.casualties is NULL, then there exists a ken_forces.casualties equal to NULL
    """
    session = model.Session()
    for btl in session.query(model.KenBattle).\
            filter(model.KenBattle.casualties_min == None):
        if session.query(model.KenForce).\
               filter(model.KenForce.battle == btl.battle).\
               filter(model.KenForce.casualties_min == None).count() == 0:
            print(''.join(["ken_battles %s: missing ken_battles.casualties_min ",
                           "and no missing ken_forces.casualties_min"]) % btl.battle)
    session.close()

def test_ken_casualties_2a():
    """ Check ken_battles.casualties_min 2

    If all ken_forces.casualties_min are not null, then
    ken_battles.casualties_min must equal the sum of
    ken_forces.casualties_min for that battle.
    
    """
    session = model.Session()
    stmt = session.query(model.KenForce.battle.label("battle"),
                         sa.func.sum(model.KenForce.casualties_min).label("casualties_tot")).\
                         filter(model.KenForce.casualties_min != None).\
                         group_by(model.KenForce.battle).\
                         having(sa.func.count(model.KenForce.casualties_min) > 1L).subquery()
    q = session.query(model.KenBattle, stmt.c.casualties_tot).\
        join((stmt, stmt.c.battle == model.KenBattle.battle)).\
        filter(model.KenBattle.casualties_min != stmt.c.casualties_tot)
    for btl, casualties in q:
        print(''.join(["ken_battles %s: casualties_min does not match aggregation of",
                       "casualties in cwsac_forces"]) % btl.battle)
    session.close()

def test_ken_casualties_2b():
    """ Check ken_battles.casualties 2b

    If all ken_forces.casualties_max are not null, then ken_battles.casualties_max must equal the
    sum of ken_forces.casualties_max for that battle.
    
    """
    session = model.Session()
    stmt = session.query(model.KenForce.battle.label("battle"),
                         sa.func.sum(model.KenForce.casualties_max).label("casualties_tot")).\
                         filter(model.KenForce.casualties_max != None).\
                         group_by(model.KenForce.battle).\
                         having(sa.func.count(model.KenForce.casualties_max) > 1L).subquery()
    q = session.query(model.KenBattle, stmt.c.casualties_tot).\
        join((stmt, stmt.c.battle == model.KenBattle.battle)).\
        filter(model.KenBattle.casualties_max != stmt.c.casualties_tot)
    for btl, casualties in q:
        print(''.join(["ken_battles %s: casualties_max does not match aggregation of",
                       "casualties in cwsac_forces"]) % btl.battle)
    session.close()


def test_ken_casualties_3():
    """ ken_battles.casualties test 3

    If ken_battles.casualties is not NULL then there must be either 0 or 2
    null entries in ken_forces.casualties.
    
    """
    session = model.Session()
    for btl in session.query(model.KenBattle).\
            filter(model.KenBattle.casualties_min != None):
        if session.query(model.KenForce).\
               filter(model.KenForce.battle == btl.battle).\
               filter(model.KenForce.casualties_min == None).count() not in (0, 2):
            print(''.join(["ken_forces, ken_battles: %s non-null total casualties",
                           "but 1 non-null ken_forces.casualties_min value"]) % btl.battle)
    session.close()

def test_tables_have_obs():
    """ Test that all tables have data """
    meta = model.Base.metadata
    for table in meta.sorted_tables:
        rowcount = table.select().execute().rowcount
        if rowcount == 0:
            print("%s: Empty" % table.name)

def main():
    model.Base.metadata.bind = sa.create_engine(sys.argv[1])
    test_cwsac_forces()
    test_cwsac_casualties_1()
    test_cwsac_casualties_2()
    test_cwsac_casualties_3()
    test_kennedy_forces()
    test_ken_casualties_1()
    test_ken_casualties_2a()
    test_ken_casualties_2b()
    test_ken_casualties_3()
    test_tables_have_obs()
    
if __name__ == '__main__':
    main()
