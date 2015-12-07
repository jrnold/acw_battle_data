Clodfelter (2008) battle data: forces
================================================================================

:name: clodfelter_forces
:path: data/clodfelter_forces.csv
:format: csv




Schema
-------





battle
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Battle
:type: string
:format: default 



       

belligerent
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Belligerent
:type: string
:format: default 
:constraints:
    
    
    
    
    
    
    
    :enum: ['US', 'Confederate']      



       

strength
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Strength
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Total number of personnel in the battle
       

infantry
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Infantry personnel
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Total number of infantry in the battle
       

cavalry
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Cavalry personnel
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Total number of cavalry in the battle
       

crewmen
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Crewmen
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Total number of naval crew in the battle
       

corps
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: corps
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of corps in the battle
       

cavalry_corps
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Cavalry Corps
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of cavalry corps in the battle
       

divisions
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Divisions
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of divisions in the battle
       

cavalry_divisions
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Cavalry Divisions
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of cavalry divisions in the battle
       

brigades
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Brigades
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of brigades in the battle
       

companies
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Companies
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of companies in the battle
       

frigates
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: frigates
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         



       

gunboats
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Gunboats
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         



       

ironclads
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Ironclads
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         



       

sloops
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Sloops
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         



       

steamers
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Steamers
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         



       

warships_and_transports
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Warships and Transports
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         



       

warships
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Warships
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         



       

wooden_warships
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Wooden Warships
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         



       

guns
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Guns
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of artillery pieces
       

casualties
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Casualties
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Casualties (killed, wounded, and missing or captured)
       

captured
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Captured
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         



       

killed
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Killed
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         



       

wounded
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Wounded
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         



       

missing
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Missing
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         



       

killed_wounded
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Killed or Wounded
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         



       

killed_missing
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Killed or Missing
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         



       

missing_captured
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Missing or Captured
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         



       

wounded_missing
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Wounded or Missing
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         



       

guns_lost
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Guns Lost
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of guns (artillery pieces) captured by the opponent.
       

guns_captured
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: guns_captured
:type: number
:format: default 



       

small_arms_lost
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Small Arms Lost
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of small arms captured by the opponent.
       

small_arms_captured
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: small_arms_captured
:type: number
:format: default 



       

warships_sunk
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Warships Sunk
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of warships sunk by the opponent.
       

warships_damaged
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Warships Damaged
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of warships damaged by the opponent.
       

gunboats_sunk
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Gunboats Sunk
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of gunboats sunk by the opponent.
       

gunboats_captured
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Gunboats Captured
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of gunboats captured by the opponent.
       

ironclads_sunk
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Ironclads Sunk
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of ironclads sunk by the opponent.
       

ironclads_captured
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Ironclads Captured
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of ironclads captured by the opponent.
       

forts_captured
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Forts Captured
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of forts captured by the opponent.
       

note
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Note
:type: string
:format: default 



       

str_mean
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Strength (mean)
:type: number
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Mean of the estimated strength in personnel of the force. See code for how it is calculated.
       

str_var
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Strength (variance)
:type: number
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Variance of the estimated strength in personnel of the force. See code for how it is calculated.
       

