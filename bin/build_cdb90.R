source("R/misc.R")

build <- function(src, dst) {
  read_csv(file.path(src, "rawdata", "cdb90", "CDB90_to_cwsac.csv")) %>%
    select(isqno, cwsac_id, relation) %>%
    write_csv(file = file.path(dst, "CDB90_to_cwsac.csv"))
}

main <- function() {
  arglist <- commandArgs(TRUE)
  build(arglist[1], arglist[2])
}

main()
