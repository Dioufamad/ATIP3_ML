
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

#--3--verify if the accession number corresponding to dataset to download and analyse are existant through these two portals
#http://www.ncbi.nlm.nih.gov/geo/browse/
#GEO2R 


#--4--Setting the dataset to manipulate (some options throughout the script change depending on chosen dataset)
# - uncomment one of these 4 following lines to choose a dataset
cohort <- "Remagus02"
# cohort <- "Remagus04"
# cohort <- "MDAnderson"
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

#--7--Select the best probeset to keep by gene
# 1) Find out annotations features that are interesting to use
# - get a peak at the desired columns to keep in replacement of the probe names
peak_at_names_in_ftdata <- gset@featureData@data # this shows us that "Gene Symbol" can be used as myFtDesired for RO2, R04 and MDA. so we set it at the start of the file 

# 2) changing the names
dictionary = gset@featureData@data[, c('ID', myFtDesired)]  #This is a lookup table for probe ID and ORF 
# test presence of ATIP3 probes : c_dict = dictionary[which(dictionary$"ID" %in% c("212093_s_at","212095_s_at","212096_s_at","239576_at")),]
#==========using JETSET to select the best probeset for each gene
library(jetset)
# the jetset library has these objects : 
# [1] "jmap" "jscores" "scores.hgu133a"
# [4] "scores.hgu133plus2" "scores.hgu95av2" "scores.u133x3p"

# The functions jmap and jscores are the intended user-level interface, and scores.* are data sets
# that support these functions


# jmap is a function that returns the best probe sets matching a list of Entrez GeneIDs, gene symbols, or
# gene aliases.
# 
# jscores is a function that returns the jetset scores for all probe sets matching a list of Entrez GeneIDs,
# gene symbols, aliases, or ensembl IDs.

# see this source for a tutorial on use of JETSET : https://cran.r-project.org/web/packages/jetset/vignettes/jetset.pdf

# - getting the best probes
# - - make sure that correct entrez_gene_id entries only stays in table
dictionary1 = dictionary
list_egi_uniks_in_dict1 = unique(as.character(dictionary1$ENTREZ_GENE_ID))
list_egi_uniks_in_dict1_no_nan <- na.omit(list_egi_uniks_in_dict1) #remove nan
list_egi_uniks_no_nanNunknown = list_egi_uniks_in_dict1_no_nan[list_egi_uniks_in_dict1_no_nan != ""] # remove "" (unknown feature data for probe)
# dictionary1_done = dictionary1[match(list_egi_uniks_no_nanNunknown, dictionary1$ENTREZ_GENE_ID), ] #xxx bad due to eliminating duplicates too early on
dictionary1_done = dictionary1[which(dictionary1$ENTREZ_GENE_ID %in% list_egi_uniks_no_nanNunknown),]
# test presence of ATIP3 probes : c_dict1 = dictionary1_done_bis[which(dictionary1_done_bis$"ID" %in% c("212093_s_at","212095_s_at","212096_s_at","239576_at")),]
# - - make sure that correct gene_symbol entries only stays in table
dictionary2 = dictionary1_done
list_gs_uniks_in_dict2 = unique(as.character(dictionary2$"Gene Symbol"))
list_gs_uniks_in_dict2_no_nan <- na.omit(list_gs_uniks_in_dict2) #remove nan
list_gs_uniks_no_nanNunknown = list_gs_uniks_in_dict2_no_nan[list_gs_uniks_in_dict2_no_nan != ""] # remove "" (unknown feature data for probe)
# dictionary2_done = dictionary2[match(list_gs_uniks_no_nanNunknown, dictionary2$"Gene Symbol"), ] #xxx bad due to eliminating duplicates too early on
dictionary2_done = dictionary2[which(dictionary2$"Gene Symbol" %in% list_gs_uniks_no_nanNunknown),]
# test presence of ATIP3 probes : c_dict2 = dictionary2_done[which(dictionary2_done$"ID" %in% c("212093_s_at","212095_s_at","212096_s_at","239576_at")),]
# - - search the best probes
best_probes_dict = dictionary2_done
best_probes_dict$Best_probe_4_new_ID = "NOT_CHANGED_YET"
for (one_of_the_rownames in rownames(best_probes_dict)) {
  long_egi = best_probes_dict[one_of_the_rownames,"ENTREZ_GENE_ID"]
  the_split_object <- strsplit(long_egi, " /// ") # the object obtained from split (contains only 1 list)
  the_list_of_components = the_split_object[[1]] # get the list containing the splited parts # is list of 1 elt if pattern absent
  for (candidate_egi_to_test in the_list_of_components) {
    search_bestprobe <-jmap(my_ma_platform, eg = candidate_egi_to_test) # best probe for ATIP3/MTUS1 is "212096_s_at" 
    bestprobe<-search_bestprobe[[1]]
    if (is.na(bestprobe)) { # !isNA(bestprobe = is not NA (a best probe has been found) 
    }else{
      best_probes_dict[one_of_the_rownames,"Best_probe_4_new_ID"] = bestprobe # store the best found probe for the long egi
    }
  }
}
# the column Best_probe_4_new_ID has now only NOT_CHANGED_YET or the bestprobeset as values 
# test presence of ATIP3 probes : c_best_probes_dict = best_probes_dict[which(best_probes_dict$"ID" %in% c("212093_s_at","212095_s_at","212096_s_at","239576_at")),]

# tidy the table 
best_probes_list_uniks = unique(as.character(best_probes_dict$"Best_probe_4_new_ID")) # the unique entries among the best probesets for each egi
best_probes_list_uniks_no_placeholder = best_probes_list_uniks[best_probes_list_uniks != "NOT_CHANGED_YET"] # remove the placeholder before knowing the best probesets
best_probes_dict_tidy <- best_probes_dict[ which(best_probes_dict$ID %in% best_probes_list_uniks_no_placeholder), ]  # drop the rows were ID is a bad probe ie ID and Best_probe_4_new_ID are not the same
names(best_probes_dict_tidy) <- c("old1","Gene Symbol","old2","ID") # these two lines will rename the columns and keep Best_probe_4_new_ID as new col ID, and the column Gene Symbol as second column
best_probes_repo = best_probes_dict_tidy[c("ID","Gene Symbol")]
# NB : best_probe_repo do not have the same rows order as the initial expression set so when changing the probes name to gene name, mind that

  
# make a version of the expression set with only the probesets kept
list_of_good_probes = as.character(best_probes_repo$ID)
ex1 <- ex[ which(rownames(ex) %in% list_of_good_probes), ]
list_of_good_probes_inter = rownames(ex1)   # a list of the best probesets 
# # or you can also do this : 
# list_of_good_probes_inter = intersect(list_of_good_probes, row.names(ex))
# ex1 = ex[list_of_good_probes_inter, ]
# test presence of ATIP3 probes : c_ex1 = ex1[which(rownames(ex1) %in% c("212093_s_at","212095_s_at","212096_s_at","239576_at")),]


# make a version of the selection but with gene names instead of probesets names
ex1_bis_with_GS = ex1
best_probes_repo_w_rows_order_of_ex1 = best_probes_repo[rownames(ex1),] # a table of best_probe_repo with rows in the same order as in the rownames of ex1 (the best probesets)
rownames(ex1_bis_with_GS) = best_probes_repo_w_rows_order_of_ex1$"Gene Symbol" # the GS col of a table with rows in the same order as in ex1 with the best probesets as rownames
list_of_good_probes_inter_GS_version = rownames(ex1_bis_with_GS) # a list of the GS for the best probesets 
# test presence of ATIP3 probes : c_ex1_bis_with_GS = ex1_bis_with_GS[which(rownames(ex1_bis_with_GS) %in% c("MTUS1")),]

    
#--8--Histograms to show see if bimodal distribution or not and manually setting the threshold between lowly expressed and highly expressed genes
# plot for two or three samples, each samples probesets kept distribution of values, 100 breaks in histogram

if (cohort=="Remagus02") {
  # for sample 1
  ex_hist_s1 <-ex1[,1]
  hist_s1 <- hist(ex_hist_s1, 100, col = "cornsilk1", freq = FALSE, 
                  main = "Histogram of the intensities for the sample GSM655624 with threshold at 4.0", 
                  border = "antiquewhite4",
                  xlab = "intensities of the best probesets",xlim = c(0,floor(max(ex_hist_s1))))
  man_threshold <- 4
  abline(v = man_threshold, col = "coral4", lwd = 2)
  # for sample 2
  ex_hist_s1 <-ex1[,2]
  hist_s1 <- hist(ex_hist_s1, 100, col = "cornsilk1", freq = FALSE, 
                  main = "Histogram of the intensities for the sample GSM655625 with threshold at 5.4", 
                  border = "antiquewhite4",
                  xlab = "intensities of the best probesets",xlim = c(0,floor(max(ex_hist_s1))))
  man_threshold <- 5.4
  abline(v = man_threshold, col = "coral4", lwd = 2)
  # for sample 3
  ex_hist_s1 <-ex1[,3]
  hist_s1 <- hist(ex_hist_s1, 100, col = "cornsilk1", freq = FALSE, 
                  main = "Histogram of the intensities for the sample GSM655626 with threshold at 4.2", 
                  border = "antiquewhite4",
                  xlab = "intensities of the best probesets",xlim = c(0,floor(max(ex_hist_s1))))
  man_threshold <- 4.2
  abline(v = man_threshold, col = "coral4", lwd = 2)
} else if (cohort=="Remagus04") {
  # for sample 1
  ex_hist_s1 <-ex1[,1]
  hist_s1 <- hist(ex_hist_s1, 100, col = "cornsilk1", freq = FALSE, 
                  main = "Histogram of the intensities for the sample GSM1550388 with threshold at 3.8", 
                  border = "antiquewhite4",
                  xlab = "intensities of the best probesets",xlim = c(0,floor(max(ex_hist_s1))))
  man_threshold <- 3.8
  abline(v = man_threshold, col = "coral4", lwd = 2)
  # for sample 2
  ex_hist_s1 <-ex1[,2]
  hist_s1 <- hist(ex_hist_s1, 100, col = "cornsilk1", freq = FALSE, 
                  main = "Histogram of the intensities for the sample GSM1550389 with threshold at 6.0", 
                  border = "antiquewhite4",
                  xlab = "intensities of the best probesets",xlim = c(0,floor(max(ex_hist_s1))))
  man_threshold <- 6.0
  abline(v = man_threshold, col = "coral4", lwd = 2)
  # for sample 3
  ex_hist_s1 <-ex1[,3]
  hist_s1 <- hist(ex_hist_s1, 100, col = "cornsilk1", freq = FALSE, 
                  main = "Histogram of the intensities for the sample GSM1550390 with threshold at 6.2", 
                  border = "antiquewhite4",
                  xlab = "intensities of the best probesets",xlim = c(0,floor(max(ex_hist_s1))))
  man_threshold <- 6.2
  abline(v = man_threshold, col = "coral4", lwd = 2)
} else if (cohort=="MDAnderson") {
  # for sample 1
  ex_hist_s1 <-ex1[,1]
  hist_s1 <- hist(ex_hist_s1, 100, col = "cornsilk1", freq = FALSE, 
                  main = "Histogram of the intensities for the sample GSM615096 with threshold at 6.0", 
                  border = "antiquewhite4",
                  xlab = "intensities of the best probesets",xlim = c(0,floor(max(ex_hist_s1))))
  man_threshold <- 6
  abline(v = man_threshold, col = "coral4", lwd = 2)
  # for sample 2
  ex_hist_s1 <-ex1[,2]
  hist_s1 <- hist(ex_hist_s1, 100, col = "cornsilk1", freq = FALSE, 
                  main = "Histogram of the intensities for the sample GSM615097 with threshold at 6.6", 
                  border = "antiquewhite4",
                  xlab = "intensities of the best probesets",xlim = c(0,floor(max(ex_hist_s1))))
  man_threshold <- 6.6
  abline(v = man_threshold, col = "coral4", lwd = 2)
  # for sample 3
  ex_hist_s1 <-ex1[,3]
  hist_s1 <- hist(ex_hist_s1, 100, col = "cornsilk1", freq = FALSE, 
                  main = "Histogram of the intensities for the sample GSM615098 with threshold at 6.2", 
                  border = "antiquewhite4",
                  xlab = "intensities of the best probesets",xlim = c(0,floor(max(ex_hist_s1))))
  man_threshold <- 6.2
  abline(v = man_threshold, col = "coral4", lwd = 2)
} else
  print("Replace this statement with a command to store the path of another_dataset_you_want_to_use")



#--9--calculate coefficient of variation and others statistics row wise ie by gene/probeset
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
    
#- part for saving on file and reread anytime
# outfilename = paste(myGSE, "_log2CV.csv", sep='')
# write.csv(myarray, outfilename, row.names=F)
# test = read.csv( outfilename, colClasses = c('character', NA, NA, NA))
# str(test)
# hist(test$myCV, br=100)
# hist(test$myStddev, br=100)
# hist(test$myMean, br=100)



#===============================================================================================
