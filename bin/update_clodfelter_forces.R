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
              by = c("battle", "belligerent"))
  write_csv(forces2,
            file = file.path(dst, "clodfelter_forces.csv"))
}

main <- function() {
  args <- commandArgs(TRUE)
  src <- args[1]
  dst <- args[2]
  update_forces(src, dst)
}

main()

