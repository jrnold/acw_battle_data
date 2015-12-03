#!/usr/bin/env Rscript
source("R/misc.R")

unit_type_map <- c(
  "corps" = "infantry corps",
  "cavalry_corps" = "cavalry corps",
  "divisions" = "infantry division",
  "cavalry_divisions" = "cavalry division",
  "brigades" = "infantry brigade",
  "companies" = "infantry company"
)

update_forces <- function(src, dst) {

  forces <- read_csv(file.path(dst, "clodfelter_forces.csv"))
  unit_sizes <- read_csv(file.path(dst, "unit_sizes.csv"))

  unit_size_values <-
    unit_sizes %>%
    select(belligerent, unit_type, mean, sd) %>%
    mutate(var = sd ^ 2) %>%
    select( - sd) %>%
    mutate(belligerent = plyr::revalue(belligerent, c("Union" = "US")))

  forces_strengths_units <-
    forces %>%
    select(battle, belligerent,
           corps, cavalry_corps, divisions, cavalry_divisions, brigades,
           companies) %>%
    gather(unit_type, units, - battle, - belligerent, na.rm = TRUE) %>%
    mutate(unit_type =
             as.character(plyr::revalue(unit_type, unit_type_map,
                                        warn_missing = FALSE))) %>%
    left_join(unit_size_values, by = c("unit_type", "belligerent")) %>%
    mutate(str_mean_units = units * mean,
           str_var_units = units ^ 2 * var) %>%
    group_by(battle, belligerent) %>%
    summarise_each(funs(sum), matches("str_(mean|var)_units"))

  forces_strengths_num <-
    forces %>%
    select(battle, belligerent,
           strength, cavalry, infantry, crewmen
    ) %>%
    mutate(strength_var = rounded_var(strength),
           cavalry_var = rounded_var(cavalry),
           infantry_var = rounded_var(infantry),
           crewmen_var = rounded_var(crewmen),
           str_mean_num = psum(strength, cavalry, infantry, crewmen),
           str_var_num = psum(strength_var, cavalry_var, infantry_var,
                              crewmen_var)) %>%
    select(battle, belligerent, str_var_num, str_mean_num)

  forces_strengths <-
    left_join(forces_strengths_num, forces_strengths_units,
              by = c("battle", "belligerent")) %>%
    mutate(str_mean = psum(str_mean_num, str_mean_units),
           str_var = psum(str_var_num, str_var_units)) %>%
    select(battle, belligerent, str_mean, str_var)

  forces2 <-
    left_join(forces, forces_strengths,
              by = c("battle", "belligerent")) %>%
    arrange(battle, belligerent)
  write_csv(forces2,
            file = file.path(dst, "clodfelter_forces.csv"))
}

update_battles <- function(src, dst) {
  clodfelter_to_cwsac <- read_csv(file.path(dst, "clodfelter_to_cwsac.csv"))
  clodfelter_battles <- read_csv(file.path(dst, "clodfelter_battles.csv"))
  nps_battles <- read_csv(file.path(dst, "nps_battles.csv"))
  results <- read_csv(file.path(src, "rawdata", "clodfelter2008",
                                "results.csv")) %>%
    select(battle, result2)

  clodfelter_results <-
    clodfelter_to_cwsac %>%
    filter(relation == "=") %>%
    rename(cwsac_id = to, battle = from) %>%
    select(- relation) %>%
    left_join(nps_battles %>% select(cwsac_id, result),
              by = "cwsac_id") %>%
    left_join(results, by = "battle") %>%
    mutate(result = pnonmiss(result2, result)) %>%
    select(battle, result)

  battles <-
    left_join(clodfelter_battles, clodfelter_results,
              by = "battle") %>%
    arrange(battle)

  write_csv(battles, file.path(dst, "clodfelter_battles.csv"))

}

update_commanders <- function(src, dst) {
  clodfelter_to_cwsac <- read_csv(file.path(dst, "clodfelter_to_cwsac.csv"))
  clodfelter_battles <- read_csv(file.path(dst, "clodfelter_battles.csv"))
  nps_commanders <- read_csv(file.path(dst, "nps_commanders.csv"))
  commanders <- read_csv(file.path(src, "rawdata", "clodfelter2008",
                                "commanders.csv")) %>%
    select(battle, belligerent, PersonID, last_name, first_name, middle_name,
           middle_initial, rank, navy)

  clodfelter_commanders <-
    clodfelter_to_cwsac %>%
    filter(relation == "=") %>%
    rename(cwsac_id = to, battle = from) %>%
    select(- relation) %>%
    left_join(nps_commanders,
              by = "cwsac_id") %>%
    bind_rows(commanders)

  write_csv(clodfelter_commanders,
            file.path(dst, "clodfelter_commanders.csv"))

}

main <- function() {
  args <- commandArgs(TRUE)
  src <- args[1]
  dst <- args[2]
  update_forces(src, dst)
  update_battles(src, dst)
  update_commanders(src, dst)
}

main()

