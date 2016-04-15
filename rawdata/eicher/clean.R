library("stringr")
library("dplyr")
chronology <- readr::read_csv("rawdata/eicher/chronology.csv")

chron <-
  chronology %>%
  mutate(date = str_replace(date, "Thurs", "Thu"),
         date = str_replace(date, "Tues", "Tue"),
         date2 = as.Date(paste0(year, date), "%Y %a %d %b")) %>%
  group_by(date2) %>%
  do({
    events <- str_c(na.omit(c(.$event1, .$event2, .$event3, .$event4, .$event5, .$event6, .$event7, .$event8)), collapse = " @ ")
    events2 <- str_trim(str_split(events, "\\s*@\\s*")[[1]])
    data_frame(events = events2)
  })

readr::write_csv(chron, "chonrology_clean.csv")
