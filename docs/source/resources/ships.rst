###############################
Union and Confederate ship list
###############################

:name: ships
:path: ships.csv
:format: csv

Names of ships and links to `dbpedia.org <http://dbpedia.org>`__ and the Dictionary of American Naval Fighting Ships (DANFS).

This contains all ships that appeared in battles in :doc:`ships_in_battles`, not all ships in the Union and Confederate navies.



Sources: [jrnold]_


Schema
======



===========  ======  ===============
ship_id      string  Ship identifier
name         string  Ship name
belligerent  string  Belligerent
url_dbpedia  string  dbpedia Link
url_danfs    string  DANFS URL
notes        string  notes
===========  ======  ===============

ship_id
-------

:title: Ship identifier
:type: string
:format: default





       
name
----

:title: Ship name
:type: string
:format: default


Name of ship, not including the prefix or year of launch.


       
belligerent
-----------

:title: Belligerent
:type: string
:format: default
:constraints:
    :enum: ['US', 'Confederate']
    




       
url_dbpedia
-----------

:title: dbpedia Link
:type: string
:format: url


URI of the dbpedia.org resource.


       
url_danfs
---------

:title: DANFS URL
:type: string
:format: url


URL of the ship in the Naval History and Heritage Ship Histories, either the Dictionary of American Naval Fighting Ships  (`DANFS <http://www.history.navy.mil/research/histories/ship-histories/danfs.html>`__) or `Confederate Ships <http://www.history.navy.mil/research/histories/ship-histories/confederate_ships.html>`__.


       
notes
-----

:title: notes
:type: string
:format: default





       

