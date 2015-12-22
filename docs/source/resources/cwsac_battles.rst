#################################
CWSAC Report battle data: battles
#################################

:name: cwsac_battles
:path: cwsac_battles.csv
:format: csv

Civil War Sites Advisory Commission 1993 Report battle data

These data are from the `CWSAC Battle Summaries
<http://www.nps.gov/hps/abpp/battles/bystate.htm>`_.  The unstructured
webpages were cleaned and converted into the structured data in these
tables.

For more information on the CWSAC data see

- http://www.nps.gov/hps/abpp/battles/tvii.htm 
- http://www.nps.gov/hps/abpp/cwsac/cws0-1.html



Sources: [CWSAC1993]_, [CWSAC1997]_, [CWSAC_by_state]_, [CWSAC_by_campgn]_


Schema
======



===============  =======  =====================
battle           string   Battle
url              string   url
battle_name      string   Battle Name
other_names      string   Other Battle Names
state            string   State
locations        string   Locations
campaign         string   Campaign
start_date       date     Start Date
end_date         date     End Date
operation        boolean  operation
assoc_battles    string   Associated battles
results_text     string   Results
result           string   result
forces_text      string   forces_text
strength         integer  strength
casualties_text  string   casualties_text
casualties       integer  Casualties
description      string   Battle summary
preservation     string   Preservation Priority
significance     string   Military significance
strength_mean    number   Strength (mean)
strength_var     number   Strength (variance)
===============  =======  =====================

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


       
url
---

:title: url
:type: string
:format: url


URL of the battle summary


       
battle_name
-----------

:title: Battle Name
:type: string
:format: default





       
other_names
-----------

:title: Other Battle Names
:type: string
:format: default



Secondary or commonly used names, such as Elkhorn Tavern (Pea Ridge), Bull Run (Manassas), and Sharpsburg (Antietam).


       
state
-----

:title: State
:type: string
:format: default
:constraints:
    :minLength: 2
    :maxLength: 2
    :pattern: [A-Z][A-Z]
    

2-letter State abbreviation


       
locations
---------

:title: Locations
:type: string
:format: default


The present day county or city in which the battlefield is located.


       
campaign
--------

:title: Campaign
:type: string
:format: default


The larger military operation with which the battle is associated.


       
start_date
----------

:title: Start Date
:type: date
:format: default





       
end_date
--------

:title: End Date
:type: date
:format: default





       
operation
---------

:title: operation
:type: boolean
:format: default


Was the battle an operation, a series of several related battles? E.g. Marietta Operations.


       
assoc_battles
-------------

:title: Associated battles
:type: string
:format: default


If the battle was an operation, this contains the names of the battles in that operation.


       
results_text
------------

:title: Results
:type: string
:format: default


Text description of the battle result

   The victor in the battle, if the outcome was definitive. If the outcome was other than definitive, that information is provided.


       
result
------

:title: result
:type: string
:format: default
:constraints:
    :enum: ['Union', 'Confederate', 'Inconclusive']
    

Categorical result of the battle: Union victory, Confederate victory, or a tie.


       
forces_text
-----------

:title: forces_text
:type: string
:format: default


Description of the forces involved in the battle.
CWSAC summary

   In most summaries, the particular company, regiment, brigade, division, corps, army, garrison, detachment, or ship. Some summaries, however, indicate the number of troops involved. In both cases, the purpose is to provide an idea of the size of the engagement. Most of the forces engaged were found in the U.S. War Department's Official Records.


       
strength
--------

:title: strength
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Total personnel involved in the battle. In some cases, CWSAC gives a number for the total personnel in the battle, but does not disaggregate by side.


       
casualties_text
---------------

:title: casualties_text
:type: string
:format: default


Description of the casualties of the battle.


       
casualties
----------

:title: Casualties
:type: integer
:format: default
:constraints:
    :minimum: 0
    


Total casualties (both sides) of the battle. In some cases, CWSAC gives a number for the total personnel in the battle, but does not disaggregate by side.
CWSAC description of casualties

   No source exists, either in print or in manuscript, that
   provides casualty figures for all Civil War battles or even
   for the 384 principal battles that the CWSAC studied. Some of
   the casualty figures for the 384 principal battles are
   unknown; in some instances reliable figures are available for
   one of the combatants but not for the other. Few casualty
   figures are definitive; sources often differ in their
   figures. A variety of sources, both official and commercial,
   printed and in manuscript, were consulted. All casualty
   figures were subjected to historical analysis before
   inclusion in the summaries.

   A partial list of sources follows.

   Dyer, Frederick. A Compendium of the War of the Rebellion . .. Des Moines, IA: Dyer Publishing Company, 1908.

   Fox, William F. Regimental Losses in the American Civil War 1861-1865: A Treatise on the Extent and Nature of the Mortuary Losses in the United States . . . Albany, NY: Albany Publishing Company,1889.

   Johnson, Robert U., and Clarence C. Buell, eds. Battles and Leaders of the Civil War . . . .4 Volumes. New York: The Century Company, 1887-88.

   Livermore, Thomas L.Numbers and Losses in the Civil War in America 1861-65. Reprint. Dayton, OH: Morningside House, Inc., 1986.

   U.S. Surgeon General's Office. Chronological Summary of Engagements and Battles [Civil War]. Washington, DC: The Government Printing Office, 1873.

   U.S. War Department. The War of the Rebellion: A Compilation ofthe Official Records of the Union and Confederate Armies. 70 Volumes in 128. Washington, DC: The Government Printing Office, 1880-1901.


       
description
-----------

:title: Battle summary
:type: string
:format: default


Short text summary of the battle.
CWSAC documentation

   A historical account or summary of the battle. A variety of sources, both general and specific, published and in manuscript, were consultedin the preparation of these accounts. The general sources consulted include those listed below. More specific published and manuscript sources were also consulted and analyzed.

   The Conservation Fund. The Civil War Battlefield Guide. Edited by Frances H. Kennedy. Boston, MA: Houghton Mifflin Company, 1990.

   Great Battles of the Civil War. By the editors of Civil War Times Illustrated. New York: Gallery Books, 1984.

   Historical Times Illustrated Encyclopedia of the Civil War. Edited by Patricia L. Faust. New York: Harper & Row, Publishers, 1986.

   Johnson, Robert U., and Clarence C. Buell, eds. Battles and Leaders of the Civil War . . . .4 Volumes. New York: The Century Company, 1887-88.

   Long, E.B., compiler. The Civil War Day by Day: An Almanac 1861-1865. Garden City, NY: Doubleday & Company, Inc., 1971.

   U.S. National Archives. A Guide-Index to the Official Records of the Union and Confederate Armies. Edited and compiled by Dallas Irvine, et al. Washington, DC: The Government Printing Office, 1968-1980.
   
   U.S. Naval History Division. Civil War Naval Chronology, 1861-1865. Washington, DC: The Government Printing Office, 1971.

   U.S. Navy Department. Official Records of the Union and Confederate Navies in the War of the Rebellion. Multivolumes. Washington, DC: The Government Printing Office, 1894-1927.

   U.S. War Department. The War of the Rebellion: A Compilation ofthe Official Records of the Union and Confederate Armies. 70 Volumes in 128. Washington, DC: The Government Printing Office, 1880-1901.


       
preservation
------------

:title: Preservation Priority
:type: string
:format: default



A designation made by the Commission based on the level of historical significance, the integrity of the remaining battlefield features, and the level of threat to the battlefield's existence. For example, IV.1 (Class D) means that the Commission determined that a particular battlefield site was Priority IV: Fragmented Battlefields, All Military Classes, Poor Integrity. (See Table 7, pages 49-53 in the Report on the Nation's Civil War Battlefield, for the preservation priority of all the battlefields studied.) Class A, B, C, or D indicates a battle's (and associated battlefield's) level of military importance within its campaign and the war. (See page v of this volume for an explanation of each of the four designations.) N/D indicates that no data is currently available to determine the levelof threat to the site.


       
significance
------------

:title: Military significance
:type: string
:format: default
:constraints:
    :enum: ['A', 'B', 'C', 'D']
    


Four-category classification of the military significance of the battle.


       
strength_mean
-------------

:title: Strength (mean)
:type: number
:format: default
:constraints:
    :minimum: 0
    

Mean of the estimated strength in personnel of the force. See code for how it is calculated.

Sources: [CWSAC1993]_, [CWSAC1997]_, [CWSAC_by_state]_, [CWSAC_by_campgn]_

       
strength_var
------------

:title: Strength (variance)
:type: number
:format: default
:constraints:
    :minimum: 0
    

Variance of the estimated strength in personnel of the force. See code for how it is calculated.

Sources: [CWSAC1993]_, [CWSAC1997]_, [CWSAC_by_state]_, [CWSAC_by_campgn]_

       

