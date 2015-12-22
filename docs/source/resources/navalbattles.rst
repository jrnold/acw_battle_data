#####################
List of naval battles
#####################

:name: navalbattles
:path: navalbattles.csv
:format: csv

List of naval battles, which navies they involved, and whether they involved land fortifications. These are any battles with a naval component in :doc:`ships_in_battles`.


Sources: [jrnold]_


Schema
======



==========================  =======  ==========================
cwsac_id                    string   CWSAC Id.
confederate_ships           integer  confederate_ships
us_ships                    integer  Union ships
confederate_fortifications  boolean  confederate_fortifications
us_fortifications           boolean  us_fortifications
==========================  =======  ==========================

cwsac_id
--------

:title: CWSAC Id.
:type: string
:format: default
:constraints:
    :pattern: [A-Z]{2}[0-9]{3}[A-Z]?
    




       
confederate_ships
-----------------

:title: confederate_ships
:type: integer
:format: default





       
us_ships
--------

:title: Union ships
:type: integer
:format: default


Number of Union ships (including gunships, wooden warships, ironclads, and rams; excluding transports)


       
confederate_fortifications
--------------------------

:title: confederate_fortifications
:type: boolean
:format: default


Were any Confederate fortifications involved in the battle?


       
us_fortifications
-----------------

:title: us_fortifications
:type: boolean
:format: default


Were any US fortifications involved in the battle?


       

