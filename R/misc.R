suppressPackageStartupMessages({
  library("tidyverse")
  library("readr")
  library("jsonlite")
  library("magrittr")
  library("stringr")
  library("yaml")
  library("rlang")
})

#'
#' # Utility Functions
#'
write_csv <- function(x, file, ..., log = TRUE) {
  if (log) {
    message("Writing: ", file)
  }
  readr::write_csv(x, file, ..., na = "")
}

read_csv <- function(x, ...) {
  read.csv(x, ..., stringsAsFactors = FALSE, na = "")
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
      10 ^ (2 * k) / 12
    }
  }
  vapply(x, f, 0)
}

# Parse CWSS unit code into components
parse_unit_code <- function(x) {
  side <- str_sub(x, 1, 1)
  state <- str_sub(x, 2, 3)
  ordinal <- str_replace(str_sub(x, 4, 7), "^0+", "")
  type <- str_sub(x, 8, 8)
  func <- str_sub(x, 9, 9)
  special <- str_sub(x, 10, 10)
  duplicate <- as.integer(str_sub(x, 11, 11))
  duplicate[duplicate == 0] <- NA_integer_
  ethnic <- str_sub(x, 12, 12)
  f <- function(x) ifelse(x == "0" | x == "", NA_character_, x)
  data_frame(unit_code = x,
             side = side,
             state = state,
             ordinal = ordinal,
             type = f(type),
             func = f(func),
             special = f(special),
             duplicate = duplicate,
             ethnic = f(ethnic))
}

#' Generate CWSS unit code from components
gen_unit_code <- function(side, state, ordinal, type, arm, special,
                          duplicate, ethnic) {
  f <- function(x) ifelse(is.na(x), "0", x)
  paste0(paste0(side,
                state,
                str_pad(ordinal, 4, "left", "0")),
         str_replace(paste0(f(type),
                            f(arm),
                            f(special),
                            f(duplicate),
                            f(ethnic), sep = ""),
                     "0+$", ""))
}

na_fill <- function(x, fill = 0) {
  x[is.na(x)] <- fill
  x
}
