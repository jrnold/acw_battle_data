############################
Batte data from civilwar.org
############################

:name: civilwarorg_battles
:path: civilwarorg_battles.csv
:format: csv

Data on battles from the `Civil War Trust <http://www.civilwar.org/>`__.
These are a subset of the National Park Service CWSAC battles, but can have slightly different, and sometimes more detailed, values for forces and casualties.


Sources: 


Schema
======



================  ======  ================
battle_id         string  Battle
battle_name       string  battle_name
url               string  url
start_date        date    Start date
end_date          date    End date
alternate_names   string  Alternate Names
location          string  Locations
state             string  state
campaign          string  Campaign
result            string  Result
total_casualties  string  Total casualties
total_strength    string  Total strength
cwsac_id          string  CWSAC Id.
dbpedia_url       string  dbpedia.org link
================  ======  ================

battle_id
---------

:title: Battle
:type: string
:format: default





       
battle_name
-----------

:title: battle_name
:type: string
:format: default





       
url
---

:title: url
:type: string
:format: url


URL of the battle on civilwar.org.


       
start_date
----------

:title: Start date
:type: date
:format: default





       
end_date
--------

:title: End date
:type: date
:format: default





       
alternate_names
---------------

:title: Alternate Names
:type: string
:format: default





       
location
--------

:title: Locations
:type: string
:format: default





       
state
-----

:title: state
:type: string
:format: default





       
campaign
--------

:title: Campaign
:type: string
:format: default


Compaign of the battle.


       
result
------

:title: Result
:type: string
:format: default


Battle result: Union victory, Confederate victory, or Inconclusive


       
total_casualties
----------------

:title: Total casualties
:type: string
:format: default


Total of Confederate and Union casualties


       
total_strength
--------------

:title: Total strength
:type: string
:format: default


Total of Confederate and Union strength (forces engaged).


       
cwsac_id
--------

:title: CWSAC Id.
:type: string
:format: default
:constraints:
    

CWSAC battle identifier. See :doc:`cwsac_battles`.

Sources: 

       
dbpedia_url
-----------

:title: dbpedia.org link
:type: string
:format: url


Link to dbpedia.org resource.

Sources: 

       

