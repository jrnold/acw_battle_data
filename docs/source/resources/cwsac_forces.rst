#######################################
CWSAC Report (1993) battle data: forces
#######################################

:name: cwsac_forces
:path: cwsac_forces.csv
:format: csv



Sources: [CWSAC1993]_, [CWSAC1997]_, [CWSAC_by_state]_, [CWSAC_by_campgn]_


Schema
======



===================  ======  ===================
battle               string  Battle
belligerent          string  belligerent
description          string  description
strength_min         number  strength_min
strength_max         number  strength_max
armies               number  armies
corps                number  corps
divisions            number  divisions
brigades             number  brigades
regiments            number  regiments
companies            number  companies
cavalry_regiments    number  cavalry_regiments
cavalry_brigades     number  cavalry_brigades
cavalry_corps        number  cavalry_corps
cavalry_divisions    number  cavalry_divisions
artillery_batteries  number  artillery_batteries
ships                number  ships
ironclads            number  ironclads
gunboats             number  gunboats
wooden_ships         number  wooden_ships
rams                 number  rams
casualties           number  casualties
killed               number  killed
wounded              number  wounded
missing              number  missing
captured             number  captured
strength_mean        number  strength_mean
strength_var         number  strength_var
===================  ======  ===================

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
    

Side of the force: Confederate or Union or Native American.


       
description
-----------

:title: description
:type: string
:format: default


Description of the force, often including the units involved.


       
strength_min
------------

:title: strength_min
:type: number
:format: default


Minimum forces engaged.


       
strength_max
------------

:title: strength_max
:type: number
:format: default


Maximum sources engaged.


       
armies
------

:title: armies
:type: number
:format: default





       
corps
-----

:title: corps
:type: number
:format: default





       
divisions
---------

:title: divisions
:type: number
:format: default





       
brigades
--------

:title: brigades
:type: number
:format: default





       
regiments
---------

:title: regiments
:type: number
:format: default





       
companies
---------

:title: companies
:type: number
:format: default





       
cavalry_regiments
-----------------

:title: cavalry_regiments
:type: number
:format: default





       
cavalry_brigades
----------------

:title: cavalry_brigades
:type: number
:format: default





       
cavalry_corps
-------------

:title: cavalry_corps
:type: number
:format: default





       
cavalry_divisions
-----------------

:title: cavalry_divisions
:type: number
:format: default





       
artillery_batteries
-------------------

:title: artillery_batteries
:type: number
:format: default





       
ships
-----

:title: ships
:type: number
:format: default





       
ironclads
---------

:title: ironclads
:type: number
:format: default





       
gunboats
--------

:title: gunboats
:type: number
:format: default





       
wooden_ships
------------

:title: wooden_ships
:type: number
:format: default





       
rams
----

:title: rams
:type: number
:format: default





       
casualties
----------

:title: casualties
:type: number
:format: default





       
killed
------

:title: killed
:type: number
:format: default





       
wounded
-------

:title: wounded
:type: number
:format: default





       
missing
-------

:title: missing
:type: number
:format: default





       
captured
--------

:title: captured
:type: number
:format: default





       
strength_mean
-------------

:title: strength_mean
:type: number
:format: default





       
strength_var
------------

:title: strength_var
:type: number
:format: default





       

