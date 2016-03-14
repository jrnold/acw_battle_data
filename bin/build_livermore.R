#!/usr/bin/env Rscript
source("R/misc.R")

COPYFILES = c("livermore_army_sizes.csv")

BELLIGERENTS <- c(UNION = "Union",
                  CONFEDERATE = "Confederate")

build <- function(src, dst) {
  LIV_BATTLES_FILE <- file.path(src, "rawdata", "livermore1900",
                                "livermore.csv")

  livrmore <- read_csv(LIV_BATTLES_FILE)

  liv_battles <-
    livrmore %>%
    select(- matches("^(US|CS)_"), - matches("^commander_")) %>%
    arrange(battle_id)

  liv_commanders <-
    read_csv(file.path(src, "rawdata", "livermore1900",
                       "livermore_commanders.csv")) %>%
    select(battle_id, belligerent, PersonID, last_name, first_name, middle_name,
           middle_initial, rank, navy)

  liv_forces <-
    livrmore %>%
    select(battle_id, matches("^(US|CS)_")) %>%
    gather(variable, value, - battle_id) %>%
    separate(variable, c("belligerent", "varname")) %>%
    mutate(belligerent = plyr::revalue(belligerent,
                                       c("US" = "Union",
                                         "CS" = "Confederate"))) %>%
    spread(varname, value) %>%
    select(battle_id, belligerent, str, kia, wia, kw, miapow) %>%
    mutate(wia = ifelse(is.na(kia) & ! is.na(wia) & ! is.na(kw), NA, wia))

  write_csv(liv_battles, file = file.path(dst, "livermore_battles.csv"))
  write_csv(liv_forces, file = file.path(dst, "livermore_forces.csv"))
  write_csv(liv_commanders, file = file.path(dst, "livermore_commanders.csv"))

  for (filename in COPYFILES) {
    file.copy(file.path(src, "rawdata" , "livermore1900", filename), dst)
  }

}

main <- function() {
  arglist <- commandArgs(TRUE)
  src <- arglist[1]
  dst <- arglist[2]
  build(src, dst)
}

main()
