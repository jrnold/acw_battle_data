######################################
Clodfelter (2008) battle data: battles
######################################

:name: clodfelter_battles
:path: clodfelter_battles.csv
:format: csv

Battle data for the battles of the American Civil War in Clodfelter, M. (2008) *Warfare And Armed Conflicts: A Statistical
Encyclopedia of Casualty and Other Figures, 1494-2007*.

Clodfelter has no strict rule for the inclusion of battles; his criteria is to include "all important and significant actions and the results of each conflict" (p. 1).
No casualty threshhold is used to select battles because that would have to vary across wars to produce sensical results.

Clodfelter divides the American Civil War into three theaters

- Eastern
- Western
- Blockade War

and divides the battles into thirteen groups: East (1861, 1862, 1863, 1864, 1865), West (1861, 1862, 1863, 1864, 1865), and Blocade War (1861--1862, 1863, 1864--1865).

Note on battle casualty percent. 15 percent for the American Civil War (p. 5).

The following battles had a significant naval component.

-  Roanoke Island (Feb 7-8, 1862): large land component (13000, 3000)
-  Hampton Roads (Mar 8, 1862): ship vs. ship.
-  New Orleans (April 24, 1862): ship vs. fort.
-  Galveston (Jan 1, 1863) Both sides had some land forces.
-  Fort Hindman (Jan 11, 1863). Both sides had significant land forces.
-  Mobile Bay (Aug 5, 1864): Mostly ships.
-  Fort Fisher (Jan 13-15). Both sides had significant land forces.
   Bombardment + assault on fort.

Quirks of the battles in this data:

- Vicksburg: divided into the overall siege and two Assaults

    - Vicksburg (siege) on 1863-5-18 to 1863-7-4
    - Vicksburg (1st assault) on 1863-5-19
    - Vicksburg (2nd assault) on 1863-5-22

- Port Hudson is divided into the overall siege and two Assaults

    - Port Hudson (Siege) on 1863-5-26 to 1863-7-9
    - Port Hudson (1st assault) on 1863-5-27
    - Port Hudson (2nd assault) on 1863-6-14

- Chattanooga: includes a battle for the overall battle and four separate Battles

    - Chattanooga on 1863-11-23 to 1863-11-25
    - Chattanooga (Orchard Knob/Indian Hill) on 11-23
    - Chattanooga (Lookout Mountain) on 11-24
    - Chattanooga (Tunnel Hill) on 11-25
    - Chattanooga (Missionary Ridge) on 11-25
- Cold Harbor: includes a battle for the overall siege and one for the assault

    - Cold Harbor (assault) on 1864-6-3
    - Cold Harbor on 1864-5-31 to 1864-6-12

- The Battle of Hampton Roads on March 8-9, 1862 is split into battles for each day

    - Hampton Roads (first day) on 1862-03-08
    - Hampton Roads (second day) on 1862-03-09

- Seven Days Battles includes an entry for the entire Seven Days Battles (June 25-July 1),
  as well as one for each separate battle.

    - The Orchard (Seven Days)
    - Mechanicsville (Seven Days)
    - Gaines's Mill (Seven Days)
    - Savage's Station (Seven Days)
    - White Oak Swamp (Seven Days)
    - Malvern Hill (Seven Days)
    
- 2nd Bull Run (Manasas) [VA026] (1862-8-28 to 1862-8-30) and Chantilly [VA027] (1862-9-1) are divided into two battles:
    - Groveton (1862-8-28)
    - Second Bull Run/Chantilly (Second Manassas) (1862-8-29 to 1862-9-1)

- 3rd Petersburg on 1865-04-02 is split into two battles

    - Fort Gregg on 1865-04-02
    - Petersburg (2nd Assault) on 1865-04-02

- Mobile Bay only includes the assault on August 5, 1864 and not the entire siege.


Sources: [Clodfelter2008]_


Schema
======



=============  =======  =============
battle_id      string   battle_id
theater        string   Theater
theater_years  string   theater_years
start_date     date     Start date
end_date       date     End Date
result         string   Result
page           integer  Page
=============  =======  =============

battle_id
---------

:title: battle_id
:type: string
:format: default





       
theater
-------

:title: Theater
:type: string
:format: default
:constraints:
    :enum: ['East', 'West', 'Blockade War']
    




       
theater_years
-------------

:title: theater_years
:type: string
:format: default
:constraints:
    :enum: ['Eastern Theater: 1861', 'Western Theater: 1861', 'The Blockade War: 1861-2', 'East: 1862', 'West: 1862', 'East: 1863', 'West: 1863', 'The Blockade War: 1863', 'East: 1864', 'West: 1864', 'The Blockade War: 1864-5', 'East: 1865', 'West: 1865']
    




       
start_date
----------

:title: Start date
:type: date
:format: default





       
end_date
--------

:title: End Date
:type: date
:format: default





       
result
------

:title: Result
:type: string
:format: default
:constraints:
    :enum: ['Union', 'Confederate', 'Indecisive']
    

Result of the battle: Union victory, Confederate victory or tie.
Clodfelter does not classify battles by result. This variable was added. The classifications follow CWSAC (:doc:`cwsac_battles`) where available.

Sources: [Clodfelter2008]_

       
page
----

:title: Page
:type: integer
:format: default


Page number in Clodfelter (2008)


       

