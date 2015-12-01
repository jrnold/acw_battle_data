#!/usr/bin/env Rscript
suppressPackageStartupMessages({
  library("tidyr")
  library("dplyr")
})

clean_forces <- function(file_clodfelter_forces, file_unit_sizes) {

  unit_sizes <- read.csv(file_unit_sizes,
                         stringsAsFactors = FALSE)

  unit_type_map <- c(
    ## "strength",
    ## "infantry",
    ## "cavalry",
    ## "crewmen",
    "corps" = "infantry corps",
    "cavalry_corps" = "cavalry corps",
    "divisions" = "infantry division",
    "cavalry_divisions" = "cavalry division",
    "brigades" = "infantry brigade",
    "companies" = "infantry company"
  )

  clodfelter_forces <-
    read.csv(file_clodfelter_forces,
             stringsAsFactors = FALSE)

  unit_size_values <-
    unit_sizes %>%
    select(belligerent, unit_type, mean, sd) %>%
    mutate(belligerent = plyr::revalue(belligerent,
                                       c("Union" = "union",
                                         "Confederate" = "confed")))


  clodfelter_str <-
    clodfelter_forces %>%
    select(battle, belligerent,
            strength, cavalry, infantry,
            corps, cavalry_corps, divisions,
            cavalry_divisions,
            brigades, companies) %>%
     gather(unit_type, value, -battle, -belligerent, na.rm=TRUE) %>%
     mutate(unit_type =
              as.character(plyr::revalue(unit_type, unit_type_map))) %>%
     left_join(unit_size_values, by = c("unit_type", "belligerent")) %>%
     mutate(strength_mean = value * mean,
            strength_var = value ^ 2 * var) %>%
     group_by(battle, belligerent) %>%
     select(battle, belligerent, strength_mean, strength_var) %>%
    summarise_each(funs(sum))
  left_join(clodfelter_forces, clodfelter_str,
            c("battle", "belligerent"))
}

build <- function(src, unit_sizes, dst) {
  forces <- clean_forces(src, unit_sizes)
  write.csv(forces, dst, row.names = FALSE, na = "")
}

main <- function() {
  arglist <- commandArgs(TRUE)
  src <- file.path(arglist[2], "clodfelter_forces.csv")
  unit_sizes <- file.path(arglist[2], "unit_sizes.csv")
  dst <- src
  build(src, unit_sizes, dst)
}

main()
