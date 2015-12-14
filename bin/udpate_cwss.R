source("R/misc.R")

build <- function(src, dst) {
  file_units <- file.path(dst, "cwss_regiments_units.csv")
  file_battleunits <- file.path(dst, "cwss_battleunitlinks.csv")

  units <- read_csv(file_units)
  battleunits <- read_csv(file_battleunits)
  new_units <- left_join(battleunits, units, by = c("unit_code" = "UnitCode"))
}

main <- function() {
  args <- commandArgs(TRUE)
  src <- args[1]
  dst <- args[2]
}

main()
