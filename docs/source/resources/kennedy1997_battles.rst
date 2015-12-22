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

-  CWSAC VA075 is split into VA075A and VA075B in Kennedy.
-  Kennedy VA031 includes CWSAC battles VA030, VA031
-  Kennedy VA032 includes CWSAC battles VA033, VA033, VA035
-  Kennedy VA038 includes CWSAC battles VA036, VA037, VA038
-  VA020A (Glendale) and VA020B (White Oak Swamp) are combined into a
   single battle VA020. The revised CWSAC reports also combine VA020A
   and VA020B into VA020.
-  Kenndy VA112 "Battle of St. Mary's Chuch" is VA066 in CWSAC.

Corrections to the casualty data:

-  Kennedy inverted the casualties for US and CS forces for TX005.


Sources: [KennedyConservation1998]_


Schema
======



===============  =======  ================
battle           string   Battle
name             string   Battle name
state            string   state
county           string   county
start_date       date     Start Date
end_date         date     End Date
casualties_min   integer  Casualties (min)
casualties_max   integer  Casualties (max)
casualties_text  string   Casualties
missing          number   missing
===============  =======  ================

battle
------

:title: Battle
:type: string
:format: default
:constraints:
    :minLength: 5
    :maxLength: 6
    :pattern: [A-Z]{2}[0-9]{3}[A-Z]?
    

CWSAC battle identifier


       
name
----

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





       
missing
-------

:title: missing
:type: number
:format: default





       

