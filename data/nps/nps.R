#' # Combined National Park Service Civil War Data
#'
#' Data from the national park service:
#'
#' - CWSAC
#' - CWSAC Revisions
#' - CWSS (Civil War Soldiers & Sailors)
#'

library("dplyr")
library("tidyr")
library("jsonlite")

read_csv <- function(x, ...) {
    tbl_df(read.csv(x, ..., stringsAsFactors = FALSE))
}

fill_na <- function(x, fill = 0) {
    x[is.na(x)] <- fill
    x
}

#'
#' Load CWSAC 2 datasets
#' 
cwsac2_forces <- read_csv("cwsac2/cwsac2_forces.csv")

#'
#' # Unit sizes
#'
#' For different sizes of units, the number of personnel.
#'
unit_sizes <- fromJSON("../organizations/unit_sizes.json")

#'
#' Standardize strengths. Convert organizations
#'
#' The CWSAC II data are more detailed and have more numeric. Thus prefer those instead of CWSAC I.
#'
union_forces <- filter(cwsac2_forces, combatant == "US")

units_to_personnel <- function(x, confederate = FALSE) {
    if (confederate) combatant <- "confederate"
    else combatant <- "union"

    vars <-
     c("strength",
       "regiments",
       "companies",
       "brigades",
       "divisions",
       "corps",
       "armies", 
       "cavalry_regiments",
       "cavalry_brigades",
       "cavalry_divisions", 
       "cavalry_corps",
       "cavalry_companies",
       "artillery_batteries",
       "artillery_sections", 
       "artillery_companies",
       "artillery_regiments", 
       "infantry_regiments")
    ## Indicator if all variables are missing
    ## all_na <-
    ##     select(x, one_of(vars)) %>% apply(1, function(rw) all(is.na(rw)))
    ## fill in NA's with 0's
    ## "strength",
    x[["regiments"]] <- x[["regiments"]] * unit_sizes[[combatant]][["infantry_regiment"]]
    x[["regiments"]] <- x[["regiments"]] * unit_sizes[[combatant]]
       "companies",
       "brigades",
       "divisions",
       "corps",
       "armies", 
       "cavalry_regiments",
       "cavalry_brigades",
       "cavalry_divisions", 
       "cavalry_corps",
       "cavalry_companies",
       "artillery_batteries",
       "artillery_sections", 
       "artillery_companies",
       "artillery_regiments", 
       "infantry_regiments")

    x[["strength"]]
    
    
    
}

#'
#' create variable `str_personnel` which aggregates all strength data
#'
summarise_each(union_forces, fill_na,
               


confed_forces <- filter(cwsac2_forces,
                        combatant == "CS")





