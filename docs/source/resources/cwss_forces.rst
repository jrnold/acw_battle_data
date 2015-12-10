########################
CWSS battle data: forces
########################

:name: cwss_forces
:path: data/cwss_forces.csv
:format: csv



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
    




       
Casualties
----------

:title: Casualties
:type: integer
:format: default
:constraints:
    :minimum: 0
    




       

