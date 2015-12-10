library("dplyr")
library("stringr")
library("magrittr")

src <- "."

path <- file.path("rawdata/cwss/nps_cwss.sqlite3")
nps_cwss <- src_sqlite(path)

regiments_unitz <- tbl(nps_cwss, "Regiments_Unitz") %>%
  select(REG_UNIT_CODE,
         REG_SIDE,
         REG_STATE,
         REG_ORDINAL,
         REG_TYPE,
         REG_SPECIAL,
         REG_DUPLICATE,
         REG_ETHNIC,
         REG_UNIT_NAME) %>%
  collect() %>%
  filter(! str_detect(REG_UNIT_CODE, regex("^admin", ignore = TRUE))) %>%
  setNames(tolower(gsub("REG_", "", names(.))))

unit_titles <-
  bind_rows(collect(tbl(nps_cwss, "Unititle")),
            collect(tbl(nps_cwss, "Contitle"))) %>%
  select(STATE, SIDE, TITLE) %>%
  setNames(tolower(names(.)))

state_name <-
  tbl(nps_cwss, "State_Name") %>%
  select(STATE_ABBR, STATE_NAME) %>%
  setNames(tolower(names(.)))

