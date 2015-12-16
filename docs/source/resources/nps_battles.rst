######################################
NPS combined data battle data: battles
######################################

:name: nps_battles
:path: data/nps_battles.csv
:format: csv

Battle level data combining the National Park Services reports: Shenandoah, preliminary CWSAC reports in the AAD (1990-1993), CWSAC Report battle summaries (1997), Civil War Soldiers and Sailors (CWSS) database, and the CWSAC Report Updates (2009-2013).




Sources: 


Schema
======



===============================  =======  ===============================
cwsac_id                         string   cwsac_id
battle_name                      string   battle_name
battle_type_cwss                 string   battle_type_cwss
start_date                       string   start_date
end_date                         string   end_date
theater_code                     string   theater_code
campaign_code                    string   campaign_code
result                           string   result
cwss_url                         string   cwss_url
partof_cwss                      boolean  partof_cwss
operation                        integer  operation
forces_text                      string   forces_text
casualties_text                  string   casualties_text
results_text                     string   results_text
preservation                     string   preservation
significance                     string   significance
cwsac_url                        string   cwsac_url
battle_name_cwsac                string   battle_name_cwsac
casualties                       number   casualties
partof_cwsac                     boolean  partof_cwsac
cws2_url                         string   cws2_url
study_area                       number   study_area
core_area                        number   core_area
potnr_boundary                   number   potnr_boundary
battle_name_cws2                 string   battle_name_cws2
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
shenandoah_url                   string   shenandoah_url
partof_shenandoah                boolean  partof_shenandoah
lat                              number   Latitude
long                             number   Longitude
state                            string   state
===============================  =======  ===============================

cwsac_id
--------

:title: cwsac_id
:type: string
:format: default





       
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





       
start_date
----------

:title: start_date
:type: string
:format: default





       
end_date
--------

:title: end_date
:type: string
:format: default





       
theater_code
------------

:title: theater_code
:type: string
:format: default





       
campaign_code
-------------

:title: campaign_code
:type: string
:format: default





       
result
------

:title: result
:type: string
:format: default





       
cwss_url
--------

:title: cwss_url
:type: string
:format: default





       
partof_cwss
-----------

:title: partof_cwss
:type: boolean
:format: default





       
operation
---------

:title: operation
:type: integer
:format: default





       
forces_text
-----------

:title: forces_text
:type: string
:format: default





       
casualties_text
---------------

:title: casualties_text
:type: string
:format: default





       
results_text
------------

:title: results_text
:type: string
:format: default





       
preservation
------------

:title: preservation
:type: string
:format: default





       
significance
------------

:title: significance
:type: string
:format: default





       
cwsac_url
---------

:title: cwsac_url
:type: string
:format: default





       
battle_name_cwsac
-----------------

:title: battle_name_cwsac
:type: string
:format: default





       
casualties
----------

:title: casualties
:type: number
:format: default





       
partof_cwsac
------------

:title: partof_cwsac
:type: boolean
:format: default





       
cws2_url
--------

:title: cws2_url
:type: string
:format: default





       
study_area
----------

:title: study_area
:type: number
:format: default





       
core_area
---------

:title: core_area
:type: number
:format: default





       
potnr_boundary
--------------

:title: potnr_boundary
:type: number
:format: default





       
battle_name_cws2
----------------

:title: battle_name_cws2
:type: string
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





       
interpretive_commander_loss
---------------------------

:title: interpretive_commander_loss
:type: integer
:format: default





       
interpretive_casualties
-----------------------

:title: interpretive_casualties
:type: integer
:format: default





       
interpretive_tactics_strategy
-----------------------------

:title: interpretive_tactics_strategy
:type: integer
:format: default





       
interpretive_public_mind
------------------------

:title: interpretive_public_mind
:type: integer
:format: default





       
interpretive_combat_arm
-----------------------

:title: interpretive_combat_arm
:type: integer
:format: default





       
interpretive_military_firsts
----------------------------

:title: interpretive_military_firsts
:type: integer
:format: default





       
interpretive_minority_troops
----------------------------

:title: interpretive_minority_troops
:type: integer
:format: default





       
interpretive_economic
---------------------

:title: interpretive_economic
:type: integer
:format: default





       
interpretive_archaelolgical
---------------------------

:title: interpretive_archaelolgical
:type: integer
:format: default





       
interpretive_logistics
----------------------

:title: interpretive_logistics
:type: integer
:format: default





       
interpretive_individual_bravery
-------------------------------

:title: interpretive_individual_bravery
:type: integer
:format: default





       
interpretive_group_behavior
---------------------------

:title: interpretive_group_behavior
:type: integer
:format: default





       
interpretive_joint_ops
----------------------

:title: interpretive_joint_ops
:type: integer
:format: default





       
interpretive_coop_armies
------------------------

:title: interpretive_coop_armies
:type: integer
:format: default





       
interpretive_naval
------------------

:title: interpretive_naval
:type: integer
:format: default





       
significance_jim
----------------

:title: significance_jim
:type: string
:format: default





       
significance_ed
---------------

:title: significance_ed
:type: string
:format: default





       
significance_bill
-----------------

:title: significance_bill
:type: string
:format: default





       
aad_url
-------

:title: aad_url
:type: string
:format: default





       
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





       
shenandoah_url
--------------

:title: shenandoah_url
:type: string
:format: default





       
partof_shenandoah
-----------------

:title: partof_shenandoah
:type: boolean
:format: default





       
lat
---

:title: Latitude
:type: number
:format: default





       
long
----

:title: Longitude
:type: number
:format: default





       
state
-----

:title: state
:type: string
:format: default





       

