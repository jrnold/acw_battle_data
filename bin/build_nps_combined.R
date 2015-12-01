#!/usr/bin/env Rscript
source("R/misc.R")

RESULTS <-
  c("Union" = "Union victory",
    "Confederate" = "Confederate victory",
    "Inconclusive" = "Indecisive")

#' Fix AAD reference IDs
aad_to_cwsac_id <- function(x) {
  plyr::revalue(x, c("AR010A" = "AR010", "GA013A" = "GA013"))
}
#' Fix CWSACII ids
cwsac2_to_cwsac_id <- function(x) {
  plye::revalue(x, c("AL002" = "AL009"))
}

#'
#' # Battlelist Comparisons
#'
#' Major differences in battle definitions between AAD, CWSAC I, CWSAC II, and CWSS.
#' Some other battles differ slightly in start and end dates.
#'
gen_battlelist <-
  function(cwss_battles, cwsac1_battles,
           cwsac2_battles, aad_battles) {

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
    mutate(reference_number = aad_to_cwsac_id(reference_number)) %>%
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
  nps_battlelist
}


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

#'
#' # Battle-Level Data
#'
#' Combine battle-level stats for each battle.
#'
gen_battles <-
  function(cwss_battles, cwsac1_battles, cwsac2_battles,
           aad_battles, shenandoah_battles,
           latlong,
           extra_data) {

  excluded_battles <- extra_data[["excluded_battles"]]

  nps_battles_cwss <- cwss_battles %>%
    filter(! BattlefieldCode %in% c("VA020A")) %>%
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
           cas_kwm_mean = TotalCasualties) %>%
    mutate(cas_kwm_var = rounded_var(cas_kwm_mean)) %>%
    select(- Comment, - ID,
           - matches("summary")) %>%
    mutate(partof_cwss = TRUE)

  nps_battles_cwsac1 <- cwsac1_battles %>%
    filter(! battle %in% c("VA020A", "VA020B")) %>%
    select(battle, operation, forces_text, casualties_text, results_text,
           preservation, significance, url, battle_name) %>%
    rename(cwsac1_url = url, cwsac_id = battle,
           battle_name_cwsac1 = battle_name) %>%
    mutate(partof_cwsac1 = TRUE)

  nps_battles_cwsac2 <- cwsac2_battles %>%
    select(battle, url, study_area, core_area, potnr_boundary,
           battle_name) %>%
    rename(cwsac_id = battle, cwsac2_url = url,
           battle_name_cwsac2 = battle_name) %>%
    mutate(partof_cwsac2 = TRUE)

  nps_battles_aad <- aad_battles %>%
    mutate(reference_number = aad_to_cwsac_id(reference_number),
           reference_number =
             plyr::revalue(reference_number, c("VA020B" = "VA020"))) %>%
    filter(! reference_number %in% c("VA020A")) %>%
    select(reference_number, matches("^interpretive_"),
           jim, ed, bill, url, type, event) %>%
    rename(cwsac_id = reference_number,
           significance_jim = jim,
           significance_ed = ed,
           significance_bill = bill,
           battle_type_aad = type,
           aad_url = url,
           battle_name_aad = event) %>%
    mutate(partof_aad = TRUE)

  nps_battles_shenandoah <- shenandoah_battles %>%
    select(cwsac_id, url) %>%
    rename(shenandoah_url = url) %>%
    mutate(partof_shenandoah = TRUE)

  nps_latlong <- latlong %>%
    rename(cwsac_id = battle) %>%
    select(cwsac_id, lat, long)

  nps_battles <-
    nps_battles_cwss %>%
      full_join(nps_battles_cwsac1, by = "cwsac_id") %>%
      full_join(nps_battles_cwsac2, by = "cwsac_id") %>%
      full_join(nps_battles_aad, by = "cwsac_id") %>%
      full_join(nps_battles_shenandoah, by = "cwsac_id") %>%
      left_join(nps_latlong, by = "cwsac_id") %>%
      filter(! cwsac_id %in% excluded_battles) %>%
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
  for (i in extra_data[["cwsac_only_battles"]]) {
    nps_battles[nps_battles[["cwsac_id"]] == i,
                c("state", "begin_date", "end_date", "result")] <-
      cwsac1_battles[cwsac1_battles[["battle"]] == i,
                     c("state", "start_date", "end_date", "result")]
  }

  #' Fill in campaigns and theaters,
  extra_battle_campaigns <- extra_data[["campaigns"]]
  for (i in names(extra_battle_campaigns)) {
    x <- extra_battle_campaigns[[i]]
    for (j in names(x)) {
      nps_battles[nps_battles[["cwsac_id"]] == i, j] <- x[[j]]
    }
  }
  nps_battles
}


#'
#' # Forces Data
#'
#' Fill in disaggregated casualty vars
#'
fill_casualty_vars <- function(x) {
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
                          rounded_var(x[[i]]), x[[varvar]])
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
#' ## CWSS
#'
cwss_forces_casstr <-
  cwss_forces %>%
  mutate(BattlefieldCode =
           ifelse(BattlefieldCode == "VA020B", "VA020", BattlefieldCode)) %>%
  rename(cwsac_id = BattlefieldCode,
         cas_kwm_mean_cwss = Casualties,
         str_mean_cwss = TroopsEngaged) %>%
  mutate(str_mean_cwss = ifelse(str_mean_cwss == 0, NA_real_, str_mean_cwss),
         str_var_cwss = rounded_var(str_mean_cwss),
         cas_kwm_var_cwss = rounded_var(cas_kwm_mean_cwss))

cwsac1_forces_casstr <-
  cwsac1_forces %>%
  mutate(cas_m_mean_cwsac1 = psum(missing, captured),
         cas_kwm_var_cwsac1 = rounded_var(casualties),
         cas_k_var_cwsac1 = rounded_var(killed),
         cas_w_var_cwsac1 = rounded_var(wounded),
         cas_m_var_cwsac1 = psum(rounded_var(missing),
                                 rounded_var(captured))) %>%
  rename(cas_kwm_mean_cwsac1 = casualties,
         cas_k_mean_cwsac1 = killed,
         cas_w_mean_cwsac1 = wounded,
         str_mean_cwsac1 = strength_mean,
         str_var_cwsac1 = strength_var,
         cwsac_id = battle) %>%
  select(cwsac_id, belligerent, matches("(str|cas)_")) %>%
  filter(! grepl("VA020[AB]", cwsac_id))

cwsac2_forces_casstr <-
  cwsac2_forces %>%
  rename(str_mean_cwsac2 = strength_mean,
         str_var_cwsac2 = strength_var,
         cwsac_id = battle) %>%
  select(cwsac_id, belligerent, matches("(str|cas)_")) %>%
  filter(! cwsac_id %in% c("AL002"))

#'
#' ## Shenandoah Data
#'
#' The Shenandoah report data is much more detailed in the disaggregation of casualties in its battles.twi
shenandoah_forces_casstr <-
  shenandoah_forces %>%
  rename(cas_k_mean_shen = killed,
         cas_w_mean_shen = wounded,
         cas_m_mean_shen = missing_captured,
         cas_kwm_mean_shen = casualties) %>%
  mutate(str_mean_shen = unif_mean(strength_min, strength_max),
         str_var_shen = ifelse(strength_min == strength_max,
                          rounded_var(strength_min),
                          unif_var(strength_min, strength_max)),
         cas_k_var_shen = rounded_var(cas_k_mean_shen),
         cas_w_var_shen = rounded_var(cas_w_mean_shen),
         cas_m_var_shen = rounded_var(cas_m_mean_shen),
         cas_kwm_var_shen = rounded_var(cas_kwm_mean_shen)) %>%
  select(belligerent, cwsac_id, matches("^cas_"), matches("^str_"))

shenandoah_battles <- unique(shenandoah_forces$cwsac_id)

casstr <-
  full_join(cwss_forces_casstr, cwsac1_forces_casstr,
            by = c("cwsac_id", "belligerent")) %>%
  full_join(cwsac2_forces_casstr, by = c("cwsac_id", "belligerent")) %>%
  full_join(shenandoah_forces_casstr, by = c("cwsac_id", "belligerent"))


for (j in c("mean", "var")) {
  casstr[[paste0("cas_kwm_", j)]] <-
    pnonmiss(casstr[[paste0("cas_kwm_", j, "_shen")]],
             casstr[[paste0("cas_kwm_", j, "_cwss")]],
             casstr[[paste0("cas_kwm_", j, "_cwsac1")]])
  casstr[[paste0("str_", j)]] <-
    pnonmiss(casstr[[paste0("str_", j, "_shen")]],
             casstr[[paste0("str_", j, "_cwss")]],
             casstr[[paste0("str_", j, "_cwsac2")]],
             casstr[[paste0("str_", j, "_cwsac1")]])
  for (i in c("k", "w", "m")) {
    varname <- paste0("cas_", i, "_", j)
    casstr[[varname]] <-
      pnonmiss(casstr[[paste0(varname, "_shen")]],
               casstr[[paste0(varname, "_cwsac")]])
  }
}

#' Manual edits for VA043 and VA097 (Appomattox Court House)
casstr[["cas_kw_mean"]] <- NA_real_
casstr[["cas_kw_var"]] <- NA_real_
# for (x in extra_data[["forces"]]) {
#   for (j in paste0("cas_", c("kwm", "k", "w", "m", "kw"), "_mean")) {
#     rownum <- which(casstr[["cwsac_id"]] == x
#   }
# }



gen_commanders <- function(cwss_people,
                           cwss_commanders,
                           cwsac_commanders,
                           extra_data) {
  people <-
    bind_rows(cwss_people, extra_data[["people"]])

  cwss_commanders <-
    bind_rows(read_csv(file.path(dst, "cwss_commanders.csv")) %>%
              mutate(BattlefieldCode =
                       plyr::revalue(BattlefieldCode,
                                     c("VA020B" = "VA020",
                                       "VA020A" = "VA020"))) %>%
                rename(PersonID = commander),
              extra_data$commanders %>%
                select(- Name)) %>%
    left_join(select(cwss_people, PersonID, LastName, FirstName, MiddleName,
                     MiddleInitial),
              by = c("PersonID")) %>%
    mutate(belligerent =
             ifelse(grepl("OK00[1-3]", BattlefieldCode) &
                           belligerent == "US",
                           "Native American", belligerent)) %>%
    rename(first_name = FirstName,
           middle_name = MiddleName,
           middle_initial = MiddleInitial,
           last_name = LastName,
           battle = BattlefieldCode)

  cwsac_commanders <-
    cwsac_commanders %>%
    mutate(cwsac = TRUE,
           belligerent = ifelse(grepl("OK00[1-3]", battle) &
                                  belligerent == "US",
                                "Native American", belligerent)) %>%
    filter(! battle %in% c("VA020A", "VA020B"),
           belligerent != "Native American")

  commanders <-
    left_join(cwss_commanders,
              select(cwsac_commanders,
                     battle, belligerent, last_name, rank, navy),
              by = c("battle", "belligerent", "last_name")) %>%
    filter(! battle %in% extra_data[["excluded_battles"]]) %>%
    arrange(belligerent, battle)
  list(people = people, commanders = commanders)
}

#' Build Everything
build <- function(src, dst) {
  extra_data <-
    fromJSON(file.path(src, "rawdata",
                       "nps_combined", "extra_data.json"))

  aad_battles <-
    read_csv(file.path(dst, "aad_battles.csv"))

  cwsac1_battles <-
    read_csv(file.path(dst, "cwsac_battles.csv"))

  cwsac1_forces <-
    read_csv(file.path(dst, "cwsac_forces.csv"))

  cwsac2_battles <-
    read_csv(file.path(dst, "cwsac2_battles.csv"))

  cwsac2_forces <-
    read_csv(file.path(dst, "cwsac2_forces.csv"))

  cwss_battles <-
    read_csv(file.path(dst, "cwss_battles.csv"))

  cwss_forces <-
    read_csv(file.path(dst, "cwss_forces.csv"))

  shenandoah_battles <-
    read_csv(file.path(dst, "shenandoah_battles.csv"))

  shenandoah_forces <-
    read_csv(file.path(dst, "shenandoah_forces.csv"))

  theaters <- read_csv(file.path(dst, "cwss_theaters.csv"))

  campaigns <- bind_rows(read_csv(file.path(dst, "cwss_campaigns.csv")),
                         extra_data[["campaigns"]])

  latlong <-
    read_csv(file.path(src, "rawdata", "nps_combined", "latlong.csv"))

  cwss_people <- read_csv(file.path(dst, "cwss_persons.csv"))

  cwss_commanders <-
    read_csv(file.path(dst, "cwss_commanders.csv"))

  cwsac_commanders <-
    read_csv(file.path(dst, "cwsac_commanders.csv"))

  battlelist <-
    gen_battlelist(cwss_battles, cwsac1_battles,
                   cwsac2_battles, aad_battles)

  battles <-
    gen_battles(cwss_battles,
                cwsac1_battles,
                cwsac2_battles,
                aad_battles,
                shenandoah_battles,
                latlong,
                extra_data)

  commanders <- gen_commanders(cwss_commanders = cwss_commanders,
                               cwsac_commanders = cwsac_commanders,
                               cwss_people = cwss_people,
                               extra_data = extra_data)

  write_csv(theaters, file.path(dst, "nps_theaters.csv"))
  write_csv(campaigns, file.path(dst, "nps_campaigns.csv"))

  write_csv(battlelist, file.path(dst, "nps_battlelist.csv"))
  write_csv(battles, file.path(dst, "nps_battles.csv"))
  write_csv(commanders$commanders, file.path(dst, "nps_commanders.csv"))
  write_csv(commanders$people, file.path(dst, "nps_people.csv"))
 #   write_csv(nps_forces, file.path(dst, "nps_forces.csv"))
}

main <- function() {
  arglist <- commandArgs(TRUE)
  src <- arglist[1]
  dst <- arglist[2]
  src <- "."
  dst <- "data"
  build(src, dst)
}

main()
