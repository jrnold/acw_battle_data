# Livermore (1900) "Number and Losses in the Civil War in America, 1861-1865"

Data from

> Thomas Leonard Livermore (1900) "Number and Losses in the Civil War in America, 1861-1865",
> http://books.google.com/books?id=Qw8pAAAAYAAJ .

## Battle Results

The `LIVRMORE` dataset in PAR includes data from Livermore, taken from the battle descriptions in the text (not Table A).
Thuse the `LIVRMORE` data includes breakdown into killed, wounded, and missing, as well as the victor of the battle.

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

When discussing the categorization of battles into victories and defeats, Livermore writes,

    For further comparison of losses under similar conditions, the 63
    battles of Table B may be classified as follows, although
    discrimination must be made between those which are styled defeats,
    because some are ranged under this head merely because the field was
    abandoned; when considered tactically, the retreating army was
    successful in the battle itself.

The table of the aggregate size of the Union and Confederate armies over time.
The data come from Table "Comparison of the Foregoing Numbers with the
Number on the Union Rolls at the Same Date", on p. 47.

While good documentation is available on the total number of troops
serving in the Union military, there is no comparable documentation on
the total number of troops serving in the Confederate military.
Livermore devotes p. 1-49 to developing the estimates of the size of
Confederate Forces which are reported in this table.

## LIVRMORE data

## Files

- `liv_battles.csv`: Battle-level data.
- `liv_forces.csv`: Force-level data.
- `liv_to_cwsac.csv`: Mapping battles to CWSAC reference numbers.
- `liv_to_dbpedia.csv`: Mapping battles to dbpedia.org URIS.
- `liv_army_sizes.csv`: Comparison of number on rolls in Confederate and Union armies; table on p. 47.

