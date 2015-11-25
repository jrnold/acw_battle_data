#' Code to generate spells, and times since last failure from failure indicator variables
library(dplyr)

fill_na <- function(x, fill = 0) {
  x[is.na(x)] <- fill
  x
}

spells_from_failures <- function(x) {
  #' if an obs is the beginning of a new spell, the previous
  #' obs will be a 1, so use dplyr::lag
  #' the first value will be NA, so need to fill it with 0
  #' add 1 so the first spell is 1 and not 0
  cumsum(fill_na(dplyr::lag(foo$events), 0)) + 1
}

#' Event is a failure time at the END of aspell
foo <- data_frame(events = c(1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0)) %>%
  mutate(spell = spells_from_failures(events)) %>%
  group_by(spell) %>%
  mutate(time = row_number())

