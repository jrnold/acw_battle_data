######################################################
Reiter (2009) Turning Points of the American Civil War
######################################################

:name: reiter2009_turning_points
:path: data/reiter2009_turning_points.csv
:format: csv

Turning Points of the American Civil War in Dan Reiter (2009) *How Wars End*.

Chapter 8 of discusses five turning points (and associated periods) of the American Civil War.
Four of these turning points are based off of those listed by James McPherson in *The Battle Cry of Freedom*; the fifth is the end of the war.


**Sources:**
- Reiter, Dan. 2009. How wars end. Princeton University Press. http://books.google.com/books?id=-_Avp1TNYjMC.; http://books.google.com/books?id=-_Avp1TNYjMC


Schema
======



===============  ================================  ===============
period           Time period of the turning point  Period
start_date       date                              Start Date
description      string                            Description
favor            string                            War Favor
war_aims_change  string                            War Aims Change
comment          string                            Comment
===============  ================================  ===============

period
------

:title: Period
:type: Time period of the turning point
:format: default





       
start_date
----------

:title: Start Date
:type: date
:format: default





       
description
-----------

:title: Description
:type: string
:format: default


Brief description of the turning point


       
favor
-----

:title: War Favor
:type: string
:format: default
:constraints:
    :enum: ['Union', 'Confederacy']
    

Which side did the turning point favor: Union or Confederacy?


       
war_aims_change
---------------

:title: War Aims Change
:type: string
:format: default


Did either side change war aims in the following period?


       
comment
-------

:title: Comment
:type: string
:format: default





       

