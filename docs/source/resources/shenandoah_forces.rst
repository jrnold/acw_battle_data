#################################################################
NPS Shenandoah Report battle data: force strengths and casualties
#################################################################

:name: shenandoah_forces
:path: shenandoah_forces.csv
:format: csv



Sources: [NPS1992]_


Schema
======



================  =======  ===================
battle_number     integer  battle_number
cwsac_id          string   CWSAC Id.
belligerent       string   Belligerent
description       string   Description
strength_min      integer  Strength (min)
strength_max      integer  Strength (max)
casualties_text   string   casualties_text
casualties        integer  Casualties
killed            integer  Killed
wounded           integer  Wounded
missing_captured  integer  Missing or Captured
================  =======  ===================

battle_number
-------------

:title: battle_number
:type: integer
:format: default





       
cwsac_id
--------

:title: CWSAC Id.
:type: string
:format: default





       
belligerent
-----------

:title: Belligerent
:type: string
:format: default
:constraints:
    :enum: ['US', 'Confederate']
    




       
description
-----------

:title: Description
:type: string
:format: default





       
strength_min
------------

:title: Strength (min)
:type: integer
:format: default


Strength in personnel of the force (minimum value).
If no range is given, the maximum and minimum are set to the same value.


       
strength_max
------------

:title: Strength (max)
:type: integer
:format: default


Strength in personnel of the force (maximum value).
If no range is given, the maximum and minimum are set to the same value.


       
casualties_text
---------------

:title: casualties_text
:type: string
:format: default


Text describing the casualties of the battle.


       
casualties
----------

:title: Casualties
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Total casualties (killed, wounded, and missing or captured)


       
killed
------

:title: Killed
:type: integer
:format: default
:constraints:
    :minimum: 0
    




       
wounded
-------

:title: Wounded
:type: integer
:format: default
:constraints:
    :minimum: 0
    




       
missing_captured
----------------

:title: Missing or Captured
:type: integer
:format: default
:constraints:
    :minimum: 0
    




       

