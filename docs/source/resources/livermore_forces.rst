############################################################
Livermore (1900) battle data: force strengths and casualties
############################################################

:name: livermore_forces
:path: livermore_forces.csv
:format: csv



Sources: [Livermore1900]_


Schema
======



===========  =======  ===================
par_id       integer  seq_no
belligerent  string   Belligerent
str          integer  str
kia          integer  Killed
wia          integer  Wounded
kw           integer  Killed or Wounded
miapow       integer  Missing or Captured
===========  =======  ===================

par_id
------

:title: seq_no
:type: integer
:format: default
:constraints:
    :minimum: 1
    



Sources: [Livermore1900]_

       
belligerent
-----------

:title: Belligerent
:type: string
:format: default
:constraints:
    :enum: ['US', 'Confederate']
    




       
str
---

:title: str
:type: integer
:format: default
:constraints:
    :minimum: 0
    




       
kia
---

:title: Killed
:type: integer
:format: default
:constraints:
    :minimum: 0
    

None


       
wia
---

:title: Wounded
:type: integer
:format: default
:constraints:
    :minimum: 0
    




       
kw
--

:title: Killed or Wounded
:type: integer
:format: default
:constraints:
    :minimum: 0
    




       
miapow
------

:title: Missing or Captured
:type: integer
:format: default
:constraints:
    :minimum: 0
    




       

