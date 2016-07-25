##########################################################################
Chronology of Some Important Civil War Dates from Eicher and Eicher (2001)
##########################################################################

:name: eicher_chronology
:path: eicher_chronology.csv
:format: csv

Events from the "Chronology of Some Important Civil War Dates" from
*Civil War High Commands* by John H. Eicher and David J. Eicher (2001), pp. 895--918.

The description of events including in this list is

> Most military expeditions, reconnaissances, and raids are listed under the
> place names of locations involved rather than by the commanders' names.
> Roman numerals are appended to non-successive events which are known by the
> same name, such as Bull Run I (1861) and Bull Run II (1862); alternate names
> and related actions are placed in parentheses. A survey of Civil War
> chronologies yields at least thirty types of military operations between the
> opposing forces ranging from battles and engagements to skirmishes and raids.
> These types of operations are neither precisely defined nor carefully
> differentiated, but yield a total of more than 11,000 military actions,
> probably closer to 8,000 when duplications are removed.
> An approximation by years gives the following distribution: 1861 (7%), 1862.
> (2.5%), 1863 (2.8%), 1864 (34%), and 1865 (6%).


Sources: [Eicher2001]_


Schema
======



==========  ======  ==========
date        date    Date
event       string  Event
superevent  string  superevent
subevent    string  subevent
==========  ======  ==========

date
----

:title: Date
:type: date
:format: default





       
event
-----

:title: Event
:type: string
:format: default


Description of the event.



       
superevent
----------

:title: superevent
:type: string
:format: default





       
subevent
--------

:title: subevent
:type: string
:format: default





       

