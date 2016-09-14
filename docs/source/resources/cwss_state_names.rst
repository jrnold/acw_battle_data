#####################
CWSS unit state names
#####################

:name: cwss_state_names
:path: cwss_state_names.csv
:format: csv

Descriptions of the unit type associated with the state abbreviations of units in :doc:`cwss_battle_units` column `state`.

This is a modified version of the CWSS database table `State_Name`.


Sources: 


Schema
======



====  ======  ============
abbr  string  Abbreviation
name  string  Name
====  ======  ============

abbr
----

:title: Abbreviation
:type: string
:format: default
:constraints:
    :minLength: 2
    :maxLength: 2
    :pattern: [A-Z]{2}
    




       
name
----

:title: Name
:type: string
:format: default





       

