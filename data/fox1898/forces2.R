library("stringr")
library("dplyr")

fill_na <- function(x) {
  x[is.na(x)] <- 0
  x
}
write_csv <- function(x, ... ) {
  write.csv(x, ..., row.names = FALSE, na = "")
}

forces2_ <- read.delim("forces2.tsv", stringsAsFactors = FALSE)
forces2 <- (forces2_
 %>% mutate(start_date = str_c(starty, "-", startm, "-", startd),
            end_date = str_c(endy, "-", endm, "-", endd),
            cavalry = fill_na(cavalry))
 %>% select(- matches("(start|end)[mdy]"), -cwsac)
)

split_cwsac <- function(x) {
  cwsacids <- str_split(x, "\\s+")[[1]]
  relations <- ifelse(length(cwsacids) > 1, ">", "=")
  data_frame(cwsac_id = cwsacids,
             relation = relations)
}

forces2_to_cwsac <-
  (forces2_
   %>% select(belligerent, battle_name, cwsac)
   %>% filter(cwsac != "")
   %>% group_by(belligerent, battle_name)
   %>% do(split_cwsac(.$cwsac))
  )

forces_ <- read.delim("forces.tsv", stringsAsFactors = FALSE)
forces <- (forces_
            %>% mutate(start_date = str_c(starty, "-", startm, "-", startd),
                       end_date = str_c(endy, "-", endm, "-", endd))
            %>% select(- matches("(start|end)[mdy]"), -cwsac)
)

forces_to_cwsac <-
  (forces_
   %>% select(belligerent, battle_name, cwsac)
   %>% filter(cwsac != "")
   %>% group_by(belligerent, battle_name)
   %>% do(split_cwsac(.$cwsac))
  )

write_csv(forces2, file = "fox_forces2.csv")
write_csv(forces2_to_cwsac, file = "fox_forces2_to_cwsac.csv")
write_csv(forces, file = "fox_forces.csv")
write_csv(forces_to_cwsac, file = "fox_forces_to_cwsac.csv")

