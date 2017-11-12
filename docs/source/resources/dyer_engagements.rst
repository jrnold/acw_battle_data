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

The data for events 1-9570 were extracted from the digitalized version of the battles in Tufts University's `Perseus Digital Library <http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A2001.05.0140>`__.
This corresponds to pages 662-991 of Dyer's *Compendium*, ignoring indexes.

Events 9570+ were entered by hand from the original copy of Dyer's Compendium since the Perseus digitalized version of Dyer's Compendium did not include entries for events in "The Territories" and "Miscellaneous" (p. 984--991).


Sources: [DyerBattles]_, [dyer1908_war_rebel]_


Schema
======



================  =======  =================
battle_id         integer  battle_id
state             string   State
start_date        date     Start Date
end_date          date     End date
nature_location   string   nature_location
troops_engaged    string   troops_engaged
event_type        string   Event type
casualties        integer  Casualties
killed_wounded    number   Killed or Wounded
killed            integer  Killed
wounded           integer  Wounded
missing_captured  number   Missing Captured
================  =======  =================

battle_id
---------

:title: battle_id
:type: integer
:format: default





       
state
-----

:title: State
:type: string
:format: default
:constraints:
    :pattern: [A-Z]{2}
    

State in which the event occurred. This uses the standard two letter abbreviations
with the following exceptions.

- "DT": Dakota Territory
- "OK": anachronistically used for the Indian Territory
- "FR": France
- "MX": Mexico



       
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





       
nature_location
---------------

:title: nature_location
:type: string
:format: default





       
troops_engaged
--------------

:title: troops_engaged
:type: string
:format: default





       
event_type
----------

:title: Event type
:type: string
:format: default


Event type: action, skirmish, siege, etc


       
casualties
----------

:title: Casualties
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Union casualties (killed, wounded, and missing or captured).


       
killed_wounded
--------------

:title: Killed or Wounded
:type: number
:format: default
:constraints:
    :minimum: 0
    

Union killed or wounded


       
killed
------

:title: Killed
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Union killed


       
wounded
-------

:title: Wounded
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Union wounded


       
missing_captured
----------------

:title: Missing Captured
:type: number
:format: default
:constraints:
    :minimum: 0
    

Union missing or captured


       

