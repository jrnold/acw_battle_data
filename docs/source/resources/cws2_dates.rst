##############################################
CWSAC Report Updates battle data: battle dates
##############################################

:name: cws2_dates
:path: cws2_dates.csv
:format: csv



Sources: [CWSII]_, [CWSIIAL]_, [CWSIIAR]_, [CWSIICO]_, [CWSIIDC]_, [CWSIIFL]_, [CWSIIGA]_, [CWSIIKS]_, [CWSIIKY]_, [CWSIIMN]_, [CWSIILA]_, [CWSIIMD]_, [CWSIIMO]_, [CWSIINC]_, [CWSIIND]_, [CWSIIOH]_, [CWSIIOK]_, [CWSIIPA]_, [CWSIISC]_, [CWSIITN]_, [CWSIIVA]_, [CWSIIWV]_


Schema
======



==========  =======  ==========
battle      string   Battle
spell       integer  Spell
start_date  date     Start Date
end_date    date     End Date
==========  =======  ==========

battle
------

:title: Battle
:type: string
:format: default
:constraints:
    :minLength: 5
    :maxLength: 6
    :pattern: [A-Z]{2}[0-9]{3}[A-Z]?
    

CWSAC battle identifier


       
spell
-----

:title: Spell
:type: integer
:format: default
:constraints:
    :minimum: 1
    :maximum: 2
    

Spell number of the battle. Only one battle had non-contiguous dates, and two spells.


       
start_date
----------

:title: Start Date
:type: date
:format: default





       
end_date
--------

:title: End Date
:type: date
:format: default





       

