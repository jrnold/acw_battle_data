#########################################################
Bodart (1908) battle data: force strengths and casualties
#########################################################

:name: bodart1908_forces
:path: data/bodart1908_forces.csv
:format: csv

Bodart (1908) data on force sizes and casualties in battles of the American Civil War

These data are from Bodart (1908), "Militär-Historisches Kreigs-Lexicon (1618-1905)".
See :doc:`bodart1908_battles` for more information on this source.

This table contains force sizes and casualties for each combatant in
each battle.

I have found that the strength values in Bodart tend to be higher in
other sources. He seems to use the total size of the unit involved in
that theater or operations, without considering which parts of that
unit participated in a given battle.


**Sources:**
- Bodart1908


Schema
======

=======================  =======  ==========================
battle_id                string   Battle id
belligerent              string   belligerent
strength                 integer  Strength
strength_engaged         integer  Strength Engaged
infantry                 integer  Infantry
cavalry                  integer  cavalry
artillery                integer  Artillery
guns                     integer  guns
killed                   integer  Killed
killed_percent           number   Killed (percent)
killed_generals          integer  killed_generals
killed_officers          integer  killed_officers
killed_wounded           integer  killed_wounded
killed_wounded_percent   number   Killed Wounded (percent)
killed_wounded_generals  integer  Generals killed or wounded
killed_wounded_officers  integer  Officers killed or wounded
wounded                  integer  wounded
wounded_percent          number   Wounded (percent)
wounded_generals         integer  Generals wounded
wounded_officers         integer  Officers wounded
captured                 integer  captured
captured_generals        integer  Generals captured
captured_officers        integer  Officers captured
missing                  integer  missing
missing_percent          number   Missing (percent)
missing_generals         integer  Generals missing
missing_officers         integer  Officers missing
casualties               integer  Casualties
casualties_percent       number   Casualties (percent)
casualties_officers      integer  Casualties (officers)
casualties_generals      integer  Casualties (generals)
losses_guns              integer  Losses of guns
losses_caissons          integer  Losses of caissons
losses_cannon            integer  Losses of cannons
losses_canons            number   losses_canons
losses_flags             integer  Losses of flags
losses_munition_wagons   integer  Losses of munition wagons
losses_wagons            integer  Losses of wagons
note                     string   note
=======================  =======  ==========================

battle_id
---------

:title: Battle id
:type: string
:format: default





       
belligerent
-----------

:title: belligerent
:type: string
:format: default





       
strength
--------

:title: Strength
:type: integer
:format: default


Total personnel


       
strength_engaged
----------------

:title: Strength Engaged
:type: integer
:format: default


Personnel engaged in combat


       
infantry
--------

:title: Infantry
:type: integer
:format: default


Number of infantry


       
cavalry
-------

:title: cavalry
:type: integer
:format: default


Number of cavalry


       
artillery
---------

:title: Artillery
:type: integer
:format: default


Number of artillery personnel


       
guns
----

:title: guns
:type: integer
:format: default


Number of guns (artillery pieces)


       
killed
------

:title: Killed
:type: integer
:format: default





       
killed_percent
--------------

:title: Killed (percent)
:type: number
:format: default
:constraints:
    :minimum: 0
    :maximum: 1
    




       
killed_generals
---------------

:title: killed_generals
:type: integer
:format: default





       
killed_officers
---------------

:title: killed_officers
:type: integer
:format: default





       
killed_wounded
--------------

:title: killed_wounded
:type: integer
:format: default





       
killed_wounded_percent
----------------------

:title: Killed Wounded (percent)
:type: number
:format: default
:constraints:
    :minimum: 0
    :maximum: 1
    




       
killed_wounded_generals
-----------------------

:title: Generals killed or wounded
:type: integer
:format: default





       
killed_wounded_officers
-----------------------

:title: Officers killed or wounded
:type: integer
:format: default





       
wounded
-------

:title: wounded
:type: integer
:format: default





       
wounded_percent
---------------

:title: Wounded (percent)
:type: number
:format: default
:constraints:
    :minimum: 0
    :maximum: 1
    




       
wounded_generals
----------------

:title: Generals wounded
:type: integer
:format: default





       
wounded_officers
----------------

:title: Officers wounded
:type: integer
:format: default





       
captured
--------

:title: captured
:type: integer
:format: default





       
captured_generals
-----------------

:title: Generals captured
:type: integer
:format: default





       
captured_officers
-----------------

:title: Officers captured
:type: integer
:format: default





       
missing
-------

:title: missing
:type: integer
:format: default





       
missing_percent
---------------

:title: Missing (percent)
:type: number
:format: default
:constraints:
    :minimum: 0
    :maximum: 1
    




       
missing_generals
----------------

:title: Generals missing
:type: integer
:format: default





       
missing_officers
----------------

:title: Officers missing
:type: integer
:format: default





       
casualties
----------

:title: Casualties
:type: integer
:format: default


Total casualties (killed, wounded, and missing or captured)


       
casualties_percent
------------------

:title: Casualties (percent)
:type: number
:format: default
:constraints:
    :minimum: 0
    :maximum: 1
    




       
casualties_officers
-------------------

:title: Casualties (officers)
:type: integer
:format: default





       
casualties_generals
-------------------

:title: Casualties (generals)
:type: integer
:format: default





       
losses_guns
-----------

:title: Losses of guns
:type: integer
:format: default





       
losses_caissons
---------------

:title: Losses of caissons
:type: integer
:format: default





       
losses_cannon
-------------

:title: Losses of cannons
:type: integer
:format: default





       
losses_canons
-------------

:title: losses_canons
:type: number
:format: default





       
losses_flags
------------

:title: Losses of flags
:type: integer
:format: default





       
losses_munition_wagons
----------------------

:title: Losses of munition wagons
:type: integer
:format: default





       
losses_wagons
-------------

:title: Losses of wagons
:type: integer
:format: default





       
note
----

:title: note
:type: string
:format: default





       

