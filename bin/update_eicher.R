# Copies any single-day events into superevent column
# Events spanning more than one days have been cleaned manually
source("R/misc.R")

build <- function(src, dst) {
  file_eicher <- file.path(dst, "eicher_chronology.csv")

  eicher <- read_csv(file_eicher)
  eicher_super <- eicher %>%
    filter(!is.na(superevent))
  eicher_single <- eicher %>%
    filter(is.na(superevent)) %>%
    mutate(superevent = event)

  eicher_out <- full_join(eicher_super, eicher_single)
  eicher_out <- arrange(eicher_out, date)


  write_csv(eicher_out,
            file.path(dst, "eicher_chronology.csv"))

}

main <- function() {
  arglist <- commandArgs(TRUE)
  src <- arglist[1]
  dst <- arglist[2]
  stopifnot(!is.na(src) & !is.na(dst))
  build(src, dst)
}

main()
