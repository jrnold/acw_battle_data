phisterer_to_cwsac
================================================================================

:name: phisterer_to_cwsac
:path: data/phisterer_to_cwsac.csv
:format: csv

Concordance between battles in ``phisterer_battles`` and CWSAC battle identifiers.

Some notes on specific battles

- 2345: includes several battles and overlaps with 2354. 
- 2351, 2355, 2366, 2373 all refer to Trenches in front of Petersburg,
  but don't seem to point to any specific battles. Most of the battles
  in the Petersburg Campaign have their own entries. See
  http://en.wikipedia.org/wiki/Siege_of_Petersburg
- 2307: Refers to all of
  http://en.wikipedia.org/wiki/Streight%27s_Raid, but there is only
  one battle.
- 2362: This is NOT http://en.wikipedia.org/wiki/Stoneman%27s_Raid.  There appears to be no battle page for this, 
  although it is discussed in http://en.wikipedia.org/wiki/George_Stoneman.
- 2372: http://en.wikipedia.org/wiki/Atlanta_campaign.  Linked to all
  battles in
  http://en.wikipedia.org/wiki/Category:Battles_of_the_Atlanta_Campaign_of_the_American_Civil_War. This battle 
  overlaps with several others.
- 2376: Price's invasion of Missouri; includes a number of engagements http://en.wikipedia.org/wiki/Price%27s_Raid.  This battle is linked to all battles in http://en.wikipedia.org/wiki/Category:Battles_of_Price%27s_Missouri_Expedition_of_the_American_Civil_War
- 2280: http://en.wikipedia.org/wiki/Seven_Days_Battles. Matched to the Seven Day's Battles except Oak Grove, 
  which has its own entry (2279).
- 2395 would appear to refer to Battle_of_Fort_Stedman, but 2394 explicitly refers to Fort Stedman. So 
  I cannot match this entry to a specific battle.
- 2397: http://en.wikipedia.org/wiki/Wilson%27s_raid




Schema
-------





from
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:label: 
:type: integer
:format: default 



       

to
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:label: 
:type: string
:format: default 



       

relation
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:label: 
:type: string
:format: default 



       

