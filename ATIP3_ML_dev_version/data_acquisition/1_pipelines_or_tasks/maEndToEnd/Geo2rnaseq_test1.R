if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")
BiocManager::install(version = "3.10")
# step : install the workflow package         
BiocManager::install("Geo2RNAseq")


library("Geo2RNAseq")

outDir <- file.path("amad", "outData")
outDir



pkgDir <- system.file("extdata", package = "readxl")
# all files created in this vignette will be written to this directory
outDir <- file.path(pkgDir, "outData")
outDir

list_executables()
geo_dat <- getGEOdata(accession = "GSE116335", outDir = file.path(outDir, "GSE116335"))
