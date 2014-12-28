#'
#' Clean the data in PAR/data/LIVRMORE.csv and split it into
#' battle and force tables
#'
library("dplyr")
library("stringr")

read_csv <- function(x, ...) {
  tbl_df(read.csv(x, ..., stringsAsFactors = FALSE,
                  check.names = FALSE))
}

write_csv <- function(x, ...) {
  write.csv(x, ..., na = "", row.names = FALSE)
}

LIV_BATTLES_FILE <- "../PAR/data/LIVRMORE.csv"
livrmore<- read_csv(LIV_BATTLES_FILE)

liv_battles <-
  (livrmore
   %>% select(seq_no, battle_name, start_date, end_date, win_side)
   %>% arrange(seq_no))

strcas_vars <- c("str", "kia")
attacker_vars <- str_c("attacker_", strcas_vars)
attacker_vars <- str_c("defender_", strcas_vars)
  
union_attacker <- 
  (livrmore
   %>% filter(attacker == "UNION")
  )
union_attacking_forces <-
  (union_attacker
   %>% select(seq_no, starts_with("attacker_"))
   %>% mutate(belligerent = "UNION", attacker = TRUE))
names(union_attacking_forces) <-
  gsub("attacker_", "", names(union_attacking_forces))

confed_defending_forces <-
  (union_attacker
   %>% select(seq_no, starts_with("defender_"))
   %>% mutate(belligerent = "CONFEDERATE", attacker = FALSE)
  )
names(confed_defending_forces) <-
  gsub("defender_", "", names(confed_defending_forces))

confed_attacker <- 
  (livrmore
   %>% filter(attacker == "CONFEDERATE")
  )
confed_attacking_forces <-
  (confed_attacker
   %>% select(seq_no, starts_with("attacker_"))
   %>% mutate(belligerent = "CONFEDERATE", attacker = TRUE))
names(confed_attacking_forces) <-
  gsub("attacker_", "", names(confed_attacking_forces))

union_defending_forces <-
  (confed_attacker
   %>% select(seq_no, starts_with("defender_"))
   %>% mutate(belligerent = "UNION", attacker = FALSE)
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

write_csv(liv_battles, file = "LIVRMORE_battles.csv")
write_csv(liv_forces, file = "LIVRMORE_forces.csv")
