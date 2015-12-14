################
Ships in battles
################

:name: ships_in_battles
:path: data/ships_in_battles.csv
:format: csv

Ships in each battle. The CWSAC battle list is used as the unit of observation.



Sources: [jrnold]_


Schema
======



===========  ======  ===========
cwsac_id     string  CWSAC Id.
belligerent  string  Belligerent
ship         string  Ship name
===========  ======  ===========

cwsac_id
--------

:title: CWSAC Id.
:type: string
:format: default


CWSAC identifier of the battle. See :doc:`cwsac_battles`.


       
belligerent
-----------

:title: Belligerent
:type: string
:format: default





       
ship
----

:title: Ship name
:type: string
:format: default


Name of ship
These names match those in :doc:`ships`.


       

