#!/usr/bin/env Rscript
#' ---
#' title: Upload data to figshare
#' ---
library("rfigshare")
library("jsonlite")
library("here")
library("glue")
library("withr")

datapackage <- here::here("build/acw_battle_data/datapackage.json")
metadata <- read_json(datapackage)

zipfile <- here::here("build/acw_battle_data.zip")

if (file.exists(zipfile)) {
  cat(glue("{zipfile} exists ... removing."))
  file.remove(zipfile)
}
with_dir("build", {
  zip(zipfile, "acw_battle_data", flags = "-r9X")
})

fs_auth()
id <- metadata$figshare$id
fs_update(id,
          title = metadata$title,
          description = metadata$title,
          type = "dataset",
          mine = TRUE)
fs_add_categories(id, metadata$figshare$categories)
fs_add_tags(id, metadata$keywords)
fs_add_links(id, metadata$homepage)
# fs_add_author ... not needed
# Delete existing files
map_dbl(fs_details(id)$files, "id") %>%
  walk(fs_delete, article_id = id)
fs_upload(id, zipfile)
fs_make_public(id)
