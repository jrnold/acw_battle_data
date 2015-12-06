Bodart (1908) battle data: force strengths and casualties
================================================================================

:name: bodart1908_forces
:path: data/bodart1908_forces.csv
:format: csv

Bodart (1908) data on force sizes and casualties in battles of the American Civil War

These data are from Bodart (1908), "Militär-Historisches Kreigs-Lexicon (1618-1905)".
See :doc:`bodart1908_battles` for more information on this source.

This table contains force sizes and casualties for each combatant in
each battle.

I have found that the strength values in Bodart tend to be higher in
other sources. He seems to use the total size of the unit involved in
that theater or operations, without considering which parts of that
unit participated in a given battle.



Schema
-------





battle_id
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Battle id
:type: string
:format: default 



       

country
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: country
:type: string
:format: default 
:constraints:
    
    
    
    
    
    
    
    :enum: ['Conferacy', 'Union']      


Belligerent (Union or Confederate) of the force.
       

victor
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Victor
:type: boolean
:format: default 


Did the side win?
       

strength
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Strength
:type: integer
:format: default 


Total personnel
       

strength_engaged
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Strength Engaged
:type: integer
:format: default 


Personnel engaged in combat
       

infantry
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Infantry
:type: integer
:format: default 


Number of infantry
       

cavalry
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: cavalry
:type: integer
:format: default 


Number of cavalry
       

artillery
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Artillery
:type: integer
:format: default 


Number of artillery personnel
       

guns
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: guns
:type: integer
:format: default 


Number of guns (artillery pieces)
       

killed
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Killed
:type: integer
:format: default 



       

killed_percent
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Killed (percent)
:type: number
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    :maximum: 1 
         



       

killed_generals
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: killed_generals
:type: integer
:format: default 



       

killed_officers
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: killed_officers
:type: integer
:format: default 



       

killed_wounded
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: killed_wounded
:type: integer
:format: default 



       

killed_wounded_percent
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Killed Wounded (percent)
:type: number
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    :maximum: 1 
         



       

killed_wounded_generals
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Generals killed or wounded
:type: integer
:format: default 



       

killed_wounded_officers
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Officers killed or wounded
:type: integer
:format: default 



       

wounded
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: wounded
:type: integer
:format: default 



       

wounded_percent
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Wounded (percent)
:type: number
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    :maximum: 1 
         



       

wounded_generals
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Generals wounded
:type: integer
:format: default 



       

wounded_officers
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Officers wounded
:type: integer
:format: default 



       

captured
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: captured
:type: integer
:format: default 



       

captured_generals
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Generals captured
:type: integer
:format: default 



       

captured_officers
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Officers captured
:type: integer
:format: default 



       

missing
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: missing
:type: integer
:format: default 



       

missing_percent
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Missing (percent)
:type: number
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    :maximum: 1 
         



       

missing_generals
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Generals missing
:type: integer
:format: default 



       

missing_officers
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Officers missing
:type: integer
:format: default 



       

casualties
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Casualties
:type: integer
:format: default 


Total casualties (killed, wounded, and missing or captured)
       

casualties_percent
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Casualties (percent)
:type: number
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    :maximum: 1 
         



       

casualties_officers
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Casualties (officers)
:type: integer
:format: default 



       

casualties_generals
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Casualties (generals)
:type: integer
:format: default 



       

losses_guns
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Losses of guns
:type: integer
:format: default 



       

losses_caissons
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Losses of caissons
:type: integer
:format: default 



       

losses_cannon
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Losses of cannons
:type: integer
:format: default 



       

losses_flags
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Losses of flags
:type: integer
:format: default 



       

losses_munition_wagons
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Losses of munition wagons
:type: integer
:format: default 



       

losses_wagons
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Losses of wagons
:type: integer
:format: default 



       

other
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Comments
:type: string
:format: default 



       

