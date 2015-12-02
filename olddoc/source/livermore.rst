Livermore (1900) "Number and Losses in the Civil War in America, 1861-1865"
=============================================================================

Data from Thomas Leonard Livermore (1900) "Number and Losses in the
Civil War in America, 1861-1865",
http://books.google.com/books?id=Qw8pAAAAYAAJ .

Tables `liv_battles` and `liv_forces$` combine data from several
tables in Livermore: "Assaults on Fortified Lines" on p. 75, the
tables on p. 76-77, and Table A (140-141).  

Livermore discusses methodology on pp. 63-77. The sample of battles 
he uses is all battles in which either side had losses (killed plus wounded) 
greater than 1,000.  

Livermore was concerned with determining the actual number of troops
engaged in battle, i.e. those that actually participated.  The
majority of the book consists of the calculations leading to the
values of forces and casualties of each battle.

Some notes on Table A

- Values of "unknown" and "...." in the original, left blank in the above table.
- `endDate` left blank if the battle lasted a single day.
- Row 59 "Nashville", column `cs_hits` "unknown, but small".
- Row 62 "Appomattox Camp", column `cs_hits` :"estimated at 6,266".
- Row 37 "Wilderness",  column `us_force` : "101,895 (ex. cavalry)".

When discussing the categorization of battles into victories and defeats, Livermore writes,

    For further comparison of losses under similar conditions, the 63
    battles of Table B may be classified as follows, although
    discrimination must be made between those which are styled defeats,
    because some are ranged under this head merely because the field was
    abandoned; when considered tactically, the retreating army was
    successful in the battle itself.


liv_battles
------------

.. include:: _tables/liv_battles.rst

liv_forces
---------------

.. include:: _tables/liv_forces.rst

liv_army_size
----------------

.. include:: _tables/liv_army_size.rst

This is the table of the aggregate size of the Union and Confederate armies over time.
The data come from Table "Comparison of the Foregoing Numbers with the
Number on the Union Rolls at the Same Date", on p. 47.

While good documentation is available on the total number of troops
serving in the Union military, there is no comparable documentation on
the total number of troops serving in the Confederate military.
Livermore devotes p. 1-49 to developing the estimates of the size of
Confederate Forces which are reported in this table.


liv_to_dbpedia
----------------

.. include:: _tables/liv_to_dbpedia.rst

Several battles are campaigns:

- Seven_Days'_Battles_1862-06-25 : http://en.wikipedia.org/wiki/Seven_Days%27_Battles
- Appomattox_Camp_1865-03-29 : http://en.wikipedia.org/wiki/Appomattox_campaign
- Atlanta_Campaign_1864-05-01 : http://dbpedia.org/resource/Atlanta_Campaign

