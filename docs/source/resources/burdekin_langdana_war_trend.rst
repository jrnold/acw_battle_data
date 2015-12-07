###########################################
War Trend from Burdekin and Langdana (1993)
###########################################

:name: burdekin_langdana_war_trend
:path: data/burdekin_langdana_war_trend.csv
:format: csv

War Trend variable used in Burdekin and Langdana (1993) "War Finance in the Southern Confederacy, 1861-1865", *Explorations in Economic History*

They classify each quarter of the war as either neutral (0), bad for the Confederacy (-1), or good for the Confederacy (+1).
All quarter are classified as 0 except

- +1 for 1863Q3: victory of Chancelorsville aand advance of Lee's army into Maryland and Pennsylvania
- -1 for 1862Q2: Richmond threatened by McClellan during the Peninsular campaign
- -1 for 1863Q4 and 1864Q1: Aftermath of Gettysburg and Vicksburg

Their clasification was based on the qualitative accounts of crises of confidence in Schwab (1901), *The Confederate States of America, 1861-1865*.
The variable is set to 0 in 1864Q2 and 1864Q3 because the Northern offensive stalls at the start of the year, and the northern Democratic party's nominates of McClellan.



**Sources:**
- BurdekinLangdana1993


Schema
======

=====  =======  =========
date   date     Date
trend  integer  War Trend
=====  =======  =========

date
----

:title: Date
:type: date
:format: default


First day of the quarter


       
trend
-----

:title: War Trend
:type: integer
:format: default


-1 (+1) if war news is unfavorable (favorable) to Confederacy; 0 otherwise.


       

