########################################
Civil War Battlefield Guide data: forces
########################################

:name: kennedy1997_forces
:path: data/kennedy1997_forces.csv
:format: csv

Kennedy (1997) casualty data

Force level data on casualties from Frances H. Kennedy (1997) *The Civil War Battlefield Guide* .
See :doc:`kennedy1997_battles` for more information.


**Sources:**
- KennedyConservation1998


Schema
======

==================  =======  =======================
battle              string   Battle
belligerent         string   belligerent
casualties_min      integer  Casualties (min)
casualties_max      integer  Casualties (max)
killed_wounded_min  integer  Killed or Wounded (min)
killed_wounded_max  integer  Killed or Wounded (max)
missing             integer  Missing or captured
==================  =======  =======================

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


       
belligerent
-----------

:title: belligerent
:type: string
:format: default
:constraints:
    :enum: ['US', 'Confederate', 'Native American']
    




       
casualties_min
--------------

:title: Casualties (min)
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Casualties (killed, wounded, and missing or captured), minimum value.
This source only gives a range for a few battles. For battles where no range is given, the mimimum and maximum are set to the same value.


       
casualties_max
--------------

:title: Casualties (max)
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Casualties (killed, wounded, and missing or captured), maximum value.      


       
killed_wounded_min
------------------

:title: Killed or Wounded (min)
:type: integer
:format: default
:constraints:
    :minimum: 0
    

This source only gives a range for a few battles. For battles where no range is given, the mimimum and maximum are set to the same value.


       
killed_wounded_max
------------------

:title: Killed or Wounded (max)
:type: integer
:format: default
:constraints:
    :minimum: 0
    




       
missing
-------

:title: Missing or captured
:type: integer
:format: default
:constraints:
    :minimum: 0
    




       

