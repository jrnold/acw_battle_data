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
