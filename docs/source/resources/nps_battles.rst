######################################
NPS combined data battle data: battles
######################################

:name: nps_battles
:path: nps_battles.csv
:format: csv

Battle level data combining the National Park Services reports: preliminary CWSAC reports in the AAD (1990-1993), CWSAC Report battle summaries (1997), Civil War Soldiers and Sailors (CWSS) database, and the CWSAC Report Updates (2009-2013).

This table combines data from those various sources in a consistent manner.


Sources: 


Schema
======



===============================  =======  ===============================
cwsac_id                         string   CWSAC Id.
battle_name                      string   battle_name
battle_type_cwss                 string   battle_type_cwss
start_date                       date     Start date
end_date                         date     End date
theater_code                     string   theater_code
campaign_code                    string   campaign_code
result                           string   result
cwss_url                         string   CWSS URL
partof_cwss                      boolean  Part of CWSS
operation                        boolean  operation
forces_text                      string   Forces text
casualties_text                  string   Casualties text
results_text                     string   Results text
preservation                     string   preservation
significance                     string   significance
cwsac_url                        string   cwsac_url
other_names                      string   other_names
partof_cwsac                     boolean  Part of CWSAC
cws2_url                         string   cws2_url
study_area                       number   Study Area
core_area                        number   Core Area
potnr_boundary                   number   potnr_boundary
partof_cws2                      boolean  partof_cws2
interpretive_political           integer  interpretive_political
interpretive_commander_loss      integer  interpretive_commander_loss
interpretive_casualties          integer  interpretive_casualties
interpretive_tactics_strategy    integer  interpretive_tactics_strategy
interpretive_public_mind         integer  interpretive_public_mind
interpretive_combat_arm          integer  interpretive_combat_arm
interpretive_military_firsts     integer  interpretive_military_firsts
interpretive_minority_troops     integer  interpretive_minority_troops
interpretive_economic            integer  interpretive_economic
interpretive_archaelolgical      integer  interpretive_archaelolgical
interpretive_logistics           integer  interpretive_logistics
interpretive_individual_bravery  integer  interpretive_individual_bravery
interpretive_group_behavior      integer  interpretive_group_behavior
interpretive_joint_ops           integer  interpretive_joint_ops
interpretive_coop_armies         integer  interpretive_coop_armies
interpretive_naval               integer  interpretive_naval
significance_jim                 string   significance_jim
significance_ed                  string   significance_ed
significance_bill                string   significance_bill
aad_url                          string   aad_url
battle_type_aad                  string   battle_type_aad
partof_aad                       boolean  partof_aad
lat                              number   Latitude
long                             number   Longitude
state                            string   State
str_total                        number   str_total
cas_kwm_total                    number   cas_kwm_total
===============================  =======  ===============================

cwsac_id
--------

:title: CWSAC Id.
:type: string
:format: default
:constraints:
    :minLength: 5
    :maxLength: 6
    :pattern: [A-Z]{2}[0-9]{3}[A-Z]?
    

CWSAC battle identifier


       
battle_name
-----------

:title: battle_name
:type: string
:format: default





       
battle_type_cwss
----------------

:title: battle_type_cwss
:type: string
:format: default
:constraints:
    :enum: ['Action', 'Assault', 'Attack', 'Battle', 'Bombardment', 'Bombardment and Capture', 'Capture', 'Capture and Destruction', 'Combat', 'Demonstration', 'Engagement', 'Engagement and Occupation', 'Explosion and Assault', 'No Data', 'Occupation', 'Operations', 'Raid', 'Recapture', 'Siege', 'Siege and Capture', 'Siege and Pursuit']
    

Battle type in the CWSS. Examples include "Battle", "Combat", "Siege", and "Raid".


       
start_date
----------

:title: Start date
:type: date
:format: default





       
end_date
--------

:title: End date
:type: date
:format: default





       
theater_code
------------

:title: theater_code
:type: string
:format: default
:constraints:
    :enum: ['LS', 'ME', 'MW', 'PC', 'TM']
    

CWSS theater code. See :doc:`nps_theaters` for descriptions of the theaters.


       
campaign_code
-------------

:title: campaign_code
:type: string
:format: default
:constraints:
    :pattern: (LS|ME|MW|PC|TM)[0-9]{3}-[0-9]{2}
    

CWSS campaign code. See :doc:`nps_campaigns` for descriptions of the campaigns.


       
result
------

:title: result
:type: string
:format: default
:constraints:
    :enum: ['Union', 'Confederate', 'Indecisive']
    

Result of the battle: Union victory, Confederate victory, or Indecisive.


       
cwss_url
--------

:title: CWSS URL
:type: string
:format: url


URL of the battle's page in the Civil War Soldiers and Sailors website.


       
partof_cwss
-----------

:title: Part of CWSS
:type: boolean
:format: default


Was this battle included in the CWSS.


       
operation
---------

:title: operation
:type: boolean
:format: default


Was this battle an operation (multiple battles)? In the data, Manasas Station Operations and Marietta Operations are classified as operations.


       
forces_text
-----------

:title: Forces text
:type: string
:format: default


Description of the forces engaged in the battle, from the CWSAC.


       
casualties_text
---------------

:title: Casualties text
:type: string
:format: default


Description of the casualties of the forces engaged in the battle, from the CWSAC.


       
results_text
------------

:title: Results text
:type: string
:format: default


Description of the result of the battle, from the CWSAC. This will sometimes include more information about the results, including whether it was a strategic or tactical victory, or if the battle's result differed from the result of the campaign.


       
preservation
------------

:title: preservation
:type: string
:format: default
:constraints:
    :pattern: (I{1,3}|IV)\.[1-4]
    

NPS preservation priority of the battlefield, based on the CWSAC report. See :doc:`cwsac_preservation` for more information.


       
significance
------------

:title: significance
:type: string
:format: default
:constraints:
    :enum: ['A', 'B', 'C', 'D']
    

The military significance of the battle, from A " having a decisive influence on a campaign and a direct impact on the course of the war" to D "having a limited influence on the outcome of their campaign or operation but achieving or affecting important local objectives". This determined by the National Part Service CWSAC Report with input from Edwin C. Bearss, William J. Cooper, and James McPherson.


       
cwsac_url
---------

:title: cwsac_url
:type: string
:format: url


URL of the battle summary on the `CWSAC Battle Summaries <http://www.nps.gov/abpp/battles/bystate.htm>` website.


       
other_names
-----------

:title: other_names
:type: string
:format: default





       
partof_cwsac
------------

:title: Part of CWSAC
:type: boolean
:format: default


Was this battle included in the 1993 CWSAC Report.


       
cws2_url
--------

:title: cws2_url
:type: string
:format: default


URL of the report including the battle in the `Draft State by State Updates to the Civil War Sites Advisory Commission Report <http://www.nps.gov/abpp/CWSII/CWSIIStateReports.htm>`.


       
study_area
----------

:title: Study Area
:type: number
:format: default


CWSAC II study area in acres. See :doc:`cws2_battles`.


       
core_area
---------

:title: Core Area
:type: number
:format: default


CWSAC II core area in acres. See :doc:`cws2_battles`.


       
potnr_boundary
--------------

:title: potnr_boundary
:type: number
:format: default





       
partof_cws2
-----------

:title: partof_cws2
:type: boolean
:format: default





       
interpretive_political
----------------------

:title: interpretive_political
:type: integer
:format: default


See :doc:`aad_battles`


       
interpretive_commander_loss
---------------------------

:title: interpretive_commander_loss
:type: integer
:format: default


See :doc:`aad_battles`


       
interpretive_casualties
-----------------------

:title: interpretive_casualties
:type: integer
:format: default


See :doc:`aad_battles`


       
interpretive_tactics_strategy
-----------------------------

:title: interpretive_tactics_strategy
:type: integer
:format: default


See :doc:`aad_battles`


       
interpretive_public_mind
------------------------

:title: interpretive_public_mind
:type: integer
:format: default


See :doc:`aad_battles`


       
interpretive_combat_arm
-----------------------

:title: interpretive_combat_arm
:type: integer
:format: default


See :doc:`aad_battles`


       
interpretive_military_firsts
----------------------------

:title: interpretive_military_firsts
:type: integer
:format: default


See :doc:`aad_battles`


       
interpretive_minority_troops
----------------------------

:title: interpretive_minority_troops
:type: integer
:format: default


See :doc:`aad_battles`


       
interpretive_economic
---------------------

:title: interpretive_economic
:type: integer
:format: default


See :doc:`aad_battles`


       
interpretive_archaelolgical
---------------------------

:title: interpretive_archaelolgical
:type: integer
:format: default


See :doc:`aad_battles`


       
interpretive_logistics
----------------------

:title: interpretive_logistics
:type: integer
:format: default


See :doc:`aad_battles`


       
interpretive_individual_bravery
-------------------------------

:title: interpretive_individual_bravery
:type: integer
:format: default


See :doc:`aad_battles`


       
interpretive_group_behavior
---------------------------

:title: interpretive_group_behavior
:type: integer
:format: default


See :doc:`aad_battles`


       
interpretive_joint_ops
----------------------

:title: interpretive_joint_ops
:type: integer
:format: default


See :doc:`aad_battles`


       
interpretive_coop_armies
------------------------

:title: interpretive_coop_armies
:type: integer
:format: default


See :doc:`aad_battles`


       
interpretive_naval
------------------

:title: interpretive_naval
:type: integer
:format: default


See :doc:`aad_battles`


       
significance_jim
----------------

:title: significance_jim
:type: string
:format: default


See :doc:`aad_battles`


       
significance_ed
---------------

:title: significance_ed
:type: string
:format: default


See :doc:`aad_battles`


       
significance_bill
-----------------

:title: significance_bill
:type: string
:format: default


See :doc:`aad_battles`


       
aad_url
-------

:title: aad_url
:type: string
:format: URL


URL of the initial battle's report for the CWSAC as archived by the AAD.


       
battle_type_aad
---------------

:title: battle_type_aad
:type: string
:format: default





       
partof_aad
----------

:title: partof_aad
:type: boolean
:format: default





       
lat
---

:title: Latitude
:type: number
:format: default


Latittude of the battle. This is roughly the midpoint of the core area of the battle as indicated in the CWSAC II report maps.


       
long
----

:title: Longitude
:type: number
:format: default


Latittude of the battle. This is roughly the midpoint of the core area of the battle as indicated in the CWSAC II report maps.


       
state
-----

:title: State
:type: string
:format: default
:constraints:
    :pattern: [A-Z]{2}
    




       
str_total
---------

:title: str_total
:type: number
:format: default
:constraints:
    :minimum: 0
    

Total (Confederate and Union) personnel engaged in the battle. This combines data from the CWSS, CWSAC, and CWSAC II sources. For some battle the total personnel is given, even though the individual Confederate and Union values are missing.


       
cas_kwm_total
-------------

:title: cas_kwm_total
:type: number
:format: default
:constraints:
    :minimum: 0
    

Total (Confederate and Union) casualties in the battle. This combines data from the CWSS and CWSAC sources. For some battle the total personnel is given, even though the individual Confederate and Union values are missing.


       

