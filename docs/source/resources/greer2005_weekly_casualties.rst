##################################################################
Weekly casualty data from Greer "Counting Casualties Week-by-Week"
##################################################################

:name: greer2005_weekly_casualties
:path: data/greer2005_weekly_casualties.csv
:format: csv

Weekly casualties from Greer (2005) *Counting Casualties Week by Week*

Weekly casualty data for the American Civil War from Darroch Greer (2005) *Counting Civil War Casualties, Week-By-Week, For The Abraham Lincoln Presidential Library and Museum*, http://www.brcweb.com/alplm/BRC_Counting_Casualties.pdf.
Greer primarily relies upon the casualty figures from Kennedy *The Civil War Battlefield Guide*, with adjustments for non-battle casualties.



**Sources:**
- Greer2005; http://www.brcweb.com/alplm/BRC_Counting_Casualties.pdf


Schema
======



=================  =======  ======================
date               date     date
description        string   Description
confederate        number   Confederate casualties
union              integer  Union casualties
theater            string   theater
cwsac_id           string   Cwsac Id.
cwsac_battle_name  string   Cwsac Battle Name
=================  =======  ======================

date
----

:title: date
:type: date
:format: default


Casualties are given by week. This is the first day of that week period.


       
description
-----------

:title: Description
:type: string
:format: default


Description of the casualties. This can either be a battle or "attrition" (for non-battle casualties).


       
confederate
-----------

:title: Confederate casualties
:type: number
:format: default
:constraints:
    :minimum: 0
    




       
union
-----

:title: Union casualties
:type: integer
:format: default
:constraints:
    :minimum: 0
    




       
theater
-------

:title: theater
:type: string
:format: default
:constraints:
    :enum: ['Lower Seaboard', 'Trans-Mississippi', 'Eastern', 'Western']
    

Theater in which the combat casualties occurred.


       
cwsac_id
--------

:title: Cwsac Id.
:type: string
:format: default


CWSAC battle associated with the casualties.


       
cwsac_battle_name
-----------------

:title: Cwsac Battle Name
:type: string
:format: default


Name of the CWSAC battle associated with the casualties.


       

