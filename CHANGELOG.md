# 9.1.0 (2017-10)

## Internal

- moved battlemisc data into separate YAML files to make it easier to extend that data.

# 4.0.0 (2017-10-24)

## Breaking

- rename `cwss_unittitles.csv` to `cwss_unit_titles.csv`

## Bug fixes

- `fox_forces.csv`: remove decimal points from integer columns
- `wikipedia_forces.csv`: fix accidental "NA" in `strength_min` and `strength_max` columns.
- `cwss_state_names.csv`: remove excess whitespace from `abbr` column
- `nps_battles.csv`: remove scientific notation in `strengths` column
- `nps_forces.csv`: remove scientific notation in `strengths_mean` column

# 4.0.1 (2017-10-25)

## Bug fixes

- `nps_forces.csv`, `nps_battles.csv`: fix incorrect cases in which casualties were greater than strengths. This included GA028, MO014, MO017, TN006, TN015.
- Remove exponential notation for large round strength and casualty figures in csv files.


# 5.0.0 (2017-10-30)

## Changes

- `nps_battles.csv`: Both CWSS and AAD sources provide battle types, but AAD is
    is more complete, to only include it.

    - removed column `battle_type_cwss`
    - renamed column `battle_type_aad` to `battle_type`

# 5.0.1 (2017-10-31)

## Bug fixes

- In CWSAC data, change value of strength for AR002 from 50 to missing.

# 6.0.0 (2017-10-31)

## Bug fixes

- `fox_forces_to_cwsac.json`: Fix incorrect match of U51 to MS002.
- Kennedy (1997): changed ID for Samaria Church from VA112 to VA066 to consistent with
    the CWSAC.
- `kennedy1997_forces`:

    - remove `aggregate` column
    - remove `battles_aggregated` column
    - `battle_id` column can contain one or more space-separated IDs

- removed `kennedy1997_forces_to_cwsac`: this was no longer necessary since CWSAC IDs
    are included in the forces table.

# 6.0.1 (2017-11-01)

## Bug fixes

- `aad_battles.csv`, `aad_events.csv`, `nps_battles`: Remove duplicate VA125 record

# 6.0.2 (2017-11-02)

## Bug fixes

- `wikipedia.org`: Fix casualty values for
- `data-raw/fox1898/fox_forces.csv`: Remove total missing and total casualty values for U63.
    Although the Confederate entry for Port Hudson includes values from May-July, it does
    not include the values of the captured.
- `data/nps_forces.csv`: Change GA001 CS casualties to 364. It was previously a 1, which
    was the US casualties.
- `data/cwss_forces.csv`: Change GA001 CS casualties to 364
- `data/kennedy1997_forces.csv`:

  - Change GA001 CS casualties to 364
  - Change MO012 CS killed/wounded from 0 to missing. Kennedy only gives the number of
      of Confederates captured, which does not imply no killed or wounded.

- `data/civilwar.org_forces`:

  - Change Confederate casualties and strength to 230 for "fort-mcallister"

# 6.0.3 (2017-11-03)

## Bug Fixes

- `data/clodfelter_to_cwsac.json`

  - Correct mapping of "Drewry's Bluff (1862-05-15-1862-05-15)" to VA053

- `data/fox_forces.csv`

  - Remove imputed killed/wounded/missing values from the observations
    formed from comments giving rough disaggregations of the casualties
    for aggregated observations.

- `data/cwss_campaigns.csv` and `data/nps_campaigns.csv`: Fix typos and truncated campaign names.
- `data/nps_*`: Remove VA030 (Suffolk: Norfleet House). Treat VA031 as including
    the entire Siege of Suffolk.
- Miscellaneous edits

# 6.0.4 (2017-11-04)

## Bug Fixes

- `data/phisterer_forces.csv`: Set 0 values of killed/wounded/missing to missing values.
