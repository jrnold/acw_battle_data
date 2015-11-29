#!/usr/bin/env Rscript
source("R/misc.R")

ROUND_METHOD <- 3

src <- "rawdata"
dst <- "data"

gen_forces <- function(dst) {
  read_csv(file.path(dst, "cwsac_forces.csv"))
}

gen_unit_sizes <- function(dst) {
  read_csv(file.path(dst, "unit_sizes.csv"))
}

gen_unit_size_values <- function(dst) {
  unit_sizes <- gen_unit_sizes(dst)

  unit_size_values_ <-
    expand.grid(belligerent = c("US", "Confederate"),
                unit_type = c("strength_other"))
  unit_size_values_$mean <- 1
  unit_size_values_$var <- 1/12

  unit_sizes %>%
    select(belligerent, unit_type, mean, sd) %>%
    mutate(var = sd ^ 2) %>%
    select( - sd) %>%
    mutate(belligerent = plyr::revalue(belligerent, c("Union" = "US"))) %>%
    bind_rows(unit_size_values_)

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
    select(battle, belligerent, strength_min, strength_max) %>%
    mutate(str_var =
             ifelse(strength_min == strength_max,
                    rounded_var(strength_min, ROUND_METHOD),
                    unif_var(stregth_min, strength_max)),
           str_mean = unif_mean(strength_min, strength_max)) %>%
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
  write_csv(forces2,
            file = file.path(dst, "cwsac_forces.csv"))
}

main <- function() {
  args <- commandArgs(TRUE)
  update_forces(args[1], args[2])
}

main()

