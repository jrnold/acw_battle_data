#'
#' Clean the data in PAR/data/LIVRMORE.csv and split it into
#' battle and force tables
#'
library("dplyr")
library("stringr")
library("readr")

read_csv <- function(x, ...) {
  tbl_df(read.csv(x, ..., stringsAsFactors = FALSE,
                  check.names = FALSE))
}

write_csv <- function(x, ...) {
  write.csv(x, ..., na = "", row.names = FALSE)
}

LIV_BATTLES_FILE <- "../../dependencies/PAR/data/LIVRMORE.csv"
LIV_BATTLES_MISC <- "./misc.csv"
livrmore <- read_csv(LIV_BATTLES_FILE) %>%
  mutate(belligerent = plyr::revalue(belligerent,
                                     UNION = "Union",
                                     CONFEDERATE = "Confederate"))
battle_misc <- read_csv(LIV_BATTLES_MISC, na = "")

liv_battles <-
  (livrmore
    %>% select(seq_no, battle_name, start_date, end_date, win_side)
    %>% arrange(seq_no)
    %>% left_join(select(battle_misc, - battle_name, - win_side, - start_date, - end_date,
                         - commander_union, - commander_confederate),
                  by = "seq_no")
  )

liv_commanders <-
  battle_misc %>%
  group_by(seq_no) %>%
  do({
    bind_rows(data_frame(commander = str_split(str_trim(.$commander_union), " +")[[1]],
                        belligerent = "Union"),
              data_frame(commander = str_split(str_trim(.$commander_confederate), " +")[[1]],
                         belligerent = "Confederate"))
  }) %>%
  select(seq_no, belligerent, commander)

strcas_vars <- c("str", "kia")
attacker_vars <- str_c("attacker_", strcas_vars)
attacker_vars <- str_c("defender_", strcas_vars)

union_attacker <-
  (livrmore
   %>% filter(attacker == "Union")
  )
union_attacking_forces <-
  (union_attacker
   %>% select(seq_no, starts_with("attacker_"))
   %>% mutate(belligerent = "Union", attacker = TRUE))
names(union_attacking_forces) <-
  gsub("attacker_", "", names(union_attacking_forces))

confed_defending_forces <-
  (union_attacker
   %>% select(seq_no, starts_with("defender_"))
   %>% mutate(belligerent = "Confederate", attacker = FALSE)
  )
names(confed_defending_forces) <-
  gsub("defender_", "", names(confed_defending_forces))

confed_attacker <-
  (livrmore
   %>% filter(attacker == "Confederate")
  )
confed_attacking_forces <-
  (confed_attacker
   %>% select(seq_no, starts_with("attacker_"))
   %>% mutate(belligerent = "Confederate", attacker = TRUE))
names(confed_attacking_forces) <-
  gsub("attacker_", "", names(confed_attacking_forces))

union_defending_forces <-
  (confed_attacker
   %>% select(seq_no, starts_with("defender_"))
   %>% mutate(belligerent = "Union", attacker = FALSE)
  )
names(union_defending_forces) <-
  gsub("defender_", "", names(union_defending_forces))

liv_forces <-
  (rbind(union_attacking_forces, confed_defending_forces,
         confed_attacking_forces, union_defending_forces)
   %>% arrange(seq_no, belligerent)
   # if KIA is missing, WIA is non-missing, but KWIA is non-missing,
   # then WIA should be missing
   %>% mutate(wia = ifelse(is.na(kia) & ! is.na(wia) & ! is.na(kw), NA, wia)))



write_csv(liv_battles, file = "liv_battles.csv")
write_csv(liv_forces, file = "liv_forces.csv")
write_csv(liv_forces, file = "liv_commanders.csv")
