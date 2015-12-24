####################################################################
Strengths and casualties for forces in the civilwar.org battle data.
####################################################################

:name: civilwarorg_forces
:path: civilwarorg_forces.csv
:format: csv

Casualties and strengths of forces in battles from the `Civil War Trust <http://www.civilwar.org/>`__.
See :doc:`civilwarorg_battles`.


Sources: 


Schema
======



================  =======  ====================
id                string   Battle id
belligerent       string   Belligerent
strength          integer  Strength
casualties        integer  Total casualties
killed            integer  Killed
wounded           integer  Wounded
missing_captured  integer  Missing and Captured
================  =======  ====================

id
--

:title: Battle id
:type: string
:format: default





       
belligerent
-----------

:title: Belligerent
:type: string
:format: default
:constraints:
    :enum: ['US', 'Confderate']
    




       
strength
--------

:title: Strength
:type: integer
:format: default
:constraints:
    

Troops engaged in the battle.


       
casualties
----------

:title: Total casualties
:type: integer
:format: default
:constraints:
    




       
killed
------

:title: Killed
:type: integer
:format: default
:constraints:
    




       
wounded
-------

:title: Wounded
:type: integer
:format: default
:constraints:
    




       
missing_captured
----------------

:title: Missing and Captured
:type: integer
:format: default
:constraints:
    




       

