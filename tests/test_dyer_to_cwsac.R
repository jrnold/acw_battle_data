library("tidyverse")
library("assertthat")
library("jsonlite")

dyer_to_cwsac <- read_json("../acw_battle_data/data/dyer_to_cwsac.json") %>%
  map_df(~ cross_df(list(cwsac_id = .x$battles_cwsac,
                         battle_id = .x$battles_from)))

dyer <- read_csv("../acw_battle_data/data/dyer_engagements.csv") %>%
  select(battle_id,
         battle_name,
         state,
         start_date,
         end_date)
nps <- read_csv("../acw_battle_data/data/nps_battles.csv") %>%
  select(cwsac_id, cwsac_name = battle_name, cwsac_state = state,
         cwsac_start = start_date, cwsac_end = end_date) %>%
  mutate(cwsac_state = case_when(
    cwsac_state == "ID" ~ "UT",
    cwsac_state == "ND" ~ "DT",
    TRUE ~ cwsac_state
  ))

dyer_to_cwsac <- dyer_to_cwsac %>%
  left_join(dyer, by = "battle_id") %>%
  left_join(nps, by = "cwsac_id")

# States should match
filter(dyer_to_cwsac, cwsac_state != state) %>%
  select(battle_id, cwsac_id, cwsac_state, state, battle_name, cwsac_name)

# Dates should overlap
filter(dyer_to_cwsac,
       (cwsac_end < start_date) | (cwsac_start > end_date)) %>%
  select(battle_id, cwsac_id, battle_name, cwsac_name,
         cwsac_start, cwsac_end, start_date, end_date) %>%
  print(width = 1000)
