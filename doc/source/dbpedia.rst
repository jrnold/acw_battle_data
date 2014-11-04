Dbpedia data
=================

These data are derived from the dbpedia.org resources of Civil War
Battles.  Dbpedia.org extracts data from Wikipedia (primarily the
infoboxes) into structured form.

I used the list
http://en.wikipedia.org/wiki/Battles_of_the_American_Civil_War
(version 16:17, 3 August 2011), as the basis of the set of dbpedia
resources that I considered battles in the American Civil War.  I made
the following changes to that list to account for the different ways
in which CWSAC and Wikipedia classify the Battle of Chattanooga (Nov
23-25 1863). Additionally, several pages which did not have dbpedia
pages were removed.

- removed Chattanooga_Campaign; replaced by component battles: Lookout Mountain and Missionary Ridge.
  See the note in :doc:`cwsac`.
- added Battle_of_Lookout_Mountain
- added Battle_of_Missionary_Ridge
- removed Draft_Riots; domestic riot -- not a battle
- removed Seven_Days_Battles; duplicates other battles
- removed Sherman's_March_to_the_Sea; a campaign, not a battle.

Civil war battles can also be identified using Wikipedia categories,
but I found that this also required significant manual intervention to account
for false positives and negatives The following sparql query on dbpedia.org will get
most of the Civil War battles.

::

    SELECT DISTINCT ?battle
    WHERE {
	{
	# battles for each campaign
	    ?battle skos:subject ?campaign . 
	    ?campaign skos:broader ?theater .
	    ?theater skos:broader dbpc:Campaigns_of_the_American_Civil_War .
	    FILTER regex(?campaign, \"/Category:Battle\")
	} UNION {
	# battles in each theater
	    ?battle skos:subject ?theater . 
	    ?theater skos:broader dbpc:Battles_of_the_American_Civil_War .
	    FILTER regex(?theater, \"/Category:Battles_of_the_.*_Theater\")
	}
    } ORDER BY ?battle



dbp_battlesg
--------------

.. include:: _tables/dbp_battles.rst
