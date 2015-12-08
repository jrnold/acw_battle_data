############################################################
Livermore (1900) battle data: force strengths and casualties
############################################################

:name: livermore_forces
:path: data/livermore_forces.csv
:format: csv



**Sources:**
- Livermore, Thomas Leonard. 1900. Number and Losses in the Civil War in America, 1861-65. Houghton, Mifflin; Company. http://books.google.com/books?id=Qw8pAAAAYAAJ.; http://books.google.com/books?id=Qw8pAAAAYAAJ


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
    




       

