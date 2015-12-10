############################
Fox (1898) battle casualties
############################

:name: fox_forces
:path: data/fox_forces.csv
:format: csv

Battle casualty data from William F. Fox *Regimental Losses in the American Civil War,
1861-1865: A Treatise on the extent and nature of the mortuary losses in
the Union regiments, with full and exhaustive statistics compiled from
the official records on file in the state military bureaus and at
Washington*, available from `Perseus <http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A2001.05.0068>`__.

The data on casualties come from the main table in "Chapter 14: the greatest battles of the war — list of victories and defeats — chronological list of battles with loss in each, Union and Confederate", p. 544-551.
The accompanying description reads

    There were 112 battles in the war, in which one side or the other
    lost over 500 in killed and wounded. In all, there were 1,882
    general engagements, battles, skirmishes, or affairs in which at
    least one regiment was engaged.

    With this chapter is given a chronological list of the battles and
    minor engagements, showing the loss in each. The figures are
    compiled from the battle reports and revised casualty lists in
    the. “Official Records of the Union and Confederate Armies,”
    published, or in process of publication, by the War Department at
    Washington.

    The figures in the table of Confederate losses are the ones
    officially reported by the Confederate generals in command, or by
    their surgeon-general, to whom, in many instances, that duty seems
    to have been entrusted. There are no official Confederate casualty
    reports for the latter part of the war, and so there is no
    statement of loss for several battles. Estimates might be quoted,
    but such figures are not within the province of this work.

The data in that tables are split into a table with battles and one with
force level casualties.

The results of battles is considered seperately in :doc:`fox_outcomes`.


Sources: [fox1898regimental]_


Schema
======

:Primary Key: ['belligerent', 'battle_name']


===========  =======  =============
belligerent  string   belligerent
battle_name  string   Battle name
start_date   date     start_date
end_date     date     end_date
state        string   State
casualties   integer  casualties
killed       integer  Killed
wounded      integer  wounded
missing      integer  missing
aggrow       boolean  Aggregate row
===========  =======  =============

belligerent
-----------

:title: belligerent
:type: string
:format: default
:constraints:
    :enum: ['Confederate', 'US']
    




       
battle_name
-----------

:title: Battle name
:type: string
:format: default





       
start_date
----------

:title: start_date
:type: date
:format: default


Start date of the battle


       
end_date
--------

:title: end_date
:type: date
:format: default


End date of the battle


       
state
-----

:title: State
:type: string
:format: default
:constraints:
    :minLength: 2
    :maxLength: 2
    :pattern: [A-Z]{2}
    

State in which the battle took place


       
casualties
----------

:title: casualties
:type: integer
:format: default


Number of casualties (killed, wounded, and missing)


       
killed
------

:title: Killed
:type: integer
:format: default


Number killed


       
wounded
-------

:title: wounded
:type: integer
:format: default


Number wounded


       
missing
-------

:title: missing
:type: integer
:format: default


Number missing


       
aggrow
------

:title: Aggregate row
:type: boolean
:format: default


Does this row aggregate casualties from several battles?


       

