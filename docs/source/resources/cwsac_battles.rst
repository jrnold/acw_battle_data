CWSAC Report battle data: battles
================================================================================

:name: cwsac_battles
:path: data/cwsac_battles.csv
:format: csv

Civil War Sites Advisory Commission 1993 Report battle data

These data are from the `CWSAC Battle Summaries
<http://www.nps.gov/hps/abpp/battles/bystate.htm>`_.  The unstructured
webpages were cleaned and converted into the structured data in these
tables.

For more information on the CWSAC data see

- http://www.nps.gov/hps/abpp/battles/tvii.htm 
- http://www.nps.gov/hps/abpp/cwsac/cws0-1.html

A couple notes about the set of battles in these data. 

- In an update on the status of battlefields `Civil War Sites Advisory Commission Report Update & Resurvey <http://www.nps.gov/history/hps/abpp/CWSII/CWSII.htm>`_, 
  the following changes were made.
  
  - AR018,  Battle of Bayou Meto (Reed's Bridge) on Aug 27, 1863 (part of the Advance on Little Rock campaign) was added. See 
    `Civil War Battlefields in the State of Arkansas - Arkansas Post to Devils Backbone <http://www.nps.gov/history/hps/abpp/CWSII/ArkansasBattlefieldProfiles/Arkansas%20Post%20to%20Devils%20Backbone.pdf>`_.
  - SC007. Fort Wagner II. Dates changed to 7-18. `Report Update
    <http://www.nps.gov/history/hps/abpp/CWSII/SouthCarolinaBattlefieldProfiles/SouthCarolinaBattlefieldProfiles.pdf>`_.
  - SC008. Fort Sumter II. Dates changed to 8-17 to 9-8. `Report
    Update
    <http://www.nps.gov/history/hps/abpp/CWSII/SouthCarolinaBattlefieldProfiles/SouthCarolinaBattlefieldProfiles.pdf>`_.
  - SC009. Charleston Harbor. Dates changed to Aug 22-23, 1863 and
    Sept 5-8, 1863.  This really appears to be to engagements.  The
    assault on Fort Sumter is the only engagement referenced in the
    initial CWSAC report.  `Report Update
    <http://www.nps.gov/history/hps/abpp/CWSII/SouthCarolinaBattlefieldProfiles/SouthCarolinaBattlefieldProfiles.pdf>`_.
    
    - Aug 22-23, 1863 Bombardment of Charleston by the Swamp Angel
    - Sept 5-8, 1863. Assault on Fort Sumter.

  - VA020A and VA020B combined into a single battle, `Source
    <http://www.nps.gov/hps/abpp/CWSII/VirginiaBattlefieldProfiles/White%20oak%20Road%20to%20Wilderness.pdf>`_.

	 Although the CWSAC identified the engagements at White Oak
	 Swamp and Glendale as part of the same offensive, it mapped the
	 battlefields individually. Upon further study, the ABPP decided to
	 combine the two engagements under one Study Area.

The Civil War Battlefield Preservation Act of 2002 directed the NPS to
update their 1993 battlefield surveys. The results of the resurvey are
available `here
<http://www.nps.gov/hps/abpp/CWSII/CWSIIStateReports.htm>`_.
These battles are largely the same as in the first CWSAC, with a few exceptions.

- Battles Glendale (VA020A) and White Oak Swamp (VA020B) were combined
  into a single battle.

    Upon review of the histories of the battles, the ABPP has combined
    White Oak Swamp (VA020a) and Glendale (VA020b) into a single
    entry: the overall count is one battlefield fewer, but both
    engagement areas are included. `Update to the Civil War Sites
    Advisory Commission Report: Commonwealth of Virigina
    <http://www.nps.gov/hps/abpp/CWSII/CWSACReportVirginiaUpdate.pdf>`_
    (p. 8).
    
- The Battle of Bayou Meto (AR018) was added. However, it does not
  appear to have been added strictly due to historical judgment of
  importance.  No military significance or casualties is given for
  this battle.  

	The CWSAC did not list Bayou Meto (Reed’s Bridge) as one of
	the principal battles of the Civil War. In 2002, however, the
	battlefield was listed in the National Register of Historic
	Places as a nationally significant historic property. Given
	the high level of significance conferred by the NRHP listing,
	the ABPP decided, as part of the fieldwork undertaken for this
	update, to assess conditions at Bayou Meto.  ` Update to the
	Civil War Sites Advisory Commission Report: State of Arkansas
	<http://www.nps.gov/hps/abpp/CWSII/CWSACReportArkansasUpdate.pdf>`_ (p. 8)

- The Battle of Athens (AL002) is redefined from the battle on January 26, 1863
  to the battle on September 23-25, 1963. Because of this I give
  the new battle the code **AL009**.  I also think that the results in the document
  are referring to the January battle because the September battle is unambiguously
  a Confederate victory.
- new variables: Acreage of the battlefield area
- revised variables: forces, principal commanders, result, battle
  dates
- Indian forces. Oklahoma battles OK001 (Round Mountain), OK002
  (Chusto-Talasah), and OK003 (Chustenahlah) classify the Creek forces
  under Opothleyahola as [US] instead of [I].  In CWSAC II, the only
  battles involving purely American Indian forces are against the
  Union and generally part of the Sioux Wars (Minnesota, North Dakota,
  Idaho).  This seems reasonable, the Creek and Seminole forces in the
  Oklahoma battles were Union allies, while the
  Sioux Indian forces fighting the Union were not allied with the
  Confederacy.

For the most part, each CWSAC battle page corresponds to a single Wikipedia page, 
making linking the two easy.

The one exception is that CWSAC considers the Battle of Chattanooga
(http://www.nps.gov/hps/abpp/battles/tn024.htm) from Nov 23-25, 1863 a
single battle. However, in Wikipedia this corresponds to two battles
in http://en.wikipedia.org/wiki/Chattanooga_Campaign:
http://en.wikipedia.org/wiki/Battle_of_Lookout_Mountain on Nov 24, and
the http://en.wikipedia.org/wiki/Battle_of_Missionary_Ridge on Nov 25.

The set of battles around Charleston Harbor July to September 1863 is confusingly
and ambiguously defined by the CWSAC. 

+-------+----------------------+--------+---------------+--------------------------+
| cwsac | name                 | result | cwsac I       | cwasc II                 |
+-------+----------------------+--------+---------------+--------------------------+
| SC005 | Fort Wagner I        | C      | 7-10 to 7-11  | 7-10 to 7-11             |
+-------+----------------------+--------+---------------+--------------------------+
| SC007 | Fort Wagner II       | C      | 7-18 to 9-7   | 7-18                     |
+-------+----------------------+--------+---------------+--------------------------+
| SC008 | Fort Sumter II       | I      | 8-17 to 12-31 | 8-17 to 9-8              |
+-------+----------------------+--------+---------------+--------------------------+
| SC009 | Charleston Harbor II | C      | 9-7 to 9-8    | 8-22 to 8-23; 9-5 to 9-8 |
+-------+----------------------+--------+---------------+--------------------------+

where cwsac I refers to the `1993 report
<http://www.nps.gov/hps/abpp/battles/bystate.htm>`_ , and cwsac II
refers to the `revised report
<http://www.nps.gov/history/hps/abpp/CWSII/SouthCarolinaBattlefieldProfiles/SouthCarolinaBattlefieldProfiles.pdf>`_.

The battles considered and the summaries from their pages are copied below.

Charleston Harbor I (SC004) occurred on April 7, 1863, and was a naval
battle between Union ships and the Charleston Harbor forts.

CWSAC Fort Wagner I (SC005)

  On July 10, Union artillery on Folly Island together with Rear
  Adm. John Dahlgren’s fleet of ironclads opened fire on Confederate
  defenses of Morris Island. The bombardment provided cover for
  Brig. Gen. George C. Strong’s brigade, which crossed Light House Inlet
  and landed by boats on the southern tip of the island. Strong’s troops
  advanced, capturing several batteries, to within range of Confederate
  Fort Wagner. At dawn, July 11, Strong attacked the fort. Soldiers of
  the 7th Connecticut reached the parapet but, unsupported, were thrown
  back.   http://www.nps.gov/hps/abpp/battles/sc005.htm

CWSAC Fort Wagner II (SC007)

  After the July 11 assault on Fort Wagner failed, Gillmore reinforced
  his beachhead on Morris Island. At dusk July 18, Gillmore launched an
  attack spearheaded by the 54th Massachusetts Infantry, a black
  regiment. The unit’s colonel, Robert Gould Shaw, was killed. Members
  of the brigade scaled the parapet but after brutal hand-to-hand combat
  were driven out with heavy casualties. The Federals resorted to siege
  operations to reduce the fort. This was the fourth time in the war
  that black troops played a crucial combat role, proving to skeptics
  that they would fight bravely if only given the chance.
  http://www.nps.gov/hps/abpp/battles/sc007.htm

Fort Sumter II (SC008)

  Federal batteries erected on Morris Island opened fire on August 17
  and continued their bombardment of Fort Sumter and the Charleston
  defenses until August 23. Despite a severe pounding, Fort Sumter’s
  garrison held out. Siege operations continued against Fort Wagner on
  Morris Island. http://www.nps.gov/hps/abpp/battles/sc008.htm

CWSAC Charleston Harbor II (SC009)

  During the night of September 6-7, Confederate forces evacuated Fort
  Wagner and Battery Gregg pressured by advancing Federal
  siegeworks. Federal troops then occupied all of Morris Island. On
  September 8, a storming party of about 400 marines and sailors
  attempted to surprise Fort Sumter. The attack was repulsed.
  http://www.nps.gov/hps/abpp/battles/sc009.htm

CWSAC II added the August bombardment of Charleston by the "The Swamp Angel" 
to Charleston Harbor II.  

In Wikipedia

1. SC005: http://en.wikipedia.org/wiki/First_Battle_of_Fort_Wagner July 10-July 11
2. SC007: http://en.wikipedia.org/wiki/Second_Battle_of_Fort_Wagner July 18
3. SC008: http://en.wikipedia.org/wiki/Second_Battle_of_Charleston_Harbor Aug 17 - Sept 8
4. SC009  http://en.wikipedia.org/wiki/Second_Battle_of_Fort_Sumter Sept 9

Timeline of July-September events in the  1863 siege of Charleston

- July 10-11. First Battle of Fort Wagner. Failed Union assault.
- July 16. Battle of Grimball's landing. Union defeated in attempt to take Charleston by land.
- July 18. Second failed assault on Fort Wagner
- July 19 Union begins siege of Fort Wagner 
- Aug 17. Batteries on Morris Island begin bombarding Fort Sumter
- Aug 22-23. Bombardment of Charleston Island by the Swamp Angel (a battery on Morris Island)
- Aug 23. Batteries on Morris Island switch bombardment to Fort Wagner.
- Sept 7. Confederates abandon Fort Wagner
- Sept 9. Union forces attempt and fail to retake Fort Sumter

It seems that the battles break down into the following periods

- July 10-11: First Battle of Fort Wagner (SC005)
- July 16: Battle of Grimball's Landing (SC006)
- July 18: Second Battle of Fort Wagner (SC007)
- (July 19) Aug 17 - Sept 8. Second Battle of Charleston Harbor =
  Siege of Fort Wagner/Sumter ending with the Confederate abandonment
  of Fort Wagner. (SC008)
- Sept 9 : Second Battle of Fort Sumter (Failed Assault)
- Continued siege??  (SC009)

Thus, confusingly:

- SC009: Charleston Harbor is the `Second Battle of Fort Sumter <http://en.wikipedia.org/wiki/Second_Battle_of_Fort_Sumter>`__ .
- SC008: Fort Sumter is the  `Second Battle of Charleston Harbor <http://en.wikipedia.org/wiki/Second_Battle_of_Charleston_Harbor>`__ .




Schema
-------





battle
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Battle
:type: string
:format: default 
:constraints:
    
    :minLength: 5 
    :maxLength: 6 
    
    :pattern: [A-Z]{2}[0-9]{3}[A-Z]? 
    
    
         


CWSAC battle identifier
       

url
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: url
:type: string
:format: url 


URL of the battle summary
       

battle_name
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Battle Name
:type: string
:format: default 



       

other_names
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Other Battle Names
:type: string
:format: default 



Secondary or commonly used names, such as Elkhorn Tavern (Pea Ridge), Bull Run (Manassas), and Sharpsburg (Antietam).
       

state
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: State
:type: string
:format: default 
:constraints:
    
    :minLength: 2 
    :maxLength: 2 
    
    :pattern: [A-Z][A-Z] 
    
    
         


2-letter State abbreviation
       

locations
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Locations
:type: string
:format: default 


The present day county or city in which the battlefield is located.
       

campaign
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Campaign
:type: string
:format: default 


The larger military operation with which the battle is associated.
       

start_date
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Start Date
:type: date
:format: default 



       

end_date
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: End Date
:type: date
:format: default 



       

operation
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: operation
:type: boolean
:format: default 


Was the battle an operation, a series of several related battles? E.g. Marietta Operations.
       

assoc_battles
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Associated battles
:type: string
:format: default 


If the battle was an operation, this contains the names of the battles in that operation.
       

results_text
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Results
:type: string
:format: default 


Text description of the battle result

   The victor in the battle, if the outcome was definitive. If the outcome was other than definitive, that information is provided.
       

result
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: result
:type: string
:format: default 
:constraints:
    
    
    
    
    
    
    
    :enum: ['Union', 'Confederate', 'Inconclusive']      


Categorical result of the battle: Union victory, Confederate victory, or a tie.
       

forces_text
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: forces_text
:type: string
:format: default 


Description of the forces involved in the battle.
CWSAC summary

   In most summaries, the particular company, regiment, brigade, division, corps, army, garrison, detachment, or ship. Some summaries, however, indicate the number of troops involved. In both cases, the purpose is to provide an idea of the size of the engagement. Most of the forces engaged were found in the U.S. War Department's Official Records.
       

strength
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: strength
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Total personnel involved in the battle. In some cases, CWSAC gives a number for the total personnel in the battle, but does not disaggregate by side.
       

casualties_text
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: casualties_text
:type: string
:format: default 


Description of the casualties of the battle.
       

casualties
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Preservation Priority
:type: string
:format: default 



A designation made by the Commission based on the level of historical significance, the integrity of the remaining battlefield features, and the level of threat to the battlefield's existence. For example, IV.1 (Class D) means that the Commission determined that a particular battlefield site was Priority IV: Fragmented Battlefields, All Military Classes, Poor Integrity. (See Table 7, pages 49-53 in the Report on the Nation's Civil War Battlefield, for the preservation priority of all the battlefields studied.) Class A, B, C, or D indicates a battle's (and associated battlefield's) level of military importance within its campaign and the war. (See page v of this volume for an explanation of each of the four designations.) N/D indicates that no data is currently available to determine the levelof threat to the site.
       

significance
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Military significance
:type: string
:format: default 
:constraints:
    
    
    
    
    
    
    
    :enum: ['A', 'B', 'C', 'D']      



Four-category classification of the military significance of the battle.
       

strength_mean
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Strength (mean)
:type: number
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Mean of the estimated strength in personnel of the force. See code for how it is calculated.
       

strength_var
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Strength (variance)
:type: number
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Variance of the estimated strength in personnel of the force. See code for how it is calculated.
       

