Fox (1898) battle casualties (revised)
================================================================================

:name: fox_forces2
:path: data/fox_forces2.csv
:format: csv

Data from William F. Fox *Regimental Losses in the American Civil War,
1861-1865: A Treatise on the extent and nature of the mortuary losses in
the Union regiments, with full and exhaustive statistics compiled from
the official records on file in the state military bureaus and at
Washington*, available from `Perseus <http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A2001.05.0068>`__.
The unit of observation is the force (battle, belligerent), because the reporting of casualties for durations and locations differs between the Union and Confederate forces.

This data is similar to :doc:`fox_forces`, but differs in some revisions, which largely come from the notes in the souce table.

-  removed aggregate rows for Union casualties in Atlanta Campaign and
   Seven Day's Battle
-  fn 8. Split Chancellorsville into casualties for Chancellorsville
   (VA032) and VA033 VA034
-  fn 24. Split Chattanooga into Orchard's Knob on 11/23, Lookout
   Mountain on 11/24 and Missionary Ridge on 11/25. The footnote only
   gives total casualties for 11/23 and 11/24, so I assume a constant
   proportion of K/W/M for all days.
-  fn 25. Split Atlanta Campaign into the components in the footnote.
   Remainder is assigned to "Lattimore's Mill; Powder Springs, etc".
-  fn 27. Split Atlanta Campaign into the components in the footnote.
   It's unclear which entries to assign to the Marietta Operations.
-  fn 28. Split Atlanta campaign into the components in the footnote.
   Remainder assigned to the Siege of Atlanta. I'm not sure what the
   Siege of Atlanta refers to so I assign it to the Jonesboro (GA020)
   and Lovejoy Station (GA021)
-  fn 29. The note says Jonesboro and Lovejoy Station, but Jonesboro
   happened on Aug 20, so it cannot be included in this row.
-  fn 70. Split Seven Days Battle into the component battles.
-  fn 74. Added the 90 casualties from White's battalion.

Fox lists alternate casualty figures for Confederates at Gettysburg that
I don't use.

The records on file at Washington bear the names of 6,802 wounded, and
5,425 unwounded Confederates captured at Gettysburg. The official
reports of Longstreet, Ewell, Hill, and Stuart indicate a loss (after
making necessary deductions) of 2,701 killed, 12,739 wounded, 7,528
missing; total, 22,968.

See :doc:`fox_forces` for more detail on the Fox data.



Schema
-------

:Primary Key:['belligerent', 'battle_name']



belligerent
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:label: 
:type: string
:format: default 

    
    
    
    
    
    
    
    :enum: ['Confederate', 'US']      



       

battle_name
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:label: 
:type: string
:format: default 



       

start_date
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:label: 
:type: date
:format: default 


Start date of the battle
       

end_date
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:label: 
:type: date
:format: default 


End date of the battle
       

state
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:label: 
:type: string
:format: default 

    
    :minLength: 2 
    :maxLength: 2 
    
    :pattern: [A-Z]{2} 
    
    
         


State in which the battle took place.
       

casualties
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:label: 
:type: integer
:format: default 


Number of casualties (killed, wounded, and missing)
       

killed
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:label: 
:type: integer
:format: default 


Number killed
       

wounded
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:label: 
:type: integer
:format: default 


Number wounded
       

missing
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:label: 
:type: integer
:format: default 


Number missing
       

cavalry
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:label: 
:type: boolean
:format: default 


Was this a cavalry battle?
       

