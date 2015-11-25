# navalbattles.csv

List of battles in

- `cwsac_id`: CWSAC ID of the battle
- `battle_name`: Name of the battle. For redundancy.
- `all_naval`: If 1, then the battle did not involve (or had very little involvement) of any land forces on one side. E.g. ship vs. ship battles (Hampton Roads) or ship vs. fort battles (e.g. Fort McAllister).
- `comments`: A short description of the fighting.

This is incomplete. The open question is: what is considered a significant naval contribution.

# battlemisc.csv

Miscellaneous variables for each CWSAC battle coded by ``jrnold``

- `attacker`. Side that initiated combat.
- `surrender`. Did one side surrender? Categorized into partial and complete.
- ``battle_name_short``. A shorter battle name useful for plots and tables.
- ``lat``. Latitude. Coded by hand from the maps in the CWSAC revised reports.
- ``long``. Longitude.

# war_trend_burdekin_langdana.csv

Burdekin, Langdana, "War Finance in the Confederacy", **, (p. 367) uses a war categorical variable for the trend of th war.
It is defined as 0 everywhere except

- +1 for 1863Q3: victory of Chancelorsville aand advance of Lee's army into Maryland and Pennsylvania
- -1 for 1862Q2: Richmond threatened by McClellan during the Peninsular campaign
- -1 for 1863Q4 and 1864Q1: Aftermath of Gettysburg and Vicksburg

The variable was defineid based on Schwab (1901), descriptions of "crises of confidence".
The dummy is set to 0 in 1864Q2 and 1864Q3 because the Northern offensive stalls at the start of the year, and the the northern Democratic party's nomination of McClellan.

date

:    date. Data are quarterly.

war

:    -1 (+1) if war news is unfavorable (favorable) to Confederacy; 0 otherwise.

# war_trend_reiter.csv

Chapter 8 of Dan Reiter (2009) *How Wars End* discusses 5 turning points in the American Civil War.
Four of these turning points are based off of the list by James McPherson; the fifth is the end of the war.

period

:    Time-period of the turning point

description

:    Brief description of the turning point

start_date

:    Date of the turning point (start date of the new period).

comment

:    Comments

favor

:    Which side the turning point favors: Union or Confederate

war_aims_change:

:    Did either side change war aims in the following period?







