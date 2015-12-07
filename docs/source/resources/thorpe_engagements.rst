#####################################################################################################
Locations of engagements from Washington Post map, "Battles and casualties of the American Civil War"
#####################################################################################################

:name: thorpe_engagements
:path: data/thorpe_engagements.csv
:format: csv

Data on the location of engagements in the American Civil War from the *Washington Post* interactive map "Battles and Casualties of the American Civil War" by Gene Thorpe:

  Thorpe, Gene (April 12, 2011) "Battles and Casualties of the Civil War Map", *Washington Post* <http://www.washingtonpost.com/wp-srv/lifestyle/special/civil-war-interactive/civil-war-battles-and-casualties-interactive-map/>

The data itself is from the file, http://www.washingtonpost.com/wp-srv/lifestyle/special/civil-war-interactive/civil-war-battles-and-casualties-interactive-map/cwFourYearsSec.xml.

The data consist of 4,340 engagements, the locations of those engagements, and casualties in these battles. It is unclear where the list of engagements comes from (Phisterer has only 2261, Dyer has 9570).


**Sources:**
- Thorpe2011


Schema
======



============  =======  ============================
battleNum     integer  Battle number
battleDetail  string   Battle details
beginDate     date     Begin date
endDate       date     End date
unknownDay    boolean  Unknown day
lat           number   Latitude
lng           number   Longitude
shrtNm        string   Short name
desc          string   Description
type          string   Type
killed        integer  Killed
usCasTot      integer  Total US casualties
csCasTot      integer  Total Confederate casualties
============  =======  ============================

battleNum
---------

:title: Battle number
:type: integer
:format: default


Battle identifier number


       
battleDetail
------------

:title: Battle details
:type: string
:format: default


Description of the battle


       
beginDate
---------

:title: Begin date
:type: date
:format: default





       
endDate
-------

:title: End date
:type: date
:format: default





       
unknownDay
----------

:title: Unknown day
:type: boolean
:format: default


Equal to 1 if the date of the battle was unknown. In which case, the first and last days of the month are used.


       
lat
---

:title: Latitude
:type: number
:format: default





       
lng
---

:title: Longitude
:type: number
:format: default





       
shrtNm
------

:title: Short name
:type: string
:format: default





       
desc
----

:title: Description
:type: string
:format: default





       
type
----

:title: Type
:type: string
:format: default


Type of engagement. E.g. skirmish, siege, engagement.


       
killed
------

:title: Killed
:type: integer
:format: default





       
usCasTot
--------

:title: Total US casualties
:type: integer
:format: default





       
csCasTot
--------

:title: Total Confederate casualties
:type: integer
:format: default





       

