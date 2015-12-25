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
id                string  Battle id
name              string  Battle name
url               string  url
dates             string  dates
alternate_names   string  Alternate Names
location          string  Locations
state             string  state
campaign          string  Campaign
result            string  Result
total_casualties  string  Total casualties
total_strength    string  Total strength
================  ======  ================

id
--

:title: Battle id
:type: string
:format: default


Battle identifier - the basename sans extentension of the URL.


       
name
----

:title: Battle name
:type: string
:format: default





       
url
---

:title: url
:type: string
:format: url


URL of the battle on civilwar.org.


       
dates
-----

:title: dates
:type: string
:format: default


Dates of the battle. This is currently an unparsed string.


       
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


       

