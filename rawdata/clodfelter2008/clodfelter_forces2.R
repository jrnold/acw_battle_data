library("tidyr")

clean_forces <- function(file_clodfelter_forces, file_unit_sizes) {
  
  unit_sizes <- read.csv(file_unit_sizes,
                         stringsAsFactors = FALSE)

  unit_type_map <- c(
    ## "strength",
    ## "infantry",
    ## "cavalry",
    ## "crewmen",
    "corps" = "infantry corps",
    "cavalry_corps" = "cavalry corps",
    "divisions" = "infantry division",
    "cavalry_divisions" = "cavalry division",
    "brigades" = "infantry brigade",
    "companies" = "infantry company"
  )
  
  unit_size_values_ <-
    expand.grid(belligerent = c("union", "confed"),
                unit_type = c("strength", "infantry",
                              "cavalry", "crewmen")) %>%
    mutate(mean = 1, sd = NA_real_)
  
  unit_size_values <-
    unit_sizes %>%
    select(belligerent, unit_type, mean, sd) %>%
    mutate(belligerent = plyr::revalue(belligerent, 
                                       c("Union" = "union", 
                                         "Confederate" = "confed"))) %>%
    rbind(unit_size_values_)

  
  clodfelter_forces <-
    read.csv(file_clodfelter_forces,
             stringsAsFactors = FALSE)
  
  clodfelter_str <-
    clodfelter_forces %>%
    select(battle, belligerent, 
            strength, cavalry, infantry, 
            corps,cavalry_corps, divisions,
            cavalry_divisions, 
            brigades, companies) %>%
     gather(unit_type, value, -battle, -belligerent, na.rm=TRUE) %>%
     mutate(unit_type =
              as.character(plyr::revalue(unit_type, unit_type_map))) %>%
     left_join(unit_size_values, by = c("unit_type", "belligerent")) %>%
     mutate(strength_mean = value * mean,
                strength_var = value * sd ^ 2) %>%
     group_by(battle, belligerent) %>%
     select(battle, belligerent, strength_mean, strength_var) %>%
     summarise_each(funs(sum))
  
  left_join(clodfelter_forces, clodfelter_str,
            c("battle", "belligerent"))
  
}

forces <- clean_forces("clodfelter_forces.csv", "../unit_sizes/unit_sizes.csv")
write.csv(forces, "clodfelter_forces2.csv",
          row.names = FALSE, na = "")
