#' ---
#' title: test Fox forces data
#' ---
library("tidyverse")
library("stringr")
library("assertthat")
library("jsonlite")

fox_forces <- read_csv("data/fox_forces.csv") %>%
  mutate(start_date = as.Date(start_date),
         end_date = as.Date(end_date)) %>%
  select(battle_id, battle_name, start_date, end_date, state)

nps <- read_csv("data/nps_battles.csv") %>%
  mutate(start_date = as.Date(start_date),
         end_date = as.Date(end_date)) %>%
  select(cwsac_name = battle_name,
         cwsac_id,
         cwsac_state = state,
         cwsac_start = start_date,
         cwsac_end = end_date)

fox_forces_to_cwsac <- read_json("data/fox_forces_to_cwsac.json") %>%
  map_df(~ cross_df(list(battle_id = .x$battles_from,
                         cwsac_id = .x$battles_to))) %>%
  left_join(nps, by = "cwsac_id") %>%
  left_join(fox_forces, by = "battle_id")

# Check that mappings have the same state
filter(fox_forces_to_cwsac, state != cwsac_state) %>%
  select(battle_id, cwsac_id, cwsac_state, state) %>%
  print(n = 100)

# Check dates of mappings
filter(fox_forces_to_cwsac,
       start_date > cwsac_end | end_date < cwsac_start) %>%
  select(battle_id, cwsac_id, cwsac_start, cwsac_end, start_date, end_date) %>%
  print(n = 100)
