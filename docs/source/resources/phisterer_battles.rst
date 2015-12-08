#########################################
Phisterer (1883) battle data: battle list
#########################################

:name: phisterer_battles
:path: data/phisterer_battles.csv
:format: csv

Phister (1883) battle

Data from Data from Phisterer, Frederick (1883) *Statistical Records of the Armies
of the United States* (`Google
books <http://books.google.com/books?id=cVNHr_nnLlYC>`__).

Data on major battles along with Union and Confederate casualties from
the table "Loss in engagements, etc., where the total was five hundred
or more on the side of the Union troops--(149)." on p. 213-219. The
caption for the table reads:

    Although the losses here given are generally based on official
    medical returns, the figures must not be taken as perfectly
    reliable, for in many instances the returns were based on
    estimates, and the totals of losses were, by *later* and more
    reliable returns, sometimes considerably reduced. Confederate
    losses are generally based on estimates.

Some notes on specific battles

-  2345: includes several battles and overlaps with 2354.
-  2351, 2355, 2366, 2373 all refer to Trenches in front of Petersburg,
   but don't seem to point to any specific battles. Most of the battles
   in the Petersburg Campaign have their own entries. See
   http://en.wikipedia.org/wiki/Siege\_of\_Petersburg
-  2307: Refers to all of
   http://en.wikipedia.org/wiki/Streight%27s\_Raid, but there is only
   one battle.
-  2362: This is NOT http://en.wikipedia.org/wiki/Stoneman%27s\_Raid.
   There appears to be no battle page for this, although it is discussed
   in http://en.wikipedia.org/wiki/George\_Stoneman.
-  2372: http://en.wikipedia.org/wiki/Atlanta\_campaign. Linked to all
   battles in
   http://en.wikipedia.org/wiki/Category:Battles\_of\_the\_Atlanta\_Campaign\_of\_the\_American\_Civil\_War.
   This battle overlaps with several others.
-  2376: Price's invasion of Missouri; includes a number of engagements
   http://en.wikipedia.org/wiki/Price%27s\_Raid. This battle is linked
   to all battles in
   http://en.wikipedia.org/wiki/Category:Battles\_of\_Price%27s\_Missouri\_Expedition\_of\_the\_American\_Civil\_War
-  2280: http://en.wikipedia.org/wiki/Seven\_Days\_Battles. Matched to
   the Seven Day's Battles except Oak Grove, which has its own entry
   (2279).
-  2395 would appear to refer to Battle\_of\_Fort\_Stedman, but 2394
   explicitly refers to Fort Stedman. So I cannot match this entry to a
   specific battle.
-  2397: http://en.wikipedia.org/wiki/Wilson%27s\_raid


Sources: [Phisterer1883]_


Schema
======



===========  =======  ===========
battle       integer  battle
battle_name  string   Battle name
state        string   state
start_date   date     Start date
end_date     date     End date
surrender    boolean  surrender
campaign     boolean  Campaign
page         integer  Page
===========  =======  ===========

battle
------

:title: battle
:type: integer
:format: default
:constraints:
    :minimum: 2262
    :maximum: 2410
    

Identifier number of the battle.
These are the numbers used in Phisterer (1883). They start at 2262 because 1-2261 refer to the events in the chronological record (see :doc:`phisterer_engagements`).


       
battle_name
-----------

:title: Battle name
:type: string
:format: default





       
state
-----

:title: state
:type: string
:format: default
:constraints:
    :pattern: [A-Z][A-Z]
    

Two-letter state code for the state of the battle.


       
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





       
surrender
---------

:title: surrender
:type: boolean
:format: default


Was the engagement a surrender rather than a battle?
Examples include the surrenders of Johnston, 


       
campaign
--------

:title: Campaign
:type: boolean
:format: default


Was the engagement a campaign rather than a battle?
Phisterer includes entries for the surrenders of Johnston, Taylor, Sam Jones, Jeff Thompson, and Kirby Smith at the end of the war.


       
page
----

:title: Page
:type: integer
:format: default


Page number in Phisterer (1883).


       

