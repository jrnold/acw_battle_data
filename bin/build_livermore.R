#!/usr/bin/env Rscript
source("R/misc.R")

COPYFILES = c("livermore_to_cwsac.csv",
               "livermore_to_dbpedia.csv",
               "livermore_army_sizes.csv")

BELLIGERENTS <- c(UNION = "Union",
                  CONFEDERATE = "Confederate")

build <- function(src, dst) {
  LIV_BATTLES_FILE <- file.path(src, "rawdata", "livermore1900",
                                "livermore.csv")

  livrmore <- read_csv(LIV_BATTLES_FILE)

  liv_battles <-
    (livrmore
     %>% select(- matches("^(US|CS)_"), - matches("^commander_"))
     %>% arrange(seq_no)
    )

  liv_commanders <-
    read_csv(file.path(src, "rawdata", "livermore1900",
                       "livermore_commanders.csv")) %>%
    select(seq_no, belligerent, PersonID, last_name, first_name, middle_name,
           middle_initial, rank, navy)

  liv_forces <-
    livrmore %>%
    select(seq_no, matches("^(US|CS)_")) %>%
    gather(variable, value, - seq_no) %>%
    separate(variable, c("belligerent", "varname")) %>%
    mutate(belligerent = plyr::revalue(belligerent,
                                       c("US" = "Union",
                                         "CS" = "Confederate"))) %>%
    spread(varname, value) %>%
    select(seq_no, belligerent, str, kia, wia, kw, miapow) %>%
    mutate(wia = ifelse(is.na(kia) & ! is.na(wia) & ! is.na(kw), NA, wia))

  livermore_to_cwsac <-
    read_csv(file.path(src, "rawdata", "livermore1900",
    "livermore_to_cwsac.csv")) %>%
    select(from, to, relation)

  livermore_to_dbpedia <-
      read_csv(file.path(src, "rawdata", "livermore1900",
      "livermore_to_dbpedia.csv")) %>%
      select(from, to, relation)

  write_csv(liv_battles, file = file.path(dst, "livermore_battles.csv"))
  write_csv(liv_forces, file = file.path(dst, "livermore_forces.csv"))
  write_csv(liv_commanders, file = file.path(dst, "livermore_commanders.csv"))
  write_csv(livermore_to_cwsac, file = file.path(dst, "livermore_to_cwsac.csv"))
  write_csv(livermore_to_dbpedia, file = file.path(dst, "livermore_to_dbpedia.csv"))

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
