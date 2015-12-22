################################
CWSAC Report Updates: commanders
################################

:name: cws2_commanders
:path: cws2_commanders.csv
:format: csv



Sources: [CWSII]_, [CWSIIAL]_, [CWSIIAR]_, [CWSIICO]_, [CWSIIDC]_, [CWSIIFL]_, [CWSIIGA]_, [CWSIIKS]_, [CWSIIKY]_, [CWSIIMN]_, [CWSIILA]_, [CWSIIMD]_, [CWSIIMO]_, [CWSIINC]_, [CWSIIND]_, [CWSIIOH]_, [CWSIIOK]_, [CWSIIPA]_, [CWSIISC]_, [CWSIITN]_, [CWSIIVA]_, [CWSIIWV]_


Schema
======



===========  ======  ===========
battle       string  Battle
belligerent  string  belligerent
fullname     string  Full name
rank         string  Rank
last_name    string  Last Name
first_name   string  First Name
middle_name  string  Middle Name
suffix       string  Suffix
===========  ======  ===========

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


       
belligerent
-----------

:title: belligerent
:type: string
:format: default
:constraints:
    :enum: ['US', 'Confederate', 'Native American']
    




       
fullname
--------

:title: Full name
:type: string
:format: default





       
rank
----

:title: Rank
:type: string
:format: default


Rank of the commander at the time of the battle


       
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





       
suffix
------

:title: Suffix
:type: string
:format: default





       

