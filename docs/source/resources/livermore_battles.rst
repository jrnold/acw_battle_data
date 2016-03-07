#########################################
Livermore (1900) battle data: battle list
#########################################

:name: livermore_battles
:path: livermore_battles.csv
:format: csv

Battle data from Livermore (1900) *Number and Losses in the Civil War in America, 1861-1865*.

Livermore discusses his methodology on pp. 63-77. The sample of
battles he uses is all battles in which either side had losses, killed
wounded, greater than 1,000.

Livermore is concerned with determining the actual number of troops
engaged in battle, i.e. those that actually participated. The majority
of the book is devoted to the calculations of the values of the
strengths of the forces in each battle.

When discussing the categorization of battles into victories and
defeats, Livermore writes,

    For further comparison of losses under similar conditions, the 63
    battles of Table B may be classified as follows, although
    discrimination must be made between those which are styled defeats,
    because some are ranged under this head merely because the field was
    abandoned; when considered tactically, the retreating army was
    successful in the battle itself.



Sources: [Livermore1900]_, [ACAA1994]_


Schema
======



=================  =======  ==========================
par_id             integer  seq_no
battle_name        string   Battle name
page               integer  page
start_date         date     Start date
end_date           date     End date
attacker           string   attacker
result             string   result
assault_fortified  string   Assault on fortified lines
assault_outcome    string   Assault outcome
union_result       string   Union result
confed_result      string   Confederate result
state              string   State
theater            string   Theater
=================  =======  ==========================

par_id
------

:title: seq_no
:type: integer
:format: default
:constraints:
    :minimum: 1
    



Sources: [Livermore1900]_, [ACAA1994]_

       
battle_name
-----------

:title: Battle name
:type: string
:format: default





       
page
----

:title: page
:type: integer
:format: default


Page in Livermore (1900) in which the battle description appears.


       
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





       
attacker
--------

:title: attacker
:type: string
:format: default
:constraints:
    :enum: ['US', 'Confederate']
    

Was the Confederate or the US the attacker in the battle?
This did not appear directly in Livermore (1900), but is from the ``PAR`` database.

Sources: [Livermore1900]_, [ACAA1994]_

       
result
------

:title: result
:type: string
:format: default
:constraints:
    :enum: ['US', 'Confederate']
    

Confederate or Union victory.
This did not appear directly in Livermore (1900), but is from the ``PAR`` database.

Sources: [Livermore1900]_, [ACAA1994]_

       
assault_fortified
-----------------

:title: Assault on fortified lines
:type: string
:format: default
:constraints:
    :enum: ['US', 'Confederate']
    

"Confederate" if it was a Confederate assault on Union fortified lines; "US" if it was a Union assault on Confederate fortified lines; missing if it was not an assault on foritied lines.
This comes from the Table "Assaults on Fortified Lines" on p. 75.


       
assault_outcome
---------------

:title: Assault outcome
:type: string
:format: default
:constraints:
    :enum: ['Failure', 'Success', 'Partial Success']
    

Assault outcome; missing if the battle was not an assault.
This comes from the Table "Assaults on Fortified Lines" on p. 75.


       
union_result
------------

:title: Union result
:type: string
:format: default
:constraints:
    :enum: ['Defeat', 'Retired', 'Rout', 'Victory']
    

Union result for the battle.
Seperate Union and Confederate results are given because the results in the tables are not symmetric. In some cases, one side is missing. In some cases, even if side has a victory, the other side can have a loss or a rout.
This comes from the tables "Routs", "Victories", and "Battles Fought to Cover a Prearranged Movement, Pursuing which the Army Retired after Repelling Attack", on p. 76--77.


       
confed_result
-------------

:title: Confederate result
:type: string
:format: default
:constraints:
    :enum: ['Defeat', 'Retired', 'Rout', 'Victory']
    

Confederate result of the battle
This comes from the tables "Routs", "Victories", and "Battles Fought to Cover a Prearranged Movement, Pursuing which the Army Retired after Repelling Attack", on p. 76--77.


       
state
-----

:title: State
:type: string
:format: default
:constraints:
    :minLength: 2
    :maxLength: 2
    :pattern: [A-Z][A-Z]
    

Two-letter abbreviation of the state in which the battle was fought.


       
theater
-------

:title: Theater
:type: string
:format: default
:constraints:
    :enum: ['MW', 'ME', 'LS', 'TM']
    

CWSAC theater of the battle. See :doc:`cwss_theaters`.

Sources: [Livermore1900]_, [ACAA1994]_

       

