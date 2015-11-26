#' ---
#' title: "List of Battles"
#' output: html_document
#' ---
#'
library("dplyr")
library("stringr")
library("tidyr")
library("stringr")
library("magrittr")
library("jsonlite")

DIR_CWSAC <- "../cwsac"
DIR_CWSAC2 <- "../cwsac2"
DIR_AAD <- "../aad"
DIR_CWSS <- "../cwss"
DIR_SHENANDOAH <- "../shenandoah/"
FILE_UNIT_SIZES <- "../unit_sizes/unit_sizes.csv"

DIR_OUT <- "."

#' Rounded variable variance method to use
ROUND_METHOD = 3

#' Mapping from CWSAC to CWSS belligerent names
BELLIGERENTS <-
  c("I" = "Native American",
    "CS" = "Confederate",
    "US" = "US")

RESULTS <-
  c("Union" = "Union victory",
    "Confederate" = "Confederate victory",
    "Inconclusive" = "Indecisive")

#'
#' # Utility Functions
#'
write_csv <- function(x, ...) {
  write.csv(x, ..., na = "", row.names = FALSE)
}

read_csv <- function(x, ...) {
  read.csv(x, ..., stringsAsFactors = FALSE)
}

psum <- function(...) {
  apply(cbind(...), 1, function(x) {
    if (all(is.na(x))) {
      NA_real_
    } else {
      sum(x, na.rm = TRUE)
    }
  })
}

pnonmiss <- function(...) {
  apply(cbind(...), 1, function(x) {
    i <- ! is.na(x)
    if (any(i)) {
      x[min(which(i, arr.ind = TRUE))]
    } else {
      NA
    }
  })
}

#' Calculate trailing zeros
#'
#' @param x numeric vector.
#' @return A vector of same size as \code{x} with the number of trailing zeros.
trailing_zeros <- function(x) {
  f <- function(x) {
    x <- abs(x[1])
    if (x %% 1 != 0 | x == 0) {
      trailing <- 0
    } else {
      magn <- floor(log10(x))
      trailing <- 0
      for (i in 1:magn) {
        if (x %% 10 ^ i == 0) {
          trailing <- i
        } else {
          break
        }
      }
    }
    trailing
  }
  vapply(x, f, 0)
}

unif_mean <- function(min, max) 0.5 * (min + max)

unif_var <- function(min, max) (1 / 12) * (max - min) ^ 2

#' Calculate variance of the measurement error of a value with trailing zeros
#'
#' Suppose \eqn{x} has \eqn{k} trailing zeros, than one model for the variance of the measurement error is,
#' \deqn{\mathrm{var}(x) = \sum_{i = 0}^k w_i \frac{1}{12} 10^{2k}}{var(x) = sum_(i = 0)^k w_i * 1/12 * 10^(2k)}
#' Method 1 is
#' \deqn{\mathrm{var}(x) = \frac{1}{k + 1} \sum_{i = 0}^k \frac{1}{12} 10^{2i}}{var(x) = (1 / k + 1) sum_(i = 0)^k 1/12 * 10^(2k) .}
#' Method 2 is
#' \deqn{\mathrm{var}(x) = \frac{1}{\sum_{i = 0}^k 10^i} \sum_{i = 0}^k \frac{1}{12} 10^{3i}}{var(x) = (1 / sum(10^0, ..., 10^k) sum_(i = 0)^k 1/12 * 10^(3k) .}
#' Method 3 is
#' \deqn{\mathrm{var}(x) = \frac{1}{12} 10^{2k}}{var(x) = (1/12) * 10^(2k) .}
#' Method 4 is
#' \deqn{\mathrm{var}(x) = \frac{1}{(k + 1) (k + 2) / 2} \sum_{i = 0}^k \frac{i + 1}{12} 10^{2i}
#' @param x The value
#' @param method see details
#' @return numeric vector with the variances for each value.
rounded_var <- function(x, method = 1) {
  f <- function(x) {
    if (is.na(x)) {
      NA
    } else {
      k <- trailing_zeros(x)
      switch(method,
             sum((10 ^ (2 * 0:k) / 12) / (k + 1)),
             sum(10 ^ (3 * 0:k) / 12) / sum(10^(0:k)),
             10 ^ (2 * k) / 12,
             sum((0:k + 1) / ((k + 1) * (k + 2) / 2) * (10 ^ (2 * 0:k) / 12))
      )
    }
  }
  vapply(x, f, 0)
}

#'
#' # Data
#'
#' Extra data
#'
#' - additional campaigns
#' - battles in CWSAC and missing from CWSS
#' - battles in CWSS to exclude from other analyses
#'
extra_data <- fromJSON("extra_data.json")



#' ## AAD
#'
#' The AAD data
aad_battles <-
  mutate(read_csv(file.path(DIR_AAD, "events.csv")),
         reference_number = plyr::revalue(reference_number,
                                          c("AR010A" = "AR010",
                                            "GA013A" = "GA013")))

#'
#' ## CWSAC I
#'
#' Original CWSAC battle summaries
cwsac1_battles <-
  read.csv(file.path(DIR_CWSAC, "cwsac_battles.csv"),
           stringsAsFactors = FALSE) %>%
  mutate(result = plyr::revalue(result, RESULTS))

cwsac1_forces <-
  read.csv(file.path(DIR_CWSAC, "cwsac_forces.csv"),
           stringsAsFactors = FALSE) %>%
  mutate(belligerent = plyr::revalue(belligerent, BELLIGERENTS),
         belligerent = ifelse(grepl("OK00[1-3]", battle) & belligerent == "US",
                              "Native American", belligerent))

#'
#' ## CWSAC II
#'
cwsac2_battles <- read.csv(file.path(DIR_CWSAC2, "cwsac2_battles.csv"),
                           stringsAsFactors = FALSE) %>%
  mutate(battle = plyr::revalue(battle, c("AL002" = "AL009")),
         battle_name = ifelse(battle == "AL009", "Athens II", battle_name),
         result = plyr::revalue(results, RESULTS)) %>%

  left_join(read.csv(file.path(DIR_CWSAC2, "cwsac2_dates.csv"),
                     stringsAsFactors = FALSE) %>%
              mutate(start_date = as.Date(start_date),
                     end_date = as.Date(end_date),
                     battle = plyr::revalue(battle, c("AL002" = "AL009"))) %>%
              group_by(battle) %>%
              summarise(start_date = as.Date(min(start_date), as.Date("1970-1-1")),
                        end_date = as.Date(max(end_date), as.Date("1970-1-1"))),
            by = "battle")

cwsac2_forces <- read.csv(file.path(DIR_CWSAC2, "cwsac2_forces.csv"),
                          stringsAsFactors = FALSE) %>%
  mutate(belligerent = plyr::revalue(belligerent, BELLIGERENTS))


#'
#' ## CWSS
#'
#' Civil War Soldiers and Sailors (CWSS) Database
cwss_battles <- read.csv(file.path(DIR_CWSS, "cwss_battles.csv"),
                         stringsAsFactors = FALSE) %>%
  mutate(BattleName = ifelse(BattlefieldCode == "AL002",
                             "Athens I", BattleName),
         BeginDate = as.Date(BeginDate),
         EndDate = as.Date(EndDate))

cwss_forces <- read.csv(file.path(DIR_CWSS, "cwss_forces.csv"),
                       stringsAsFactors = FALSE)


#'
#' ## Shenandoah Battefields
#'
shenandoah_2_cwsac <-
  read.csv(file.path(DIR_SHENANDOAH, "shenandoah_to_cwsac.csv"),
           stringsAsFactors = FALSE) %>%
  rename(cwsac_id = to)

shenandoah_battles <-
  read.csv(file.path(DIR_SHENANDOAH, "shenandoah_battles.csv"),
           stringsAsFactors = FALSE) %>%
  left_join(shenandoah_2_cwsac, by = c(number = "from"))

shenandoah_forces <-
  read.csv(file.path(DIR_SHENANDOAH, "shenandoah_forces.csv"),
           stringsAsFactors = FALSE) %>%
  left_join(shenandoah_2_cwsac, by = c(number = "from"))


#'
#' # Theaters and Campaigns
#'
theaters <-
  read.csv(file.path(DIR_CWSS, "cwss_theaters.csv"),
           stringsAsFactors = FALSE)

campaigns <-
  bind_rows(read.csv(file.path(DIR_CWSS, "cwss_campaigns.csv"),
                     stringsAsFactors = FALSE),
            extra_data$campaigns)

#'
#'
#' # Battlelist Comparisons
#'
#' Major differences in battle definitions between AAD, CWSAC I, CWSAC II, and CWSS.
#' Some other battles differ slightly in start and end dates.
#'
battlelist_cwss <-
  cwss_battles %>%
  select(BattlefieldCode, BattleName) %>%
  rename(cwsac_id = BattlefieldCode, battle_name = BattleName) %>%
  mutate(cwss = TRUE)

battlelist_cwsac1 <-
  cwsac1_battles %>%
  select(battle, battle_name) %>%
  rename(cwsac_id = battle, battle_name_cwsac1 = battle_name) %>%
  mutate(cwsac1 = TRUE)

battlelist_cwsac2 <-
  cwsac2_battles %>%
  select(battle, battle_name) %>%
  rename(cwsac_id = battle, battle_name_cwsac2 = battle_name) %>%
  mutate(cwsac2 = TRUE)

battlelist_aad <-
  aad_battles %>%
  select(reference_number, event) %>%
  rename(cwsac_id = reference_number, battle_name_aad = event) %>%
  mutate(aad = TRUE)

nps_battlelist <-
  battlelist_cwss %>%
  full_join(battlelist_cwsac1, by = "cwsac_id") %>%
  full_join(battlelist_cwsac2, by = "cwsac_id") %>%
  full_join(battlelist_aad, by = "cwsac_id") %>%
  mutate(battle_name = pnonmiss(battle_name, battle_name_cwsac1,
                                battle_name_cwsac2, battle_name_aad)) %>%
  select(- battle_name_cwsac1, - battle_name_cwsac2, - battle_name_aad) %>%
  mutate(cwss = ! is.na(cwss),
         cwsac1 = ! is.na(cwsac1),
         cwsac2 = ! is.na(cwsac2),
         aad = ! is.na(aad),
         notall = ! apply(cbind(cwss, cwsac1, cwsac2, aad), 1, all))

#'
#' Differences in battles
#'
#' More details about these differences:
#'
#' - AL002. Battle of Athens
#'
#' 	- AAD, CWSAC I, CWSS: Battle on 1864-1-26
#' 	- CWSAC II: Battle on 1864-9-23 to 1864-9-25.
#'
#' The Battle of Athens (AL002) entry mostly refers to a different battle of Athens (Sept 1864).
#' This seems largely to have been chosen since the battlefield of the primary battle (Jan 1864) is completely destroyed, while the battelfield of the other battle is north of the town and able to be maintained. However, the second battle is non-trivial; and included one of the larger surrenders of Union forces in the western theater.
#'
#' - Differing dates on Charleston battles
#'
#' 	- SC004 Charleston Harbor I
#'
#'       - 1863-4-7: AAD, CWSAC I, CWSAC II, CWSS
#'
#' 	- SC005 Fort Wagner I
#'
#'       - 1863-7-11: AAD
#' 	    - 1863-7-10 to 1863-7-11: CWSAC I, CWSAC II, CWSS
#'
#' 	- SC007 Fort Wagner II/Morris Island
#'
#' 	    - 1863-7-18 to 1863-9-7: AAD, CWSAC I
#' 		  - 1863-7-18 : CWSAC II, CWSS
#'
#' 	- SC008 Fort Sumter II
#'
#'     - 1863-8-17 to 1863-12-31 : AAD, CWSAC I
#' 		- 1863-8-17 to 1863-9-8 : CWSAC II, CWSS
#'
#' 	- SC009 Charleston Harbor II
#'
#'     - 1863-9-7 to 1863-9-8: AAD, CWSAC I
#' 		- 1963-8-22 to 1863-8-23 and 1863-9-5 to 1863-9-8 : CWSAC II
#' 		- 1863-9-5 to 1863-9-8 : CWSS
#'
#' - AR018 Bayou Meto (1863-8-27) only appears in CWSAC II
#' - VA126 "Cumberland Gap" (1865-4-6) only appears in CWSS. This appears to just be another name for Sayler's Creek. It is the same day as Sayler's Creek, has the same commanders (Sheridan, Ewell), and has alternate names referring to Sayler's Creek (Hillsman Farm, Locett Farm).
#' - GA024 Dalton III (1864-10-13): only appears in AAD and CWSS.
#' - AL008 Ebenezer Church (?): only appears in CWSS (but no data). This is probably the battle on April 1, 1865 between Wilson and Forrest, the day before the Battle of Selma on April 2, 1865.
#' - White Oak Swamp and Glendale (VA020)
#'
#'     - Split into VA020a (White Oak Swamp) into VA020b (Glendale) : AAD, CWSAC I
#' 	  - Combined: CWSAC II
#' 	  - CWSAC has data with VA020A, VA020B, and VA020
#'
#' Which to exclude?
#'
## ------------------------------------------------------------------------


#' And ensure that VA020A and VA020B are combined into a single battle.
#' The battles in CWSAC and not in CWSS
## ------------------------------------------------------------------------
CWSAC_ONLY_BATTLES <- extra_data$cwsac_only_battles
EXCLUDED_BATTLES <- extra_data$excluded_battles

#'
#' # Battle-Level Data
#'
#' Combine battle-level stats for each battle.
#'
nps_battles_cwss <- cwss_battles %>%
  filter(! BattlefieldCode %in% c(EXCLUDED_BATTLES, "VA020A")) %>%
  mutate(BattlefieldCode =
           plyr::revalue(BattlefieldCode, c("VA020B" = "VA020")),
         BattleName = ifelse(BattlefieldCode == "VA020",
                             "Glendale/White Oak Swamp", BattleName)) %>%
  rename(cwsac_id = BattlefieldCode,
         battle_name = BattleName,
         battle_type_cwss = BattleType,
         begin_date = BeginDate,
         end_date = EndDate,
         state = State,
         theater_code = TheaterCode,
         campaign_code = CampaignCode,
         result = Result,
         summary = Summary,
         summary_source = SummarySource,
         short_summary = ShortSummary,
         short_summary_source = ShortSummarySource,
         cas_kwm_mean = TotalCasualties) %>%
  mutate(cas_kwm_var = rounded_var(cas_kwm_mean, ROUND_METHOD)) %>%
  select(- Comment, - ID,
         - matches("summary")) %>%
  mutate(partof_cwss = TRUE)

nps_battles_cwsac1 <- cwsac1_battles %>%
  filter(! battle %in% EXCLUDED_BATTLES,
         ! battle %in% c("VA020A", "VA020B")) %>%
  select(battle, operation, forces_text, casualties_text, results_text,
         preservation, significance, url, battle_name) %>%
  rename(cwsac1_url = url, cwsac_id = battle,
         battle_name_cwsac1 = battle_name) %>%
  mutate(partof_cwsac1 = TRUE)

nps_battles_cwsac2 <- cwsac2_battles %>%
  filter(! battle %in% EXCLUDED_BATTLES) %>%
  select(battle, url, study_area, core_area, potnr_boundary,
         battle_name) %>%
  rename(cwsac_id = battle, cwsac2_url = url,
         battle_name_cwsac2 = battle_name) %>%
  mutate(partof_cwsac2 = TRUE)

nps_battles_aad <- aad_battles %>%
  filter(! reference_number %in% EXCLUDED_BATTLES) %>%
  select(reference_number, matches("^interpretive_"),
         jim, ed, bill, url, type, event) %>%
  filter(! reference_number %in% c("VA020A")) %>%
  mutate(reference_number =
           plyr::revalue(reference_number, c("VA020B" = "VA020"))) %>%
  rename(cwsac_id = reference_number,
         significance_jim = jim,
         significance_ed = ed,
         significance_bill = bill,
         battle_type_aad = type,
         aad_url = url,
         battle_name_aad = event) %>%
  mutate(partof_aad = TRUE)

nps_battles_shenandoah <- shenandoah_battles %>%
  filter(! cwsac_id %in% EXCLUDED_BATTLES) %>%
  select(cwsac_id, url) %>%
  rename(shenandoah_url = url) %>%
  mutate(partof_shenandoah = TRUE)

nps_latlong <- read_csv(file.path("latlong.csv")) %>%
  rename(cwsac_id = battle) %>%
  select(- cwsac_name)

nps_battles <-
  nps_battles_cwss %>%
  full_join(nps_battles_cwsac1, by = "cwsac_id") %>%
  full_join(nps_battles_cwsac2, by = "cwsac_id") %>%
  full_join(nps_battles_aad, by = "cwsac_id") %>%
  full_join(nps_battles_shenandoah, by = "cwsac_id") %>%
  left_join(nps_latlong, by = "cwsac_id") %>%
  filter(! cwsac_id %in% EXCLUDED_BATTLES) %>%
  mutate(partof_cwss = ! is.na(partof_cwss),
         partof_cwsac1 = ! is.na(partof_cwsac1),
         partof_cwsac2 = ! is.na(partof_cwsac2),
         partof_aad = ! is.na(partof_aad),
         partof_shenandoah = ! is.na(partof_shenandoah),
         battle_name =
           pnonmiss(battle_name, battle_name_cwsac1,
                    battle_name_cwsac2,
                    battle_name_aad)) %>%
  select(- battle_name_cwsac1,
         - battle_name_cwsac2,
         - battle_name_aad)

#'
#' Fill in battles missing in CWSS but in CWSAC data,
for (i in CWSAC_ONLY_BATTLES) {
  nps_battles[nps_battles[["cwsac_id"]] == i,
              c("state", "begin_date", "end_date", "result")] <-
    cwsac1_battles[cwsac1_battles[["battle"]] == i,
                   c("state", "start_date", "end_date", "result")]
}

#' Fill in campaigns and theaters,
for (i in names(extra_battle_campaigns)) {
  x <- extra_battle_campaigns[[i]]
  for (j in names(x)) {
    nps_battles[nps_battles[["cwsac_id"]] == i, j] <- x[[j]]
  }
}

#'
#' # Forces Data
#'
#' ## Functions
#'
#' Fill in disaggregated casualty vars
#'
fill_casualty_vars <- function(x, rounded_type = 2) {
  # Names of all casualty variables
  cas_types <- c("k", "w", "m", "kw", "km", "wm", "kwm")
  all_mean_vars <- paste0("cas_", cas_types, "_mean")
  all_var_vars <- gsub("_mean", "_var", all_mean_vars)
  all_vars <- c(all_mean_vars, all_var_vars)
  # Ensure that all casualty variables are in the dataset
  for (i in all_vars) {
    if (! i %in% names(x)) {
      x[[i]] <- NA_real_
    }
  }
  # Fill in missing variances with that implied by rounded variables
  for (i in all_mean_vars) {
    varvar <- gsub("_mean", "_var", i)
    x[[varvar]] <- ifelse(is.na(x[[varvar]]),
                          rounded_var(x[[i]], rounded_type), x[[varvar]])
  }
  # Fill in aggregated casualty variables implied by disaggregated casualty variables
  for (v in c("mean", "var")) {
    # killed, wounded -> killed + wounded
    x[[paste0("cas_kw_", v)]] <-
      ifelse(! is.na(x[[paste0("cas_k_", v)]])
             & ! is.na(x[[paste0("cas_w_", v)]]),
             x[[paste0("cas_k_", v)]] + x[[paste0("cas_w_", v)]],
             x[[paste0("cas_kw_", v)]])
    # killed, missing -> killed/missing
    x[[paste0("cas_km_", v)]] <-
      ifelse(! is.na(x[[paste0("cas_k_", v)]])
             & ! is.na(x[[paste0("cas_m_", v)]]),
             x[[paste0("cas_k_", v)]] + x[[paste0("cas_m_")]],
             x[[paste0("cas_km_", v)]])
    # wounded, missing -> wounded/missing
    x[[paste0("cas_wm_", v)]] <-
      ifelse(! is.na(x[[paste0("cas_w_", v)]])
             & ! is.na(x[[paste0("cas_m_", v)]]),
             x[[paste0("cas_w_", v)]] + x[[paste0("cas_m_", v)]],
             x[[paste0("cas_wm_", v)]])
    # casualties
    x[[paste0("cas_kwm_", v)]] <-
      ifelse(! is.na(x[[paste0("cas_kw_", v)]])
             & ! is.na(x[[paste0("cas_m_", v)]]),
             x[[paste0("cas_kw_", v)]] + x[[paste0("cas_m_", v)]],
             x[[paste0("cas_kwm_", v)]])
    x[[paste0("cas_kwm_", v)]] <-
      ifelse(is.na(x[[paste0("cas_kwm_", v)]])
             & ! is.na(x[[paste0("cas_kw_", v)]])
             & ! is.na(x[[paste0("cas_m_", v)]]),
             x[[paste0("cas_kw_", v)]] + x[[paste0("cas_m_", v)]],
             x[[paste0("cas_kwm_", v)]])
    x[[paste0("cas_kwm_", v)]] <-
      ifelse(is.na(x[[paste0("cas_kwm_", v)]])
             & ! is.na(x[[paste0("cas_wm_", v)]])
             & ! is.na(x[[paste0("cas_k_", v)]]),
             x[[paste0("cas_wm_", v)]] + x[[paste0("cas_k_", v)]],
             x[[paste0("cas_kwm_", v)]])
  }
  x
}

#'
#' ## Unit Sizes
#'
#' The number of personnel in each unit type, e.g. the number of personnel in a regiment
#' as a distribution accounting for attrition.
#' This data is used to convert unit types to personnel strength numbers.
unit_sizes <- read_csv(FILE_UNIT_SIZES)

unit_type_map <- c(
  "regiments" = "infantry regiment",
  "companies" = "infantry company",
  "brigades" = "infantry brigade",
  "divisions"= "infantry division",
  "corps" = "infantry corps",
  "armies" = "army",
  "cavalry_regiments" = "cavalry regiment",
  "cavalry_brigades" = "cavalry brigade",
  "cavalry_divisions" = "cavalry division",
  "cavalry_corps" = "cavalry corps",
  "cavalry_companies" = "cavalry company",
  "artillery_batteries" = "artillery battery",
  "artillery_companies" = "artillery company",
  "artillery_regiments" = "artillery regiment",
  "artillery_sections" = "artillery section",
  "infantry_regiments" = "infantry regiment"
)

unit_size_values_ <-
  expand.grid(belligerent = c("US", "CS"),
              unit_type = c("strength_other"))
unit_size_values_$mean <- 1
unit_size_values_$var <- 1 / 12

unit_size_values <-
  unit_sizes %>%
  select(belligerent, unit_type, mean, sd) %>%
  mutate(var = sd ^ 2) %>%
  select( - sd) %>%
  mutate(belligerent = plyr::revalue(belligerent, c("Union" = "US"))) %>%
  bind_rows(unit_size_values_)

#'
#' ## CWSS
#'
cwss_forces_casstr <-
  cwss_forces %>%
  mutate(BattlefieldCode =
           ifelse(BattlefieldCode == "VA020B", "VA020", BattlefieldCode)) %>%
  rename(cwsac_id = BattlefieldCode,
         cas_kwm_mean = Casualties,
         str_mean = TroopsEngaged) %>%
  mutate(str_mean = ifelse(str_mean == 0, NA_real_, str_mean),
         str_var = rounded_var(str_mean, ROUND_METHOD),
         cas_k_mean = NA_real_,
         cas_w_mean = NA_real_,
         cas_m_mean = NA_real_,
         cas_kw_mean = NA_real_,
         cas_km_mean = NA_real_,
         cas_wm_mean = NA_real_)

#'
#' ## CWSAC I
#'
#' - WV009 is not in CWSS
#' - WV010 has a different total than in CWSAC
#' - VA019 (Savage's Station):
#'
#'     - CWSAC includes 2500 captured after the Union retreats, making > 4000 casualties total.
#'     - CWSS only includes casualties from the battle itself for about 1363.
#'
#' - VA043: Has total casualties + a number for Confederate captured.
#'
cwsac_disagg_cas <- c("NC002", "WV009", "WV010")

cwsac1_str <-
  cwsac1_forces %>%
  rename(cwsac_id = battle) %>%
  select(cwsac_id, belligerent,
         armies, corps, divisions, brigades, regiments, companies,
         matches("cavalry_"),
         matches("artillery_")) %>%
  gather(unit_type, units, - cwsac_id, - belligerent, na.rm = TRUE) %>%
  mutate(unit_type =
           as.character(plyr::revalue(unit_type, unit_type_map,
                                      warn_missing = FALSE))) %>%
  left_join(unit_size_values, by = c("unit_type", "belligerent")) %>%
  mutate(str_mean = units * mean,
         str_var = units * var) %>%
  filter(! is.na(str_var)) %>%
  group_by(cwsac_id, belligerent) %>%
  summarise_each(funs(sum), matches("str_(mean|var)")) %>%
  rename(str_units_mean = str_mean,
         str_units_var = str_var)

cwsac1_forces_casstr <-
  cwsac1_forces %>%
  rename(cwsac_id = battle) %>%
  mutate(str_raw_mean = unif_mean(strength_min, strength_max),
         str_raw_var = ifelse(strength_min == strength_max,
                        rounded_var(strength_min, ROUND_METHOD),
                        unif_var(strength_min, strength_max)),
         cas_kwm_mean = casualties,
         cas_k_mean = killed,
         cas_w_mean = wounded,
         cas_m_mean = psum(missing, captured)
         ) %>%
  select(belligerent, cwsac_id, matches("^cas_"), matches("^str_"),
         description) %>%
  left_join(cwsac1_str, by = c("cwsac_id", "belligerent")) %>%
  filter(! cwsac_id %in% c("VA020A", "VA020B")) %>%
  mutate(str_mean = psum(str_raw_mean, str_units_mean),
         str_var = psum(str_raw_var, str_units_var))


#'
#' ## CWSAC II
#'
cwsac2_str <-
  cwsac2_forces %>%
  rename(cwsac_id = battle) %>%
  select(cwsac_id, belligerent,
         armies, corps, divisions, brigades, regiments, companies,
         matches("cavalry_"),
         matches("artillery_"),
         strength_other) %>%
  gather(unit_type, units, - cwsac_id, - belligerent, na.rm = TRUE) %>%
  mutate(unit_type =
           as.character(plyr::revalue(unit_type, unit_type_map,
                                      warn_missing = FALSE))) %>%
  left_join(unit_size_values, by = c("unit_type", "belligerent")) %>%
  mutate(str_mean = units * mean,
         str_var = units * var) %>%
  filter(! is.na(str_var)) %>%
  group_by(cwsac_id, belligerent) %>%
  summarise_each(funs(sum), matches("str_(mean|var)")) %>%
  rename(str_units_mean = str_mean,
         str_units_var = str_var)

cwsac2_forces_casstr <-
  cwsac2_forces %>%
  rename(cwsac_id = battle) %>%
  mutate(str_raw_mean = strength,
         str_raw_var = rounded_var(strength, ROUND_METHOD)) %>%
  select(belligerent, cwsac_id, matches("^str_"),
         description) %>%
  left_join(cwsac2_str, by = c("cwsac_id", "belligerent")) %>%
  mutate(str_mean = psum(str_raw_mean, str_units_mean),
         str_var = psum(str_raw_var, str_units_var))

#'
#' ## Shenandoah Data
#'
#' The Shenandoah report data is much more detailed in the disaggregation of casualties in its battles.twi
shenandoah_forces_casstr <-
  shenandoah_forces %>%
  rename(cas_k_mean = killed,
         cas_w_mean = wounded,
         cas_m_mean = missing_captured) %>%
  mutate(str_mean = unif_mean(strength_min, strength_max),
         str_var = unif_var(strength_min, strength_max),
         belligerent = plyr::revalue(belligerent,
                                     c(Confederate = "Confederate",
                                       Union = "US"))) %>%
  select(belligerent, cwsac_id, matches("^cas_"), matches("^str_"))

#'
#' ## Combined
#'
nps_forces <-
  bind_rows(
    filter(cwss_forces_casstr,
           ! cwsac_id %in% c(cwsac_disagg_cas, CWSAC_ONLY_BATTLES,
                             shenandoah_forces_casstr$cwsac_id)),
    filter(select(cwsac1_forces_casstr, cwsac_id, belligerent,
                  matches("^cas_")),
           cwsac_id %in% c(cwsac_disagg_cas, CWSAC_ONLY_BATTLES)),
    shenandoah_forces_casstr) %>%
  filter(! cwsac_id %in% EXCLUDED_BATTLES)

#'
#' Fix Appmattomax Court House Data. The original data does not include
#' the Confederate Casualties.
# Fix appomattox court house
nps_forces[nps_forces[["cwsac_id"]] == "VA097"
           & nps_forces[["belligerent"]] == "US",
           c("cas_kwm_mean")] <- 167
nps_forces[nps_forces[["cwsac_id"]] == "VA097"
           & nps_forces[["belligerent"]] == "Confederate",
           c("cas_kw_mean", "cas_m_mean")] <- c(500, 27805)

#' Add Confederate captured to VA043
va043_m_mean_C <- 1600
nps_forces[nps_forces[["cwsac_id"]] == "VA043"
           & nps_forces[["belligerent"]] == "Confederate", "cas_m_mean"] <-
  va043_m_mean_C
nps_forces[nps_forces[["cwsac_id"]] == "VA043"
           & nps_forces[["belligerent"]] == "Confederate", "cas_kw_mean"] <-
  nps_forces[nps_forces[["cwsac_id"]] == "VA043"
             & nps_forces[["belligerent"]] == "Confederate", "cas_kwm_mean"] -
  va043_m_mean_C

#' Add strengths from units
nps_forces %<>%
  left_join(select(rename(cwsac2_forces_casstr,
                          str_mean_cwsac = str_mean,
                          str_var_cwsac = str_var),
                   cwsac_id, belligerent,
                   matches("^str_.*_cwsac"), description),
            by = c("cwsac_id", "belligerent"))

nps_forces %<>%
  fill_casualty_vars(rounded_type = ROUND_METHOD) %>%
  arrange(cwsac_id, belligerent)

#'
#' # Commanders
#'
cwss_people <-
  bind_rows(read_csv(file.path(DIR_CWSS, "cwss_persons.csv")),
            extra_data$people)

cwss_commanders <-
  bind_rows(read_csv(file.path(DIR_CWSS, "cwss_commanders.csv")) %>%
              mutate(BattlefieldCode = plyr::revalue(BattlefieldCode,
                                                     c("VA020B" = "VA020",
                                                       "VA020A" = "VA020"))) %>%
              rename(PersonID = commander),
            extra_data$commanders %>%
              select(- Name)) %>%
  left_join(select(cwss_people, PersonID, LastName, FirstName, MiddleName,
                   MiddleInitial),
            by = c("PersonID")) %>%
  mutate(
         belligerent = ifelse(grepl("OK00[1-3]", BattlefieldCode) &
                                belligerent == "US",
                              "Native American", belligerent)) %>%
  rename(first_name = FirstName,
         middle_name = MiddleName,
         middle_initial = MiddleInitial,
         last_name = LastName,
         battle = BattlefieldCode)


cwsac_commanders <-
  read.csv(file.path(DIR_CWSAC, "cwsac_commanders.csv"),
           stringsAsFactors = FALSE) %>%
  mutate(cwsac = TRUE,
         belligerent = plyr::revalue(belligerent, BELLIGERENTS),
         belligerent = ifelse(grepl("OK00[1-3]", battle) & belligerent == "US",
                              "Native American", belligerent)) %>%
  filter(! battle %in% c("VA020A", "VA020B"),
         belligerent != "Native American")

nps_commanders <-
  left_join(cwss_commanders,
            select(cwsac_commanders,
                   battle, belligerent, last_name, rank, navy),
            by = c("battle", "belligerent", "last_name")) %>%
  filter(! battle %in% EXCLUDED_BATTLES) %>%
  arrange(belligerent, battle)

#'
#' # Save
#'
write_csv(theaters, file.path(DIR_OUT, "nps_theaters.csv"))
write_csv(campaigns, file.path(DIR_OUT, "nps_campaigns.csv"))
write_csv(nps_battlelist, file.path(DIR_OUT, "nps_battlelist.csv"))
write_csv(nps_battles, file.path(DIR_OUT, "nps_battles.csv"))
write_csv(nps_forces, file.path(DIR_OUT, "nps_forces.csv"))
write_csv(nps_commanders, file.path(DIR_OUT, "nps_commanders.csv"))
write_csv(cwss_people, file.path(DIR_OUT, "nps_people.csv"))
