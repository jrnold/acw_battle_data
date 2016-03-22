########################
CWSS battle data: forces
########################

:name: cwss_forces
:path: cwss_forces.csv
:format: csv

Force strength and casualty data from the CWSS database.

This was extracted from the CWSS database file ``battle.xml``.


Sources: [CWSS]_


Schema
======



===============  =======  ===============
BattlefieldCode  string   BattlefieldCode
belligerent      string   belligerent
TroopsEngaged    integer  Troops engaged
Casualties       integer  Casualties
===============  =======  ===============

BattlefieldCode
---------------

:title: BattlefieldCode
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
    




       
TroopsEngaged
-------------

:title: Troops engaged
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Number of troops engaged.
A value of "0" means missing.



       
Casualties
----------

:title: Casualties
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Number of troops engaged.
A value of "0" can mean *either* missing or that there were zero casualties.



       

