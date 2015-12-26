######################################
Commanders in civilwar.org battle data
######################################

:name: civilwarorg_commanders
:path: civilwarorg_commanders.csv
:format: csv

Commanders of battles from the `Civil War Trust <http://www.civilwar.org/>`__.
See :doc:`civilwarorg_battles`.


Sources: 


Schema
======



===========  ======  ===================
id           string  Battle id
belligerent  string  belligerent
name         string  Commander Name
url          string  Commander's Bio URL
===========  ======  ===================

id
--

:title: Battle id
:type: string
:format: default





       
belligerent
-----------

:title: belligerent
:type: string
:format: default
:constraints:
    :enum: ['US', 'Confederate']
    




       
name
----

:title: Commander Name
:type: string
:format: default





       
url
---

:title: Commander's Bio URL
:type: string
:format: url


URL to the biography of the commander at http://www.civilwar.org/education/history/biographies/.


       

