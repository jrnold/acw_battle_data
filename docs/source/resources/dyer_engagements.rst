###########################
Dyer (1908) list of battles
###########################

:name: dyer_engagements
:path: dyer_engagements.csv
:format: csv

Engagements and casualties in Frederick Dyer *Compendium of the War of the Rebellion* (1908)

This contains the engagements listed in Dyer's *Compendium*, "Part II: Chronological Arrangement of the Campaigns, Battles, Engagements, Actions, Combats, Sieges, Skirmishes, Etc., in the United States, Connected with the War of the Rebellion, 1861 to 1865."
Dyer's list is a tabular version of the engagements reported in the *Official Records of the War of the Rebellion*.
For each engagment it notes the location, type of engagement (action, skirmish, etc.), Union units engaged in the action, and Union casualties. It does not provide any information 

Dyer's description of the engagements was as follows (p. 581),

  Campagains, Battles, Engagements, Skirmishes, etc. showing Union troops engaged in each event.

  This list shows loss of only such campaigns, battles, skirmishes, etc., as were, in this particular, officially reported. The losses of many actions, skirmishes, erc. occuring in the various campaigns were included in the final statement of the campaign, making it impossible to give accurately the loss in each event. Many of the skirmishes and other events show no loss whatever, or report none. All important campaigns, battles, raids, etc., will be found on this list, however, showing losses as officially reported.
  
The data are extracted from the digitalized version of the battles in Tufts University's `Perseus Digital Library <http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A2001.05.0140>`__.
This corresponds to pages 662-991 of Dyer's *Compendium*, ignoring indexes.



Sources: [DyerBattles]_, [dyer1908_war_rebel]_


Schema
======



================  =======  =================
battle_id         integer  battle_id
event_type        string   Event type
state             string   State
year              integer  Year
battle_name       string   Battle Name
start_date        date     Start Date
end_date          date     End date
text              string   Text
casualties        integer  Casualties
killed            integer  Killed
wounded           integer  Wounded
killed_wounded    number   Killed or Wounded
missing_captured  number   Missing Captured
================  =======  =================

battle_id
---------

:title: battle_id
:type: integer
:format: default





       
event_type
----------

:title: Event type
:type: string
:format: default


Event type: action, skirmish, siege, etc


       
state
-----

:title: State
:type: string
:format: default


State in which the event occurred.


       
year
----

:title: Year
:type: integer
:format: default


Year of the event.


       
battle_name
-----------

:title: Battle Name
:type: string
:format: default





       
start_date
----------

:title: Start Date
:type: date
:format: default





       
end_date
--------

:title: End date
:type: date
:format: default





       
text
----

:title: Text
:type: string
:format: default


Original text of the engagement, including the Union forces involved.


       
casualties
----------

:title: Casualties
:type: integer
:format: default


Union casualties (killed, wounded, and missing or captured).


       
killed
------

:title: Killed
:type: integer
:format: default


Union killed


       
wounded
-------

:title: Wounded
:type: integer
:format: default


Union wounded


       
killed_wounded
--------------

:title: Killed or Wounded
:type: number
:format: default


Union killed or wounded


       
missing_captured
----------------

:title: Missing Captured
:type: number
:format: default


Union missing or captured


       

