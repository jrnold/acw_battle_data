#' ---
#' title: test Fox forces data
#' ---
library("tidyverse")
library("stringr")
library("assertthat")

fox_forces <- read_csv("data/fox_forces.csv") %>%
  mutate(start_date = as.Date(start_date),
         end_date = as.Date(end_date))

# Check validity of IDs
assert_that(length(unique(fox_forces$battle_id)) == nrow(fox_forces))
assert_that(all(str_detect(fox_forces$battle_id, "[UC]\\d+[A-Z]?")))

# belligerents
BELLIGERENTS <- c("US", "Confederate")
assert_that(all(!is.na(fox_forces$belligerent)))
assert_that(all(fox_forces$belligerent %in% BELLIGERENTS))

# states
STATES <- c("AR", "DC", "FL", "GA", "KY", "LA", "MD", "MO",
            "MS", "NC", "PA", "SC", "TN", "VA", "WV")
assert_that(all(!is.na(fox_forces$state)))
assert_that(all(fox_forces$state %in% STATES))

# battle names
assert_that(all(!is.na(fox_forces$battle_name)))
assert_that(is.character(fox_forces$battle_name))

# dates
MIN_DATE <- as.Date("1861-04-10")
MAX_DATE <- as.Date("1865-04-17")
MAX_DURATION <- 119
assert_that(all(!is.na(fox_forces$start_date)))
assert_that(all(!is.na(fox_forces$end_date)))
assert_that(!nrow(filter(fox_forces, start_date < MIN_DATE)))
# assert_that(!nrow(filter(fox_forces, end_date > MAX_DATE)))
assert_that(!nrow(filter(fox_forces, end_date < start_date)))
# longest entry is 119 days (Atlanta Campaign)
assert_that(!nrow(filter(fox_forces,
                         as.integer(end_date - start_date)
                         <= UQ(MAX_DURATION))))

# killed
MAX_KILLED <- 4423
assert_that(min(fox_forces$killed, nr.rm = TRUE) >= 0)
assert_that(max(fox_forces$killed, na.rm = TRUE) <= MAX_KILLED)

# wounded
# Number wounded is so large because of the Atlanta Campaign
MAX_WOUNDED <- 22822
assert_that(min(fox_forces$wounded, nr.rm = TRUE) >= 0)
assert_that(max(fox_forces$wounded, na.rm = TRUE) <= MAX_WOUNDED)

# killed
MAX_MISSING <- 13829
assert_that(min(fox_forces$missing, na.rm = TRUE) >= 0)
assert_that(max(fox_forces$missing, na.rm = TRUE) <= MAX_MISSING)

# total casualties
MAX_CASUALTIES <- 31687
assert_that(min(fox_forces$casualties, nr.rm = TRUE) >= 0)
assert_that(max(fox_forces$casualties, na.rm = TRUE)
            <= MAX_CASUALTIES)
