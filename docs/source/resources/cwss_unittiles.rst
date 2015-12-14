################
CWSS Unit Titles
################

:name: cwss_unittiles
:path: data/cwss_unittiles.csv
:format: csv



Sources: 


Schema
======



=====  ======  ==========
state  string  state
side   string  side
title  string  Unit Title
=====  ======  ==========

state
-----

:title: state
:type: string
:format: default
:constraints:
    :pattern: [A-Z]{2}
    

2-letter abbreviation of the state or unit type. This includes more than states, e.g. US for Union Colored troops, and UR for Union regular army.


       
side
----

:title: side
:type: string
:format: default





       
title
-----

:title: Unit Title
:type: string
:format: default


Unit type


       

