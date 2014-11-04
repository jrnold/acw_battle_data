library("lubridate")
library("dplyr")
library("testthat")


INPUT_FILE <- "greer2005_raw.csv"
OUTPUT_FILE <- "greer2005_weekly_casualties.csv"

.data <- 
  (read.csv(INPUT_FILE, stringsAsFactors = FALSE)
   %.% mutate(date = as.Date(date))
  )

alldates <- seq(as.Date("1861-4-7"), as.Date("1865-6-18"), by = "week")

clean_obs <- function(x) {
  if (x$battle != "") {
    uc <- data.frame(date = x$date, battle = x$battle, 
                     confederate = x$casualties_confed,
                     union = x$casualties_union,
                     stringsAsFactors = FALSE)    
  } else {
    uc <- NULL
  }
  if (!is.na(x$attrition_union)) {  
    attrit <- data.frame(date = x$date, battle = "attrition",
                         confederate = x$attrition_confed,
                         union = x$attrition_union,
                         stringsAsFactors = FALSE
                         )
  } else {
    attrit <- NULL
  }
  rbind(uc, attrit)
}

# expect_true(all(.data$date %in% alldates))
# expect_true(all(alldates %in% .data$date))
# expect_equal(nrow(filter(.data, weekdays(date) != "Sunday")), 0L)

data_disagg <- .data %.% rowwise() %.% do(clean_obs(.))

# data_weekly <- (ungroup(data_disagg)
#                 %.% group_by(date)
#                 %.% summarise(union = sum(union, na.rm = TRUE),
#                               confederate = sum(confederate, na.rm = TRUE)))

write.csv(data_disagg, file = OUTPUT_FILE,
          row.names = FALSE, na = "")
