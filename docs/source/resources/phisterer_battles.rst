#########################################
Phisterer (1883) battle data: battle list
#########################################

:name: phisterer_battles
:path: phisterer_battles.csv
:format: csv

Phister (1883) Battle

Data from Data from

>   Phisterer, Frederick (1883) *Statistical Records of the Armies of the United States* (`Google books <http://books.google.com/books?id=cVNHr_nnLlYC>`__).

Data on major battles along with Union and Confederate casualties from
the table "Loss in engagements, etc., where the total was five hundred
or more on the side of the Union troops--(149)." on p. 213-219. The
caption for the table reads:

>    Although the losses here given are generally based on official
>    medical returns, the figures must not be taken as perfectly
>    reliable, for in many instances the returns were based on
>    estimates, and the totals of losses were, by *later* and more
>    reliable returns, sometimes considerably reduced. Confederate
>    losses are generally based on estimates.

Notes
+++++++++

- The Seven Days battles is split into two engagements, with Oak Grove on June 25th separate from The
  remaining battles (June 26-July 1).

  - 2279: Oak Grove, Va, VA (1862-6-25 - 1862-6-25)
  - 2280: Seven Day's retreat; includes Mechanicsville, Gaines' Mills, Chickahominy,
    Peach Orchard, Savage Station, Charles City Cross Roads, and Malvern Hill, VA
    (1862-6-26 - 1862-7-1)

-  2283: Guerilla campaign in Missouri; includes with Porter's and Poindexter's Guerillas, MO (1862-7-20 - 1862-9-20).
   This includes Missouri battles MO013, MO014, MO015.
-  The battle of 2nd Manassas (Bull Run) is split into two battles

   - 2284: Groveton and Gainesville, Va, VA (1862-8-28 - 1862-8-29)
   - 2285: Bull Run, Va (2d), VA (1862-8-30 - 1862-8-30)

-  2307: Refers to all of
   [Steight's Raid](http://en.wikipedia.org/wiki/Streight%27s\_Raid). There is only one battle in CWSAC (Day's Gap).
-  2298: Foster's expedition to Goldsboro, N.C., NC (1862-12-12 - 1862-12-18). This includes several CWSAC battles.
-  2311: Siege of Vicksburg, Miss., MS (1863-5-18 - 1863-7-4) includes the whole siege. There are not separate entries for the assaults.
-  2312: Siege of Port Hudson, La., LA (1863-5-27 - 1863-7-9) includes the whole siege. There are not separate entries for the assaults.
-  2323:  Chattanooga, Tenn.; includes Orchard Knob, Lookout Mountain, and Missionary Ridge, TN (1863-11-23 - 1863-11-25). There are not
   separate entries for the engagements within the battle of Chattanooga.

-  2345: "Kenesaw Mountain, Ga.; includes Pine Mountain, Pine Knob, Golgotha,
   Culp's House, general assault, June 27th; McAfee's Cross Roads, Lattemore's
   Mills, and Powder Springs., GA (1864-6-9 - 1864-6-30)". This includes several CWSAC Battles
   including GA013 (Marietta), GA014 (Kolb's Farm), and GA015 (Kenesaw Mountain).
   There is also a separate entry for the assault on Kenesaw Mountaing (2354).

-  2351, 2355, 2366, 2373 all refer to Trenches in front of Petersburg,
   but don't seem to point to any specific battles. Most of the battles
   in the Petersburg Campaign have their own entries.

-  2352: Wilson's raid on the Weldon Railroad, Va., VA (1864-6-22 - 1864-6-30).
   This includes several battles: Staunton River Bridge (VA113; 1864-06-25),
   Sappony Church (VA067; 1864-06-28), Ream's Station I (VA068; 1864-06-29).

-  2354: Kenesaw Mountain, general assault. See No. 2345. This covers the
   assualt on June 27, 1864. The entry 2345 includes this assault as well as
   operations in Marietta and Kolb's Farm.

-  2362: This is NOT `Stoneman's Raid <http://en.wikipedia.org/wiki/Stoneman%27s_Raid>`.
   There appears to be no battle page for this, although it is discussed
   in http://en.wikipedia.org/wiki/George\_Stoneman.

-  2372: Campaign in Northern Georgia, from Chattanooga, Tenn., to Atlanta, Ga., TN (1864-5-5 - 1864-9-8)
   This includes several CWSAC battles, and also overlaps with several other entries in the data.

-  2376: Price's invasion of Missouri; includes a number of engagements This battle is linked
   to all battles in `Price's Missouri Expedition <http://en.wikipedia.org/wiki/Category:Battles_of_Price%27s_Missouri_Expedition_of_the_American_Civil_War>`

-  2395 and 2394: both appear to refer to the Battle of Fort Stedman since it was the major
   action in Petersburg on March 25, 1865.

-  2397: Wilson's raid from Chickasaw, Ala., to Macon, Ga.; includes a number
   of engagements, GA (1865-3-22 - 1865-4-24). However, Selma (AL007) is the only
   major battle in this.


Sources: [Phisterer1883]_


Schema
======



===========  =======  ===========
battle_id    integer  Battle
battle_name  string   Battle name
state        string   state
start_date   date     Start date
end_date     date     End date
surrender    boolean  surrender
campaign     boolean  Campaign
page         integer  Page
===========  =======  ===========

battle_id
---------

:title: Battle
:type: integer
:format: default
:constraints:
    :minimum: 2262
    :maximum: 2410
    

Identifier number of the battle.
These are the numbers used in Phisterer (1883). They start at 2262 because 1-2261 refer to the events in the chronological record (see :doc:`phisterer_engagements`).


       
battle_name
-----------

:title: Battle name
:type: string
:format: default





       
state
-----

:title: state
:type: string
:format: default
:constraints:
    :pattern: [A-Z][A-Z]
    

Two-letter state code for the state of the battle.


       
start_date
----------

:title: Start date
:type: date
:format: default





       
end_date
--------

:title: End date
:type: date
:format: default





       
surrender
---------

:title: surrender
:type: boolean
:format: default


Was the engagement a surrender rather than a battle?
Examples include the surrenders of Johnston, 


       
campaign
--------

:title: Campaign
:type: boolean
:format: default


Was the engagement a campaign rather than a battle?
Phisterer includes entries for the surrenders of Johnston, Taylor, Sam Jones, Jeff Thompson, and Kirby Smith at the end of the war.


       
page
----

:title: Page
:type: integer
:format: default


Page number in Phisterer (1883).


       

