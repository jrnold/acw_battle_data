library("dplyr")
library("stringr")

CASUALTY_TYPES <- c("k", "w", "m", "p",
                    "kw", "km", "kp", "wm", "wp", "mp",
                    "kwm", "kwp", "wmp",
                    "kwmp")


#' Read csv with better settings
read_csv <- function(x, ...) {
    tbl_df(read.csv(x, ..., stringsAsFactors = FALSE))
}

#' 
#' Given several variables, for each element return the value of the
#' first non-missing variable
#' 
non_na <- function(...) {
    apply(cbind(...), 1, function(x) x[!is.na(x)][1])
}

#' Path to the directory with Clodfelter 
clodfelter_path <- "../clodfelter2008"

#' Datasets to use 
clodfelter_forces <- read_csv(file.path(clodfelter_path, "clodfelter_forces.csv"))
clodfelter_to_cwsac <- read_csv(file.path(clodfelter_path, "clodfelter_to_cwsac.csv"))

#'
#' Adds the full set of casualty variables.
#' - If any combination of cas_[kwmp] doesn't exist, adds the variable with all missings.
#' - Then fills in all casualty variables based off of non-missingness of component variables.
#'   E.g. if cas_k and cas_w exist, then cas_kw can be calculated.
#'
fill_casualty_variables <- function(x) {
    cas_vars <- str_c("cas_", CASUALTY_TYPES)
    for (i in setdiff(cas_vars, names(x))) {
        x[[i]] <- NA_real_
    }
    mutate(x,
           cas_kw = ifelse(is.na(cas_kw), cas_k + cas_w, cas_kw),
           cas_km = ifelse(is.na(cas_km), cas_k + cas_m, cas_km),
           cas_kp = ifelse(is.na(cas_kp), cas_k + cas_p, cas_kp),
           cas_wm = ifelse(is.na(cas_wm), cas_w + cas_m, cas_wm),
           cas_wp = ifelse(is.na(cas_wp), cas_w + cas_p, cas_wp),           
           cas_mp = ifelse(is.na(cas_mp), cas_m + cas_p, cas_mp),
           cas_kwm = ifelse(is.na(cas_kwm), non_na(cas_kw + cas_m, cas_k + cas_wm), cas_kwm),
           cas_kwp = ifelse(is.na(cas_kwp), non_na(cas_kw + cas_p, cas_k + cas_wp), cas_kwp),
           cas_wmp = ifelse(is.na(cas_wmp), non_na(cas_w + cas_mp, cas_wm + cas_p), cas_wmp),
           cas_kwmp = ifelse(is.na(cas_kwmp), non_na(cas_kwm + cas_p, cas_kwp + cas_m,
               cas_wmp + cas_k, cas_kw + cas_mp, cas_km + cas_wp, cas_kp + cas_wm), cas_kwmp)
           )
}

#'
#' Add total casualty variables (
#' 
fill_total_casualties <- function(x) {
    for (i in CASUALTY_TYPES) {
        if (! str_c("cas_", i, "_total") %in% names(x)) {
            x[[str_c("cas_", i, "_total")]] <- NA_real_
        }
        x[[str_c("cas_", i, "_total")]] <-
            non_na(x[[str_c("cas_", i, "_total")]],
                   x[[str_c("cas_", i, "_C")]] + x[[str_c("cas_", i, "_U")]])
    }
    x
}

#'
#' Standardize clodfelter casualty variable names
#' 
clodfelter_standardize_cas <- function(x) {
    y <- (x %>% select(battle, belligerent, killed, captured, wounded,
                       killed_wounded, captured_missing, wounded_missing, killed_missing,
                       casualties)
          %>% rename(cas_k = killed, cas_p = captured, cas_w = wounded,
                     cas_kw = killed_wounded, cas_km = killed_missing, cas_wm = wounded_missing,
                     cas_mp = captured_missing, cas_kwmp = casualties)
          %>% mutate(belligerent = plyr::mapvalues(belligerent, c("union", "confed"), c("U", "C")))
          # %>% fill_casualty_variables() 
          )
    
    ## reshape data to long format
    union <- filter(y, belligerent == "U") %>% select(-belligerent)
    cas_vars <- grepl("^cas_", names(union))
    names(union)[cas_vars] <- str_c(names(union)[cas_vars], "_U")
    confed <- filter(y, belligerent == "C") %>% select(-belligerent)
    cas_vars <- grepl("^cas_", names(confed))
    names(confed)[cas_vars] <- str_c(names(confed)[cas_vars], "_C")
    (merge(confed, union, by = "battle")
     # %>% fill_total_casualties()
     )
}

#'
#' Battles with are sub-events of CWSAC battles
#'
filter(clodfelter_to_cwsac, relation == "<")

#'
#' Cold Harbor data includes siege and assault.
#'
filter(clodfelter_to_cwsac, cwsac == "VA062")

#'
#' Port Hudson includes assaults + siege
#' 
filter(clodfelter_to_cwsac, cwsac == "LA010")

#'
#' Vicksburg includes assaults + siege. 
#' 
filter(clodfelter_to_cwsac, cwsac == "MS011")

#'
#' Battles which are superbattles of CWSAC
#'
filter(clodfelter_to_cwsac, relation == ">")

clodfelter_cas <- clodfelter_standardize_cas(clodfelter_forces)

#' Merge clodfelter with CWSAC
#' Only consider battles that are equivalent or subevents of CWSAC battles
#' Take account of the special cases discussed previousl
clodfelter_cwsac <-
    (merge(clodfelter_cas,
           filter(clodfelter_to_cwsac, relation %in% c("=", "<")),
           by = "battle")
     %>% filter(! (battle %in% c("LA010", "MS011", "VA062") & relation == "<"))
     %>% group_by(cwsac)
     %>% select(-battle, -relation)
     %>% summarise_each(funs(sum))
     )

