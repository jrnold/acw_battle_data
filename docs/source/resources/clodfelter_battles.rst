######################################
Clodfelter (2008) battle data: battles
######################################

:name: clodfelter_battles
:path: data/clodfelter_battles.csv
:format: csv

Battle data for the battles of the American Civil War in

    Clodfelter, M. (2008) *Warfare And Armed Conflicts: A Statistical
Encyclopedia of Casualty and Other Figures, 1494-2007*

Criteria for battles is to include "all important and significant actions and the results of each conflict" (p. 1).
No casualty threshhold is used to select battles because that would have to vary across wars.

Clodfelter divides the American Civil War into three theaters

- Eastern
- Western
- Blockade War

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


**Sources:**
- Clodfelter2008


Schema
======

=============  =======  =============
battle         string   Battle
theater        string   Theater
theater_years  string   theater_years
start_date     date     Start date
end_date       date     End Date
result         string   Result
page           integer  Page
=============  =======  =============

battle
------

:title: Battle
:type: string
:format: default


Battle name


       
theater
-------

:title: Theater
:type: string
:format: default





       
theater_years
-------------

:title: theater_years
:type: string
:format: default





       
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

**Sources:**
- self
- CWSAC1993b

       
page
----

:title: Page
:type: integer
:format: default


Page number in Clodfelter (2008)


       

