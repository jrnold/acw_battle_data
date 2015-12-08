#################
Naval battle data
#################

:name: navalbattles
:path: data/navalbattles.csv
:format: csv

List of naval battles

List of naval battles, which navies they involved, and whether they involved land fortifications. These were coded for this data primarily using the descriptions of the battles in the CWSAC and Wikipedia.


Sources: [jrnold]_


Schema
======



===========  =======  =================
cwsac_id     string   CWSAC Id.
battle_name  string   Battle name
all_naval    boolean  All Naval Battle?
us_navy      boolean  US Navy
cs_navy      integer  Confederate Navy
us_fort      integer  US Fort
cs_fort      integer  Confederate Fort
comments     string   Comments
===========  =======  =================

cwsac_id
--------

:title: CWSAC Id.
:type: string
:format: default
:constraints:
    :pattern: [A-Z]{2}[0-9]{3}[A-Z]?
    




       
battle_name
-----------

:title: Battle name
:type: string
:format: default





       
all_naval
---------

:title: All Naval Battle?
:type: boolean
:format: default


Did the battle only involve naval forces?


       
us_navy
-------

:title: US Navy
:type: boolean
:format: default


Did the battle involve the US Navy?


       
cs_navy
-------

:title: Confederate Navy
:type: integer
:format: default


Did the battle involve the Confederate Navy?


       
us_fort
-------

:title: US Fort
:type: integer
:format: default


Did the battle involve a US fort?


       
cs_fort
-------

:title: Confederate Fort
:type: integer
:format: default


Did the battle involve a Confederate fort?


       
comments
--------

:title: Comments
:type: string
:format: default





       

