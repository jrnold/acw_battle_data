Some miscellaneous datasets coded by jrnold

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
