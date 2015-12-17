suppressPackageStartupMessages({
  library("dplyr")
  library("jsonlite")
  library("magrittr")
  library("stringr")
  library("tidyr")
  library("yaml")
  library("purrr")
})

#'
#' # Utility Functions
#'
write_csv <- function(x, file, ..., log = TRUE) {
  if (log) {
    message("Writing: ", file, "\n")
  }
  write.csv(x, file, ..., na = "", row.names = FALSE)
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


