##########################################################
Size of the Union and Confederate Armies (Livermore, 1900)
##########################################################

:name: livermore_army_sizes
:path: data/livermore_army_sizes.csv
:format: csv

Size of the Union and Confederate Armies from Livermore (1900)

The table of the aggregate size of the Union and Confederate armies over
time. The data come from Table "Comparison of the Foregoing Numbers with
the Number on the Union Rolls at the Same Date", on p. 47.

While good documentation is available on the total number of troops
serving in the Union military, there is no comparable documentation on
the total number of troops serving in the Confederate military.
Livermore devotes p. 1-49 to developing the estimates of the size of
Confederate Forces which are reported in this table.

The data exclude the columns with averages, and the size of the Confederate army as a percent of the Union army since they can be calculated from the column with the number in each army at each date.


**Sources:**
- Livermore1900


Schema
======



==================  =======  ==========================
date                date     date
union_number        integer  No. on Union Rolls
confederate_number  integer  No. on Confederate Returns
==================  =======  ==========================

date
----

:title: date
:type: date
:format: default





       
union_number
------------

:title: No. on Union Rolls
:type: integer
:format: default





       
confederate_number
------------------

:title: No. on Confederate Returns
:type: integer
:format: default





       

