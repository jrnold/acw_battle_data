library("tidyverse")
library("here")
library("glue")

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

casualties <- read_csv(infile) %>%
  fill(page, year) %>%
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
pattern <- glue("^({months})\\.? +({ordinal}|[-]+)(?:(?:, (186[12345]),)? (?:to|and) (?:({months})\\.? )?+({ordinal})(?:, (186[12345]))?)?$")

foo <- str_match(casualties$date, pattern) %>%
  `[`( ,-1) %>%
  as_tibble() %>%
  bind_cols(select(casualties, year)) %>%
  mutate(year_min = coalesce(year, as.integer(V3)),
         year_min = coalesce(as.integer(V6), year_min),
         month_min = V1,
         month_max = coalesce(V4, month_min),
         month_min = as.integer(set_names(seq_along(MONTHS), MONTHS)[month_min]),
         month_max = as.integer(set_names(seq_along(MONTHS), MONTHS)[month_max]),
         day_min = if_else(V2 == "-", 1L, as.integer(V2)))
#         day_max = coalesce(as.integer(V5), day_min))
#
#          date_min = lubridate::ymd(year_min, month_min, day_min),
#          date_max = lubridate::ymd(year_max, month_max, day_max))
#
#
