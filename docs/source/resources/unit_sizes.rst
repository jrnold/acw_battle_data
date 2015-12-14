##################################
Distributions of peronnel in units
##################################

:name: unit_sizes
:path: data/unit_sizes.csv
:format: csv

Distributions of the number of personnel per unit (e.g. regiment,

Using the distribution of personnel per regiment from Livermore's (1900) examples of regiment sizes, and the table of units in Eicher and Eicher (2002), this data is the distribution of personnel in each type of unit (company, regiment, brigade, division, corps, army, etc.).
See the `source <https://github.com/jrnold/acw_battle_data/blob/master/rawdata/unit_sizes/unit_sizes.Rmd>`__ for the details of how this data was simuated.
This data is used for estimates of strenghts in battles when the source gives only the number and types of units (e.g. :doc:`clodfelter_forces`, :doc:`cwsac_forces`, :doc:`cws2_forces`).


Sources: [jrnold]_, [eicher2002civil]_, [Livermore1900]_


Schema
======



===========  ======  ===========
belligerent  string  belligerent
unit_type    string  unit_type
mean         number  mean
sd           number  sd
p025         number  p025
p25          number  p25
median       number  median
p75          number  p75
p975         number  p975
===========  ======  ===========

belligerent
-----------

:title: belligerent
:type: string
:format: default





       
unit_type
---------

:title: unit_type
:type: string
:format: default





       
mean
----

:title: mean
:type: number
:format: default





       
sd
--

:title: sd
:type: number
:format: default





       
p025
----

:title: p025
:type: number
:format: default





       
p25
---

:title: p25
:type: number
:format: default





       
median
------

:title: median
:type: number
:format: default





       
p75
---

:title: p75
:type: number
:format: default





       
p975
----

:title: p975
:type: number
:format: default





       

