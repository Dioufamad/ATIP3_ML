
####>>>>>>>>>>> SCRIPT FOR GEO DATASETS EXPRESSION ANALYSIS <<<<<<<<### 
# source : https://github.com/hongqin/RCompBio/blob/master/ncbigeo/ncbiGEO2012Nov14-demo-youtube.R
# tutorial here : https://www.youtube.com/watch?v=gC-WuK4BbJY&list=PLMpDEwpxDXcYl4fBsFpom95SBaymcNGpm&index=3&t=0s
#2012 Nov 14

#--1--Clean up the environment (optional)
# rm(list=ls())

#--2--Load needed librairies
# # - install to make if library GEOquery is not yet installed
# source("http://bioconductor.org/biocLite.R")
# biocLite("GEOquery")

library(GEOquery)
library(psych) # to compute geometric mean
install.packages("psych",dependencies = TRUE)          # Install psych package
library("psych")   

#--3--verify if the accession number corresponding to dataset to download and analyse are existant through these two portals
#http://www.ncbi.nlm.nih.gov/geo/browse/
#GEO2R 


#--4--Setting the dataset to manipulate (some options throughout the script change depending on chosen dataset)
# - uncomment one of these 4 following lines to choose a dataset
# cohort <- "Remagus02"
# cohort <- "Remagus04"
cohort <- "MDAnderson"
# cohort <-  "another_dataset_you_want_to_use"

#--5--store the related infos necessary to analysis and changing from dataset to datset
if (cohort=="Remagus02") {
  myGSE = "GSE26639" # R02
  myGPL = "GPL570"
  myFtDesired <-c("Gene Symbol","ENTREZ_GENE_ID")
  my_ma_platform = "hgu133plus2"
} else if (cohort=="Remagus04") {
  myGSE = "GSE63471" # R04  
  myGPL = "GPL571" 
  myFtDesired <-c("Gene Symbol","ENTREZ_GENE_ID")
  my_ma_platform = "hgu133a" # NB : we use hgu133a because we did not find the u133A 2.0 that is really used to produce  R04
} else if (cohort=="MDAnderson") {
  myGSE = "GSE25066" # MDA
  myGPL = "GPL96"
  myFtDesired <-c("Gene Symbol","ENTREZ_GENE_ID")
  my_ma_platform = "hgu133a"
} else
  print("Replace this statement with a command to store the path of another_dataset_you_want_to_use")


#--6--Download raw data and make an expression set from it
gset_raw <- getGEO(myGSE, GSEMatrix =TRUE)
if (length(gset_raw) > 1) idx <- grep(myGPL, attr(gset_raw, "names")) else idx <- 1
gset <- gset_raw[[idx]]

ex <- exprs(gset) #This is the expression matrix

if (cohort=="Remagus02") {
  list_of_atip3_probes <- c("Model","212093_s_at","212095_s_at","212096_s_at","239576_at") # for R02
} else if (cohort=="Remagus04") {
  list_of_atip3_probes <- c("Model","212093_s_at","212095_s_at","212096_s_at") # for R04
} else if (cohort=="MDAnderson") {
  list_of_atip3_probes <- c("Model","212093_s_at","212095_s_at","212096_s_at") # for MDA
} else
  print("Replace this statement with a command to rename the columns with shorter names in another_dataset_you_want_to_use")


ex_atip3_only <- ex[ which(rownames(ex) %in% list_of_atip3_probes), ]
myarray <-t(ex_atip3_only)
summary(myarray)

myarray1 <- cbind(myarray,apply(myarray,1,geoMean))

myVar = apply(myarray, 1, FUN=function(x){geometric.mean(x, na.rm=T)})

ex4=

ex4 = ex1 
myVar = apply( ex4, 1, FUN=function(x){var(x, na.rm=T)}) # compute variance after removal of NA values 
myStddev = sqrt(myVar) # compute std dev
myMean = apply( ex4, 1, FUN=function(x){mean(x, na.rm=T)})
myCV = myStddev / myMean
myarray= data.frame(cbind( myStddev, myMean, myCV))
myarray$GS_best_probeset = list_of_good_probes_inter_GS_version
myarray = myarray[, c(4, 1:3)]
summary(myarray)
hist(myarray$myCV, br=100)
hist(myarray$myStddev, br=100)
hist(myarray$myMean, br=100)