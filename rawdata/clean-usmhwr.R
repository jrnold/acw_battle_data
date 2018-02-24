library("tidyverse")
library("here")
library("glue")
library("magrittr")
library("lubridate")

infile <- here::here("rawdata", "usmhwr", "conflicts.csv")

STATES <- c("Alabama", "Arkansas", "Florida", "Georgia",
            "Louisiana", "Maryland", "Mississippi", "Missouri",
            "North Carolina", "South Carolina", "Texas",
            "(West )?Virginia", "Oregon",
            "Arizona Territory", "Tennessee", "Kentucky",
            "Indian Territory", "New Mexico",
            "Kansas", "Colorado Territory", "Dakota Territory",
            "Ohio", "Indiana", "Pennsylvania", "Utah Territory",
            "Washington Territory", "Minnesota", "CHerokee Cherokee Nation",
            "(West )?Va\\.", "Ala\\.", "Ky\\.", "Ga\\.", "N\\. C\\.", "Tenn\\.", "Miss\\.", "La\\.", "Ark\\.", "Nevada Territory", "D\\. C\\.",
            "California", "Illinois", "Nebraska", "Mo\\.", "D\\. T\\.",
            "Cherokee Nation", "Idaho Territory", "New York City")

STATE_ABBR <- c("West Va." = "West Virginia",
                "Mo." = "Missouri",
                "Ga." = "Georgia",
                "New York City" = "New York",
                "La." = "Louisiana",
                "Ark." = "Arkansas",
                "Miss." = "Mississippi",
                "Tenn." = "Tennessee",
                "N. C." = "North Carolina",
                "Ky." = "Kentucky",
                "Ala." = "Alabama",
                "Va." = "Virginia",
                "Cherokee Nation" = "Indian Territory",
                "Oregon" = "Oregon Territory",
                "D. C." = "District of Columbia",
                "D. T." = "Dakota Territory",
                "New Mexico" = "New Mexico Territory",
                "Nebraska" = "Nebraska Territory")

locality_lookup <- yaml::yaml.load_file("rawdata/usmhwr/localities.yaml") %>%
  enframe() %>%
  mutate(value = flatten_chr(value))

col_types <- cols(
  page = col_integer(),
  year = col_integer(),
  date = col_character(),
  locality = col_character(),
  union_troops_engaged = col_character(),
  union_killed = col_character(),
  union_wounded = col_character(),
  union_missing = col_character(),
  confederate_killed = col_character(),
  confederate_wounded = col_character(),
  confederate_missing = col_character(),
  remarks = col_character()
)


casualties <- read_csv(infile, col_types = col_types) %>%
  fill(page, year) %>%
  mutate(duplicate = is.na(locality)) %>%
  mutate(date = if_else(duplicate, lag(date), date),
         locality = if_else(duplicate, lag(locality), locality),
         union_troops_engaged = if_else(duplicate, lag(union_troops_engaged),
                                        union_troops_engaged),
         remarks = if_else(duplicate, lag(remarks), remarks)) %>%
  mutate(state = str_match(locality,
                           str_c("\\b(", str_c(STATES, collapse = "|"),
                                 ")$"))[ , 2],
         state = if_else(state %in% names(STATE_ABBR),
                         STATE_ABBR[state], state)) %>%
  left_join(select(locality_lookup, locality = name, state2 = value),
            by = "locality") %>%
  mutate(state = coalesce(state, state2),
         date = str_replace(date, " +", " "),
         date = str_replace_all(date, "’(6[2345])", "18\\1"),
         date = str_replace_all(date, "Apr\\.", "April"),
         date = str_replace_all(date, "Sep\\.", "Sept.")) %>%
  select(-state2)

ordinal <- "[0-9]+(?:th|d|st)"
MONTHS <- c("Jan", "Feb", "Mar", "April", "May", "June",
            "July", "Aug", "Sept", "Oct", "Nov", "Dec")
months <- str_c("(?:", str_c(c(MONTHS), collapse = "|"), ")")
pattern <-
  glue("^({months})\\.? +",
       "({ordinal}(?:,? (?:and )?{ordinal})*|[-]+)",
       "(?:(?:, (186[12345]),)? ?(?:to|and) ?(?:({months})\\.? )?+",
       "({ordinal})(?:, (186[12345]))?)?$")

make_start_date <- function(year1, month1, days1, ...) {
  ymd(str_c(year1, month1, days1, sep = "-"))
}

make_end_date <- function(year2, month2, days2, ...) {
  ymd(str_c(year2, month2, days2, sep = "-"))
}

#' Last day of the month
last_dom <- function(x) {
  rollback(x + days(31))
}

dates <- str_match(casualties$date, pattern) %>%
  `[`( , -1) %>%
  `colnames<-`(c("month1", "days1", "year1",
                 "month2", "days2", "year2")) %>%
  as_tibble() %>%
  # split lists of days
  mutate(month_only = map_lgl(days1, ~ str_detect(.x[1], "^[-]+$")),
         days1 = if_else(str_detect(days1, "^[-]+$"),
                         list(1L),
                         map(str_match_all(days1, "[0-9]+"), as.integer)))

casualties %<>% bind_cols(dates) %>%
  mutate(year1 = as.integer(year1),
         year2 = as.integer(year2),
         year1 = coalesce(year1, year),
         year2 = coalesce(year2, year1),
         month2 = coalesce(month2, month1),
         month1 = match(month1, MONTHS),
         month2 = match(month2, MONTHS),
         dates_and = str_detect(date, "and")) %>%
  mutate(
    start_date = pmap(list(year1, month1, days1), make_start_date),
    end_date = pmap(list(year2, month2, days2), make_end_date),
    dates = pmap(list(start_date, end_date, dates_and, month_only),
                 function(start_date, end_date, dates_and, month_only, ...) {
                   if (month_only) {
                     last_dom(start_date)
                   } else if (is.na(end_date)) {
                     start_date
                   } else {
                     if (dates_and) {
                       c(start_date, end_date)
                     } else {
                       seq(start_date, end_date, by = 1L)
                     }
                   }
                 })
  ) %>%
  select(-matches("^(month|year|days?)[12]$"),
         -dates_and, -matches("^(start|end)_date$")) %>%
  mutate(date_min = map_chr(dates, ~ format(min(.x))),
         date_max = map_chr(dates, ~ format(max(.x))))


