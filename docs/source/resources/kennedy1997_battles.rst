#########################################
Civil War Battlefield Guide data: battles
#########################################

:name: kennedy1997_battles
:path: kennedy1997_battles.csv
:format: csv

Kennedy (1997) battle data

Data from

    Frances H. Kennedy and the Conservation Fund (1998) "The Civil War
    Battlefield Guide", http://books.google.com/books?id=qHObJArDHZMC.

The battles in this source correspond to the CWSAC battles and have use
the same identifiers. However, in a few cases, casualty totals for
several battles are aggregated.

Although Kennedy largely follows the CWSAC battle definitions, there are
a few differences:

- In several battles, although the descriptions and battle-level data are separate, the
  casualties are combined.

  -  VA031 includes VA030, VA031
  -  VA032 includes VA033, VA033, VA035
  -  VA038 includes VA036, VA037, VA038

-  VA112 "Battle of St. Mary's Chuch" is VA066 in CWSAC.

Corrections:

-  The casualties for US and CS forces were inverted for TX005.


Sources: [KennedyConservation1998]_


Schema
======

:Primary Key: ['battle_id']


===============  =======  ================
battle_id        string   Battle
battle_name      string   Battle name
state            string   state
county           string   county
start_date       date     Start Date
end_date         date     End Date
casualties_min   integer  Casualties (min)
casualties_max   integer  Casualties (max)
casualties_text  string   Casualties
cwsac_id         string   CWSAC Id
===============  =======  ================

battle_id
---------

:title: Battle
:type: string
:format: default
:constraints:
    :minLength: 5
    :maxLength: 6
    :pattern: [A-Z]{2}[0-9]{3}[A-Z]?
    

Battle identifier


       
battle_name
-----------

:title: Battle name
:type: string
:format: default





       
state
-----

:title: state
:type: string
:format: default
:constraints:
    :minLength: 2
    :maxLength: 2
    :pattern: [A-Z][A-Z]
    




       
county
------

:title: county
:type: string
:format: default


Counties in which the battle took place.


       
start_date
----------

:title: Start Date
:type: date
:format: default





       
end_date
--------

:title: End Date
:type: date
:format: default





       
casualties_min
--------------

:title: Casualties (min)
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Total casualties (killed, wounded, and missing or captured) for both sides, minimum value. For a few battles a total casualty value is given, while no disaggregated casualties are provided.
This source only gives a range for a few battles. For battles where no range is given, the mimimum and maximum are set to the same value.


       
casualties_max
--------------

:title: Casualties (max)
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Total casualties (killed, wounded, and missing or captured) for both sides, maximum value.


       
casualties_text
---------------

:title: Casualties
:type: string
:format: default





       
cwsac_id
--------

:title: CWSAC Id
:type: string
:format: default
:constraints:
    :pattern: [A-Z]{2}[0-9]{3}[A-Z]?
    

CWSAC battle identifiers of the battles. These are almost the same as the Kennedy identifiers with a few exceptions. All battles are one-to-one mappings onto the CWSAC battles.


       

