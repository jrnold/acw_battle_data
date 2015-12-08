########################################
Livermore (1900) battle data: commanders
########################################

:name: livermore_commanders
:path: data/livermore_commanders.csv
:format: csv

Principal commanders of the battles listed in Livermore (1900) *Numbers and Losses in the Civil War in America*.

Livermore does not directly list the principal commander of the battles. These were added for this data. They primarily follow the principal commanders for each battle given by the CWSAC (:doc:`cwsac_commanders`).


**Sources:**
- jrnold; jeffrey.arnold@gmail.com


Schema
======



==============  ==============================  ==============
seq_no          integer                         Battle number
belligerent     string                          belligerent
PersonID        string                          PersonID
last_name       string                          Last Name
first_name      string                          First Name
middle_name     string                          Middle Name
middle_initial  string                          Middle Initial
rank            string                          Rank
navy            Was the commander in the navy?  navy
==============  ==============================  ==============

seq_no
------

:title: Battle number
:type: integer
:format: default





       
belligerent
-----------

:title: belligerent
:type: string
:format: default
:constraints:
    :enum: ['US', 'Confederate']
    




       
PersonID
--------

:title: PersonID
:type: string
:format: uuid


CWSS PersonID of the commander. See :doc:`cwss_persons`.


       
last_name
---------

:title: Last Name
:type: string
:format: default





       
first_name
----------

:title: First Name
:type: string
:format: default





       
middle_name
-----------

:title: Middle Name
:type: string
:format: default





       
middle_initial
--------------

:title: Middle Initial
:type: string
:format: default





       
rank
----

:title: Rank
:type: string
:format: default





       
navy
----

:title: navy
:type: Was the commander in the navy?
:format: default





       

