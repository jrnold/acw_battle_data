import codecs
import datetime
import json
import csv

import yaml

import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy import types
from sqlalchemy.ext import declarative

Base = declarative.declarative_base()
Session = orm.sessionmaker()

ACW_START_DATE = datetime.date(1861, 4, 1)
ACW_END_DATE = datetime.date(1865, 7, 1)

class CheckConstraintNonNeg(sa.CheckConstraint):
    def __init__(self, col, **kwargs):
        super(CheckConstraintNonNeg, self).__init__('%s >= 0' % col, **kwargs)

class CheckConstraintPositive(sa.CheckConstraint):
    def __init__(self, col, **kwargs):
        super(CheckConstraintPositive, self).__init__('%s > 0' % col, **kwargs)

class Mixin(object):

    @classmethod
    def load_from_csv(cls, session, file):
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                session.add(cls(**row))

    @classmethod
    def load_from_yaml(cls, session, file):
        with open(file, 'r') as f:
            data = yaml.load(f)
        for row in data:
            session.add(cls(**row))

    @classmethod
    def load_from_json(cls, session, file):
        with open(file, 'r') as f:
            data = json.load(f)
        for row in data:
            session.add(cls(**row))

class ForeignKey(sa.ForeignKey):
    """ Subclass sqlalchemy.ForeignKey with different defaults """
    def __init__(self, column, **kwargs):
        ## ondelete = CASCADE makes it easier when unloading tables
        ## initially deferred and deferrable are useful in loading
        defaults = {'onupdate' : "CASCADE",
                  'ondelete' : "CASCADE",
                  'initially' : "DEFERRED",
                  'deferrable' : True}

        defaults.update(kwargs)
        super(ForeignKey, self).__init__(column, **defaults)

class State(Base, Mixin):
    """ United States States

    State abbreviations and names (current states)

    """
    __tablename__ = 'states'
    abbr = sa.Column(sa.Unicode(2), primary_key=True)
    name = sa.Column(sa.Unicode, unique=True, nullable=False)
    dbpedia = sa.Column(sa.Unicode, unique=True, nullable=False)
    
class Combatant(Base, Mixin):
    """ Civil War Combatants

    E.g. Union, Confederate, and American Indian.
    These are standardized across datasets to facilitate merging.
    
    """
    __tablename__ = 'combatants'
    combatant = sa.Column(sa.Unicode, primary_key = True,
                          doc = "Combatant abbreviation")
    description = sa.Column(sa.Unicode,
                            doc = "description")


class Version(Base, Mixin):
    """ Database version """
    __tablename__ = 'version'
    version = sa.Column(sa.Unicode, primary_key = True,
                        doc = "ACWARD version number")

    
# class DbpBattle(Base, Mixin):
#     __tablename__ = 'dbp_battles'
    
#     uri = sa.Column(sa.Unicode, primary_key=True,
#                     doc = "Dbpedia URI")
#     date = sa.Column(sa.Unicode,
#                      doc = "Date, http://dbpedia.org/ontology/date")
#     latitude = sa.Column(sa.Float,
#                          doc = "Latitude")
#     longitude = sa.Column(sa.Float,
#                           doc = "Longitude")
#     place = sa.Column(sa.Unicode,
#                       doc = """Location,
#                       http://dbpedia.org/ontology/place""")
#     result = sa.Column(sa.Unicode,
#                        doc = """Battle result,
#                        http://dbpedia.org/ontology/result""")
#     union_victory = sa.Column(sa.Boolean,
#                               doc = """Union victory,
#                               http://dbpedia.org/page/Category:Union_victories_of_the_American_Civil_War""")
#     confederate_victory = sa.Column(sa.Boolean,
#                                doc = """Confederate victory,
#                                http://dbpedia.org/page/Category:Confederate_victories_of_the_American_Civil_War""")
#     inconclusive = sa.Column(sa.Boolean,
#                         doc = """Inconclusive,
#                         http://dbpedia.org/page/Category:Inconclusive_battles_of_the_American_Civil_War""")
#     siege = sa.Column(sa.Boolean,
#                       doc = """Siege,
#                       http://dbpedia.org/resource/Category:Sieges_of_the_American_Civil_War""")
#     naval_battle = sa.Column(sa.Boolean,
#                       doc = """Naval battle,
#                       http://dbpedia.org/resource/Category:Naval_battles_of_the_American_Civil_War""")
#     massacre = sa.Column(sa.Boolean,
#                          doc = """Massacre,
#                          http://dbpedia.org/page/Category:Massacres_of_the_American_Civil_War""")
#     theater = sa.Column(sa.Unicode,
#                         ForeignKey(Theater.__table__.c.theater),
#                         doc = "Theater")

class CwsacTheater(Base, Mixin):
    """ Theaters of the American Civil War

    The CWSAC defined five theaters of the American Civil War.

    1. Main Eastern 
    2. Main Western 
    3. Trans-Mississippi
    4. Lower Seaboard Theater and Gulf Approach
    5. Pacific Coast

    These theaters are also used in wikipedia/dbpedia. Futhermore
    each CWSAC campaign is assigned a theater.

    """
    __tablename__ = 'cwsac_theaters'
    theater = sa.Column(sa.Unicode, primary_key =True,
                        doc = "Theater name")
    dbp_resource = sa.Column(sa.Unicode, unique = True,
                             doc = "URI of dbpedia page")
    dbp_category = sa.Column(sa.Unicode, unique = True,
                             doc = "URI of dbpedia Category: page")


class CwsacCampaign(Base, Mixin):
    __tablename__ = 'cwsac_campaigns'

    campaign = sa.Column(sa.Unicode, primary_key=True,
                         doc = "Campaign name")
    theater = sa.Column(sa.Unicode,
                        ForeignKey(CwsacTheater.__table__.c.theater),
                        nullable = False,
                        doc = "Theater")
    dbpedia = sa.Column(sa.Unicode,
                        doc = "URI of dbpedia resource")
    start_year = sa.Column(sa.Integer, nullable=True)
    start_month = sa.Column(sa.Integer, nullable=True)
    end_year = sa.Column(sa.Integer, nullable=True)
    end_month = sa.Column(sa.Integer, nullable=True)

class CwsacBattle(Base, Mixin):
    __tablename__ = 'cwsac_battles'
    __table_args__ = (#sa.CheckConstraint('us or cs or indian'),
                      #sa.CheckConstraint('not (us and cs and indian)'),
                      sa.CheckConstraint('start_date <= end_date'),)

    battle = sa.Column(sa.Unicode(6), primary_key=True,
                       doc = "CWSAC id")
    battle_name = sa.Column(sa.Unicode, nullable=False,
                            doc = "Battle name")
    start_date = sa.Column(sa.Date, nullable=False,
                           doc = "Start date")
    end_date = sa.Column(sa.Date, nullable=False,
                         doc = "End date")
    location = sa.Column(sa.Unicode, nullable=False,
                         doc = "Battle location")
    state = sa.Column(sa.Unicode(2), 
                      ForeignKey(State.__table__.c.abbr),
                      nullable=False,
                      doc = "State the battle occured in")
    results = sa.Column(sa.Enum("Confederate", "Union", "Inconclusive",
                                name="enum_cwsac_results"),
                        nullable=False,
                        doc = "Battle outcome")
    results_text = sa.Column(sa.Unicode, nullable=False,
                        doc = "Battle outcome")
    casualties_text = sa.Column(sa.Unicode, nullable=False)
    forces_text = sa.Column(sa.Unicode, nullable=False)
    forces_description = sa.Column(sa.Unicode, nullable=True)
    strength = sa.Column(sa.Integer,
                         CheckConstraintNonNeg('strength'))
    casualties = sa.Column(sa.Integer,
                           CheckConstraintNonNeg('casualties'),
                           doc = "Total casualties")
    significance = sa.Column(sa.Enum("A", "B", "C", "D",
                                     name='enum_cwsac_mil_sig'),
                             nullable=False,
                             doc = "CWSAC Battle significance [A-D]")
    preservation = sa.Column(sa.Unicode, nullable=True,
                             doc = "Preservation priority")
    description = sa.Column(sa.Unicode, nullable=False)
    other_names = sa.Column(sa.Unicode, nullable=True)
    assoc_battles = sa.Column(sa.Unicode, nullable=True)
    operation = sa.Column(sa.Boolean, nullable=False)
    # us = sa.Column(sa.Boolean, nullable=False,
    #                   doc = "Union was a combatant")
    # cs = sa.Column(sa.Boolean, nullable=False,
    #                    doc = "Confederacy was a combatant")
    # indian = sa.Column(sa.Boolean, nullable=False,
    #                    doc = "American Indians were a combatant")
    campaign = sa.Column(sa.Unicode,
                         ForeignKey(CwsacCampaign.__table__.c.campaign),
                         doc = "Campaign")
    url = sa.Column(sa.Unicode, nullable=False)


class CwsacForce(Base, Mixin):
    __tablename__ = 'cwsac_forces'
    __table_args__ = (sa.CheckConstraint("strength_min <= strength_max"),
                      sa.CheckConstraint("killed + wounded + missing + captured = casualties"),
                      sa.CheckConstraint("casualties <= strength_min"))

    forceid = sa.Column(sa.Unicode, primary_key=True)
    battle = sa.Column(sa.Unicode,
                       ForeignKey(CwsacBattle.__table__.c.battle))
    combatant = sa.Column(sa.Unicode,
                          ForeignKey(Combatant.__table__.c.combatant))
    strength_min = sa.Column(sa.Integer,
                             CheckConstraintNonNeg('strength_min'),
                             doc = "Force size in number of men (min)")
    strength_max = sa.Column(sa.Integer,
                             CheckConstraintNonNeg('strength_max'),
                             doc = "Force size in number of men (max)")
    casualties = sa.Column(sa.Integer,
                           CheckConstraintNonNeg('casualties'),
                           doc = "Number of casualties")
    killed = sa.Column(sa.Integer,
                       CheckConstraintNonNeg('killed'),
                       doc = "Killed")
    wounded = sa.Column(sa.Integer,
                        CheckConstraintNonNeg('wounded'),
                        doc = "Wounded")
    missing = sa.Column(sa.Integer,
                        CheckConstraintNonNeg('missing'),
                        doc = "Missing")
    captured = sa.Column(sa.Integer,
                         CheckConstraintNonNeg('captured'),
                         doc = "Captured")
    description = sa.Column(sa.Unicode, nullable=True)

class CwsacCommander(Base, Mixin):
    __tablename__ = 'cwsac_commanders'
    forceid = sa.Column(sa.Unicode, 
                        ForeignKey(CwsacForce.__table__.c.forceid),
                        primary_key=True)
    fullname = sa.Column(sa.Unicode, primary_key=True)
    rank = sa.Column(sa.Unicode, nullable=False)

class CwsacToDbpedia(Base, Mixin):
    __tablename__ = 'cwsac_to_dbpedia'
    rowid = sa.Column(sa.Integer, primary_key = True)
    id_from = sa.Column(sa.Unicode)
    id_to = sa.Unicode(sa.Unicode)
    relation = sa.Unicode(1)

# class Cwsac2Battle(Base, Mixin):
#     __tablename__ = 'cwsac2_battles'
#     # __table_args__ = (sa.CheckConstraint('us or cs or indian'),
#     #                   sa.CheckConstraint('not (us and cs and indian)'))

#     battle = sa.Column(sa.Unicode(5), primary_key = True)
#     battle_name = sa.Column(sa.Unicode,
#                             doc = "Battle name")
#     dates = sa.Column(sa.Unicode,
#                       doc = "Date range")
#     state = sa.Column(sa.Unicode(2),
#                       ForeignKey(State.__table__.c.abbr),
#                       doc = "State. Primary state in which the battle took place.")
#     campaign = sa.Column(sa.Unicode,
#                          doc = "Campaign")
#     forces_text = sa.Column(sa.Unicode,
#                             doc = "Forces engaged")
#     forces = sa.Column(sa.Unicode,
#                        doc = "Forces engaged")
#     strength = sa.Column(sa.Integer,
#                          CheckConstraintNonNeg('strength'))
#     results_text = sa.Column(sa.Unicode,
#                              doc = "Results description")
#     results = sa.Column(sa.Enum("Confederate", "Union", "Inconclusive",
#                                 name="enum_cwsac2_results"),
#                         doc = "Results")
#     url = sa.Column(sa.Unicode, nullable = False)
#     # us = sa.Column(sa.Boolean, nullable=False,
#     #                   doc = "Union was a combatant")
#     # cs = sa.Column(sa.Boolean, nullable=False,
#     #                    doc = "Confederacy was a combatant")
#     # indian = sa.Column(sa.Boolean, nullable=False,
#     #                    doc = "American Indians were a combatant")
#     study_area = sa.Column(sa.Float,
#                            CheckConstraintNonNeg('study_area'),
#                            doc = """Study Area (in acres) represents the historic
#                            extent of the battle as
#                            it unfolded across the landscape. The Study
#                            Area contains resources known to relate to
#                            or contribute to the battle event: where
#                            troops maneuvered and deployed, immediately
#                            before, during, and after combat, and where
#                            they fought during combat. Historic
#                            accounts, terrain analysis, and feature
#                            identification inform the delineation of
#                            the Study Area boundary. The Study Area
#                            indicates the extent to which historic and
#                            archeological resources associated with the
#                            battle (areas of combat, command,
#                            communications, logistics, medical
#                            services, etc.)  may be found. Surveyors
#                            delineated Study Area boundaries for every
#                            battle site that was positively identified
#                            through research and field survey,
#                            regardless of its present integrity.""".strip())
#     core_area = sa.Column(sa.Float,
#                           CheckConstraintNonNeg('core_area'),
#                           doc = """The Core Area represents the areas of direct
#                           engagement on the battlefield. Positions
#                           that delivered or received fire, and the space
#                           connecting them, fall within the Core Area.
#                           Frequently described as \"hallowed ground,\"
#                           land within the Core Area is often the first to
#                           be targeted for protection. There may be
#                           more than one Core Area on a battlefield,
#                           but all lie within the Study Area.""")
#     potnr_boundary = sa.Column(sa.Float,
#                                CheckConstraintNonNeg('potnr_boundary'),
#                                doc = """
#                                Unlike the Study and Core Area, which are
#                                based only upon the interpretation of historic
#                                events, the Potential National Register
#                                (PotNR) boundary represents ABPP's
#                                assessment of a Study Area's current integrity
#                                (the surviving landscape and features that
#                                convey the site's historic sense of place). The
#                                PotNR boundary may include all or some of
#                                the Study Area, and all or some of the Core
#                                Area. Although preparing a National Register
#                                of Historic Places nomination may require
#                                further assessment of historic integrity and
#                                more documentation than that provided by
#                                the ABPP survey, PotNR boundaries identify
#                                land that merits this additional effort.""")


# class Cwsac2BattleDate(Base, Mixin):
#     """ CWSAC II Battle date ranges

#     This is a separate table from cwsac2_battles because the
#     battle SC00? has two separate periods of fighting.
        
#     """
#     __tablename__ = 'cwsac2_battle_dates'

#     battle = sa.Column(sa.Unicode(5), ForeignKey(Cwsac2Battle.__table__.c.battle),
#                        primary_key=True)
#     spell = sa.Column(sa.Integer, primary_key=True)
#     start_date = sa.Column(sa.Date, doc="Start date")
#     end_date = sa.Column(sa.Date, doc="End date")


# class Cwsac2Force(Base, Mixin):
#     __tablename__ = 'cwsac2_forces'

#     forceid = sa.Column(sa.Unicode, primary_key=True)
#     battle = sa.Column(sa.Unicode,
#                        ForeignKey(Cwsac2Battle.__table__.c.battle))
#     combatant = sa.Column(sa.Unicode,
#                           ForeignKey(Combatant.__table__.c.combatant))
#     forces = sa.Column(sa.Unicode)
#     strength = sa.Column(sa.Integer,
#                          CheckConstraintNonNeg('strength'))

# class Cwsac2Commander(Base, Mixin):
#     __tablename__ = 'cwsac2_commanders'
#     forceid = sa.Column(sa.Unicode, 
#                         ForeignKey(Cwsac2Force.__table__.c.forceid),
#                         primary_key=True)
#     fullname = sa.Column(sa.Unicode, primary_key=True)
#     rank = sa.Column(sa.Unicode, nullable=False)

# class Cwsac2Location(Base, Mixin):
#     __tablename__ = 'cwsac2_locations'
#     battle = sa.Column(sa.Unicode,
#                        ForeignKey(Cwsac2Battle.__table__.c.battle),
#                        primary_key=True)
#     locnum = sa.Column(sa.Integer, primary_key=True)
#     location = sa.Column(sa.Unicode)
#     state = sa.Column(sa.Unicode(2),
#                       ForeignKey(State.__table__.c.abbr))


# class BodBattle(Base, Mixin):
#     """ Battles from Bodart """
#     __tablename__ = 'bod_battles'
#     battle = sa.Column(sa.Unicode,
#                        primary_key = True,
#                        doc = "Battle")
#     battle_name = sa.Column(sa.Unicode,
#                             doc = "Battle name")
#     start_date = sa.Column(sa.Date,
#                            doc = "Start date")
#     end_date = sa.Column(sa.Date,
#                          doc = "End date")
#     order = sa.Column(sa.Integer,
#                         doc = "Severity category [1-6]")
    # battle = sa.Column(sa.Boolean,
    #                      doc = "Schlacht (battle category); battle")
    # meeting = sa.Column(sa.Boolean,
    #                     doc = "Treffen (battle category); meeting/encounter")
    # siege = sa.Column(sa.Boolean,
    #                   doc = "Belagerung (battle category); siege")
    # capture = sa.Column(sa.Boolean,
    #                      doc = "Einnahme (battle category); capture")
    # surrender = sa.Column(sa.Boolean,
    #                       doc = "Kapitulation (battle category); surrender")


# class BodForce(Base, Mixin):
#     """ Military forces from Bodart """
#     __tablename__ = 'bod_forces'

#     battle = sa.Column(sa.Unicode,
#                        ForeignKey(BodBattle.__table__.c.battle),
#                        primary_key = True,
#                        doc = "Battle")
#     victor = sa.Column(sa.Boolean,
#                        doc = "victor",
#                        primary_key = True)
#     combatant = sa.Column(sa.Unicode,
#                           ForeignKey(Combatant.__table__.c.combatant),
#                           doc = "Combatant")
#     infantry = sa.Column(sa.Integer,
#                            CheckConstraintNonNeg('infanterie'),
#                            doc = "Number of infantry")
#     cavalry = sa.Column(sa.Integer,
#                            CheckConstraintNonNeg('kavallerie'),
#                            doc = "Number of cavalry")
#     artillery = sa.Column(sa.Integer,
#                            CheckConstraintNonNeg('artillerie'),
#                            doc = "Number of artillery")
#     guns = sa.Column(sa.Integer,
#                           CheckConstraintNonNeg('geschutze'),
#                           doc = "Number of guns")
#     strength = sa.Column(sa.Integer,
#                               CheckConstraintNonNeg('gesamt_starke'),
#                               doc = "Total strength")
#     strength_engaged = sa.Column(sa.Integer,
#                                  CheckConstraintNonNeg('hievon_im_kampfe'),
#                                  doc = "Number of troops engaged in battle")
#     killed = sa.Column(sa.Integer,
#                     CheckConstraintNonNeg('tot'),
#                     doc = "Killed")
#     killed_officers = sa.Column(sa.Integer,
#                          CheckConstraintNonNeg('tot_offz'),
#                          doc = "Officers killed")
#     killed_generals = sa.Column(sa.Integer,
#                         CheckConstraintNonNeg('tot_gen'),
#                         doc = "Generals killed")
  
#     wounded = sa.Column(sa.Integer,
#                           doc = "Wounded")
#     wounded_officers = sa.Column(sa.Integer,
#                                doc = "Officers wounded")
#     wounded_generals = sa.Column(sa.Integer,
#                               doc = "Generals wounded")
  
#     killed_wounded = sa.Column(sa.Integer,
#                                  doc = "Killed and wounded")
#     killed_wounded_officers = sa.Column(sa.Integer,
#                                       doc = "Officers killed and wounded")
#     killed_wounded_generals = sa.Column(sa.Integer,
#                                      doc = "Generals killed and wounded")

#     captured = sa.Column(sa.Integer,
#                          doc = "Captured")
#     captured_officers = sa.Column(sa.Integer,
#                               doc = "Officers captured")
#     captured_generals = sa.Column(sa.Integer,
#                              doc = "Generals captured")
  
#     missing_gefangen = sa.Column(sa.Integer,
#                                   doc = "Missing and captured")
#     missing_gefangen_offz = sa.Column(sa.Integer,
#                                        doc = "Officers missing and captured")
#     missing_gefangen_gen = sa.Column(sa.Integer,
#                                       doc = "Generals missing and captured")
     
#     casualties = sa.Column(sa.Integer,
#                                doc = "Casualties")
#     casualties_officers = sa.Column(sa.Integer,
#                                     doc = "Officer casualties")
#     casualties_generals = sa.Column(sa.Integer,
#                                    doc = "General casualties")
    

# class BodToCwsac(Base, Mixin):
#     __tablename__ = 'bod_to_cwsac'
#     rowid = sa.Column(sa.Integer, primary_key = True)
#     id_from = sa.Column(sa.Unicode)
#     id_to = sa.Unicode(sa.Unicode)
#     relation = sa.Unicode(1)

# class BodToDbpedia(Base, Mixin):
#     __tablename__ = 'bod_to_dbpedia'
#     rowid = sa.Column(sa.Integer, primary_key = True)
#     id_from = sa.Column(sa.Unicode)
#     id_to = sa.Unicode(sa.Unicode)
#     relation = sa.Unicode(1)

# --------------------
    
# # class DyerBattle(Base, Mixin):
# #     """ Battle from Dyer's Compendium """
# #     __tablename__ = 'dyer_battle'
# #     battle = sa.Column(sa.Integer,
# #                        primary_key = True,
# #                        doc = "Battle id")
# #     battle_name = sa.Column(sa.Unicode)
# #     state = sa.Column(sa.Unicode(2),
# #                       ForeignKey(State.__table__.c.abbr),
# #                       doc = "location (State)")
# #     year = sa.Column(sa.Integer, doc = "Year")
# #     start_date = sa.Column(sa.Date, doc = "Start date")
# #     end_date = sa.Column(sa.Date, doc = "End date")
# #     event_type = sa.Column(sa.Unicode, doc = "Event type")
# #     killed = sa.Column(sa.Integer,
# #                        CheckConstraintNonNeg('killed'))
# #     wounded = sa.Column(sa.Integer,
# #                         CheckConstraintNonNeg('wounded'))
# #     missing = sa.Column(sa.Integer,
# #                         CheckConstraintNonNeg('missing'))
# #     cap_missing = sa.Column(sa.Integer,
# #                             CheckConstraintNonNeg('cap_missing'))
# #     casualties = sa.Column(sa.Integer,
# #                            CheckConstraintNonNeg('casualties'))
# #     text = sa.Column(sa.Unicode)

# ----------------

class _FoxForceMixin(object):
    battle = sa.Column(sa.Integer,
                       primary_key=True,
                       doc = "Battle id")
    combatant = sa.Column(sa.Unicode,
                          doc = "Combatant")
    battle_name = sa.Column(sa.Unicode,
                            doc = "Battle name")
    state = sa.Column(sa.Unicode(2))
    start_date = sa.Column(sa.Date, doc = "Start date")
    end_date = sa.Column(sa.Date, doc = "End date")
    killed = sa.Column(sa.Integer,
                       CheckConstraintNonNeg('killed'),
                       doc = "Killed")
    wounded = sa.Column(sa.Integer,
                        CheckConstraintNonNeg('wounded'),
                        doc = "Wounded, including mortally wounded")
    missing = sa.Column(sa.Integer,
                        CheckConstraintNonNeg('missing'),
                        doc = "Captured and missing")
    casualties = sa.Column(sa.Integer,
                           CheckConstraintNonNeg('casualties'),
                           doc = "Total casualties")


class FoxForce(Base, Mixin, _FoxForceMixin):
    """ Battle from Fox's Regimental Losses

    From the original source on p. 542.

      With this chapter is given a chronological list of the battles and
      minor engagements, showing the loss in each. The figures are compiled
      from the battle reports and revised casualty lists in the. \"Official
      Records of the Union and Confederate Armies,\" published, or in process
      of publication, by the War Department at Washington.

      The figures in the table of Confederate losses are the ones
      officially reported by the Confederate generals in command, or by
      their surgeon-general, to whom, in many instances, that duty seems
      to have been entrusted. There are no official Confederate casualty
      reports for the latter part of the war, and so there is no
      statement of loss for several battles. Estimates might be quoted,
      but such figures are not within the province of this work.

    Fox does not use consistent battle names in his tables, and no effort has
    been made (yet) to match these; largely because the definitions of 
    engagements differ between Confederate and Union casualty data; see
    the Atlanta campaign.

    'Siege of Fort Wagner, S. C.' and 'Siege of Knoxville' only have a year and month,
    so the start and end dates are set to the first and last days of the month.
    
    """

    __tablename__ = 'fox_forces'
    __table_args__ = (sa.ForeignKeyConstraint(['combatant'],
                                              [Combatant.__table__.c.combatant],
                                              initially="DEFERRED", deferrable=True),
                      sa.ForeignKeyConstraint(['state'],
                                              [State.__table__.c.abbr],
                                              initially="DEFERRED", deferrable=True),
                      sa.CheckConstraint('killed + wounded + missing = casualties')
                      )
    aggrow = sa.Column(sa.Boolean, doc = 'Row aggregates other rows')
    comment = sa.Column(sa.Unicode,
                        doc = "Comment")


class FoxForce2(Base, Mixin, _FoxForceMixin):
    """ Casualty data from Fox's Regimental Losses (revised)

    The Table of casualties in Fox's regimental losses contains
    a lot of additional data in the footnotes.  This version integrates
    that data, and removes the aggregates rows.

    """
    __tablename__ = 'fox_forces_2'
    __table_args__ = (sa.ForeignKeyConstraint(['combatant'],
                                              [Combatant.__table__.c.combatant],
                                              initially="DEFERRED", deferrable=True),
                      sa.ForeignKeyConstraint(['state'],
                                              [State.__table__.c.abbr],
                                              initially="DEFERRED", deferrable=True),
                      sa.CheckConstraint('killed + wounded + missing = casualties')
                      )

    cavalry = sa.Column(sa.Boolean,
                        doc = "Cavalry engagement (if indicated in a footnote). ")
    


class FoxOutcome(Base, Mixin):
    """ Victories and defeats from Fox's Regimental Losses

    These data from tables on p. 543-544.

    Fox's discussion of determining victories and defeats (543)

       In connection with these matters the question naturally
       arises,--Which were victories, and which were defeats?

       To answer fairly and without prejudice would only invite bitter and
       senseless criticism from both sides. It is too soon to attempt any
       discussion of this much vexed topic. Still, there are certain conceded
       facts relative to this matter which one might venture to recall to
       mind. They may be premised with the military axioms,--that when an
       army retains possession of the battle field and buries its enemy's
       dead, it certainly cannot be considered as a defeated army; and that
       when an army abandons the field, either slowly or in rout, and leaves
       its dead and wounded in the hands of the enemy, it certainly should
       not claim a victory.

    The tables in Fox correspond to unique combinations of (**union**,
    **victory_type**)

    In the case (Union, victory)

       In the following named battles the Union armies remained in
       undisturbed possession of the field, the enemy leaving many of their
       wounded, and most of their dead unburied:

    In the case (Union, assault)

       The Union armies were successful, also, in the following
       assaults. They were the attacking party, and carried the forts,
       or intrenched positions, by storm.

    For (Confederate, victory)

       In the following battles the Confederates remained in undisturbed
       possession of the field, the Union armies leaving its unburied
       dead and many of its wounded in their hands:

    In the case (Confederate, defense)

        In the following assaults the Confederates successfully
        repulsed the attacks of the enemy:

    In the case (Union, defense)

        In the following assaults, or sorties, the Confederates were
        the attacking party, and were repulsed:

    There are no battles in which the Confederates were successful in
    assaulting a fortified Union position, e.g. there are no instances
    of (Confederate, assault).

    Fox implies that any battles not listed were inconclusive.

       Other instances on each side could be mentioned, but they would
       invite discussion and are better omitted.

    Like Livermore, Fox groups battles into assaults on fortified positions
    and other battles, and uses different criteria to judge the victor of the
    battle in these cases.

    Several \"battles\" are coded as Confederate victories, even
    though the Union clearly won these battles. These observations
    refer to a failed an assault on the Confederate
    fortified position, within a siege that the Union would eventually win.
    These observations are:

    - Vicksburg, Miss (May 19) 
    - Vicksburg, Miss (May 22) 
    - Port Hudson (May 27) 
    - Port Hudson (May 27)
    
    """
    __tablename__ = 'fox_outcomes'
    battle = sa.Column(sa.Integer,
                      primary_key = True,
                      doc = 'Battle id')
    battle_name = sa.Column(sa.Unicode,
                            doc = "Battle name")
    state = sa.Column(sa.Unicode(2),
                      ForeignKey(State.__table__.c.abbr))
    union_victory = sa.Column(sa.Boolean, 
                              doc = "Union victory else Confederate victory.")
    victory_type = sa.Column(sa.Enum("victory", "assault", "defense",
                                     name="enum_fox_victory_types"), 
                             doc = "Victory type, see documentation")


class FoxOutcomeToCwsac(Base, Mixin, CwsacLink):
    """ Relationships between Fox Outcomes and CWSAC battle ids """
    __tablename__ = 'fox_outcome_to_cwsac'
    battle = sa.Column(sa.Integer,
                       ForeignKey(FoxOutcome.__table__.c.battle),
                       primary_key=True)


# # class FoxForceToCwsac(Base, Mixin, CwsacLink):
# #     """ Relationships between Fox Forces and CWSAC battle ids """
# #     __tablename__ = 'fox_forces_to_cwsac'
# #     battle = sa.Column(sa.Integer,
# #                        ForeignKey(FoxForce.__table__.c.battle),
# #                        primary_key=True)


# # class FoxForce2ToCwsac(Base, Mixin, CwsacLink):
# #     """ Relationships between Livermore and CWSAC battle ids """
# #     __tablename__ = 'fox_forces_2_to_cwsac'
# #     battle = sa.Column(sa.Integer,
# #                        ForeignKey(FoxForce2.__table__.c.battle),
# #                        primary_key=True)


# # class KenBattle(Base, Mixin):
# #     """ Battle from Kennedy (1998) """
# #     __tablename__ = 'ken_battles'
# #     __table_args__ = (sa.CheckConstraint('us or cs or indian'),
# #                       sa.CheckConstraint('not (us and cs and indian)'),
# #                       sa.CheckConstraint('casualties_min <= casualties_max'),
# #                       sa.CheckConstraint('(casualties_min is null and casualties_max is null) or (casualties_min is not null and casualties_max is not null)'))

# #     battle = sa.Column(sa.Unicode, primary_key=True,
# #                         doc = "CWSAC battle id")
# #     casualties_min = sa.Column(sa.Integer,
# #                                CheckConstraintNonNeg('casualties_min'),
# #                                doc = "Total Casualties (minimum)")
# #     casualties_max = sa.Column(sa.Integer,
# #                                CheckConstraintNonNeg('casualties_max'),
# #                                doc = "Total Casualties (maximum)")
# #     us = sa.Column(sa.Boolean,
# #                        doc = "Union forces participated")
# #     cs = sa.Column(sa.Boolean,
# #                        doc = "Confederate forces participated") 
# #     indian = sa.Column(sa.Boolean,
# #                        doc = "American Indians forces participated")


# # class KenForce(Base, Mixin):
# #     """ Military Force from Kennedy (1998) """
# #     __tablename__ = 'ken_forces'
# #     __table_args__ = (sa.CheckConstraint('casualties_min <= casualties_max'),
# #                       sa.CheckConstraint('(casualties_min is null and casualties_max is null) or (casualties_min is not null and casualties_max is not null)')
# #                       )

# #     forceid = sa.Column(sa.Unicode, primary_key=True,
# #                         doc = "Military force ID")
# #     battle = sa.Column(sa.Unicode,
# #                        ForeignKey(KenBattle.__table__.c.battle),
# #                        doc = "CWSAC battle id")
# #     combatant = sa.Column(sa.Unicode,
# #                           ForeignKey(Combatant.__table__.c.combatant),
# #                           doc = "Combatant")
# #     casualties_min = sa.Column(sa.Integer,
# #                                CheckConstraintNonNeg('casualties_min'),
# #                                doc = "Casualties (minimum)")
# #     casualties_max = sa.Column(sa.Integer,
# #                                CheckConstraintNonNeg('casualties_max'),
# #                                doc = "Casualties (maximum)")


# # class KenToCwsac(Base, Mixin, CwsacLink):
# #     """ Relationships between Livermore and CWSAC battle ids """
# #     __tablename__ = 'ken_to_cwsac'
# #     battle = sa.Column(sa.Unicode, ForeignKey(KenBattle.__table__.c.battle), primary_key=True)


# # class KenToDbpedia(Base, Mixin, DbpediaLink):
# #     """ Relationships between Kennedy and Dbpedia battle ids"""
# #     __tablename__ = 'ken_to_dbpedia'
# #     battle = sa.Column(sa.Unicode, ForeignKey(KenBattle.__table__.c.battle), primary_key=True)


# class LivBattle(Base, Mixin):
#     """Battle data from Livermore (1908) """
#     __tablename__ = 'liv_battles'
#     battle = sa.Column(sa.Unicode, primary_key=True,
#                          doc = "Battle id")
#     battle_name = sa.Column(sa.Unicode,
#                      doc = "Battle name")
#     start_date = sa.Column(sa.Date,
#                            doc = "Start date")
#     end_date = sa.Column(sa.Date,
#                          doc = "End date")
#     iscampaign = sa.Column(sa.Boolean, 
#                            doc = "Entry aggregates multiple engagements")
#     parent = sa.Column(sa.Unicode, 
#                        doc = "Is a sub-event of the entry")
#     assault = sa.Column(sa.Boolean, nullable=True,
#                           doc = "Assault on a fortified position")
#     us_attack = sa.Column(sa.Boolean, nullable=True,
#                          doc = "The U.S. was the attacker")
#     assault_result = sa.Column(sa.Unicode, nullable=True,
#                                doc = "Assault Result")

# class LivForce(Base, Mixin):
#     """Military force data in Livermore (1908)"""
#     __tablename__ = 'liv_forces'
#     #__table_args__ = (sa.CheckConstraint('hit < force'),)
#     battle = sa.Column(sa.Unicode,
#                        ForeignKey(LivBattle.__table__.c.battle),
#                        primary_key = True,
#                        doc = "Battle")
#     combatant = sa.Column(sa.Unicode,
#                           ForeignKey(Combatant.__table__.c.combatant),
#                           primary_key = True,
#                           doc = "Combatant")
#     force = sa.Column(sa.Integer,
#                       CheckConstraintNonNeg('force'),
#                       doc = "Forces engaged in battle")
#     hit = sa.Column(sa.Integer,
#                     CheckConstraintNonNeg('force'),
#                     doc = "Hits (killed and wounded)")
#     result = sa.Column(sa.Unicode,
#                        nullable = True,
#                        doc = "Battle result")

# class LivArmySize(Base, Mixin):
#     """ Livermore's estimates of the Union and Confederate Army Sizes """
#     __tablename__ = 'liv_army_size'
#     date = sa.Column(sa.Date, primary_key = True,
#                      doc = "Date")
#     union = sa.Column(sa.Integer,
#                       nullable = False,
#                       doc = "Number on Union rolls")
#     confed = sa.Column(sa.Integer,
#                        doc = "Number on Confederate Returns")



# # class LivToDbpedia(Base, Mixin, DbpediaLink):
# #     """ Relationships between Livermore and Dbpedia battle ids"""
# #     __tablename__ = 'liv_to_dbpedia'
# #     battle = sa.Column(sa.Unicode, ForeignKey(LivBattle.__table__.c.battle), primary_key=True)


# # class LivToCwsac(Base, Mixin, CwsacLink):
# #     """ Relationships between Livermore and CWSAC battle ids """
# #     __tablename__ = 'liv_to_cwsac'
# #     battle = sa.Column(sa.Unicode, ForeignKey(LivBattle.__table__.c.battle), primary_key=True)


# class _PhiForce(object):
#     battle = sa.Column(sa.Integer,
#                        primary_key=True,
#                        doc = "Battle id")
#     combatant = sa.Column(sa.Unicode,
#                           primary_key=True,
#                           doc = "Combatant")
#     killed = sa.Column(sa.Integer,
#                        CheckConstraintNonNeg('killed'),
#                        doc = "Number killed")
#     wounded = sa.Column(sa.Integer,
#                         CheckConstraintNonNeg('wounded'),
#                         doc = "Number wounded")
#     missing = sa.Column(sa.Integer,
#                         CheckConstraintNonNeg('missing'),
#                         doc = "Number missing")
#     losses = sa.Column(sa.Integer,
#                        CheckConstraintNonNeg('losses'),
#                        doc = "Total losses (killed + wounded + missing)")


# class PhiBattle(Base, Mixin):
#     """ Battle data from Phister """
#     __tablename__ = 'phi_battles'

#     battle = sa.Column(sa.Integer, primary_key=True,
#                          doc = "Battle id")
#     battle_name = sa.Column(sa.Unicode, nullable = False,
#                             doc = "Battle name")
#     start_date = sa.Column(sa.Date, nullable = False,
#                            doc = "Start date")
#     end_date = sa.Column(sa.Date, nullable = False,
#                          doc = "End date")
#     campaign = sa.Column(sa.Boolean, nullable = False,
#                            doc = "Entry consists of multiple engagements")
#     surrender = sa.Column(sa.Boolean, nullable = False,
#                           doc = "Entry was a surrender")


# class PhiForce(Base, Mixin, _PhiForce):
#     "Military Force data from Phister"
#     __tablename__ = 'phi_forces'
#     __table_args__ = (sa.ForeignKeyConstraint(['battle'],
#                                               [PhiBattle.__table__.c.battle],
#                                               initially="DEFERRED", deferrable=True),
#                       sa.ForeignKeyConstraint(['combatant'],
#                                               [Combatant.__table__.c.combatant],
#                                               initially="DEFERRED", deferrable=True),
#                       #sa.CheckConstraint('killed + wounded + missing = losses')
#                       )



# class PhiForce2(Base, Mixin, _PhiForce):
#     """Military Force data from Phister (cleaned)

#     The following edits are made to the table **phi_forces**:

#     - fill in missing killed, wounded, and missing values of US force in 2354 
#       using the proportions of K/W/M in battle 2345.
#     - Adjust battle 2345 by subtracting 2354 losses (and imputed killed, wounded,
#       and missing from the previous step), since
#       battle 2345 includes 2354 losses.
#     - Delete 2372 ('Campaign in Northern Georgia, from Chattanooga, Tenn., to Atlanta, Ga.')
#       which overlaps (I think?) with battles 2371, 2364, 2360, 2354, 2345, 2342, 2333 2338.

#     This table should be merged with CWSAC ids using **phi_to_cwsac_2**.
#     """
#     __tablename__ = 'phi_forces_2'
#     __table_args__ = (sa.ForeignKeyConstraint(['battle'],
#                                               [PhiBattle.__table__.c.battle],
#                                               initially="DEFERRED", deferrable=True),
#                       sa.ForeignKeyConstraint(['combatant'],
#                                               [Combatant.__table__.c.combatant],
#                                               initially="DEFERRED", deferrable=True),
#                       #sa.CheckConstraint('killed + wounded + missing = losses')
#                       )

#     @classmethod
#     def from_phi_force(cls, x):
#         obj = cls()
#         for col in [c.name for c in x.__table__.columns]:
#             setattr(obj, col, getattr(x, col))
#         return obj


# class PhiToDbpedia(Base, Mixin, DbpediaLink):
#     """ Relationships between Phister and Dbpedia battles """
#     __tablename__ = 'phi_to_dbpedia'
#     battle = sa.Column(sa.Integer, ForeignKey(PhiBattle.__table__.c.battle), primary_key=True)


# class PhiToCwsac(Base, Mixin, CwsacLink):
#     """ Relationships between Phister and CWSAC battle ids """
#     __tablename__ = 'phi_to_cwsac'
#     battle = sa.Column(sa.Integer, ForeignKey(PhiBattle.__table__.c.battle), primary_key=True)


# class PhiToCwsac2(Base, Mixin, CwsacLink):
#     """ Relationships between Phister and CWSAC battle ids (cleaned)

#     This table accounts for edits made in **phi_forces_2**. Battle
#     2345 now does not include casualties from Kennesaw Mountain, and
#     thus is no longer linked to GA015.

#     """
#     __tablename__ = 'phi_to_cwsac_2'
#     battle = sa.Column(sa.Integer, ForeignKey(PhiBattle.__table__.c.battle), primary_key=True)

#     @classmethod
#     def from_phi_to_cwsac(cls, x):
#         return cls(battle = x.battle,
#                    relation = x.relation,
#                    cwsac = x.cwsac)


# class WikiForces(Base, Mixin):
#     """ Military force data from wikipedia

#     I had to enter this by hand from Wikipedia on August 10, 2011.
#     The since the dbpedia data for military conflicts drops the sides
#     of the combatants. Additionally the data from the infobox is unstructured
#     enough to make parsing casualties and strength hard.

#     I intend this table to be a short-term fix until better data can be gathered
#     from dbpedia or freebase.
#     """
#     __tablename__ = 'wiki_forces'
#     __table_args__ = (sa.CheckConstraint('strength_min <= strength_max'), )
    
#     battle = sa.Column(sa.Unicode, primary_key = True,
#                        doc = "dbpedia URI of the battle")
#     combatant = sa.Column(sa.Unicode,
#                           ForeignKey(Combatant.__table__.c.combatant),
#                           primary_key = True,
#                           doc = "Combatant")
#     strength_min = sa.Column(sa.Integer,
#                              CheckConstraintNonNeg('strength_min'),
#                              doc = "Minimum strength in number of troops") 
#     strength_max = sa.Column(sa.Integer,
#                              CheckConstraintNonNeg('strength_max'),
#                              doc = "Maximum strength in number of troops")
#     casualties_min = sa.Column(sa.Integer,
#                              CheckConstraintNonNeg('casualties_min'),
#                              doc = "Minimum casualties") 
#     casualties_max = sa.Column(sa.Integer,
#                              CheckConstraintNonNeg('casualties_max'),
#                              doc = "Maximum casualties")

