##########################################
Bodart (1908) battle data: generals killed
##########################################

:name: bodart1908_generals_killed
:path: bodart1908_generals_killed.csv
:format: csv

Bodart (1908) data on the generals killed in battles of the American Civil War

These data are from Bodart (1908), "Militär-Historisches Kreigs-Lexicon (1618-1905)".
See :doc:`bodart1908_battles` for more information on this source.

This table contains the generals killed in battle for each battle in Bodart.

Bodart also lists the generals killed in battle on p. 910-911.

Bodart's correpondence of ranks

- Gen. = general = kommandierender General
- Lieut.-Gen. = liutenant-general = Generalleutenant
- Maj.-Gen. = major-general = Generalmajor
- Brig.-Gen. = brigadier-general = Brigade-general


Sources: [Bodart1908]_


Schema
======



===========  ======  ===========
battle_id    string  Battle Id.
belligerent  string  belligerent
name         string  Name
last_name    string  Last name
first_name   string  First name
middle_name  string  Middle name
suffix       number  Suffix
rank         string  Rank
date         date    date
dbpedia      string  Dbpedia URI
===========  ======  ===========

battle_id
---------

:title: Battle Id.
:type: string
:format: default





       
belligerent
-----------

:title: belligerent
:type: string
:format: default





       
name
----

:title: Name
:type: string
:format: default





       
last_name
---------

:title: Last name
:type: string
:format: default





       
first_name
----------

:title: First name
:type: string
:format: default





       
middle_name
-----------

:title: Middle name
:type: string
:format: default





       
suffix
------

:title: Suffix
:type: number
:format: default





       
rank
----

:title: Rank
:type: string
:format: default


Rank of the general


       
date
----

:title: date
:type: date
:format: default


Date the general was killed (if given).


       
dbpedia
-------

:title: Dbpedia URI
:type: string
:format: url


URI of the dbpedia.org resource for the person.


       

