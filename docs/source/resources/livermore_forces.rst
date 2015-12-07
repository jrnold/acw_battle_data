############################################################
Livermore (1900) battle data: force strengths and casualties
############################################################

:name: livermore_forces
:path: data/livermore_forces.csv
:format: csv



**Sources:**
- Livermore1900


Schema
======



===========  =======  ===================
seq_no       integer  seq_no
belligerent  string   Belligerent
str          integer  str
kia          integer  Killed
wia          integer  Wounded
kw           integer  Killed or Wounded
miapow       integer  Missing or Captured
===========  =======  ===================

seq_no
------

:title: seq_no
:type: integer
:format: default
:constraints:
    :minimum: 1
    

Battle number.


       
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
    




       

