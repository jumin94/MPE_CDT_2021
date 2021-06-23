# Title     : Simple data ingestion example
# Created by: Gabriel Perez
# Created on: 20/05/2021


# Reading data
path <- 'MPEForecastVerification/Project4/data/raw/'
file_ecmwf <- list.files(path, pattern='*ecmwf-JJA-1959-2001.txt', full.names = TRUE)
file_ukmo <- list.files(path, pattern='*ukmo-JJA-1959-2001.txt', full.names = TRUE)
file_mf <- list.files(path, pattern='*mf-JJA-1959-2001.txt', full.names = TRUE)

df_ecmwf <- read.table(file_ecmwf)
df_ukmo <- read.table(file_ukmo)
df_mf <- read.table(file_mf)