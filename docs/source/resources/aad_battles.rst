####################################################################################################################
Records About Civil War Battle Sites, created by the CWSAC, 1990-1993, and deposited with the National Archives AAD.
####################################################################################################################

:name: aad_battles
:path: data/aad_battles.csv
:format: csv

gBattle-level data of the battles in the original reports of the Civil War Sites Advisory Commision compiled during 1990-1993.

These reports were deposited with the `National Archives <https://archives.gov>`__ `Access to Archival Databases <https://aad.archives.gov/aad/series-description.jsp?s=1076&cat=WR25&bc=,sl>`__.

Each observation in the data is a battle.
The battles are those identified by the CWSAC as the prinicipal battles of the American Civil War, and later used in the official CWSAC Report and its updates, and the CWSS database.

The original documentation reads:

    The Civil War Sites Advisory Commission created this database to
    support its congressional mandate to identify Civil War
    battlefields, determine their historic significance, assess short-
    and long-term threats to their integrity, and propose new ideas
    about their preservation and interpretation. The Commission
    intended the recommendations to be used as the basis for
    legislative proposals in the area of battlefield preservation.

    The Civil War Sites Advisory Commission data files contain
    information relating to battlefields of the American Civil War,
    1861-1865. Four data files compose this series: Events, Counties,
    Campaign, and Theater files. The Events file is the primary data
    file. Of 10,500 armed conflicts in the military history of the
    Civil War, the file contains information on 384 conflicts that the
    Commission identified as the principal battles. Each record
    identifies the following information: state and county or counties
    of the historic site, the type of battle or event that occurred
    there, the theater of operations and the campaign to which the
    engagement relates, the dates of the battle or event, the current
    ownership of the site, and the assessment of three subject area
    experts of the military significance, physical integrity, historic
    preservation status, and interpretive potential of the site or
    event, and whether it should be a priority for protection of
    cultural property. The records of the Counties file identify the
    county location(s) of each battlefield and are linked to the
    Events file by a common battlefield reference number. The records
    of the Campaign file include a code for each of 116 campaigns and
    provide its name, dates, and a ranking of the military importance
    of the campaign's battle events. The records of the Campaign file
    are linked by the campaign code to the records in the Events
    file. The Theater file records identify five designated Civil War
    theaters of operation and are linked to the Events file by a
    theater code.

    The records in this file potentially identify the following information: state and county or counties of the historic site, the type of battle or event that occurred there, the theater of operations and the campaign to which the engagement relates, the dates of the battle or event, the current ownership of the site, and the assessment of three subject area experts of the military significance, physical integrity, historic preservation status, and interpretive potential of the site or event, and whether it should be a priority for protection of cultural property.


**Sources:**
- CWSAC_AAD; https://aad.archives.gov/aad/series-description.jsp?s=1076&cat=WR25&bc=,sl


Schema
======



===============================  =======  ===================================================================================================
reference_number                 string   Reference Number
event                            string   event
type                             string   Type
start_date                       date     Start date
end_date                         date     End date
theater                          string   Theater
campaign                         string   campaign
threats                          number   threats
ownership_federal                boolean  Ownership (Federal)
ownership_local                  boolean  Ownership (local government)
ownership_private                boolean  Ownership (private)
ownership_state                  boolean  Ownership (state government)
ownership_unknown                boolean  Ownership (unknown)
park                             boolean  park
integrity                        string   integrity
military                         string   military
interpretive_political           boolean  Interpretive Potential: effect upon international diplomacy
interpretive_commander_loss      boolean  Interpretive Potential: Loss of significant commander (Wounding, Death, Relieved of Command)
interpretive_casualties          boolean  Interpretive Potential: Unusually High Casualties
interpretive_tactics_strategy    boolean  Interpretive Potential: Illustrates Important Lessons in Military Tactics and Strategy
interpretive_public_mind         boolean  Interpretive Potential: Unusual Importanve in the Public Mind and Imagination
interpretive_combat_arm          boolean  Interpretive Potential: Significant Participation of Cavalry, Artillery, or Other Single Combat Arm
interpretive_military_firsts     boolean  Interpretive Potential: Military Firsts
interpretive_minority_troops     boolean  Interpretive Potential: Participation of Significant Numbers of Minority Troops
interpretive_economic            boolean  Interpretive Potential: Significant Economic Consequences
interpretive_archaelolgical      boolean  Interpretive Potential: High Archaelogical Potential
interpretive_logistics           boolean  Interpretive Potential: Unusually Significant Logistics or Supply Feat
interpretive_individual_bravery  boolean  Interpretive Potential: Exception Individual Initiative in Bravery or Command
interpretive_group_behavior      boolean  Interpretive Potential: Exceptional Group Behavior
interpretive_joint_ops           boolean  Interpretive Potential: Illustrates Joint Operations (Army, Navy)
interpretive_coop_armies         boolean  Interpretive Potential: Illustrates Cooperation of Separate Military Departments or Armies
interpretive_naval               boolean  Interpretive Potential: Naval Operations
jim                              string   jim
ed                               string   Military (Ed)
bill                             string   Military (Bill)
protected                        number   Protected land area (acres)
percent                          number   Protected (percent of land area)
county                           string   County
value                            string   value
priority1                        boolean  priority1
url                              string   url
===============================  =======  ===================================================================================================

reference_number
----------------

:title: Reference Number
:type: string
:format: default



The reference number assigned to the battle site/event. The first two letters are the abbreviation of the state in which the battle site/event is located. The number reflects the order in which the battle site/events in the state were assigned a reference number.


       
event
-----

:title: event
:type: string
:format: default





       
type
----

:title: Type
:type: string
:format: default



The kind of conflict as designated in The War of the Rebellion: A Compilation of the Official Records of the Union and Confederate Armies (Washington, DC: GPO, 1880-1901).


       
start_date
----------

:title: Start date
:type: date
:format: default



Beginning day of the event.


       
end_date
--------

:title: End date
:type: date
:format: default



End day of the event.      


       
theater
-------

:title: Theater
:type: string
:format: default



The name of the theater. 1 Main Eastern Theater of operation. 2 Lower Seaboard Theater of Operation. 3 Main Western Theater of Operations & the Gulf Approach (1861-1863). 4 Trans-Mississippi Theater of Operations 5 Pacific Coast Theater Robert N. Scott, the overall editor of The War of the Rebellion: A Compilation of the Official Records of the Union and Confederate Armies (Washington, DC: The Government Printing Office, 1880-1901), arranged Series I, of that publication, according to the campaigns and several theaters of operations .... The Official Records editors recognized five theaters of operations, Main Eastern, Lower Seaboard, Main Western, Trans-Mississippi, and Pacific Coast. Dr. Dallas D. Irvine, the creator and major compiler-editor of Military Operations of the Civil War: A Guide-Index to Official Records of the Union and Confederate Armies, 1861-1865 (Washington, DC: The Government Printing Office, 1968-80), modified this arrangement by removing the Gulf Approach operations from the Main Western Theater and combining them with the Lower Seaboard Theater. The Commission study used Irvine's classification system.


       
campaign
--------

:title: campaign
:type: string
:format: default





       
threats
-------

:title: threats
:type: number
:format: default



The degree of anticipated threats to the battle sites' integrity over the next 10 years. The Commission assigned the degree of threat based on short- and long-term threats identified by the field investigator on the battle site survey form.


       
ownership_federal
-----------------

:title: Ownership (Federal)
:type: boolean
:format: default



The kind(s) of known ownership of the battle site. The Commission relied on the ownership information provided on the survey forms and additional data collected by staff members. The field surveyors and the Commission staff did not consult official ownership records, such as County tax records or maps. Many of the battle sites probably have more kinds of ownership than indicated in the Commission's database.


       
ownership_local
---------------

:title: Ownership (local government)
:type: boolean
:format: default





       
ownership_private
-----------------

:title: Ownership (private)
:type: boolean
:format: default





       
ownership_state
---------------

:title: Ownership (state government)
:type: boolean
:format: default





       
ownership_unknown
-----------------

:title: Ownership (unknown)
:type: boolean
:format: default





       
park
----

:title: park
:type: boolean
:format: default



Park means any size or kind (historical, recreations, natural, etc.) of federal, state, local, or private park. A park presence does not mean that the battle is interpreted or even that the battle site is protected.


       
integrity
---------

:title: integrity
:type: string
:format: default


Integrity is the measure of the battle site's condition.
A battle site with fair integrity is largely intact with some changes in primary geographical and topographical configuration and mass and scale of the buildings.
A battle site with good integrity is essentially unchanged from the historic period with respect to terrain, land use, road network, and mass and scale of buildings.
A battle site with poor integrity is significantly altered in terms of its primary geographical and topographical configuration and mass and scale of the buildings. Road construction and changes in land use are usually evident at sites with poor integrity. Sites with poor integrity sometimes retain core parcels (50-200 acres) intact within the generally fragmented landscape.
A local site has changed beyond recognition, meaning that a local resident of the time returning to the site today presumably would not recognize his surroundings. Lost battlefields may retain small (1-50 acres) parcels suitable for commemoration, however, the ability to interpret the battle on the landscape has been lost.


       
military
--------

:title: military
:type: string
:format: default
:constraints:
    :enum: ['A', 'B', 'C', 'D']
    


The Military Importance or Military Class; Military Importance = Military Class. The Commission ranked each battle (and its associated battle site) within the framework of its campaign and the war.
Decisive: A general engagement involving field armies in which a commander achieved a vital strategic objective. Such a result might include an indisputable victory on the field or be limited to the success or termination of a campaign offensive. Decisive battles had a direct, observable impact on the direction, duration, conduct, or outcome of the war.
Formative: An engagement involving divisions or detachments of the field armies in which a commader accomplished a limited campaign objective of reconnaissance, disruption, defense, or occupation. Formative battles had an observable influence on the direction, duration, or conduct of the campaign.
Limited: An engagement, typically involving detachments of the field armies, in which a commander achived a limited tactical objective of reconnaissance, defense, or occupation. Limited battles maintained contact between the combatants without observable influence on the direction of the campaign.
Major: An engagement of magnitude involving field armies or divisions of the armies in which a commander achived an important strategic objective within the context of an ongoing campaign offensive. Major battles had a direct, observable impact on the direction, duration, conduct, or outcome of the campaign.


       
interpretive_political
----------------------

:title: Interpretive Potential: effect upon international diplomacy
:type: boolean
:format: default





       
interpretive_commander_loss
---------------------------

:title: Interpretive Potential: Loss of significant commander (Wounding, Death, Relieved of Command)
:type: boolean
:format: default





       
interpretive_casualties
-----------------------

:title: Interpretive Potential: Unusually High Casualties
:type: boolean
:format: default





       
interpretive_tactics_strategy
-----------------------------

:title: Interpretive Potential: Illustrates Important Lessons in Military Tactics and Strategy
:type: boolean
:format: default





       
interpretive_public_mind
------------------------

:title: Interpretive Potential: Unusual Importanve in the Public Mind and Imagination
:type: boolean
:format: default





       
interpretive_combat_arm
-----------------------

:title: Interpretive Potential: Significant Participation of Cavalry, Artillery, or Other Single Combat Arm
:type: boolean
:format: default





       
interpretive_military_firsts
----------------------------

:title: Interpretive Potential: Military Firsts
:type: boolean
:format: default





       
interpretive_minority_troops
----------------------------

:title: Interpretive Potential: Participation of Significant Numbers of Minority Troops
:type: boolean
:format: default





       
interpretive_economic
---------------------

:title: Interpretive Potential: Significant Economic Consequences
:type: boolean
:format: default





       
interpretive_archaelolgical
---------------------------

:title: Interpretive Potential: High Archaelogical Potential
:type: boolean
:format: default





       
interpretive_logistics
----------------------

:title: Interpretive Potential: Unusually Significant Logistics or Supply Feat
:type: boolean
:format: default





       
interpretive_individual_bravery
-------------------------------

:title: Interpretive Potential: Exception Individual Initiative in Bravery or Command
:type: boolean
:format: default





       
interpretive_group_behavior
---------------------------

:title: Interpretive Potential: Exceptional Group Behavior
:type: boolean
:format: default





       
interpretive_joint_ops
----------------------

:title: Interpretive Potential: Illustrates Joint Operations (Army, Navy)
:type: boolean
:format: default





       
interpretive_coop_armies
------------------------

:title: Interpretive Potential: Illustrates Cooperation of Separate Military Departments or Armies
:type: boolean
:format: default





       
interpretive_naval
------------------

:title: Interpretive Potential: Naval Operations
:type: boolean
:format: default





       
jim
---

:title: jim
:type: string
:format: default





       
ed
--

:title: Military (Ed)
:type: string
:format: default
:constraints:
    :enum: ['A', 'B', 'C', 'D']
    

Dr. Edwin C. Bearss. The letter in this field is Mr. Bearss 'initial opinion regarding the military importance of the event. (Refer to MILITARY above.) An entry was made in this field only when Mr. Bearss disagreed with the first military importance value assigned to the event. Differences of opinion about the military importance of specific battle events were resolved at an October 23, 1992 meeting.


       
bill
----

:title: Military (Bill)
:type: string
:format: default
:constraints:
    :enum: ['A', 'B', 'C', 'D']
    


Dr. William J. Cooper, Jr.. The letter in this field is Dr. Cooper's initial opinion regarding the military importance of the event. (Refer to MILITARY above.) An entry was made in this field only when Dr. Cooper disagreed with the first military importance value assigned to the event. Differences of opinion about the military importance of specific battle events were resolved at an October 23, 1992 meeting.


       
protected
---------

:title: Protected land area (acres)
:type: number
:format: default



The number of acres of the battle site that are protected; for example, by easement or park status. This field is ill-defined and incomplete. The data may be inaccurate. The Commission did not use the data in this field.


       
percent
-------

:title: Protected (percent of land area)
:type: number
:format: default


Percentage of the land area of the battlefield that is protected. This field is ill-defined and incomplete. The data may be inaccurate. The Commission did not use the data in this field.


       
county
------

:title: County
:type: string
:format: default



The county, or counties, in which the battle site is located. In Virginia, incorporated cities are not part of their surrounding jurisdiction. Note: The Commission used its Counties database (counties.dbf) for county information rather than this entry in the events database.


       
value
-----

:title: value
:type: string
:format: default



The assessed land value of the battle site. This field is incomplete and the data may be inaccurate. The Commission did not use the data in this field.


       
priority1
---------

:title: priority1
:type: boolean
:format: default


"1" = The battle site/event is one of the Commission's Priority One battlefields. "0" = The battle site/event is not one of the Commission's Priority One battlefields. This field was never completed.


       
url
---

:title: url
:type: string
:format: url


URL to the record on aad.archives.gov.


       

