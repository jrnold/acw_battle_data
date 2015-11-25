library("stringr")
library("dplyr")

read_csv <- function(x, ...) {
  read.csv(x, ..., stringsAsFactors = FALSE)
}
read_delim <- function(x, ...) {
  read.delim(x, ..., stringsAsFactors = FALSE)
}

toint <- function(x) {
  str_replace_all(x, "[^0-9]", "")
}
write_csv <- function(x, ... ) {
  write.csv(x, ..., row.names = FALSE, na = "")
}

na_fill <- function(x, fill = 0) {
  x[is.na(x)] <- fill
  x
}

update_cwsac <- function(x) {
    cwsacids <- str_split(x, "\\s+")[[1]]
    relations <- if (length(x) > 1) ">" else "="
    data_frame(cwsac_id = cwsacids, relation = relations)
}

fox_forces <- read_csv("fox_forces.csv")
fox_forces2 <- read_csv("fox_forces2.csv")

fox_forces_to_cwsac <-
  (
    fox_forces
    %>% select(belligerent, battle_name, cwsac_id)
    %>% filter(cwsac_id != "")
    %>% group_by(belligerent, battle_name)
    %>% do(update_cwsac(.$cwsac_id))
  )

fox_forces2_to_cwsac <-
  (
    fox_forces2
    %>% select(belligerent, battle_name, cwsac_id)
    %>% filter(cwsac_id != "")
    %>% group_by(belligerent, battle_name)
    %>% do(update_cwsac(.$cwsac_id))
  )

write_csv(fox_forces_to_cwsac, file = "fox_forces_to_cwsac.csv")
write_csv(fox_forces2_to_cwsac, file = "fox_forces2_to_cwsac.csv")


