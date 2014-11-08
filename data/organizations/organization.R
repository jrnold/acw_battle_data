#' Simulate distributions of personnel size for military units in the Civil War
#'
#' Often  the number of units is known, but the exact number of troops is not given or known.
#' The following code simulates the size of those units using uncertainty about the number of subunits and the number of troops in a regiment (given attrition).
#'
#' In usage, these may scaled by the "effective" size multipliers used in Livermore (1900), p. 69. The Union army did not consistently report "effective" forces, while the Confederates appeared to do a better job of reporting effective forces.
#'
#' - Union artillery and infantry: 0.93
#' - Union cavalry: 0.85
#' - Proportion of Union officers: 4--7%
#' - Proportion of Confederate officers: 6.5--11%
#'
#' Strength of regiments (Livermore 1900, p. 67).
#' Regiment of 1050 includes 70 non-combatants (10 staff, 20 musicians, 40 band, wagoners, men detailed to HQ, quartermaster of medical).
#'
#' Average regimental present for duty
#'
#' - Shiloh: 560
#' - Fair Oaks: 650
#' - Chancellorsville: 530
#' - Gettysburg: 375
#' - Chickamagua: 440
#' - Wilderness: 440
#' - Sherman's army in May 1864: 305
#'
#' In the OR, numbers of "effectives" in infantry divisions or corps is 89--93 percent of number "present for duty", while in the cavalry these numbers are 83--86 percent.
#' 
#' 
library("plyr")
library("jsonlite")
#library("triangle")
set.seed(276184053)
N <- 500

#' # General Functions
#'
#' The distributions will be summarized by the mean, sd, and 5th, 25th, 50th, 75th, and 95th percentiles.
summarize_data <- function(x) {
    summarize(x,
              mean = mean(troops),
              median = median(troops),
              sd = sd(troops),
              p75 = quantile(troops, 0.75),
              p25 = quantile(troops, 0.25),
              p05 = quantile(troops, 0.05),
              p95 = quantile(troops, 0.95)
              )
}

#' If the exact size of the unit is known (or assumed).
exact_size <- function(n) {
    data.frame(mean = n,
               median = n,
               sd = 0,
               p05 = n, p95 = n,
               p25 = n, p25 = n)
}

#' If the the size of the unit is distributed uniform, then return the exact values:
uniform_size <- function(low, high) {
    range <- high - low
    data.frame(mean = 0.5 * (low + high),
               median = 0.5 * (low + high),
               sd = 0,
               p05 = 0.05 * range + low,
               p25 = 0.25 * range + low,
               p75 = 0.75 * range + low,
               p95 = 0.95 * range + low)

}

#' Special functions to draw the standard units in the infantry.
#' 
#' The number of troops in a regiment is drawn from a uniform distribution
#' between low and high.
draw_regiment <- function(n = 1, low = 300, high = 650) {
    data.frame(troops = round(runif(n, low, high)))
}

draw_brigade <- function(low = 2, high = 12, mode = 4, regiment = draw_regiment) {
    rng <- high - low
    n <- low + rbinom(1, rng, (mode - low) / (rng + 1))
    ## n <- round(rtriangle(1, a = low, b = high, c = mode), 0)
    troops <- sum(regiment(n))
    data.frame(regiments = n, troops = troops)
}

draw_division <- function(low = 2, high = 5, mode = 3, brigade = draw_brigade, ...) {
    #n <- round(rtriangle(1, a = low, b = high, c = mode), 0)
    rng <- high - low
    n <- low + rbinom(1, rng, (mode - low) / (rng + 1))
    ret <- colwise(sum)(rdply(n, brigade(...)))
    ret$.n <- NULL
    ret$brigades <- n
    ret
}

draw_corps <- function(low = 2, high = 6, mode = 3, division = draw_division, ...) {
    rng <- high - low
    n <- low + rbinom(1, rng, (mode - low) / (rng + 1))
    ## n <- round(rtriangle(1, a = low, b = high, c = mode), 0)
    ret <- colwise(sum)(rdply(n, division(...)))
    ret$.n <- NULL
    ret$divisions <- n
    ret
}

draw_army <- function(low = 1, high = 8, mode = 3, corps = draw_corps, ...) {
    rng <- high - low
    n <- low + rbinom(1, rng, (mode - low) / (rng + 1))
    ## n <- round(rtriangle(1, a = low, b = high, c = mode), 0)
    ret <- colwise(sum)(rdply(n, corps(...)))
    ret$.n <- NULL
    ret$corps <- n
    ret
}

#'
#' Ships complements. Get distribution from the complements of all ships found in the
#' Union and Confederate navies on dbpedia.
#' 
#' 
ships <- read.csv("ships.csv")
## Remove outliers and older ships.
ship_complements <-
    summarize(data.frame(troops = with(ships, complement[complement > 10 & complement < 500])),
          mean = mean(troops),
          median = median(troops),
          sd = sd(troops),
          p75 = quantile(troops, 0.75),
          p25 = quantile(troops, 0.25),
          p05 = quantile(troops, 0.05),
          p95 = quantile(troops, 0.95)
          )


#' # Union Army
#'
#' ## Infantry
#'
#' Union companies were 100 men, but assume 30-65%.
union_company <- uniform_size(30, 65)

#' 
#' Union regiments were 1000, but on the field due to attrition ranged between 300 and 400
draw_union_regiment <- function(n) draw_regiment(n, 300, 650)
union_regiment <- uniform_size(300, 650)

#'
#' Brigade: 2-12 regiments per brigade, mode = 4
draw_union_brigade <- function() {
    draw_brigade(low = 2, high = 12, mode = 4,
                 regiment = draw_union_regiment)
}
union_brigade <- summarize_data(rdply(N, draw_union_brigade))

#'
#' Division: 2-5 brigades per division, mode = 3
draw_union_division <- function() {
    draw_division(low = 2, high = 5, mode = 3,
                  brigade = draw_union_brigade)
}
union_division <- summarize_data(rdply(N, draw_union_division))

#'
#' Corps: 2-6 divisions per corps, mode = 3
draw_union_corps <- function () {
    draw_corps(low = 2, high = 6, mode = 3,
               division = draw_union_division)
}
union_corps <- summarize_data(rdply(N, draw_union_corps))

#'
#' Armies: 1-8 corps per army, mode = 3
draw_union_army <- function() {
    draw_army(low = 1, high = 8, mode = 3,
              corps = draw_union_corps)

}
union_army <- summarize_data(rdply(N, draw_union_army))

#'
#' ## Cavalry
#'
#' Union cavalry regiment is the same size as an infantry regiment.
draw_union_cav_regiment <- function(n) draw_regiment(n, 300, 650)
union_cav_regiment <- uniform_size(300, 650)

#'
#' Brigade: 2-20 regiments per brigade, mode = 5
draw_union_cav_brigade <- function() {
    draw_brigade(low = 2, high = 4, mode = 3,
                 regiment = draw_union_cav_regiment)
}
union_cav_brigade <- summarize_data(rdply(N, draw_union_cav_brigade))

#'
#' Division: 2-7 brigades per division, mode = 4
draw_union_cav_division <- function() {
    draw_division(low = 2, high = 4, mode = 3,
                  brigade = draw_union_cav_brigade)
}
union_cav_division <- summarize_data(rdply(N, draw_union_cav_division))
#'
#' Cavalry corps had 3 divisions.
draw_union_cav_corps <- function() {
    draw_corps(low = 3, high = 3, mode = 3,
               brigade = draw_union_cav_division)
}
union_cav_corps <- summarize_data(rdply(N, draw_union_cav_corps))

#'
#' ## Artillery
#'
#' Union artillery regiment is the same size as infantry regiment
union_artillery_regiment <- uniform_size(300, 650)
#'
#' Section = 2 guns, battery = 6 guns; brigades = 5 batteries
union_artillery_section <- exact_size(2 * 12 + 1)
union_artillery_battery <- exact_size(6 * 12 + 1)
union_artillery_brigade <- exact_size((6 * 12 + 1) * 5 + 1)

#'
#'
#' ## Ships
#'
union_ships <- ship_complements

#'
#' # Confederate
#'
#' 

#'
#' ## Infantry
#'
#'
#' Companies of 100, assume 30-65% fill
confed_company <- uniform_size(30, 65)

#'
#' Confed regiments were 1000, but on the field due to attrition ranged between 300 and 400
draw_confed_regiment <- function(n) draw_regiment(n, 300, 400)
confed_regiment <- uniform_size(300, 650)

#' 
#' Brigade: 2-20 regiments per brigade, mode = 5
draw_confed_brigade <- function() {
    draw_brigade(low = 2, high = 12, mode = 5,
                 regiment = draw_confed_regiment)
}
confed_brigade <- summarize_data(rdply(N, draw_confed_brigade))

#'
#' Division: 2-7 brigades per division, mode = 4
draw_confed_division <- function() {
    draw_division(low = 2, high = 7, mode = 4,
                  brigade = draw_confed_brigade)
}
confed_division <- summarize_data(rdply(N, draw_confed_division))

#'
#' Corps: 2-6 divisions per corps, mode = 3
draw_confed_corps <- function () {
    draw_corps(low = 2, high = 12, mode = 3,
               division = draw_confed_division)
}
confed_corps <- summarize_data(rdply(N, draw_confed_corps))

#'
#' Armies: 1-4 corps per army, mode = 2
draw_confed_army <- function() {
    draw_army(low = 1, high = 4, mode = 2,
              corps = draw_confed_corps)
}
confed_army <- summarize_data(rdply(N, draw_confed_army))

#'
#' ## Cavalry
#' 

#'
#' Cavalry regiment, the same size as infantry regiment
draw_confed_cav_regiment <- function(n) draw_regiment(n, 300, 650)
confed_cav_regiment <- uniform_size(300, 650)

#'
#' Brigade: 2-20 regiments per brigade, mode = 5
draw_confed_cav_brigade <- function() {
    draw_brigade(low = 2, high = 4, mode = 3,
                 regiment = draw_confed_cav_regiment)
}
confed_cav_brigade <- summarize_data(rdply(N, draw_confed_cav_brigade))

#'
#' Division: 2-7 brigades per division, mode = 4
draw_confed_cav_division <- function() {
    draw_division(low = 2, high = 4, mode = 3,
                  brigade = draw_confed_cav_brigade)
}
confed_cav_division <- summarize_data(rdply(N, draw_confed_cav_division))

#'
#' Cavalry corps assumed same size as infantry
draw_confed_cav_corps <- function() {
    draw_corps(low = 2, high = 12, mode = 3,
               brigade = draw_confed_cav_division)
}
confed_cav_corps <- summarize_data(rdply(N, draw_confed_cav_corps))

#'
#' ## Artillery
#'
#' Union artillery regiment is the same size as infantry regiment
confed_artillery_regiment <- uniform_size(300, 650)
#'
#' Section = 2 guns, battery = 4 guns; brigades = 5 batteries
confed_artillery_section <- exact_size(2 * 12 + 1)
confed_artillery_battery <- exact_size(4 * 12 + 1)
confed_artillery_brigade <- exact_size((4 * 12 + 1) * 5 + 1)

#'
#' ## Ships
#'
confed_ships <- ship_complements

#'
#' # Data
#'
organization_sizes <-
    list(union =
         list(
             company = union_company,
             regiment = union_regiment,
             brigade = union_brigade,
             division = union_division,
             corps = union_corps,
             army = union_army,
             cavalry_regiment = union_cav_regiment,
             cavalry_brigade = union_cav_brigade,
             cavalry_division = union_cav_division,
             cavalry_corps = union_cav_corps,
             artillery_regiment = union_artillery_regiment,
             artillery_section = union_artillery_section,             
             artillery_battery = union_artillery_battery,
             artillery_brigade = union_artillery_brigade,
             ship = union_ships),
         confederate =
         list(
             company = confed_company,
             regiment = confed_regiment,
             brigade = confed_brigade,
             division = confed_division,
             corps = confed_corps,
             army = confed_army,
             cavalry_regiment = confed_cav_regiment,
             cavalry_brigade = confed_cav_brigade,
             cavalry_division = confed_cav_division,
             cavalry_corps = confed_cav_corps,
             artillery_regiment = confed_artillery_regiment,
             artillery_section = confed_artillery_section,             
             artillery_battery = confed_artillery_battery,
             artillery_brigade = confed_artillery_brigade,
             ship = confed_ships)
         )
             
con <- file("unit_sizes.json", "w")
cat(toJSON(organization_sizes),
    file = con)
close(con)

