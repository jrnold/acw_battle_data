#!/usr/bin/env Rscript
suppressPackageStartupMessages({
  library("dplyr")
  library("stringr")
  library("readr")
})

COPYFILES = c("livermore_to_cwsac.csv",
               "livermore_to_dbpedia.csv",
               "livermore_army_sizes.csv")

read_csv <- function(x, ...) {
  tbl_df(read.csv(x, ..., stringsAsFactors = FALSE,
                  check.names = FALSE))
}

write_csv <- function(x, ...) {
  write.csv(x, ..., na = "", row.names = FALSE)
}


BELLIGERENTS <- c(UNION = "Union",
                  CONFEDERATE = "Confederate")

build <- function(src, dst) {
  LIV_BATTLES_FILE <- file.path(src, "rawdata", "livermore1900",
                                "livermore.csv")

#   livrmore <- read_csv(file.path(src, "dependencies/PAR/data/LIVRMORE.csv"))
#   for (i in c("str", "kia", "wia", "kw", "miapow")) {
#     livrmore[[paste0("CS_", i)]] <- ifelse(livrmore[["attacker"]] == "CONFEDERATE",
#                                            livrmore[[paste0("attacker_", i)]],
#                                            livrmore[[paste0("defender_", i)]])
#   }
#   for (i in c("str", "kia", "wia", "kw", "miapow")) {
#     livrmore[[paste0("US_", i)]] <- ifelse(livrmore[["attacker"]] == "UNION",
#                                            livrmore[[paste0("attacker_", i)]],
#                                            livrmore[[paste0("defender_", i)]])
#   }
#   write.csv(livrmore, file = "livrmore2.csv", row.names = FALSE, na = "")

  livrmore <- read_csv(LIV_BATTLES_FILE)

  liv_battles <-
    (livrmore
     %>% select(- matches("^(US|CS)_"), - matches("^commander_"))
     %>% arrange(seq_no)
    )

  liv_commanders <-
    livrmore %>%
    group_by(seq_no) %>%
    do({
      bind_rows(data_frame(commander = str_split(str_trim(.$commander_union), " +")[[1]],
                          belligerent = "Union"),
                data_frame(commander = str_split(str_trim(.$commander_confederate), " +")[[1]],
                           belligerent = "Confederate"))
    }) %>%
    select(seq_no, belligerent, commander)

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

  write_csv(liv_battles, file = file.path(dst, "livermore_battles.csv"))
  write_csv(liv_forces, file = file.path(dst, "livermore_forces.csv"))
  write_csv(liv_commanders, file = file.path(dst, "livermore_commanders.csv"))

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
