
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

#--5--store the related infos necessary to analysis and changing from dataset to datset ##! add entries for the remaining GSEs
myGSE = "GSE25055" # used also to set the dataset's name
myGPL = "GPL96"
#--4.4--Setting the type of probesets to keep (all probests or the best probeset) ##! later on add a treatment to get the summarized ones into genes
part_of_probesets_kept <- "ATIP3probesetsonly"
#--4.5--Setting the version to save (with probes name or genes names)
version_to_save <- "probesnames"


#--5--old storing code
# if (cohort=="Remagus02") {
#   myGSE = "GSE26639" # R02
#   myGPL = "GPL570"
#   myFtDesired <-c("Gene Symbol","ENTREZ_GENE_ID")
#   my_ma_platform = "hgu133plus2"
# } else if (cohort=="Remagus04") {
#   myGSE = "GSE63471" # R04  
#   myGPL = "GPL571" 
#   myFtDesired <-c("Gene Symbol","ENTREZ_GENE_ID")
#   my_ma_platform = "hgu133a" # NB : we use hgu133a because we did not find the u133A 2.0 that is really used to produce  R04
# } else if (cohort=="MDAnderson") {
#   myGSE = "GSE25066" # MDA
#   myGPL = "GPL96"
#   myFtDesired <-c("Gene Symbol","ENTREZ_GENE_ID")
#   my_ma_platform = "hgu133a"
# } else
#   print("Replace this statement with a command to store the path of another_dataset_you_want_to_use")


#--6--Download raw data and make an expression set from it
gset_raw <- getGEO(myGSE, GSEMatrix =TRUE)
if (length(gset_raw) > 1) idx <- grep(myGPL, attr(gset_raw, "names")) else idx <- 1
gset <- gset_raw[[idx]]

ex <- exprs(gset) #This is the expression matrix

#####################################trial for ATIP3probesetsonly
#--7--restrict the dataset to the samples that are TNBC and PCR is available and with only the columns of as ATIP3 probesets
# 1) get info a report on the cohort composition, keep a table of the TNBC samples for future restriction on them
# - get a peak at the desired columns
peak_at_names_in_phdata <- gset@phenoData@data
# - see the cols names to copy what to keep
colnames(peak_at_names_in_phdata)
# - make the restriction 
myphcolsDesired <- c("geo_accession","characteristics_ch1.6","characteristics_ch1.4","characteristics_ch1.5","characteristics_ch1.11")
peak_at_names_in_phdata_restricted <- peak_at_names_in_phdata[, myphcolsDesired]
# rename the cols for more controlable colnames
names(peak_at_names_in_phdata_restricted) <- c("geo_accession","ER_status","PR_status","HER2_status","pCR_status") # these two lines will rename the columns
# make the cols entries as strings to be able to change the content
peak_at_names_in_phdata_restricted$geo_accession <- as.character(peak_at_names_in_phdata_restricted$geo_accession) 
peak_at_names_in_phdata_restricted$ER_status <- as.character(peak_at_names_in_phdata_restricted$ER_status) 
peak_at_names_in_phdata_restricted$PR_status <- as.character(peak_at_names_in_phdata_restricted$PR_status) 
peak_at_names_in_phdata_restricted$HER2_status <- as.character(peak_at_names_in_phdata_restricted$HER2_status) 
peak_at_names_in_phdata_restricted$pCR_status <- as.character(peak_at_names_in_phdata_restricted$pCR_status) 
# display the unique values in each column to copy them later in the line changing the content
unique(peak_at_names_in_phdata_restricted$ER_status) 
unique(peak_at_names_in_phdata_restricted$PR_status) 
unique(peak_at_names_in_phdata_restricted$HER2_status) 
unique(peak_at_names_in_phdata_restricted$pCR_status) 
# make a better content of each col
peak_at_names_in_phdata_restricted$ER_status[which((peak_at_names_in_phdata_restricted$ER_status %in% c("er_status_ihc_esr1_for indeterminate: P")))]<-"positive"
peak_at_names_in_phdata_restricted$ER_status[which((peak_at_names_in_phdata_restricted$ER_status %in% c("er_status_ihc_esr1_for indeterminate: N")))]<-"negative"
peak_at_names_in_phdata_restricted$PR_status[which((peak_at_names_in_phdata_restricted$PR_status %in% c("pr_status_ihc: P")))]<-"positive"
peak_at_names_in_phdata_restricted$PR_status[which((peak_at_names_in_phdata_restricted$PR_status %in% c("pr_status_ihc: N")))]<-"negative"
peak_at_names_in_phdata_restricted$HER2_status[which((peak_at_names_in_phdata_restricted$HER2_status %in% c("her2_status: P")))]<-"positive"
peak_at_names_in_phdata_restricted$HER2_status[which((peak_at_names_in_phdata_restricted$HER2_status %in% c("her2_status: N")))]<-"negative"
peak_at_names_in_phdata_restricted$pCR_status[which((peak_at_names_in_phdata_restricted$pCR_status %in% c("pathologic_response_pcr_rd: pCR")))]<-"Yes"
peak_at_names_in_phdata_restricted$pCR_status[which((peak_at_names_in_phdata_restricted$pCR_status %in% c("pathologic_response_pcr_rd: RD")))]<-"No"
# restrict to taxanes treated patients 
# peak_at_names_in_phdata_restricted_b4_tax_restriction <- peak_at_names_in_phdata_restricted  # already all samples are treated with taxanes # 310 samples
# peak_at_names_in_phdata_restricted <- peak_at_names_in_phdata_restricted[which((peak_at_names_in_phdata_restricted$treatment %in% c("treatment arm: Paclitaxel"))),] # 310 samples
# make the TNBC column
peak_at_names_in_phdata_restricted$TNBC <- "NOT_CHANGED_YET"
peak_at_names_in_phdata_restricted$TNBC[which((peak_at_names_in_phdata_restricted$HER2_status %in% c("positive"))
                                              |(peak_at_names_in_phdata_restricted$ER_status %in% c("positive"))
                                              |(peak_at_names_in_phdata_restricted$PR_status %in% c("positive")))]<-"no"
peak_at_names_in_phdata_restricted$TNBC[which((peak_at_names_in_phdata_restricted$HER2_status %in% c("negative"))
                                              &(peak_at_names_in_phdata_restricted$ER_status %in% c("negative"))
                                              &(peak_at_names_in_phdata_restricted$PR_status %in% c("negative")))]<-"yes"
peak_at_names_in_phdata_restricted2TNBC <- peak_at_names_in_phdata_restricted[which(peak_at_names_in_phdata_restricted$TNBC %in% c("yes")),] ##! to save  # 114 samples


# 2) find the MTUS1 probes and restrict dataset to them
# - get a peak at the desired columns to look for the gene name 
peak_at_names_in_ftdata <- gset@featureData@data # this shows us that "Gene Symbol" can be used as myFtDesired for RO2, R04 and MDA. so we set it at the start of the file 
# - see the cols names to copy what to keep
colnames(peak_at_names_in_ftdata)
# - make the restriction 
myFtDesired <- c("ID","Gene Symbol","ENTREZ_GENE_ID")
# 2) changing the names
peak_at_names_in_ftdata_restricted <- peak_at_names_in_ftdata[, myFtDesired] 
# compute the number of genes tracked by the probes
list_of_uniques_genes_tracked = unique(as.character(peak_at_names_in_ftdata_restricted$"Gene Symbol"))
list_of_uniques_genes_tracked_no_nan <- na.omit(list_of_uniques_genes_tracked) #remove nan
list_of_uniques_genes_tracked_no_nanNunknown = list_of_uniques_genes_tracked_no_nan[list_of_uniques_genes_tracked_no_nan != ""] # remove "" (unknown feature data for probe)
num_of_uniques_genes_tracked <- length(list_of_uniques_genes_tracked_no_nanNunknown) # 13515 uniques genes tracked
# test presence of ATIP3 probes : c_dict = peak_at_names_in_ftdata_restricted[which(peak_at_names_in_ftdata_restricted$"ID" %in% c("212093_s_at","212095_s_at","212096_s_at","239576_at")),]
peak_at_names_in_ftdata_restricted2MTUS1 <- peak_at_names_in_ftdata_restricted[which(peak_at_names_in_ftdata_restricted$"Gene Symbol" %in% c("MTUS1")),] # 3 probes (rows)

# 3) make a restricted version (to only the MTUS1 probes) of the expression set
list_of_variables_kept = as.character(peak_at_names_in_ftdata_restricted2MTUS1$ID)
ex_ATIP3_only <- ex[ which(rownames(ex) %in% list_of_variables_kept), ]
# 4) make a restricted version (to only the taxanes treated samples) of the expression set
list_of_samples_kept = as.character(peak_at_names_in_phdata_restricted$geo_accession)
ex_ATIP3_only <- ex_ATIP3_only[ ,which(colnames(ex_ATIP3_only) %in% list_of_samples_kept) ]
######################################end of trial

# - reporting the number of TNBC found
num_total_of_samples_in_cohort <-ncol(ex)
num_final_of_taxanes_samples_in_cohort <-ncol(ex_ATIP3_only) # or nrow(peak_at_names_in_phdata_restricted)
num_total_of_variables_in_cohort <-nrow(ex)
# we got the num_of_uniques_genes_tracked
num_tnbc_in_cohort<-nrow(peak_at_names_in_phdata_restricted2TNBC)
paste("Report on the cohort initial composition : ", sep='')
paste("- initial # of samples : ",num_total_of_samples_in_cohort, sep='') 
paste("- final taxanes treated # of samples : ",num_final_of_taxanes_samples_in_cohort, sep='') 
paste("- initial # of variables : ",num_total_of_variables_in_cohort, sep='') 
paste("- final # of genes tracked by variables : ",num_of_uniques_genes_tracked, sep='') 
paste("- # of TNBC samples in final taxanes treated samples : ",num_tnbc_in_cohort, sep='') 

# --0--part for saving on file and reread anytime
# - choose the data structure to save...
data_struct2save <- ex_ATIP3_only
num_not_defined_rownames_data<-sum(is.nan(rownames(data_struct2save))) # ...check the dimensions of the data struct to save if they are not NA
num_not_defined_colnames_data<-sum(is.nan(colnames(data_struct2save)))
if (num_not_defined_rownames_data!=0 | num_not_defined_colnames_data!=0) {
  paste("WARNING!!! A DIMENSION HAS AN UNKNOWN!", sep='')
}
paste("For the data_structure, # rows not defined : ", num_not_defined_rownames_data, ". # cols not defined :", num_not_defined_colnames_data, "../..", sep='') # ...get the dimensions
num_rows_data_struct2save<-nrow(data_struct2save) # ... make a report
num_cols_data_struct2save<-ncol(data_struct2save)
paste("For the data_structure, # rows is : ", num_rows_data_struct2save, ". # cols is :", num_cols_data_struct2save, "../..", sep='')
outfilename_data = paste(myGSE,"_",part_of_probesets_kept,"_",version_to_save,"_",num_rows_data_struct2save,"x",num_cols_data_struct2save,"_GEX.csv", sep='') # ....build the file name
write.csv(data_struct2save, outfilename_data, row.names=T) # ... save the file
# - choose the ph structure to save...
ph_struct2save <- peak_at_names_in_phdata_restricted
# - the dimensions of the ph struct to save and the file name
num_not_defined_rownames_ph<-sum(is.nan(rownames(ph_struct2save))) # ...check the dimensions of the data struct to save if they are not NA
num_not_defined_colnames_ph<-sum(is.nan(colnames(ph_struct2save)))
if (num_not_defined_rownames_ph!=0 | num_not_defined_colnames_ph!=0) {
  paste("WARNING!!! A DIMENSION HAS AN UNKNOWN!", sep='')
}
paste("For the pheno_structure, # rows not defined : ", num_not_defined_rownames_ph, ". # cols not defined :", num_not_defined_colnames_ph, "../..", sep='') # ...get the dimensions
num_rows_ph_struct2save<-nrow(ph_struct2save) # ... make a report
num_cols_ph_struct2save<-ncol(ph_struct2save)
paste("For the ph_structure, # rows is : ", num_rows_ph_struct2save, ". # cols is :", num_cols_ph_struct2save, "../..", sep='')
outfilename_ph = paste(myGSE,"_",part_of_probesets_kept,"_",version_to_save,"_",num_rows_ph_struct2save,"x",num_cols_ph_struct2save,"_ph.csv", sep='') # ....build the file name
write.csv(ph_struct2save, outfilename_ph, row.names=T) # ... save the file

















