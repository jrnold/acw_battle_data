livermore_battles
================================================================================

:name: livermore_battles
:path: data/livermore_battles.csv
:format: csv

Livermore (1900) battle data

Data from

    Thomas Leonard Livermore (1900) "Number and Losses in the Civil War
    in America, 1861-1865",
    http://books.google.com/books?id=Qw8pAAAAYAAJ .

Livermore discusses his methodology on pp. 63-77. The sample of battles
he uses is all battles in which either side had losses (killed plus
wounded) greater than 1,000.

Livermore was concerned with determining the actual number of troops
engaged in battle, i.e. those that actually participated. The majority
of the book consists of the calculations leading to the values of forces
and casualties of each battle.

When discussing the categorization of battles into victories and
defeats, Livermore writes,

::

    For further comparison of losses under similar conditions, the 63
    battles of Table B may be classified as follows, although
    discrimination must be made between those which are styled defeats,
    because some are ranged under this head merely because the field was
    abandoned; when considered tactically, the retreating army was
    successful in the battle itself.

The table of the aggregate size of the Union and Confederate armies over
time. The data come from Table "Comparison of the Foregoing Numbers with
the Number on the Union Rolls at the Same Date", on p. 47.

While good documentation is available on the total number of troops
serving in the Union military, there is no comparable documentation on
the total number of troops serving in the Confederate military.
Livermore devotes p. 1-49 to developing the estimates of the size of
Confederate Forces which are reported in this table.



Schema
-------





seq_no
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: seq_no
:type: integer
:format: default 



       

battle_name
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: battle_name
:type: string
:format: default 



       

page
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: page
:type: integer
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



       

attacker
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: attacker
:type: string
:format: default 



       

result
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: result
:type: string
:format: default 



       

assault_fortified
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: assault_fortified
:type: string
:format: default 



       

assault_outcome
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: assault_outcome
:type: string
:format: default 



       

union_result
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: union_result
:type: string
:format: default 



       

confed_result
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: confed_result
:type: string
:format: default 



       

state
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: state
:type: string
:format: default 



       

theater
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: theater
:type: string
:format: default 



       

