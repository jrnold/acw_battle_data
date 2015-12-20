#!/usr/bin/env Rscript
source("R/misc.R")


#' Fix AAD reference IDs
aad_to_cwsac_id <- function(x) {
  plyr::revalue(x, c("AR010A" = "AR010", "GA013A" = "GA013"))
}
#' Fix CWSACII ids
cws2_to_cwsac_id <- function(x) {
  plyr::revalue(x, c("AL002" = "AL009"))
}

#'
#' # Battlelist Comparisons
#'
#' Major differences in battle definitions between AAD, CWSAC I, CWSAC II, and CWSS.
#' Some other battles differ slightly in start and end dates.
#'
gen_battlelist <-
  function(cwss_battles, cwsac_battles,
           cws2_battles, aad_battles) {

  battlelist_cwss <-
    cwss_battles %>%
    select(BattlefieldCode, BattleName) %>%
    rename(cwsac_id = BattlefieldCode, battle_name = BattleName) %>%
    mutate(cwss = TRUE)

  battlelist_cwsac <-
    cwsac_battles %>%
    select(battle, battle_name) %>%
    rename(cwsac_id = battle, battle_name_cwsac = battle_name) %>%
    mutate(cwsac = TRUE)

  battlelist_cws2 <-
    cws2_battles %>%
    select(battle, battle_name) %>%
    rename(cwsac_id = battle, battle_name_cws2 = battle_name) %>%
    mutate(cws2 = TRUE)

  battlelist_aad <-
    aad_battles %>%
    mutate(reference_number = aad_to_cwsac_id(reference_number)) %>%
    select(reference_number, event) %>%
    rename(cwsac_id = reference_number, battle_name_aad = event) %>%
    mutate(aad = TRUE)

  nps_battlelist <-
    battlelist_cwss %>%
    full_join(battlelist_cwsac, by = "cwsac_id") %>%
    full_join(battlelist_cws2, by = "cwsac_id") %>%
    full_join(battlelist_aad, by = "cwsac_id") %>%
    mutate(battle_name = pnonmiss(battle_name, battle_name_cwsac,
                                  battle_name_cws2, battle_name_aad)) %>%
    select(- battle_name_cwsac, - battle_name_cws2, - battle_name_aad) %>%
    mutate(cwss = ! is.na(cwss),
           cwsac = ! is.na(cwsac),
           cws2 = ! is.na(cws2),
           aad = ! is.na(aad),
           notall = ! apply(cbind(cwss, cwsac, cws2, aad), 1, all))
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
#'    - 1863-8-17 to 1863-12-31 : AAD, CWSAC I
#' 		- 1863-8-17 to 1863-9-8 : CWSAC II, CWSS
#'
#' 	- SC009 Charleston Harbor II
#'
#'    - 1863-9-7 to 1863-9-8: AAD, CWSAC I
#' 		- 1963-8-22 to 1863-8-23 and 1863-9-5 to 1863-9-8 : CWSAC II
#' 		- 1863-9-5 to 1863-9-8 : CWSS
#'
#' - AR018 Bayou Meto (1863-8-27) only appears in CWSAC II
#' - VA126 "Cumberland Gap" (1865-4-6) only appears in CWSS. This appears to just be another name for Sayler's Creek. It is the same day as Sayler's Creek, has the same commanders (Sheridan, Ewell), and has alternate names referring to Sayler's Creek (Hillsman Farm, Locett Farm).
#' - GA024 Dalton III (1864-10-13): only appears in AAD and CWSS.
#' - AL008 Ebenezer Church (?): only appears in CWSS (but no data). This is probably the battle on April 1, 1865 between Wilson and Forrest, the day before the Battle of Selma on April 2, 1865.
#' - White Oak Swamp and Glendale (VA020)
#'
#'    - Split into VA020a (White Oak Swamp) into VA020b (Glendale) : AAD, CWSAC I
#' 	  - Combined: CWSAC II
#' 	  - CWSAC has data with VA020A, VA020B, and VA020
#'
#' Which to exclude?
#'

CWSS_RESULTS = c("Union Victory" = "Union",
                 "Union Victory (strategic)" = "Union",
                 "Confederate Victory (tactical)" = "Confederate",
                 "Confederate Victory" = "Confederate")

#'
#' # Battle-Level Data
#'
#' Combine battle-level stats for each battle.
#'
gen_battles <-
  function(cwss_battles,
           cwsac_battles,
           cws2_battles,
           aad_battles,
           shenandoah_battles,
           latlong,
           extra_battles,
           forces,
           excluded_battles) {

  nps_battles_cwss <- cwss_battles %>%
    filter(! BattlefieldCode %in% c("VA020A")) %>%
    mutate(BattlefieldCode =
             plyr::revalue(BattlefieldCode, c("VA020B" = "VA020")),
           BattleName = ifelse(BattlefieldCode == "VA020",
                               "Glendale/White Oak Swamp", BattleName)) %>%
    rename(cwsac_id = BattlefieldCode,
           battle_name = BattleName,
           battle_type_cwss = BattleType,
           start_date = BeginDate,
           end_date = EndDate,
           theater_code = TheaterCode,
           campaign_code = CampaignCode,
           result = Result,
           summary = Summary,
           cas_kwm_cwss = TotalCasualties,
           cwss_url = URL) %>%
    select(- Comment, - ID, - State,
           - matches("summary")) %>%
    mutate(partof_cwss = TRUE,
           result = plyr::revalue(result, CWSS_RESULTS))

  nps_battles_cwsac <- cwsac_battles %>%
    filter(! battle %in% c("VA020A", "VA020B")) %>%
    select(battle, operation, forces_text, casualties_text, results_text,
           preservation, significance, url, battle_name,
           start_date, end_date,
           result, casualties, strength) %>%
    rename(cwsac_url = url, cwsac_id = battle,
           battle_name_cwsac = battle_name,
           start_date_cwsac = start_date,
           end_date_cwsac = end_date,
           result_cwsac = result,
           cas_kwm_cwsac = casualties,
           str_cwsac = strength) %>%
    mutate(partof_cwsac = TRUE,
           result_cwsac = plyr::revalue(result_cwsac,
                                         c("Inconclusive" = "Indecisive")))

  nps_battles_cws2 <- cws2_battles %>%
    select(battle, url, study_area, core_area, potnr_boundary,
           battle_name, strength) %>%
    rename(cwsac_id = battle, cws2_url = url,
           battle_name_cws2 = battle_name,
           str_cws2 = strength) %>%
    mutate(partof_cws2 = TRUE)

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
    select(cwsac_id, lat, long)

  forces_agg <- forces %>%
    group_by(cwsac_id) %>%
    summarize(cas_kwm_forces = sum(cas_kwm_mean),
              str_forces = sum(str_mean))

  nps_battles <-
    nps_battles_cwss %>%
      full_join(nps_battles_cwsac, by = "cwsac_id") %>%
      full_join(nps_battles_cws2, by = "cwsac_id") %>%
      full_join(nps_battles_aad, by = "cwsac_id") %>%
      full_join(nps_battles_shenandoah, by = "cwsac_id") %>%
      left_join(nps_latlong, by = "cwsac_id") %>%
      left_join(forces_agg, by = "cwsac_id") %>%
      filter(! cwsac_id %in% excluded_battles) %>%
      mutate(partof_cwss = ! is.na(partof_cwss),
             partof_cwsac = ! is.na(partof_cwsac),
             partof_cws2 = ! is.na(partof_cws2),
             partof_aad = ! is.na(partof_aad),
             partof_shenandoah = ! is.na(partof_shenandoah),
             battle_name =
               pnonmiss(battle_name, battle_name_cwsac,
                        battle_name_cws2,
                        battle_name_aad),
             result = pnonmiss(result, result_cwsac),
             start_date = pnonmiss(start_date, start_date_cwsac),
             end_date = pnonmiss(end_date, end_date_cwsac),
             state = str_sub(cwsac_id, 1, 2),
             str_total = pnonmiss(str_forces, str_cws2, str_cwsac),
             cas_kwm_total = pnonmiss(cas_kwm_forces,
                                      cas_kwm_cwss, cas_kwm_cwsac)) %>%
      select(- matches("battle_name_(cwsac|cws2|aad)"),
             - matches("(start|end)_date_cwsac"),
             - matches("result_cwsac"),
             - matches("(cas_kwm|str)_(forces|cwsac|cws2|cwss)"))

  #' Fill in campaigns and theaters,
  extra_battles <- extra_battles
  for (i in names(extra_battles)) {
    x <- extra_battles[[i]]
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

gen_forces <- function(cwss_forces,
                       cwsac_forces,
                       cws2_forces,
                       shenandoah_forces,
                       extra_forces,
                       excluded_battles) {
  # Adjust VA020. Only use cas/strength from VA020.
  # Drop AL002, since it refers to a different battle than the Battle of Athens
  cwss_forces_casstr <-
    cwss_forces %>%
    filter(! BattlefieldCode %in% c("VA020A")) %>%
    mutate(BattlefieldCode =
             ifelse(BattlefieldCode == "VA020B", "VA020", BattlefieldCode)) %>%
    rename(cwsac_id = BattlefieldCode,
           cas_kwm_mean_cwss = Casualties,
           str_mean_cwss = TroopsEngaged) %>%
    mutate(str_mean_cwss = ifelse(str_mean_cwss == 0, NA_real_, str_mean_cwss),
           str_var_cwss = rounded_var(str_mean_cwss),
           cas_kwm_var_cwss = rounded_var(cas_kwm_mean_cwss),
           belligerent =
             ifelse(grepl("OK00[1-3]", cwsac_id) &
                      belligerent == "US",
                    "Native American", belligerent))

  cwsac_forces_casstr <-
    cwsac_forces %>%
    filter(! battle %in% c("VA020A", "VA020B")) %>%
    mutate(cas_m_mean_cwsac = psum(missing, captured),
           cas_kwm_mean_cwsac = casualties,
           cas_k_mean_cwsac = killed,
           cas_w_mean_cwsac = wounded,
           str_mean_cwsac = unif_mean(strength_min, strength_max),
           str_var_cwsac = ifelse(strength_min == strength_max,
                                  rounded_var(strength_min),
                                  unif_var(strength_min, strength_max)),
           cas_kwm_var_cwsac = rounded_var(casualties),
           cas_k_var_cwsac = rounded_var(cas_k_mean_cwsac),
           cas_w_var_cwsac = rounded_var(cas_w_mean_cwsac),
           cas_m_var_cwsac = rounded_var(cas_m_mean_cwsac),
           cwsac_id = battle) %>%
    select(cwsac_id, belligerent, matches("(str|cas)_"))

  cws2_forces_casstr <-
    cws2_forces %>%
    rename(str_mean_cws2 = strength,
           cwsac_id = battle) %>%
    select(cwsac_id, belligerent, matches("(str|cas)_")) %>%
    filter(! cwsac_id %in% c("AL002")) %>%
    mutate(belligerent =
             ifelse(grepl("OK00[1-3]", cwsac_id) &
                      belligerent == "US",
                    "Native American", belligerent),
           str_var_cws2 = rounded_var(str_mean_cws2))

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

  casstr <-
    full_join(cwss_forces_casstr, cwsac_forces_casstr,
              by = c("cwsac_id", "belligerent")) %>%
    full_join(cws2_forces_casstr, by = c("cwsac_id", "belligerent")) %>%
    full_join(shenandoah_forces_casstr, by = c("cwsac_id", "belligerent"))


  for (j in c("mean", "var")) {
    casstr[[paste0("cas_kwm_", j)]] <-
      pnonmiss(casstr[[paste0("cas_kwm_", j, "_shen")]],
               casstr[[paste0("cas_kwm_", j, "_cwss")]],
               casstr[[paste0("cas_kwm_", j, "_cwsac")]])
    casstr[[paste0("str_", j)]] <-
      pnonmiss(casstr[[paste0("str_", j, "_shen")]],
               casstr[[paste0("str_", j, "_cwss")]],
               casstr[[paste0("str_", j, "_cws2")]],
               casstr[[paste0("str_", j, "_cwsac")]])
    for (i in c("k", "w", "m")) {
      varname <- paste0("cas_", i, "_", j)
      casstr[[varname]] <-
        pnonmiss(casstr[[paste0(varname, "_shen")]],
                 casstr[[paste0(varname, "_cwsac")]])
    }
  }

  #' Manual edits
  casstr[["cas_kw_mean"]] <- NA_real_
  casstr[["cas_kw_var"]] <- NA_real_
  for (i in names(extra_forces)) {
    x <- extra_forces[[i]]
    for (j in grep("^(cas|str)_.*(mean|var)", names(x), value = TRUE)) {
      keys <- str_split_fixed(i, fixed("|"), 2)
      cwsac_id <- keys[1, 1]
      belligerent <- keys[1, 2]
      rownum <- which(casstr[["cwsac_id"]] == cwsac_id &
                      casstr[["belligerent"]] == belligerent)
      casstr[rownum, j] <-
        if (! is.null(x[[j]])) {
          x[[j]]
        } else {
          NA_real_
        }
    }
  }

  casstr %>%
    select(cwsac_id, belligerent,
           matches("^cas_(k|w|m|kw|kwm)_(mean|var)$"),
           matches("^str_(mean|var)$")) %>%
    fill_casualty_vars() %>%
    filter(! cwsac_id %in% excluded_battles) %>%
    arrange(cwsac_id, belligerent)

}

gen_people <- function(cwss_people, extra_people) {
    bind_rows(cwss_people %>%
                rename(person_id = PersonID,
                       last_name = LastName,
                       first_name = FirstName,
                       middle_name = MiddleName,
                       middle_initial = MiddleInitial,
                       suffix = Suffix,
                       keywords = Keywords,
                       rank = Rank,
                       bio = Bio,
                       bio_source = BioSource,
                       narrative_link_1 = NarrativeLink1,
                       narrative_link_2 = NarrativeLink2
                       ) %>%
                select(- ID) %>%
                mutate(added = FALSE),
              extra_people %>% mutate(added = TRUE))
}

#' - Editing VA068, VA095
#' - Add commanders for some other battles
#'
gen_commanders <- function(cwss_commanders,
                           cwsac_commanders,
                           extra_commanders,
                           people,
                           excluded_battles) {

  people_ <- select(people, person_id,
                    last_name, suffix, first_name,
                    middle_name, middle_initial)

  cwss_commanders_ <- cwss_commanders %>%
    mutate(BattlefieldCode =
             plyr::revalue(BattlefieldCode,
                           c("VA020B" = "VA020",
                             "VA020A" = "VA020")),
           belligerent = ifelse(grepl("OK00[1-3]", BattlefieldCode) &
                                belligerent == "US",
                                "Native American", belligerent),
           added = FALSE) %>%
    filter(! BattlefieldCode %in% c("VA068", "VA095")) %>%
    filter(! (BattlefieldCode == "SC009" & belligerent == "US")) %>%
    rename(cwsac_id = BattlefieldCode) %>%
    bind_rows(select(extra_commanders, - name) %>%
                mutate(added = TRUE)) %>%
    left_join(people_, by = c("commander" = "person_id"))

  cwsac_commanders_ <-
    cwsac_commanders %>%
    mutate(cwsac = TRUE,
           belligerent = ifelse(grepl("OK00[1-3]", battle) &
                                  belligerent == "US",
                                "Native American", belligerent)) %>%
    filter(! battle %in% c("VA020A", "VA020B"),
           belligerent != "Native American") %>%
    rename(cwsac_id = battle)

  left_join(cwss_commanders_,
            select(cwsac_commanders_, cwsac_id, belligerent,
                   last_name, rank, navy),
            by = c("cwsac_id", "belligerent", "last_name")) %>%
    group_by(cwsac_id, belligerent) %>%
    mutate(commander_number = row_number()) %>%
    arrange(cwsac_id, belligerent, commander_number)
}

gen_units <- function(cwss_units, extra_units) {
  bind_rows(mutate(cwss_units, added = FALSE),
            mutate(jsonlite:::simplify(extra_units),
                   added = TRUE))

}

gen_battle_units <- function(cwss_battle_units, extra_battle_units) {
  to_df <- function(x) {
    bind_rows(bind_rows(map(x[["US"]][["units"]], as_data_frame)) %>%
                mutate(belligerent = "US"),
              bind_rows(map(x[["Confederate"]][["units"]], as_data_frame)) %>%
                mutate(belligerent = "Confederate"))
  }
  extra_battle_units_ <-
    sapply(names(extra_battle_units),
           function(k) {
             to_df(extra_battle_units[[k]]) %>%
               mutate(cwsac_id = k)
           }) %>% bind_rows()

  BELLIGERENTS <- c("U" = "US", "C" = "Confederate")

  bind_rows(cwss_battle_units %>%
              rename(cwsac_id = BattlefieldCode,
                     comment = Comment,
                     unit_code = UnitCode) %>%
              mutate(belligerent = BELLIGERENTS[str_sub(unit_code, 1, 1)],
                     added = FALSE),
            extra_battle_units_)

}

#' Build Everything
build <- function(src, dst) {
  nps_dir <- file.path(src, "rawdata", "nps_combined")

  extra_battles <- yaml.load_file(file.path(nps_dir, "battles.yaml"))
  extra_battle_units <- yaml.load_file(file.path(nps_dir, "battleunits.yaml"))
  extra_forces <- yaml.load_file(file.path(nps_dir, "forces.yaml"))
  extra_data <- yaml.load_file(file.path(nps_dir, "extra.yaml"))
  extra_people <- read_csv(file.path(nps_dir, "people.csv"))
  extra_commanders <- read_csv(file.path(nps_dir, "commanders.csv"))
  latlong <-
    read_csv(file.path(src, "rawdata", "nps_combined", "latlong.csv"))

  aad_battles <-
    read_csv(file.path(dst, "aad_battles.csv"))

  cwsac_battles <-
    read_csv(file.path(dst, "cwsac_battles.csv"))
  cwsac_forces <-
    read_csv(file.path(dst, "cwsac_forces.csv"))
  cwsac_commanders <-
    read_csv(file.path(dst, "cwsac_commanders.csv"))

  cws2_battles <-
    read_csv(file.path(dst, "cws2_battles.csv"))
  cws2_forces <-
    read_csv(file.path(dst, "cws2_forces.csv"))

  cwss_battles <-
    read_csv(file.path(dst, "cwss_battles.csv"))
  cwss_forces <-
    read_csv(file.path(dst, "cwss_forces.csv"))
  cwss_theaters <- read_csv(file.path(dst, "cwss_theaters.csv"))
  cwss_campaigns <- read_csv(file.path(dst, "cwss_campaigns.csv"))
  cwss_people <- read_csv(file.path(dst, "cwss_people.csv"))
  cwss_commanders <-
    read_csv(file.path(dst, "cwss_commanders.csv"))
  cwss_units <- read_csv(file.path(dst, "cwss_regiments_units.csv"))
  cwss_battle_units <-
    read_csv(file.path(dst, "cwss_battle_units.csv"))


  shenandoah_battles <-
    read_csv(file.path(dst, "shenandoah_battles.csv"))
  shenandoah_forces <-
    read_csv(file.path(dst, "shenandoah_forces.csv"))

  battlelist <-
    gen_battlelist(cwss_battles,
                   cwsac_battles,
                   cws2_battles,
                   aad_battles)

  people <- gen_people(cwss_people, extra_people)

  commanders <- gen_commanders(cwss_commanders,
                               cwsac_commanders,
                               extra_commanders,
                               people,
                               extra_data[["excluded_battles"]])

  units <- gen_units(cwss_units, extra_battle_units[["units"]])
  battle_units <- gen_battle_units(cwss_battle_units,
                                   extra_battle_units[["battles"]])

  forces <-
    gen_forces(cwss_forces,
               cwsac_forces,
               cws2_forces,
               shenandoah_forces,
               extra_forces,
               extra_data[["excluded_battles"]])

  battles <-
    gen_battles(cwss_battles,
                cwsac_battles,
                cws2_battles,
                aad_battles,
                shenandoah_battles,
                latlong,
                extra_battles,
                forces,
                extra_data[["excluded_battles"]])


  write_csv(battlelist, file.path(dst, "nps_battlelist.csv"))

  write_csv(cwss_theaters, file.path(dst, "nps_theaters.csv"))
  write_csv(cwss_campaigns, file.path(dst, "nps_campaigns.csv"))
  write_csv(commanders, file.path(dst, "nps_commanders.csv"))
  write_csv(people, file.path(dst, "nps_people.csv"))
  write_csv(units, file.path(dst, "nps_units.csv"))
  write_csv(battle_units, file.path(dst, "nps_battle_units.csv"))
  write_csv(battles, file.path(dst, "nps_battles.csv"))
  write_csv(forces, file.path(dst, "nps_forces.csv"))

}

main <- function() {
  arglist <- commandArgs(TRUE)
  src <- arglist[1]
  dst <- arglist[2]
  build(src, dst)
}

main()
