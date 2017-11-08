library("tidyverse")
library("assertthat")
library("yaml")

dyer <- read_csv("../acw_battle_data/rawdata/dyer1908/engagements.csv")

# Read some constants
dyer_constants <- yaml.load_file("../acw_battle_data/rawdata/dyer1908/misc.yaml")

MIN_DATE <- as.Date("1860-12-20")
MAX_DATE <- as.Date("1865-12-05")
MAX_DURATION <- 333

# Battle IDs
assert_that(is_integerish(dyer$battle_id))
assert_that(all(!is.na(dyer$battle_id)))
# 1 ... n IDs are all there
assert_that(all(seq_len(nrow(dyer)) %in% dyer$battle_id))

# State
assert_that(is_character(dyer$state))
assert_that(all(!is.na(dyer$state)))
valid_state_values <- map_chr(dyer_constants$states, "abbrev")
assert_that(!nrow(filter(dyer, !state %in% UQ(valid_state_values))))

# Event Types
assert_that(is_character(dyer$event_type))
assert_that(all(!is.na(dyer$event_type)))
valid_event_types <- dyer_constants$event_types
assert_that(!nrow(filter(dyer, !event_type %in% UQ(valid_event_types))))

# Start dates
assert_that(!all(is.na(dyer$start_date)))
# in plausible range - there is redundancy here
assert_that(all(dyer$start_date >= MIN_DATE))
assert_that(all(dyer$start_date < MAX_DATE))

# End dates - all are non-missing
assert_that(all(!is.na(dyer$end_date)))
# less than end of war
assert_that(all(dyer$end_date >= MIN_DATE))
assert_that(all(dyer$end_date < MAX_DATE))
assert_that(all(dyer$end_date >= dyer$start_date))
assert_that(!nrow(filter(dyer,
                         as.integer(end_date - start_date) > MAX_DURATION)))

# Battle Name
assert_that(is.character(dyer$battle_name))
assert_that(all(!is.na(dyer$battle_name)))
assert_that(all(str_length(dyer$battle_name) > 0))

# text
assert_that(is.character(dyer$text))

# Casualty variables
# maximum killed in the data
KILLED_MAX <- 7621
assert_that(is_integerish(dyer$killed))
assert_that(min(dyer$killed, na.rm = TRUE) >= 0)
assert_that(max(dyer$killed, na.rm = TRUE) <= KILLED_MAX)

# maximum wounded in data
# Wounded value is so high due to "May 4-June 12: Campaign from the Rapidan River to the James River"
WOUNDED_MAX <- 38339
assert_that(is_integerish(dyer$wounded))
assert_that(min(dyer$wounded, na.rm = TRUE) >= 0)
assert_that(min(dyer$wounded, na.rm = TRUE) <= WOUNDED_MAX)

# Missing and captured
MISS_MAX <- 12520
assert_that(is_integerish(dyer$missing_captured))
assert_that(min(dyer$missing_captured, na.rm = TRUE) >= 0)
assert_that(max(dyer$missing_captured, na.rm = TRUE) <= MISS_MAX)

# Killed wounded
KW_MAX <- 45960
assert_that(is_integerish(dyer$killed_wounded))
assert_that(min(dyer$killed_wounded, na.rm = TRUE) >= 0)
assert_that(max(dyer$killed_wounded, na.rm = TRUE) <= KW_MAX)
assert_that(nrow(filter(dyer, !is.na(killed) & !is.na(wounded) &
                          (killed + wounded) != killed_wounded)) == 0)

# Total
CAS_MAX <- 54926
assert_that(is_integerish(dyer$casualties))
assert_that(min(dyer$casualties, na.rm = TRUE) >= 0)
assert_that(max(dyer$casualties, na.rm = TRUE) <= CAS_MAX)

