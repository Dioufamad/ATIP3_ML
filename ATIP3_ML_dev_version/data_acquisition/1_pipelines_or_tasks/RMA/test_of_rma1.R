set.seed(1)
pms <- 2^matrix(rnorm(1000), nc=20)
colnames(pms) <- paste("sample", 1:20, sep="")
pns <- rep(letters[1:10], each=5)
res <- basicRMA(pms, pns, TRUE, TRUE)
res[, 1:3]

# trying with rma
res_rma <- oligo::rma(pms, target = "core")

# ############# trying with my files
###install biomart
# step : install the proper version of bioinconductor for the proper R version  that you have (see https://www.bioconductor.org/install/)
if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")
BiocManager::install(version = "3.10")
# step : install the workflow package         
BiocManager::install("biomaRt")

#--imports
library("oligo")
library("biomaRt")
#--3--Setting the dataset to manipulate (some options throughout the script change depending on chosen dataset)
# - uncomment one of these 4 following lines to choose a dataset
cohort <- "Remagus02"
# cohort <- "Remagus04"
# cohort <- "MDAnderson"
# cohort <-  "another_dataset_you_want_to_use"
# - store the path of the dataset
if (cohort=="Remagus02") {
  path2file = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/atip3_material/datasets_to_process_folder/3cohort_unchanged_fts/BRCA_Treatment11_REMAGUS02xNACx226Sx54675Fx4RasRCH3HSall_GEX.csv" # for R02
} else if (cohort=="Remagus04") {
  path2file = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/atip3_material/datasets_to_process_folder/3cohort_unchanged_fts/BRCA_Treatment12_REMAGUS04xNACx142Sx22277Fx4RasRCH3HSall_GEX.csv" # for R04
} else if (cohort=="MDAnderson") {
  path2file = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/atip3_material/datasets_to_process_folder/3cohort_unchanged_fts/BRCA_Treatment13_MDAndersonxNACx133Sx22283Fx4RasRCH3HSall_GEX.csv" # for MDA
} else
  print("Replace this statement with a command to store the path of another_dataset_you_want_to_use")

#--4--Data preparation
# - make a dataframe from dataset# 
df_file  <- read.csv(file = path2file, header = TRUE)
  # - a preview of the dataframe
# head(otter) # uncomment to use; not recommended because too much features a dataset for this head to show a complete line 
# - restrict the dataframe to only the columns needed (drop the responses)
cols2drop1 <- c("BestResCat_as_RCH","BestResCat_as_RO","BestResCat_as_RP","BestResCat_as_HER2")
df_file_restricted1 = df_file[,!(names(df_file) %in% cols2drop1)]
# - restrict the dataframe to only the columns needed (move the samples columns to the start)
df_file_restricted2 <- df_file_restricted1 %>% select(Model, everything())
# - make the samples names as index (can also be done at import using df <- read.csv("/mydata.csv", header=TRUE, row.names="Date") )
rownames(df_file_restricted2) <- df_file_restricted2$Model
cols2drop2 <- c("Model")
df_file_restricted3 = df_file_restricted2[,!(names(df_file_restricted2) %in% cols2drop2)]
# - put the columns in aphabetical order to easily compare after basicRMA is applied the values of some probes
df_file_restricted4 <- df_file_restricted3[ , order(names(df_file_restricted3))]
# - transpose the df
dframe_log2 <-t(df_file_restricted4)
# - change the values back to non log2 values because basicRMA outputs log2 values
dframe <- 2^dframe_log2

#--5--Lets try the basicRMA on a df of log2 already values   
pb_names <-rownames(dframe) 
# res_basicRMA <- basicRMA(dframe, pb_names, TRUE, TRUE) # simple line
res_basicRMA <- basicRMA(dframe, pb_names, normalize = TRUE, background = TRUE, bgversion = 2, destructive = FALSE, verbose = TRUE) # explicit line
# check results
dframe[1:5, 1:5]
nrow(dframe)
ncol(dframe)
res_basicRMA[1:5, 1:5]
nrow(res_basicRMA)
ncol(res_basicRMA)
# check longer results (from the head)
dframe[1:10, 1:10]
nrow(dframe)
ncol(dframe)
res_basicRMA[1:10, 1:10]
nrow(res_basicRMA)
ncol(res_basicRMA)
# check longer results (from the tail)
dframe[(nrow(dframe)-10):nrow(dframe), 1:10]
nrow(dframe)
ncol(dframe)
res_basicRMA[(nrow(res_basicRMA)-10):nrow(res_basicRMA), 1:10]
nrow(res_basicRMA)
ncol(res_basicRMA)


### Part 2 : get the genes symbols
listMarts()  
ensembl <- useMart("ensembl")
datasets <- listDatasets(ensembl)
head(datasets)
# ensembl = useDataset("hsapiens_gene_ensembl",mart=ensembl)
ensembl = useMart("ensembl",dataset="hsapiens_gene_ensembl")
filters = listFilters(ensembl)
filters[1:5,]
attributes = listAttributes(ensembl)
attributes[1:5,]  
# as in the test
affyids=c("202763_at","209310_s_at","207500_at")
getBM(attributes=c('affy_hg_u133_plus_2', 'entrezgene_id'), 
      filters = 'affy_hg_u133_plus_2', 
      values = affyids, 
      mart = ensembl)
# trial with atip3 probes 
affyids=c("212093_s_at","212095_s_at","212096_s_at","239576_at")
getBM(attributes=c('affy_hg_u133_plus_2', 'entrezgene_id',"ensembl_gene_id","ensembl_gene_id_version","external_gene_name","external_gene_source"), 
      filters = 'affy_hg_u133_plus_2', 
      values = affyids, 
      mart = ensembl)























