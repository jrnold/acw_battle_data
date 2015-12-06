bodart1908_battles
================================================================================

:name: bodart1908_battles
:path: data/bodart1908_battles.csv
:format: csv

Bodart (1908) data on battles of the American Civil War

These data are from Bodart (1908), "Militär-Historisches
Kreigs-Lexicon (1618-1905)" for the 50 battles that are part of the
American Civil War (Nordamerikanischer Bürgerkrieg), pp. 522-542.

The scope of his work

  "The most important Engagements, meetings, battles, sieges,
  assaults, capitulations all wars, with the exception of the colonial
  wars in periods of 1618-1905."

His basis for including battles is that they were either of

  - great consequences, e.g. termination of a campaign, lifting a siege, taking a capital city or surrender
  - great number of losses

    - if land battle: losses of greater than 2,000 men on both sides
    - if sea battle: to express their importance and because sea
      battles had fewer men, some with losses of less than 1000 were
      included

He determined the victor of the battle as follows

1. the side that claimed the battlefield or achieved purpose of fighting
2. if not 1. the side which had a lower percentage of casualties 
   
Force strength. Includes all forces that could be disposable for the
battle, even if they did not participate. His reasoning is that even
if not used, they influence the calculations of the enemy.

Google Books translation of pages 45-47 reads

    On admission, the statistically treated battles meeting, sieges, etc.,
    the author has been guided by the principle that only those battles
    were included, who have played in the history of individual states a
    greater role.  

    There were so taken up such fights, which attracted
    great consequences for themselves (such as termination of the
    campaign, lifting a siege, taking a capital city, surrender, and so
    forth), or without regard to such consequences such battles, which,
    either by the Assembly of a large number of combatants on the
    battlefield or as result of their great losses appeared worthy of
    inclusion.  

    As a basis for the great loss by the host position to be
    taken to the author, the total loss figure of 2,000 men served
    together on both sides.

    An exception was held regarding the naval battles and Seetreffen, even
    those which were taken up by what were only 1,000 men or less of total
    loss and for the reason, because the author wanted the neglected,
    fighting to give the lake one of its important place.  

    In the naval
    battles of modern wars has been the tonnage of the ships, the number
    of indicated horse-power of the machines, the size, type and number of
    guns, and the Bemannungsstand account. With the loss of information in
    addition to human losses appear the ship's gun and loss account.  

    The
    place of the victor in the comparisons is always on the left side, the
    search for the right of the vanquished.  In so-called indecisive
    battles that party was considered a winner, which claimed the
    battlefield or the purpose sought by the fighting reached, even if
    their material loss was greater. If the above factors were not
    available, the party was given the victory, which scored a minority of
    the same success as her opponent with a larger Struiterzahl.  Since
    the loss data provide absolute figures for the size of the sustained
    loss of any scale for the comparative assessment was performed in all
    loss of Perzentsatz determined the same by the G esam t-Strei terzah
    1, which allows an immediate comparison of the enemy's losses to their
    relative amount is.  

    Where it was feasible, the loss of trophies and
    war material were attached.  

    When the strength data were always armed
    forces led those who were the battle for disposable and emergency
    could be used, therefore, still in and not just those who were really
    in the fight. Author went here from consideration of that that even
    that of a number of troops at a the field of battle not too distant
    places the opponent in his dispositions affect and presence on the
    course of events influence affect could, therefore those troops if
    they are also on the fight and the decision took no share, were
    included.

Translations of the German terms used in Bodart

- Streitkräfte = "armed forces"
  - "hievon im Kampfe" = "thereof in conflict"
  - "infanterie" = infantry
  - "kavallerie" = cavalry
  - "artillerie" = artillery
  - "Gesamt - Stärke" = "Total - Strength"
  - "geschütze", "gesch." = guns 
- "verluste" = casualties
  - "tot" = dead
  - "verwundet", "verw." = "wounded"
  - "blutige einbusse" = "bloody losses"  (seems to mean dead + wounded)
  - "vermixßt, gefangen" = "missing, captured"
  - "gefangen", "gefg." = "captured"
  - "gesamt - verslust" = "Total - casualties"
  - "tot und verwundet", "tot u. verw." = "dead and wounded"
  - "offz." = "Officers"
  - "Gen." = "Generals"
- "Gefallene Generale" = "fallen generals"
- "Verl. an Trophäen" = "??? at trophies"
   - "Kan.", "Kanonen" = "canon"
   - "Fahnen" = "flag"
   - "Wagen" = "wagon"
   - "Geschutze", "Gesch." = "artillery"
   - "Munitionswagen" = "gun wagons"?
   - "Gewehre" = "guns"
- "kanonen", "kan." = cannon
- "fahnen" = flags
- "geschütze", "gesch." = guns 

While most entries are presented in an almost tabular form, some
entries only have a paragraph of text.  An example of this is from
p. 528, Schlacht bei Perryville,

 Sieg der Konföderierten (68.000 M.) unter Gen. Bragg über die Unierten
 (54.000 M.) unter GM. Buell. 

The Google Books translation of this passage is 

 Victory for the Confederates (68,000 meters) under General. Bragg on the Uniate
 (54,000 meters) in GM. Buell."

The relevant data that I extract from this text is,

- Confederates are the victor
- Confederate force
  - gesamt-starke = 68000
  - commander = "Gen. Bragg"
- Union force
  - gesamt-starke = 54000
  - commander "GM. Buell"

The format of date variables in the battle descriptions is as follows:

- "1862 31./12. bis 1863 3./1." = date range 1862-12-31 to 1863-01-03
- "1862 11.-15./12." = date range 1862-12-11 to 1862-12-15
- "1862 7./12." = 1862-07-12 (July 12, 1862)

The type of battle is identified as

- Belagerung : siege
- Einnahme : taking
- Treffen : meeting, encounter
- Schlacht : battle
- Kapitulation : surrender
- Erstürmung : storming
- Einschliessung : confinement
- Gefecht :  battle
- Überfall : raid
- Vergebliche belagerung : unsuccessful siege
- Seeschlacht : naval battle 

These battle types are placed into 4 categories (see pp 602-607) with subcategories.

- "Land-schlachten, -Treffen, -Gefechte"
- "See-Schlachten, -Treffen, -Gefechte"
- "Angriff, Erstürmung, Belagerung, Kapitulation befestigter Plätse" ("Attack, assault, siege, capitulation fortified places")
- "Kapitulation auf freiem Felde ("capitulation in the open field")

There is also a category entitled "Summe der"

- Kämpfe zu Lande ("battles on land")
- Kämpfe zur See ("battles at sea")
- Belagerungen ("siege")
- Kapitulation ("surrender")

Final total category "Gesamtsumme der Kämpfe" ("total fights")

- "die bedeutendsten niederlagen der Foo gegen die Bar" : "the most significant defeats of Foo against Bar"
- "die größten Siege der Foo gegen die Bar" : "the biggest victories of Foo against Bar"

Corrections

- Bodart listed the date of the Battle of Ringgold as 1863-11-13 to 1863-11-25; I changed this to 
  1863-11-23 to 1863-11-25, the correct dates for this battle.

Several "battles" in Bodart are more like campaigns.

- Petersburg_18640609 spans June 9, 1864 (First Battle of Petersburg) to April 3, 1865 (capture of Petersburg 
  after the Third Battle of Petersburg). This includes parts of the Richmond-Petersburg Campaign and
  Appomattox Campaign.  While it matches the http://en.wikipedia.org/wiki/Siege_of_Petersburg, the Siege 
  of Petersburg is not an individual battle. Thus I match it to all battles in those campaigns.




Schema
-------





battle_id
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: battle_id
:type: string
:format: default 



       

name
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: name
:type: string
:format: default 



       

other_name
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: other_name
:type: string
:format: default 



       

start_date
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: start_date
:type: string
:format: default 



       

end_date
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: end_date
:type: string
:format: default 



       

location
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: location
:type: string
:format: default 



       

order
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: order
:type: number
:format: default 



       

siege
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: siege
:type: integer
:format: default 



       

battle
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: battle
:type: integer
:format: default 



       

meeting
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: meeting
:type: integer
:format: default 



       

surrender
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: surrender
:type: integer
:format: default 



       

siege.1
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: siege.1
:type: integer
:format: default 



       

capture
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: capture
:type: integer
:format: default 



       

page
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: page
:type: integer
:format: default 



       

