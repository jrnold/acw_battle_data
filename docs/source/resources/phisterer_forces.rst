##############################################
Phisterer (1883) battle data: force casualties
##############################################

:name: phisterer_forces
:path: phisterer_forces.csv
:format: csv

Phisterer (1883) data on casualties of forces.

See :doc:`phisterer_battles` for more on the Phisterer (1883) data.

In this data each observation is a force (belligerent, battle).


Sources: [Phisterer1883]_


Schema
======

:Primary Key: ['battle_id', 'belligerent']


===========  =======  ===========
battle_id    integer  battle_id
belligerent  string   belligerent
casualties   number   casualties
killed       number   killed
wounded      number   wounded
missing      number   missing
===========  =======  ===========

battle_id
---------

:title: battle_id
:type: integer
:format: default





       
belligerent
-----------

:title: belligerent
:type: string
:format: default
:constraints:
    :enum: ['US', 'Confederate']
    




       
casualties
----------

:title: casualties
:type: number
:format: default
:constraints:
    :minimum: 0
    




       
killed
------

:title: killed
:type: number
:format: default
:constraints:
    :minimum: 0
    




       
wounded
-------

:title: wounded
:type: number
:format: default
:constraints:
    :minimum: 0
    




       
missing
-------

:title: missing
:type: number
:format: default
:constraints:
    :minimum: 0
    




       

