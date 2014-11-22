library("stringr")
library("dplyr")

read_csv <- function(x, ...) {
  read.csv(x, ..., stringsAsFactors = FALSE)
}

toint <- function(x) {
  str_replace_all(x, "[^0-9]", "")
}
write_csv <- function(x,... ) {
  write.csv(x, ..., row.names = FALSE, na = "")
}

fox_forces2 <-
  (read.csv("fox_forces2.csv") %>%
   mutate(killed = toint(killed),
          wounded = toint(wounded),
          missing = toint(missing),
          casualties = toint(casualties)))

fox_forces <-
  (read.csv("fox_forces.csv") %>%
     mutate(killed = toint(killed),
            wounded = toint(wounded),
            missing = toint(missing),
            casualties = toint(casualties)))

write_csv(fox_forces, file = "fox_forces.csv")
write_csv(fox_forces2, file= "fox_forces2.csv")
