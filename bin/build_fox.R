#!/usr/bin/env Rscript
suppressPackageStartupMessages({
  library("stringr")
  library("dplyr")
})
source("R/misc.R")

toint <- function(x) {
  str_replace_all(x, "[^0-9]", "")
}

na_fill <- function(x, fill = 0) {
  x[is.na(x)] <- fill
  x
}

update_cwsac <- function(x) {
    cwsacids <- str_split(x, "\\s+")[[1]]
    relations <- if (length(x) > 1) "gt" else "eq"
    data_frame(to = cwsacids, relation = relations)
}

build <- function(src, dst) {
  foxdir <- file.path(src, "rawdata", "fox1898")
  fox_forces <- read_csv(file.path(foxdir, "fox_forces.csv")) %>%
    select(belligerent, battle_name, start_date, end_date,
           state, casualties, killed, wounded, missing, aggrow, cwsac_id) %>%
    arrange(belligerent, battle_name)

  fox_forces2 <- read_csv(file.path(foxdir, "fox_forces2.csv")) %>%
    select(belligerent, battle_name, start_date, end_date,
           state, casualties, killed, wounded, missing, cavalry, cwsac_id) %>%
    arrange(belligerent, battle_name)

  fox_forces_to_cwsac <-
    (
      fox_forces
      %>% select(belligerent, battle_name, cwsac_id)
      %>% filter(cwsac_id != "")
      %>% group_by(belligerent, battle_name)
      %>% do(update_cwsac(.$cwsac_id))
      %>% group_by(belligerent, to)
      %>% mutate(relation = ifelse(relation == "eq" & n() > 1, "lt", relation))
      )

  fox_forces2_to_cwsac <-
    (
      fox_forces2
      %>% select(belligerent, battle_name, cwsac_id)
      %>% filter(cwsac_id != "")
      %>% group_by(belligerent, battle_name)
      %>% do(update_cwsac(.$cwsac_id))
      %>% mutate(relation = ifelse(relation == "eq" & n() > 1, "lt", relation))
    )
  write_csv(fox_forces %>% select(- cwsac_id), file = file.path(dst, "fox_forces.csv"))
  write_csv(fox_forces2 %>% select(- cwsac_id), file = file.path(dst, "fox_forces2.csv"))
  write_csv(fox_forces_to_cwsac, file = file.path(dst, "fox_forces_to_cwsac.csv"))
  write_csv(fox_forces2_to_cwsac, file = file.path(dst, "fox_forces2_to_cwsac.csv"))
}

copyfiles <- function(src, dst) {
  for (fn in c("fox_outcomes.csv")) {
    file.copy(file.path(src, "rawdata", "fox1898", fn), dst)
  }
}

main <- function() {
  arglist <- commandArgs(TRUE)
  src <- arglist[1]
  dst <- arglist[2]
  build(src, dst)
  copyfiles(src, dst)
}

main()
