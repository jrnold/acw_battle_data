library("dplyr")
library("readr")
library("purrr")

battles <- read_csv("data/nps_battles.csv")
locations <- read_csv("data/cws2_locations.csv") %>%
  group_by(battle) %>%
  do({
    data_frame(state = list(.$state),
               location = paste(.$location, .$state,
                                sep = ", ", collapse = ";"))
  })

dyer <- read_csv("data/dyer_engagements.csv") %>%
  mutate(start_date = as.Date(start_date),
         end_date = as.Date(end_date))

find_matches <- function(x) {
  is_match <- (dyer[["start_date"]] <= x$end_date &
                 dyer[["end_date"]] >= x$start_date &
                 dyer[["state"]] %in% x$state)

  dyer[!is.na(is_match) & is_match, "battle", drop = FALSE]
}

matches <-
  battles %>%
    select(cwsac_id, battle_name, other_names, start_date, end_date) %>%
    left_join(locations, by = c("cwsac_id" = "battle")) %>%
    mutate(start_date = as.Date(start_date),
           end_date = as.Date(end_date)) %>%
    group_by(cwsac_id) %>%
    do(find_matches(.))

write_csv(matches, path = "dyer_cwsac_potential_matches.csv", na = "")


