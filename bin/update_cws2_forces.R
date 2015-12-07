#!/usr/bin/env Rscript
source("R/misc.R")

gen_forces <- function(dst) {
  read_csv(file.path(dst, "cws2_forces.csv"))
}

gen_unit_sizes <- function(dst) {
  read_csv(file.path(dst, "unit_sizes.csv"))
}

gen_unit_size_values <- function(dst) {
  unit_sizes <- gen_unit_sizes(dst)

  unit_sizes %>%
    select(belligerent, unit_type, mean, sd) %>%
    mutate(var = sd ^ 2) %>%
    select( - sd) %>%
    mutate(belligerent = plyr::revalue(belligerent, c("Union" = "US")))
}

unit_type_map <- c(
  "regiments" = "infantry regiment",
  "companies" = "infantry company",
  "brigades" = "infantry brigade",
  "divisions"= "infantry division",
  "corps" = "infantry corps",
  "armies" = "army",
  "cavalry_regiments" = "cavalry regiment",
  "cavalry_brigades" = "cavalry brigade",
  "cavalry_divisions" = "cavalry division",
  "cavalry_corps" = "cavalry corps",
  "cavalry_companies" = "cavalry company",
  "artillery_batteries" = "artillery battery",
  "artillery_companies" = "artillery company",
  "artillery_regiments" = "artillery regiment",
  "artillery_sections" = "artillery section",
  "infantry_regiments" = "infantry regiment"
)

update_forces <- function(src, dst) {
  forces <- gen_forces(dst)
  unit_size_values <- gen_unit_size_values(dst)
  forces_strengths_units <-
    forces %>%
    select(battle, belligerent,
           armies, corps, divisions, brigades, regiments, companies,
           matches("cavalry_"),
           matches("artillery_")) %>%
    gather(unit_type, units, - battle, - belligerent, na.rm = TRUE) %>%
    mutate(unit_type =
             as.character(plyr::revalue(unit_type, unit_type_map,
                                        warn_missing = FALSE))) %>%
    left_join(unit_size_values, by = c("unit_type", "belligerent")) %>%
    mutate(str_units_mean = units * mean,
           str_units_var = units ^ 2 * var) %>%
    group_by(battle, belligerent) %>%
    summarise_each(funs(sum), matches("str_units_(mean|var)"))

  forces_strengths_exact <-
    forces %>%
    select(battle, belligerent, strength, strength_other) %>%
    mutate(str_var = psum(rounded_var(strength), rounded_var(strength_other)),
           str_mean = psum(strength, strength_other)) %>%
    select(battle, belligerent, str_mean, str_var)

  forces_strengths <-
    left_join(forces_strengths_exact, forces_strengths_units,
              by = c("battle", "belligerent")) %>%
    mutate(strength_mean = psum(str_mean, str_units_mean),
           strength_var = psum(str_var, str_units_var)) %>%
    select(battle, belligerent, strength_mean, strength_var)

  forces2 <-
    left_join(forces, forces_strengths,
              by = c("battle", "belligerent"))

  battles_strengths <-
    forces_strengths %>%
    group_by(battle) %>%
    summarise(strength_mean = sum(strength_mean),
              strength_var = sum(strength_var))

  battles <-
    read_csv(file.path(dst, "cws2_battles.csv")) %>%
    left_join(battles_strengths, by = "battle") %>%
    mutate(strength_mean = pnonmiss(strength_mean, strength),
           strength_var = pnonmiss(strength_var, rounded_var(strength)))

  write_csv(forces2,
            file = file.path(dst, "cws2_forces.csv"))
  write_csv(battles,
            file = file.path(dst, "cws2_battles.csv"))
}

main <- function() {
  args <- commandArgs(TRUE)
  src <- args[1]
  dst <- args[2]
  update_forces(src, dst)
}

main()

