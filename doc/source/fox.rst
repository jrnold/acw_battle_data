Fox "Regimental Losses in the American Civil War, 1861-1865"
=============================================================

**TODO: I haven't added these data yet**

Data from William F. Fox *Regimental Losses in the American Civil War,
1861-1865: A Treatise on the extent and nature of the mortuary losses
in the Union regiments, with full and exhaustive statistics compiled
from the official records on file in the state military bureaus and at
Washington*, available at
http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A2001.05.0068.

The data on casualties come from the main table in "Chapter 14: the
greatest battles of the war — list of victories and defeats —
chronological list of battles with loss in each, Union and
Confederate", p. 544-551.

    There were 112 battles in the war, in which one side or the other
    lost over 500 in killed and wounded. In all, there were 1,882
    general engagements, battles, skirmishes, or affairs in which at
    least one regiment was engaged.

    With this chapter is given a chronological list of the battles and
    minor engagements, showing the loss in each. The figures are
    compiled from the battle reports and revised casualty lists in
    the. “Official Records of the Union and Confederate Armies,”
    published, or in process of publication, by the War Department at
    Washington.

    The figures in the table of Confederate losses are the ones
    officially reported by the Confederate generals in command, or by
    their surgeon-general, to whom, in many instances, that duty seems
    to have been entrusted. There are no official Confederate casualty
    reports for the latter part of the war, and so there is no
    statement of loss for several battles. Estimates might be quoted,
    but such figures are not within the province of this work.

The data in that tables are split into a table with battles and one with
force level casualties.

fox_battles
-------------

fox_forces
--------------


fox_outcomes
---------------

In Chapter 14, p. 541-543 Fox has several tables categorizing battles into
victories for each side. Both his categorization and results are similar
to [livermore1900]_.

   In connection with these matters the question naturally arises,--Which
   were victories, and which were defeats?

   To answer fairly and without prejudice would only invite bitter and
   senseless criticism from both sides. It is too soon to attempt any
   discussion of this much vexed topic. Still, there are certain conceded
   facts relative to this matter which one might venture to recall to
   mind. They may be premised with the military axioms,--that when an
   army retains possession of the battle field and buries its enemy's
   dead, it certainly cannot be considered as a defeated army; and that
   when an army abandons the field, either slowly or in rout, and leaves
   its dead and wounded in the hands of the enemy, it certainly should
   not claim a victory.

Fox categorizes battle outcomes into the following five categories:

   In the following named battles the Union armies remained in
   undisturbed possession of the field, the enemy leaving many of their
   wounded, and most of their dead unburied

   The Union armies were successful, also, in the following
   assaults. They were the attacking party, and carried the forts, or
   intrenched positions, by storm.

   In the following battles the Confederates remained in undisturbed
   possession of the field, the Union armies leaving its unburied dead
   and many of its wounded in their hands:

   In the following assaults the Confederates successfully repulsed the
   attacks of the enemy:

   In the following assaults, or sorties, the Confederates were the
   attacking party, and were repulsed:

With regards to battles not considered, Fox writes,

  Other instances on each side could be mentioned, but they would
  invite discussion and are better omitted.

Revised data
-------------------

- removed aggregate rows for Union casualties in Atlanta Campaign and Seven Day's Battle
- fn 8. Split Chancellorsville into casualties for Chancellorsville (VA032) and VA033 VA034 
- fn 24. Split Chattanooga into Orchard's Knob on 11/23, Lookout
  Mountain on 11/24 and Missionary Ridge on 11/25. The footnote only
  gives total casualties for 11/23 and 11/24, so I assume a constant
  proportion of K/W/M for all days.
- fn 25. Split Atlanta Campaign into the components in the footnote.  Remainder is assigned to 
  "Lattimore's Mill; Powder Springs, etc". 
- fn 27. Split Atlanta Campaign into the components in the footnote.  It's unclear which entries
  to assign to the Marietta Operations.
- fn 28. Split Atlanta campaign into the components in the footnote. Remainder assigned to the Siege of Atlanta.
  I'm not sure what the Siege of Atlanta refers to so I assign it to the Jonesboro (GA020) and Lovejoy Station (GA021)
- fn 29. The note says Jonesboro and Lovejoy Station, but Jonesboro
  happened on Aug 20, so it cannot be included in this row.
- fn 70. Split Seven Days Battle into the component battles.
- fn 74. Added the 90 casualties from White's battalion.

Fox lists alternate casualty figures for Confederates at Gettysburg that I don't use.

   The records on file at Washington bear the names of 6,802 wounded,
   and 5,425 unwounded Confederates captured at Gettysburg. The
   official reports of Longstreet, Ewell, Hill, and Stuart indicate a
   loss (after making necessary deductions) of 2,701 killed, 12,739
   wounded, 7,528 missing; total, 22,968.

CWSAC 
------------------

- 'Manassas gap' on 1863-7-21 is not matched to VA108 because 'Wapping
  Heights' on 1863-7-23 is matched to that battle.
- 'Petersburg Trenches' entries are not matched to any CWSAC
  battles. All the battles in the Petersburg and Appomattox Campaigns
  appear to be outside the trenches, or assaults that have separate entries in Fox.
