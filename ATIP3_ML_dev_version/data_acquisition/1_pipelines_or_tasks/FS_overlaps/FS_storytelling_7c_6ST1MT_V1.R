# this script is the test for counting and identifying the genes that tells the same story ie their differents coefs in regression works have the same sign

# imports 
library(readxl) # for ability to read xlsx and xls files  
library(UpSetR) # for the upset plots
library(ggplot2) # for the attribute plots
library(dplyr) # for the operations on multiples frames using pipes in succession


# - collectors for the entry data to use (will be use to access the entire data through loops on these collectors)
list_paths2files_NNC <- c() # >>>>>>>>>>> a list of paths (non nul coefs fts tables)
list_paths2files_RAW <- c() # >>>>>>>>>>> a list of paths (raw coefs values for fts tables)
list_tag_alg <- c() # >>>>>>>>>>> a list of tag_alg
list_tag_numcohort <- c() # >>>>>>>>>>> a list of tag_numcohort
list_tag_nickname_cohort <- c() # >>>>>>>>>>> a list of tag_nickname_cohort

# - supply the path of all FS to open here and add their respective info to the previous collectors
# >>> FS 1
path2file1_NNC = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0061_NonNullCoefs.csv"
path2file1_RAW = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0061_RawListOfCoefs.csv"
tag_alg1 = "FS_ST_L1"
tag_numcohort1 = "GSE41998"
tag_nickname_cohort1 = "BMS_Horak_2013"
list_paths2files_NNC <- c(list_paths2files_NNC,path2file1_NNC)
list_paths2files_RAW <- c(list_paths2files_RAW,path2file1_RAW)
list_tag_alg <- c(list_tag_alg,tag_alg1)
list_tag_numcohort <- c(list_tag_numcohort,tag_numcohort1)
list_tag_nickname_cohort <- c(list_tag_nickname_cohort,tag_nickname_cohort1)

# >>> FS 2
path2file2_NNC = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0062_NonNullCoefs.csv"
path2file2_RAW = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0062_RawListOfCoefs.csv"
tag_alg2 = "FS_ST_L1"
tag_numcohort2 = "GSE26639"
tag_nickname_cohort2 = "Remagus02"
list_paths2files_NNC <- c(list_paths2files_NNC,path2file2_NNC)
list_paths2files_RAW <- c(list_paths2files_RAW,path2file2_RAW)
list_tag_alg <- c(list_tag_alg,tag_alg2)
list_tag_numcohort <- c(list_tag_numcohort,tag_numcohort2)
list_tag_nickname_cohort <- c(list_tag_nickname_cohort,tag_nickname_cohort2)

# >>> FS 3
path2file3_NNC = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0063_NonNullCoefs.csv"
path2file3_RAW = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0063_RawListOfCoefs.csv"
tag_alg3 = "FS_ST_L1"
tag_numcohort3 = "GSE32646"
tag_nickname_cohort3 = "Osaka_Miyake_2012"
list_paths2files_NNC <- c(list_paths2files_NNC,path2file3_NNC)
list_paths2files_RAW <- c(list_paths2files_RAW,path2file3_RAW)
list_tag_alg <- c(list_tag_alg,tag_alg3)
list_tag_numcohort <- c(list_tag_numcohort,tag_numcohort3)
list_tag_nickname_cohort <- c(list_tag_nickname_cohort,tag_nickname_cohort3)

# >>> FS 4
path2file4_NNC = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0064_NonNullCoefs.csv"
path2file4_RAW = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0064_RawListOfCoefs.csv"
tag_alg4 = "FS_ST_L1"
tag_numcohort4 = "GSE25055"
tag_nickname_cohort4 = "MDAnderson_part1of2_310"
list_paths2files_NNC <- c(list_paths2files_NNC,path2file4_NNC)
list_paths2files_RAW <- c(list_paths2files_RAW,path2file4_RAW)
list_tag_alg <- c(list_tag_alg,tag_alg4)
list_tag_numcohort <- c(list_tag_numcohort,tag_numcohort4)
list_tag_nickname_cohort <- c(list_tag_nickname_cohort,tag_nickname_cohort4)

# >>> FS 5
path2file5_NNC = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0065_NonNullCoefs.csv"
path2file5_RAW = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0065_RawListOfCoefs.csv"
tag_alg5 = "FS_ST_L1"
tag_numcohort5 = "GSE20194"
tag_nickname_cohort5 = "Fudan_MAQC2BR"
list_paths2files_NNC <- c(list_paths2files_NNC,path2file5_NNC)
list_paths2files_RAW <- c(list_paths2files_RAW,path2file5_RAW)
list_tag_alg <- c(list_tag_alg,tag_alg5)
list_tag_numcohort <- c(list_tag_numcohort,tag_numcohort5)
list_tag_nickname_cohort <- c(list_tag_nickname_cohort,tag_nickname_cohort5)

# >>> FS 6
path2file6_NNC = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0066_NonNullCoefs.csv"
path2file6_RAW = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0066_RawListOfCoefs.csv"
tag_alg6 = "FS_ST_L1"
tag_numcohort6 = "GSE63471"
tag_nickname_cohort6 = "Remagus04"
list_paths2files_NNC <- c(list_paths2files_NNC,path2file6_NNC)
list_paths2files_RAW <- c(list_paths2files_RAW,path2file6_RAW)
list_tag_alg <- c(list_tag_alg,tag_alg6)
list_tag_numcohort <- c(list_tag_numcohort,tag_numcohort6)
list_tag_nickname_cohort <- c(list_tag_nickname_cohort,tag_nickname_cohort6)

# >>> FS 7 aka MT
path2file7_NNC = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/spams_sparse_group_lasso_l2__l1onlyused_6cohortes/Output_Regr_SPAMSSparseGroupL1LogReg_Allfts_Multitaskof6_BRCA_NACTaxanesBR_GEX_MA_Trial004_NonNullCoefs.csv"
path2file7_RAW = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/spams_sparse_group_lasso_l2__l1onlyused_6cohortes/Output_Regr_SPAMSSparseGroupL1LogReg_Allfts_Multitaskof6_BRCA_NACTaxanesBR_GEX_MA_Trial004_RawListOfCoefs.csv"
tag_alg7 = "FS_MT_SGL1"
tag_numcohort7 = "6GSEs"
tag_nickname_cohort7 = "6_joined_dts"
list_paths2files_NNC <- c(list_paths2files_NNC,path2file7_NNC)
list_paths2files_RAW <- c(list_paths2files_RAW,path2file7_RAW)
list_tag_alg <- c(list_tag_alg,tag_alg7)
list_tag_numcohort <- c(list_tag_numcohort,tag_numcohort7)
list_tag_nickname_cohort <- c(list_tag_nickname_cohort,tag_nickname_cohort7)

# >>>>>>>>>> the colname where the selected features will be in each file
# Features


# for each gene, we define the following booleans : A1, Q1, M1 , F1, S1 and A2, Q2, M2 , F2, S2 (see explanation in design and put here later)
# A boolean is 1 or 0 but we need to get after adding up the boolans from different models a score that as such : 
# -- the number at pos x is the score for the xth type of models ran (64 means 6 over all the type 1 models and 4 over all the type 2 models)
# this means the boolean yes and no cant be always resp. 1 and 0 but will change following the number of types of models ran
# to avoid changing in lots of places across the script we define it here (in order to change it only here we need be)
# * lets get the different types of alg analysed here (not needed but because the marks on qualities of the coefs are independent of it now but we keep to better characterize our analysis)
count_type_alg_1_ie_ST = 0
count_type_alg_2_ie_MT = 0
for (index_a_tag_algi in c(1:length(list_tag_alg))) {
  a_tag_algi = list_tag_alg[index_a_tag_algi]
  if (grepl("_ST_", a_tag_algi, fixed=TRUE)){
    count_type_alg_1_ie_ST = count_type_alg_1_ie_ST + 1
  } else if (grepl("_MT_", a_tag_algi, fixed=TRUE)){
    count_type_alg_2_ie_MT = count_type_alg_2_ie_MT + 1
  }
}
# lets created the boolean following the number of types of alg we have to analyse
# score is as "the number at pos x is the score for the xth type of models ran"
# # -- version 1 with change 1 (deprecated)
# if ((count_type_alg_1_ie_ST>=1)&(count_type_alg_2_ie_MT>=1)){
#   for_type_alg_1_value_bool_yes = 1 # was 10 before change1
#   for_type_alg_1_value_bool_no = 0
#   for_type_alg_2_value_bool_yes = 0.1 # was 1 before change1
#   for_type_alg_2_value_bool_no = 0
# } else if((count_type_alg_1_ie_ST==0)|(count_type_alg_2_ie_MT==0)){
#   for_type_alg_1_value_bool_yes = 1
#   for_type_alg_1_value_bool_no = 0
#   for_type_alg_2_value_bool_yes = 1
#   for_type_alg_2_value_bool_no = 0
# }
# before change1 for_type_alg_1_value_bool_yes was 10 and for_type_alg_2_value_bool_yes was 1 using unit number as for alg 2 score and ten's number as alg 1 score 
# but separating with a comma can bring a clearer separation, while giving more of the feeling of "parts" as the individual fts are in the MT as well as giving us a lot of insights 
#when the code has some exceptions that   it does not take into account
# -- version 2 (include booleans to mark the signs of the majority coefs counted) and does not depend on the counts of type of FS found (the same marks are used always)
# ---  these are to mark the quality of the majority sign among the counted coefs
for_type_alg_1_value_bool_yes = 1
for_type_alg_1_value_bool_no = 0
for_type_alg_2_value_bool_yes = 0.1 
for_type_alg_2_value_bool_no = 0
# ---  these are to keep what was the majority sign among the counted coefs
for_type_alg_1_value_bool_yes_for_maj_with_sign_neg = 10
for_type_alg_1_value_bool_no_for_maj_with_sign_neg = 0
for_type_alg_1_value_bool_yes_for_maj_with_sign_pos = 1
for_type_alg_1_value_bool_no_for_maj_with_sign_pos = 0
for_type_alg_2_value_bool_yes_for_maj_with_sign_neg = 0.1
for_type_alg_2_value_bool_no_for_maj_with_sign_neg = 0
for_type_alg_2_value_bool_yes_for_maj_with_sign_pos = 0.01
for_type_alg_2_value_bool_no_for_maj_with_sign_pos = 0


#--- Ideas and remarks for the following steps: 
# - Idea 1 : loop on the genes in the table of raw coefs and supply each one with the values of the booleans that describe its storytelling ability
# (each boolean is the ability of the storytelling when judge from a specific level of being stringent)
# - NB1:  some way to access the gene of each row using : 
# for (one_of_the_rownames in rownames(fs_table_raw_nnc_only)) {}
# but the column containing the features not usually the row names and we want to keep the number on the rownames as such to keep track of
# if the present list of features is from a discontinued or non discontued list of featurs by the previous restriction done
# hence we will access the rows using each name in the column Features



# - defining collectors
list_fs_tables_retrieved_NNC = list()
list_fs_tables_retrieved_RAW = list()
list_fs_tables_retrieved_RAW_w_stats_and_marks = list()
list_fs_tables_retrieved_RAW_marks_only_and_pruned = list()
# output is fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs (a table with all unique genes, each one with its marks for storytelling) 
num_initial_sets_analysed <- 0


#>>>>>>>>>>> - for each alg (1 alg gives 1 specific FS with 1 table of raw coefs and 1 table of non nul coefs), lets load its needed csv files, makes the needed computations and stash them
for (index_of_an_alg in c(1:length(list_tag_alg))) { # for test use index_of_an_alg = 1
  # - keep the tag of the present FS alg in case we need it later (for example to known what type of FS we are analysing)
  tag_alg_corresp_2_fs_retrieved = list_tag_alg[index_of_an_alg]
  # - keep the nickname of the cohort of the present FS alg in case we need it later
  tag_nickname_cohort_corresp_2_fs_retrieved = list_tag_nickname_cohort[index_of_an_alg]
  # - lets state the FS that is will be analysed
  paste("- FS ",index_of_an_alg," analysis started and it is for ",tag_alg_corresp_2_fs_retrieved,"_on_",tag_nickname_cohort_corresp_2_fs_retrieved, sep='')
  # - get the path for each the 2 files needed (raw coefs table and non nuls coefs table)
  path2file_NNC = list_paths2files_NNC[index_of_an_alg]
  path2file_RAW = list_paths2files_RAW[index_of_an_alg]
  # - get the table corresponding to the path
  fs_table_nnc <- read.csv(file = path2file_NNC, header = TRUE)
  fs_table_raw <- read.csv(file = path2file_RAW, header = TRUE)
  # - add it to the collector of the fs_tables
  list_fs_tables_retrieved_NNC[[index_of_an_alg]] <- fs_table_nnc
  list_fs_tables_retrieved_RAW[[index_of_an_alg]] <- fs_table_raw
  # - check if the colname of the selected features column is in the colnames of the FS table (to be sure that there will be no surprises as to the colname we use to get the fts))
  colnames_in_fs_table_nnc = names(fs_table_nnc) # use it to also see the cols (to see which ones to keep)
  if ("Features" %in% colnames_in_fs_table_nnc) { 
    paste("- the known colname of the selected features column is in the colnames of the NON NULS COEFS FS table !", sep='')
  }else{
    paste("- Warning : the known colname of the selected features column IS NOT in the colnames of the NON NULS COEFS FS table.", sep='')
  }
  colnames_in_fs_table_raw = names(fs_table_raw) # use it to also see the cols (to see which ones to keep)
  if ("Features" %in% colnames_in_fs_table_raw) { 
    paste("- the known colname of the selected features column is in the colnames of the RAW COEFS FS table !", sep='')
  }else{
    paste("- Warning : the known colname of the selected features column IS NOT in the colnames of the RAW COEFS FS table.", sep='')
  }
  # - restrict the raw table using the nnc table
  # * for a test of the ability to really restrict the raw table using the nnc table, we shorten the nnc table to only the first 20 lines with this :
  # fs_table_nnc <- fs_table_nnc[1:20,]
  list_fts_in_nnc = unique(as.character(fs_table_nnc$Features))
  fs_table_raw_nnc_only = fs_table_raw[which(fs_table_raw$Features %in% list_fts_in_nnc),]
  
  ## Idea : utiliser une definition du score de qualité 2 chiffres et la récupérer pour chaque FS resultat d'un alg
  # -----------------chunk 1
  # for each table of raw coefs that we loop on, we : 
  #...make a copy of the table that wont be modified and always available in its native form to get the values needed more easily in terms of code
  fs_table_raw_nnc_only_stash = fs_table_raw_nnc_only
  #...get the list of genes in the table in order to call it in the all the calls where we need a gene
  list_fts_in_raw_nnc_only = unique(as.character(fs_table_raw_nnc_only_stash$Features))
  #...add to the version of the table to modify the columns that will be supplied with values
  fs_table_raw_nnc_only$space_init_Min = NA
  fs_table_raw_nnc_only$space_init_Max = NA
  fs_table_raw_nnc_only$space_init_LB = NA
  fs_table_raw_nnc_only$space_init_HB = NA
  fs_table_raw_nnc_only$space_init_Num_outliers = NA
  fs_table_raw_nnc_only$space_fin_Size = NA
  fs_table_raw_nnc_only$space_fin_Num_zeros = NA
  fs_table_raw_nnc_only$space_fin_Num_signs = NA
  fs_table_raw_nnc_only$space_fin_Num_pos = NA
  fs_table_raw_nnc_only$space_fin_Num_neg = NA
  fs_table_raw_nnc_only$crit_A1 = NA
  fs_table_raw_nnc_only$crit_Q1 = NA
  fs_table_raw_nnc_only$crit_M1 = NA
  fs_table_raw_nnc_only$crit_S1 = NA
  fs_table_raw_nnc_only$crit_F1 = NA
  fs_table_raw_nnc_only$crit_T1 = NA
  fs_table_raw_nnc_only$crit_A2 = NA
  fs_table_raw_nnc_only$crit_Q2 = NA
  fs_table_raw_nnc_only$crit_M2 = NA
  fs_table_raw_nnc_only$crit_S2 = NA
  fs_table_raw_nnc_only$crit_F2 = NA
  fs_table_raw_nnc_only$crit_T2 = NA
  # >>>>>>>>>>>>>> loop on the genes (precisely on the indexes of the list of genes) of the table of raw coefs and update the version of this table to modify
  for (index_of_a_gene in c(1:length(list_fts_in_raw_nnc_only))) { # index_of_a_gene = 3 # use this for tests 
    # for each gene, get the initial space of values (of coefs)
    present_gene = list_fts_in_raw_nnc_only[index_of_a_gene]
    row_present_gene_coefs_only<-fs_table_raw_nnc_only_stash[which(fs_table_raw_nnc_only_stash$Features %in% present_gene),-1] # all cols except 1st col that contains the name of the gene and not a coef
    space_initial <-as.numeric(as.vector(row_present_gene_coefs_only))
    # for each gene, get the needed stats among the IQR stats
    space_initial_min = min(space_initial)
    space_initial_max = max(space_initial)
    space_initial_q1 = quantile(space_initial,0.25)[[1]] # quantile gives a named element as a resultat so we treat it as a list to get the desired value
    space_initial_q3 = quantile(space_initial,0.75)[[1]]
    space_initial_iqr = IQR(space_initial)
    space_initial_lower_bracket = space_initial_q1 - (1.5*space_initial_iqr)
    space_initial_higher_bracket = space_initial_q3 + (1.5*space_initial_iqr)
    # for each gene, get the outliers and the space_final vectors
    space_initial_outliers <- c()
    space_final <- c()
    for (index_a_val in c(1:length(space_initial))) {
      a_val = space_initial[index_a_val]
      if ((a_val < space_initial_lower_bracket) | (a_val > space_initial_higher_bracket)) {
        space_initial_outliers <- c(space_initial_outliers,a_val)
      }else{
        space_final <- c(space_final,a_val)
      }
    }
    space_initial_outliers_size = length(space_initial_outliers)
    space_final_size = length(space_final)
    # for each gene, get the Npos (vec of pos coefs), the Nneg (vec of neg coefs), the Nzeros (vec of zeros coefs) and the Nmaj (majority sign)
    space_final_pos <- c()
    space_final_neg <- c()
    space_final_zeros <- c()
    for (index_a_coef in c(1:length(space_final))) {
      a_coef = space_final[index_a_coef]
      if (a_coef > 0) {
        space_final_pos <- c(space_final_pos,a_coef)
      } else if (a_coef < 0) {
        space_final_neg <- c(space_final_neg,a_coef)
      } else {
        space_final_zeros <- c(space_final_zeros,a_coef)
      }
    }
    Npos = length(space_final_pos)
    Nneg = length(space_final_neg)
    Nzeros = length(space_final_zeros)
    Nsigns = Npos + Nneg
    Nmaj = 0 # initialized at zeros because cant be zero (would be zero if all coefs are zeros and such case have been removed because only nnc are kept)
    if (Npos > Nneg) {
      Nmaj = Npos
    } else if (Nneg > Npos){
      Nmaj = Nneg
    } else { # Npos = Nneg
      Nmaj = (Nsigns / 2)
    }
    # for each gene, get the median and the q3 if values can be counted from 1 until Nsigns (they will be used as arbitrary limit of a space 1-Nsigns instead of 1-10seeds)
    Nsigns_counts_med = median(c(0:Nsigns)) # ie 5 for a Nsigns=10 (case of all coefs used)
    Nsigns_counts_q3 = quantile(c(0:Nsigns),0.75)[[1]] # ie 7.5 for a Nsigns=10 (case of all coefs used)
    # for each gene, we defined previously the following booleans : A1, Q1, M1 , F1, S1 and A2, Q2, M2 , F2, S2 
    # but we need to define what type of alg we are currently analysing in this step of the loop and decide the proper boolean values to use
    if (grepl("_ST_", tag_alg_corresp_2_fs_retrieved, fixed=TRUE)){
      type_alg_specific_value_bool_yes = for_type_alg_1_value_bool_yes
      type_alg_specific_value_bool_no = for_type_alg_1_value_bool_no
      type_alg_specific_value_bool_yes_for_maj_with_sign_neg = for_type_alg_1_value_bool_yes_for_maj_with_sign_neg 
      type_alg_specific_value_bool_no_for_maj_with_sign_neg = for_type_alg_1_value_bool_no_for_maj_with_sign_neg 
      type_alg_specific_value_bool_yes_for_maj_with_sign_pos = for_type_alg_1_value_bool_yes_for_maj_with_sign_pos
      type_alg_specific_value_bool_no_for_maj_with_sign_pos = for_type_alg_1_value_bool_no_for_maj_with_sign_pos
    } else if (grepl("_MT_", tag_alg_corresp_2_fs_retrieved, fixed=TRUE)){
      type_alg_specific_value_bool_yes = for_type_alg_2_value_bool_yes
      type_alg_specific_value_bool_no = for_type_alg_2_value_bool_no
      type_alg_specific_value_bool_yes_for_maj_with_sign_neg = for_type_alg_2_value_bool_yes_for_maj_with_sign_neg 
      type_alg_specific_value_bool_no_for_maj_with_sign_neg = for_type_alg_2_value_bool_no_for_maj_with_sign_neg 
      type_alg_specific_value_bool_yes_for_maj_with_sign_pos = for_type_alg_2_value_bool_yes_for_maj_with_sign_pos
      type_alg_specific_value_bool_no_for_maj_with_sign_pos = for_type_alg_2_value_bool_no_for_maj_with_sign_pos
    }
    
    # for each gene, we give the value of the booleans following the gene's final space of coefs values
    # T1 is always defined with "T1 = type_alg_specific_value_bool_yes" because it is a counter (it is not added up if the gene if not gone through while analysing a FS because it is absent there)
    if (Nzeros!=0){ # the final space of coefs values has at least one zero so the gallery of bools to change is A2, Q2, M2 , F2, S2
      A1 = 0
      Q1 = 0
      M1 = 0
      S1 = 0
      F1 = 0
      T1 = 0 
      T2 = type_alg_specific_value_bool_yes # the gene is analysed so T for the gallery to change is added up with bool yes
      if((Npos == Nneg)|(Nsigns==0)|(Nsigns==1)){ # the values when Nsigns gallery is not admissible for use 
        F2=type_alg_specific_value_bool_yes
        A2=0
        Q2=0
        M2=0
        S2=0
      }else{ # the values when Nsigns gallery is admissible for use 
        F2=type_alg_specific_value_bool_no
        if(Nmaj==Nsigns){
          A2=type_alg_specific_value_bool_yes
        }else{
          A2=type_alg_specific_value_bool_no
        }
        if(Nmaj>=Nsigns_counts_q3){
          Q2=type_alg_specific_value_bool_yes
        }else{
          Q2=type_alg_specific_value_bool_no
        }
        if(Nmaj>Nsigns_counts_med){
          M2=type_alg_specific_value_bool_yes
        }else{
          M2=type_alg_specific_value_bool_no
        }
        if(Nneg > Npos){
          S2=type_alg_specific_value_bool_yes_for_maj_with_sign_neg + type_alg_specific_value_bool_no_for_maj_with_sign_pos
        }else if (Npos > Nneg){
          S2=type_alg_specific_value_bool_no_for_maj_with_sign_neg + type_alg_specific_value_bool_yes_for_maj_with_sign_pos
        } else { # Npos = Nneg
          S2 = 0
        }
      }
    }else{ # Nzeros==0 ie # the final space of coefs does not have zeros so the gallery of bools to change is A1, Q1, M1 , F1, S1
      A2 = 0
      Q2 = 0
      M2 = 0
      S2 = 0
      F2 = 0
      T2 = 0
      T1 = type_alg_specific_value_bool_yes # the gene is analysed so T for the gallery to change is added up with bool yes
      if((Npos == Nneg)|(Nsigns==0)|(Nsigns==1)){ # the values when Nsigns gallery is not admissible for use 
        F1=type_alg_specific_value_bool_yes
        A1=0
        Q1=0
        M1=0
        S1=0
      }else{ # the values when Nsigns gallery is admissible for use 
        F1=type_alg_specific_value_bool_no
        if(Nmaj==Nsigns){
          A1=type_alg_specific_value_bool_yes
        }else{
          A1=type_alg_specific_value_bool_no
        }
        if(Nmaj>=Nsigns_counts_q3){
          Q1=type_alg_specific_value_bool_yes
        }else{
          Q1=type_alg_specific_value_bool_no
        }
        if(Nmaj>Nsigns_counts_med){
          M1=type_alg_specific_value_bool_yes
        }else{
          M1=type_alg_specific_value_bool_no
        }
        if(Nneg > Npos){
          S1=type_alg_specific_value_bool_yes_for_maj_with_sign_neg + type_alg_specific_value_bool_no_for_maj_with_sign_pos
        }else if (Npos > Nneg){
          S1=type_alg_specific_value_bool_no_for_maj_with_sign_neg + type_alg_specific_value_bool_yes_for_maj_with_sign_pos
        } else { # Npos = Nneg
          S1 = 0
        }
      }
    }
    # for each gene, update the values of the 8 new cols that are crit_A1 through crit_S2 
    # ie storing in its row inside the raw table the values related to its coefs space and booleans of storytelling ability
    fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"space_init_Min"] = space_initial_min
    fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"space_init_Max"] = space_initial_max
    fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"space_init_LB"] = space_initial_lower_bracket
    fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"space_init_HB"] = space_initial_higher_bracket
    fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"space_init_Num_outliers"] = space_initial_outliers_size
    fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"space_fin_Size"] = space_final_size
    fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"space_fin_Num_zeros"] = Nzeros
    fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"space_fin_Num_signs"] = Nsigns
    fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"space_fin_Num_pos"] = Npos
    fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"space_fin_Num_neg"] = Nneg
    fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_A1"] = A1
    fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_Q1"] = Q1
    fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_M1"] = M1
    fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_S1"] = S1
    fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_F1"] = F1
    fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_T1"] = T1
    fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_A2"] = A2
    fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_Q2"] = Q2
    fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_M2"] = M2
    fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_S2"] = S2
    fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_F2"] = F2
    fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_T2"] = T2
    # end of the work on a gene (one row of a table of raw coefs)
  }        
  # end of the work on a table of raw coefs for one model
  
  # - lets add to a collector, this output table with stats and marks 
  list_fs_tables_retrieved_RAW_w_stats_and_marks[[index_of_an_alg]] <- fs_table_raw_nnc_only
  
  # - lets add to another collector, a version of this table that is: 
  # ... pruned (only a unique row is kept for each gene present multiple times) 
  # ... with only the marks cols
  # -- step 1 : lets produce a version with only the marks cols (ie the last 12 cols)
  set_of_cols_2_keep_for_marks <- c(colnames(fs_table_raw_nnc_only)[1],tail(colnames(fs_table_raw_nnc_only), 12))
  fs_table_raw_nnc_only_marks_only <- fs_table_raw_nnc_only[, set_of_cols_2_keep_for_marks]
  # -- step 2 : lets make a unique row for each gene present multiple times
  # this step is done only when the multitask noted MT is the type of alg of the FS
  # --- check if the list unique features got for this initial set does not have redundancies in it
  list_fts_unik_in_fs_table_raw_nnc_only_marks_only = unique(as.character(fs_table_raw_nnc_only_marks_only$Features))
  if (length(list_fts_unik_in_fs_table_raw_nnc_only_marks_only) == nrow(fs_table_raw_nnc_only_marks_only)) {  
    paste("- There is no redundancy among the genes of the pruned table of storytelling scores for ",tag_alg_corresp_2_fs_retrieved,"_on_",tag_nickname_cohort_corresp_2_fs_retrieved, sep='')
  }else{
    paste("- Warning : there is redundancy among the genes of the pruned table of storytelling scores for ",tag_alg_corresp_2_fs_retrieved,"_on_",tag_nickname_cohort_corresp_2_fs_retrieved, sep='')
  }
  # --- following the type of alg used for the FS, we do the pruning (MT alg FSs) or not (ST alg FSs)
  if (grepl("_ST_", tag_alg_corresp_2_fs_retrieved, fixed=TRUE)){
    # keep the previous table
    fs_table_raw_nnc_only_marks_only_and_pruned = fs_table_raw_nnc_only_marks_only
  } else if (grepl("_MT_", tag_alg_corresp_2_fs_retrieved, fixed=TRUE)){
    # prune the previous table to keep only one copy/row for a gene 
    # ... lets split the MT features names to get the correct initial names of the fts in order to initialise the table of one copy per gene
    list_fts_all_in_fs_table_as_correct_names <- c()
    for (index_a_MT_ft_name in c(1:length(list_fts_unik_in_fs_table_raw_nnc_only_marks_only))){
      a_MT_ft_name = list_fts_unik_in_fs_table_raw_nnc_only_marks_only[index_a_MT_ft_name]
      pieces_of_ftname_as_MT_name <- strsplit(a_MT_ft_name, "_in_")[[1]] # NB : if the sep is not found, a vector of only the entire word is kept so getting the 1st elt gives it also
      ftname_as_correct_initial_name <-pieces_of_ftname_as_MT_name[1]
      list_fts_all_in_fs_table_as_correct_names <- c(list_fts_all_in_fs_table_as_correct_names,ftname_as_correct_initial_name)
    }
    list_fts_all_in_fs_table_as_correct_names_uniks = unique(list_fts_all_in_fs_table_as_correct_names)
    #...make a new table with only one gene copy and its marks are each a sum of the copies marks
    my_one_gene_copy_matrix = as.data.frame(matrix(NA, nrow = length(list_fts_all_in_fs_table_as_correct_names_uniks), ncol = dim(fs_table_raw_nnc_only_marks_only)[2]))
    colnames(my_one_gene_copy_matrix) <- colnames(fs_table_raw_nnc_only_marks_only)
    my_one_gene_copy_matrix[,"Features"] = list_fts_all_in_fs_table_as_correct_names_uniks
    for (index_a_correct_gene_name in c(1:length(list_fts_all_in_fs_table_as_correct_names_uniks))){
      a_correct_gene_name = list_fts_all_in_fs_table_as_correct_names_uniks[index_a_correct_gene_name]
      # lets get a list of the fts written in a MT fashion that were composed from a_correct_gene_name
      list_fts_MT_names_corresponding_to_a_correct_gene_name <- c()
      for (index_a_MT_ft_name2 in c(1:length(list_fts_unik_in_fs_table_raw_nnc_only_marks_only))){
        a_MT_ft_name2 = list_fts_unik_in_fs_table_raw_nnc_only_marks_only[index_a_MT_ft_name2]
        pieces_of_ftname_as_MT_name2 <- strsplit(a_MT_ft_name2, "_in_")[[1]] # NB : if the sep is not found, a vector of only the entire word is kept so getting the 1st elt gives it also
        ftname_as_correct_initial_name2 <-pieces_of_ftname_as_MT_name2[1]
        if (ftname_as_correct_initial_name2==a_correct_gene_name){
          list_fts_MT_names_corresponding_to_a_correct_gene_name = c(list_fts_MT_names_corresponding_to_a_correct_gene_name,a_MT_ft_name2)
        }
      }
      # lets get restrict the table with marks to only the rows that contain the correct gene name
      # fs_table_raw_nnc_only_marks_only_1_gene_rows <- fs_table_raw_nnc_only_marks_only[which(grepl(a_correct_gene_name, fs_table_raw_nnc_only_marks_only$Features, fixed=TRUE)), ] # deprecated
      fs_table_raw_nnc_only_marks_only_1_gene_rows <- fs_table_raw_nnc_only_marks_only[which(fs_table_raw_nnc_only_marks_only$Features %in% list_fts_MT_names_corresponding_to_a_correct_gene_name), ]
      # lets compute an added row that will contain the total of each column of marks
      fs_table_raw_nnc_only_marks_only_1_gene_rows_no_ft_col = fs_table_raw_nnc_only_marks_only_1_gene_rows[,2:13]
      fs_table_raw_nnc_only_marks_only_1_gene_rows_no_ft_col["Total" ,] <- colSums(fs_table_raw_nnc_only_marks_only_1_gene_rows_no_ft_col)
      # lets add the result row as a row in our matrix containing only the correct names of genes
      my_one_gene_copy_matrix[my_one_gene_copy_matrix$Features == a_correct_gene_name,2:13] <- fs_table_raw_nnc_only_marks_only_1_gene_rows_no_ft_col["Total",]
    }
    # keep the new table
    fs_table_raw_nnc_only_marks_only_and_pruned = my_one_gene_copy_matrix
  }
  
  # - lets add to a collector, this output table with marks only and with only one copy of each gene
  # NB : to facilitate a future aggregation into one of these tables, the col 1 (Features is used as rownames)
  rownames(fs_table_raw_nnc_only_marks_only_and_pruned) <- fs_table_raw_nnc_only_marks_only_and_pruned[,1]
  fs_table_raw_nnc_only_marks_only_and_pruned[,1] <- NULL
  list_fs_tables_retrieved_RAW_marks_only_and_pruned[[index_of_an_alg]] <- fs_table_raw_nnc_only_marks_only_and_pruned
  # -----------------chunk 1

  # - lets give an update on what have just been completed
  paste("- FS ",index_of_an_alg," analysis finished and it is for ",tag_alg_corresp_2_fs_retrieved,"_on_",tag_nickname_cohort_corresp_2_fs_retrieved, sep='')
  num_initial_sets_analysed <- num_initial_sets_analysed + 1
  paste("Number of FSs analysed : ",num_initial_sets_analysed, sep='')
}
# end of work on all FSs
        
# - lets unify the tables that contains only one copy of a gene and the marks cols only
# add rownames as a column in each data.frame and bind rows
# ------ TO CHANGE IF DATA CHANGES :  for now, we dont have a way to make loop for the pipes so we just resort to modifying the precedent chunk of code that unifies thefinal tables to get the big ones
# always copy and paste below, then modify before launching a different version 
#>>>>>>>>>>>>>>version for 7 FSs analysis (uncomment to use)
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs <- bind_rows(list_fs_tables_retrieved_RAW_marks_only_and_pruned[[1]] %>% add_rownames(), 
                                                                 list_fs_tables_retrieved_RAW_marks_only_and_pruned[[2]] %>% add_rownames(),
                                                                 list_fs_tables_retrieved_RAW_marks_only_and_pruned[[3]] %>% add_rownames(),
                                                                 list_fs_tables_retrieved_RAW_marks_only_and_pruned[[4]] %>% add_rownames(),
                                                                 list_fs_tables_retrieved_RAW_marks_only_and_pruned[[5]] %>% add_rownames(),
                                                                 list_fs_tables_retrieved_RAW_marks_only_and_pruned[[6]] %>% add_rownames(),
                                                                 list_fs_tables_retrieved_RAW_marks_only_and_pruned[[7]] %>% add_rownames()) %>% 
  # evaluate following calls for each value in the rowname column
  group_by(rowname) %>% 
  # add all non-grouping variables
  summarise_all(sum)
#<<<<<<<<<<<<<<<<<<<<<<
# #>>>>>>>>>>>>>>version for 6 FSs analysis (uncomment to use)
# fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs <- bind_rows(list_fs_tables_retrieved_RAW_marks_only_and_pruned[[1]] %>% add_rownames(), 
#                                                                  list_fs_tables_retrieved_RAW_marks_only_and_pruned[[2]] %>% add_rownames(),
#                                                                  list_fs_tables_retrieved_RAW_marks_only_and_pruned[[3]] %>% add_rownames(),
#                                                                  list_fs_tables_retrieved_RAW_marks_only_and_pruned[[4]] %>% add_rownames(),
#                                                                  list_fs_tables_retrieved_RAW_marks_only_and_pruned[[5]] %>% add_rownames(),
#                                                                  list_fs_tables_retrieved_RAW_marks_only_and_pruned[[6]] %>% add_rownames()) %>% 
#   # evaluate following calls for each value in the rowname column
#   group_by(rowname) %>% 
#   # add all non-grouping variables
#   summarise_all(sum)
# #<<<<<<<<<<<<<<<<<<<<<<
# #>>>>>>>>>>>>>>version for 2 FSs analysis (uncomment to use)
# fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs <- bind_rows(list_fs_tables_retrieved_RAW_marks_only_and_pruned[[1]] %>% add_rownames(), 
#                                                                  list_fs_tables_retrieved_RAW_marks_only_and_pruned[[2]] %>% add_rownames()) %>% 
#   # evaluate following calls for each value in the rowname column
#   group_by(rowname) %>% 
#   # add all non-grouping variables
#   summarise_all(sum)
# #<<<<<<<<<<<<<<<<<<<<<<


# - styling the final table
# -- rename the Features column that got used as rownames and brought bacl as a column
colnames(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs)[1] <- "Features"
# # -- Optional : with this line, we can remove the Feat4Intercept (_SyntheticFeat4Intercept) and call it table V1
# fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs$Features !="_SyntheticFeat4Intercept"),]

# - lets make a version of the final unified table that will have this in addition : 
#... an additionnal set of A to S cols without a number such as LETTER = LETTER1 + LETTER2
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2 = fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_A <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_A1 + fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_A2
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_Q <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_Q1 + fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_Q2
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_M <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_M1 + fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_M2
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_S <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_S1 + fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_S2
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_F <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_F1 + fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_F2
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_T <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_T1 + fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_T2
#... an additional col O (as number of Operational final spaces : this is the number of the actionnable final spaces ie the ones used for the count ebcause they did not have been eliminated through the cleaning or due to exceptions)
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_O <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_T - fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_F

# #---------------------Optional : isolate the non pruned and the pruned tables collected in order to verify computations and look for exceptions to deal with
# # a small part to isolate all the pruned in separate tables
# pruned1 = list_fs_tables_retrieved_RAW_marks_only_and_pruned[[1]]
# pruned2 = list_fs_tables_retrieved_RAW_marks_only_and_pruned[[2]]
# pruned3 = list_fs_tables_retrieved_RAW_marks_only_and_pruned[[3]]
# pruned4 = list_fs_tables_retrieved_RAW_marks_only_and_pruned[[4]]
# pruned5 = list_fs_tables_retrieved_RAW_marks_only_and_pruned[[5]]
# pruned6 = list_fs_tables_retrieved_RAW_marks_only_and_pruned[[6]]
# pruned7 = list_fs_tables_retrieved_RAW_marks_only_and_pruned[[7]]
# # a small part to isolate all non pruned yet in separate tables
# non_pruned1 = list_fs_tables_retrieved_RAW_w_stats_and_marks[[1]]
# non_pruned2 = list_fs_tables_retrieved_RAW_w_stats_and_marks[[2]]
# non_pruned3 = list_fs_tables_retrieved_RAW_w_stats_and_marks[[3]]
# non_pruned4 = list_fs_tables_retrieved_RAW_w_stats_and_marks[[4]]
# non_pruned5 = list_fs_tables_retrieved_RAW_w_stats_and_marks[[5]]
# non_pruned6 = list_fs_tables_retrieved_RAW_w_stats_and_marks[[6]]
# non_pruned7 = list_fs_tables_retrieved_RAW_w_stats_and_marks[[7]]

# #---------------------Optional : lets write some lines about finding the uniques values in each col (in order to known how to better write requests for restrictions on our V2 table)
# paste("- unique values for the col crit_A1 are :",sep='')
# unique(sort(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_A1,decreasing = TRUE))
# paste("- unique values for the col crit_Q1 are :",sep='')
# unique(sort(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_Q1,decreasing = TRUE))
# paste("- unique values for the col crit_M1 are :",sep='')
# unique(sort(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_M1,decreasing = TRUE))
# paste("- unique values for the col crit_S1 are :",sep='')
# unique(sort(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_S1,decreasing = TRUE))
# paste("- unique values for the col crit_F1 are :",sep='')
# unique(sort(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_F1,decreasing = TRUE))
# paste("- unique values for the col crit_T1 are :",sep='')
# unique(sort(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_T1,decreasing = TRUE))
# paste("- unique values for the col crit_A2 are :",sep='')
# unique(sort(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_A2,decreasing = TRUE))
# paste("- unique values for the col crit_Q2 are :",sep='')
# unique(sort(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_Q2,decreasing = TRUE))
# paste("- unique values for the col crit_M2 are :",sep='')
# unique(sort(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_M2,decreasing = TRUE))
# paste("- unique values for the col crit_S2 are :",sep='')
# unique(sort(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_S2,decreasing = TRUE))
# paste("- unique values for the col crit_F2 are :",sep='')
# unique(sort(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_F2,decreasing = TRUE))
# paste("- unique values for the col crit_T2 are :",sep='')
# unique(sort(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_T2,decreasing = TRUE))
# paste("- unique values for the col crit_A are :",sep='')
# unique(sort(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_A,decreasing = TRUE))
# paste("- unique values for the col crit_Q are :",sep='')
# unique(sort(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_Q,decreasing = TRUE))
# paste("- unique values for the col crit_M are :",sep='')
# unique(sort(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_M,decreasing = TRUE))
# paste("- unique values for the col crit_S are :",sep='')
# unique(sort(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_S,decreasing = TRUE))
# paste("- unique values for the col crit_F are :",sep='')
# unique(sort(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_F,decreasing = TRUE))
# paste("- unique values for the col crit_T are :",sep='')
# unique(sort(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_T,decreasing = TRUE))
# #----------------- 


# lets make a V3 version of the final table with additionnal cols for easy requests answering
# lexical : "fsc"=final space of coefs; "afsc" = actionnable final space of coefs
# - a col "At_least_1_afsc" ie 
# - a col "Same_Sign_Always" ie All_model_occurences_with_Same_Sign_Always
# - a col "All_afsc_were_critA"
# - a col "All_afsc_were_critQ"
# - a col "All_afsc_were_critM"
# - a col "At_least_1_afsc_was_critA"
# - a col "At_least_1_afsc_was_critQ"
# - a col "At_least_1_afsc_was_critM"
# to fill each col, we have to : 
# - create the col and fill it with a default value "_NOT_CHANGED_YET" (the string starting with _ make it appears on top when sorting the col for easy observation if all cells were filled or not)
# - the list of genes for rows where a col has to have a "Y" (Y is for Yes)
# - the list of genes for rows where a col has to have a "N" (N is for No)
# - fill each col with the value for the gene according to its qualities


# -- lets create the cols and initialize them 
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3 = fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc <- "_NOT_CHANGED_YET"
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Same_Sign_Always <- "_NOT_CHANGED_YET"
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Same_Sign_Always_Sign <- "_NOT_CHANGED_YET"
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$All_afsc_were_critA <- "_NOT_CHANGED_YET"
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$All_afsc_were_critQ <- "_NOT_CHANGED_YET"
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$All_afsc_were_critM <- "_NOT_CHANGED_YET"
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc_was_critA <- "_NOT_CHANGED_YET"
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc_was_critQ <- "_NOT_CHANGED_YET"
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc_was_critM <- "_NOT_CHANGED_YET"

# -- lets get the 2 lists of genes for each col
# ---lets get a list of the genes in the final table to loop over them and add each one in the list its has to be into because of certain qualities
list_fts_in_table_V3 = unique(as.character(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features))
# ---lets make the collector lists of genes according to each quality
list_fts_At_least_1_afsc_Yes = c()
list_fts_At_least_1_afsc_No = c()
list_fts_Same_Sign_Always_Yes = c()
list_fts_Same_Sign_Always_No = c()
list_fts_Same_Sign_Always_Yes_Pos = c()
list_fts_Same_Sign_Always_Yes_Neg = c()
list_fts_All_afsc_were_critA_Yes = c()
list_fts_All_afsc_were_critA_No = c()
list_fts_All_afsc_were_critQ_Yes = c()
list_fts_All_afsc_were_critQ_No = c()
list_fts_All_afsc_were_critM_Yes = c()
list_fts_All_afsc_were_critM_No = c()
list_fts_At_least_1_afsc_was_critA_Yes = c()
list_fts_At_least_1_afsc_was_critA_No = c()
list_fts_At_least_1_afsc_was_critQ_Yes = c()
list_fts_At_least_1_afsc_was_critQ_No = c()
list_fts_At_least_1_afsc_was_critM_Yes = c()
list_fts_At_least_1_afsc_was_critM_No = c()
# ---lets loop on the genes now and add each in the lists its has to be into
for (a_ft_in_table_V3 in list_fts_in_table_V3){ # for test use a_ft_in_table_V3 = list_fts_in_table_V3[3]
  # for the ft, lets get the value of each of the cols to use for computations of qualities
  # - the val in the col crit_O (val_O)
  val_O = fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$crit_O[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features == a_ft_in_table_V3)]
  # - the val in the col crit_S (val_S) and its components as letters A B C D in S (S = AB,CD) in order to compute val_all_neg and val_all_pos
  val_S = fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$crit_S[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features == a_ft_in_table_V3)]
  val_A = floor(val_S/10) # got one
  val_AB = floor(val_S)
  val_B = val_AB - (val_A*10) # got one
  val_ABC = floor(val_S*10)
  val_C = val_ABC - (val_AB*10) # got one
  val_ABCD = floor(val_S*100)
  val_D = val_ABCD - (val_ABC*10) # got one
  # paste("- in succession, here are S,A,B,C,D : ",val_S,val_A,val_B,val_C,val_D,sep=' - ') # to test
  val_all_neg_in_val_O = val_A + (val_C/10) # lets get the value of the total negatives in the form of (crit_T - crit_F)
  va_all_pos_in_val_O = val_B + (val_D/10)
  # - the val in the col crit_A (val_A)
  val_A = fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$crit_A[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features == a_ft_in_table_V3)]
  # - the val in the col crit_Q (val_Q)
  val_Q = fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$crit_Q[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features == a_ft_in_table_V3)]
  # - the val in the col crit_M (val_M)
  val_M = fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$crit_M[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features == a_ft_in_table_V3)]
  
  # for the ft, lets add it in the proper list for each quality
  # - the quality "At_least_1_afsc"
  if (val_O > 0.0){
    list_fts_At_least_1_afsc_Yes = c(list_fts_At_least_1_afsc_Yes,a_ft_in_table_V3)
    # NB : only because the gene has at least 1 afsc, the following cols will see their val changed
    # - the quality "Same_Sign_Always"
    if ((val_O==val_all_neg_in_val_O)|(val_O==va_all_pos_in_val_O)){
      list_fts_Same_Sign_Always_Yes = c(list_fts_Same_Sign_Always_Yes,a_ft_in_table_V3)
      if (val_O==val_all_neg_in_val_O){ # keeping it in the squad of the always neg 
        list_fts_Same_Sign_Always_Yes_Neg = c(list_fts_Same_Sign_Always_Yes_Neg,a_ft_in_table_V3)
      } else if (val_O==va_all_pos_in_val_O) { # keeping it in the squad of the always pos
        list_fts_Same_Sign_Always_Yes_Pos = c(list_fts_Same_Sign_Always_Yes_Pos,a_ft_in_table_V3)
      }
    } else{
      list_fts_Same_Sign_Always_No = c(list_fts_Same_Sign_Always_No,a_ft_in_table_V3)
    }
    # - the quality "All_afsc_were_critA"
    if (val_O == val_A){
      list_fts_All_afsc_were_critA_Yes = c(list_fts_All_afsc_were_critA_Yes,a_ft_in_table_V3)
    } else{
      list_fts_All_afsc_were_critA_No = c(list_fts_All_afsc_were_critA_No,a_ft_in_table_V3)
    }
    # - the quality "All_afsc_were_critQ"
    if (val_O == val_Q){
      list_fts_All_afsc_were_critQ_Yes = c(list_fts_All_afsc_were_critQ_Yes,a_ft_in_table_V3)
    } else{
      list_fts_All_afsc_were_critQ_No = c(list_fts_All_afsc_were_critQ_No,a_ft_in_table_V3)
    }
    # - the quality "All_afsc_were_critM"
    if (val_O == val_M){
      list_fts_All_afsc_were_critM_Yes = c(list_fts_All_afsc_were_critM_Yes,a_ft_in_table_V3)
    } else{
      list_fts_All_afsc_were_critM_No = c(list_fts_All_afsc_were_critM_No,a_ft_in_table_V3)
    }
    # - the quality "At_least_1_afsc_was_critA"
    if (val_A >= 0.1){
      list_fts_At_least_1_afsc_was_critA_Yes = c(list_fts_At_least_1_afsc_was_critA_Yes,a_ft_in_table_V3)
    } else{
      list_fts_At_least_1_afsc_was_critA_No = c(list_fts_At_least_1_afsc_was_critA_No,a_ft_in_table_V3)
    }
    # - the quality "At_least_1_afsc_was_critQ"
    if (val_Q >= 0.1){
      list_fts_At_least_1_afsc_was_critQ_Yes = c(list_fts_At_least_1_afsc_was_critQ_Yes,a_ft_in_table_V3)
    } else{
      list_fts_At_least_1_afsc_was_critQ_No = c(list_fts_At_least_1_afsc_was_critQ_No,a_ft_in_table_V3)
    }
    # - the quality "At_least_1_afsc_was_critM"
    if (val_M >= 0.1){
      list_fts_At_least_1_afsc_was_critM_Yes = c(list_fts_At_least_1_afsc_was_critM_Yes,a_ft_in_table_V3)
    } else{
      list_fts_At_least_1_afsc_was_critM_No = c(list_fts_At_least_1_afsc_was_critM_No,a_ft_in_table_V3)
    }
  } else{
    list_fts_At_least_1_afsc_No = c(list_fts_At_least_1_afsc_No,a_ft_in_table_V3)
    # NB : because the gene DONT HAVE at least 1 afsc, the following cols will NOT see their val changed
    # cols "Same_Sign_Always","All_afsc_were_critA/Q/M", "At_least_1_afsc_was_critA/Q/M" will still have the default placeholder value _NOT_CHANGED_YET"
  }
  # for the present ft, it has been added in all proper list of qualities ! 
}

# -- lets fill each col with the value for the gene according to its qualities
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features %in% list_fts_At_least_1_afsc_Yes)] <- "Y"
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features %in% list_fts_At_least_1_afsc_No)] <- "N"

fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Same_Sign_Always[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features %in% list_fts_Same_Sign_Always_Yes)] <- "Y"
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Same_Sign_Always[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features %in% list_fts_Same_Sign_Always_No)] <- "N"

fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Same_Sign_Always_Sign[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features %in% list_fts_Same_Sign_Always_Yes_Neg)] <- "Neg"
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Same_Sign_Always_Sign[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features %in% list_fts_Same_Sign_Always_Yes_Pos)] <- "Pos"


fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$All_afsc_were_critA[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features %in% list_fts_All_afsc_were_critA_Yes)] <- "Y"
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$All_afsc_were_critA[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features %in% list_fts_All_afsc_were_critA_No)] <- "N"

fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$All_afsc_were_critQ[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features %in% list_fts_All_afsc_were_critQ_Yes)] <- "Y"
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$All_afsc_were_critQ[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features %in% list_fts_All_afsc_were_critQ_No)] <- "N"

fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$All_afsc_were_critM[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features %in% list_fts_All_afsc_were_critM_Yes)] <- "Y"
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$All_afsc_were_critM[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features %in% list_fts_All_afsc_were_critM_No)] <- "N"

fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc_was_critA[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features %in% list_fts_At_least_1_afsc_was_critA_Yes)] <- "Y"
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc_was_critA[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features %in% list_fts_At_least_1_afsc_was_critA_No)] <- "N"

fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc_was_critQ[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features %in% list_fts_At_least_1_afsc_was_critQ_Yes)] <- "Y"
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc_was_critQ[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features %in% list_fts_At_least_1_afsc_was_critQ_No)] <- "N"

fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc_was_critM[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features %in% list_fts_At_least_1_afsc_was_critM_Yes)] <- "Y"
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc_was_critM[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Features %in% list_fts_At_least_1_afsc_was_critM_No)] <- "N"

# - lets get the numbers for the requests we might need to answer 
# --ALL) Number of unique genes across the models, wether its fsc has zeros or not (num_unique_genes)
num_unique_genes <-dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3)[1]
paste("- Number of unique genes across the models wether its fsc has zeros or not : ",num_unique_genes,sep='')


# --0) Number of unique genes across the models, wether its fsc has zeros or not, that have at least 1 afsc across all models (num_unique_genes_At_least_1_afsc_Yes) 
#...also we get the number of the rest (num_unique_genes_At_least_1_afsc_No)
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_At_least_1_afsc_Yes <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc == "Y"),]
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_At_least_1_afsc_No <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc == "N"),]
num_unique_genes_At_least_1_afsc_Yes <- dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_At_least_1_afsc_Yes)[1]
num_unique_genes_At_least_1_afsc_No <- dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_At_least_1_afsc_No)[1]
paste("- Number of unique genes across the models, wether its fsc has zeros or not, that have at least 1 afsc across all models : ",num_unique_genes_At_least_1_afsc_Yes,sep='')
paste("- Number of unique genes across the models, wether its fsc has zeros or not, that DONT have at least 1 afsc across all models : ",num_unique_genes_At_least_1_afsc_No,sep='')


# --1) Number of unique genes across the models, wether its fsc has zeros or not, that have at least 1 afsc across all models, and that have the Same Sign across all models analysed (num_unique_genes_Same_Sign_Always_Yes) 
#...also we get the number of the rest (num_unique_genes_Same_Sign_Always_No)
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3[which((fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc == "Y")
                                                                                                                                            &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Same_Sign_Always == "Y")),]
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_No <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3[which((fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc == "Y")
                                                                                                                                           &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Same_Sign_Always == "N")),]
num_unique_genes_Same_Sign_Always_Yes <- dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes)[1]
num_unique_genes_Same_Sign_Always_No <- dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_No)[1]
paste("- Number of unique genes across the models, wether its fsc has zeros or not, that have at least 1 afsc across all models, and that have the Same Sign across all models analysed : ",num_unique_genes_Same_Sign_Always_Yes,sep='')
paste("- Number of unique genes across the models, wether its fsc has zeros or not, that have at least 1 afsc across all models, and that DONT have the Same Sign across all models analysed : ",num_unique_genes_Same_Sign_Always_No,sep='')

    
# --2) Number of unique genes across the models, wether its fsc has zeros or not, that have at least 1 afsc across all models, and that have the Same Sign across all models analysed, and where we have a certain stringency limit for stats of models as : 
#...- always same sign genes where at least 1 afsc had crit_A as 1 (num_unique_genes_Same_Sign_Always_Yes_atleast1afscascritA) 
#...- always same sign genes where at least 1 afsc had crit_Q as 1 (num_unique_genes_Same_Sign_Always_Yes_atleast1afscascritQ) 
#...- always same sign genes where at least 1 afsc had crit_M as 1 (num_unique_genes_Same_Sign_Always_Yes_atleast1afscascritM)    
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes_atleast1afscascritA <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3[which((fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc == "Y")
                                                                                                                                            &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Same_Sign_Always == "Y")
                                                                                                                                            &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc_was_critA == "Y")),]
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes_atleast1afscascritQ <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3[which((fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc == "Y")
                                                                                                                                            &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Same_Sign_Always == "Y")
                                                                                                                                            &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc_was_critQ == "Y")),]
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes_atleast1afscascritM <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3[which((fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc == "Y")
                                                                                                                                            &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Same_Sign_Always == "Y")
                                                                                                                                            &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc_was_critM == "Y")),]
num_unique_genes_Same_Sign_Always_Yes_atleast1afscascritA <- dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes_atleast1afscascritA)[1]
num_unique_genes_Same_Sign_Always_Yes_atleast1afscascritQ <- dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes_atleast1afscascritQ)[1]
num_unique_genes_Same_Sign_Always_Yes_atleast1afscascritM <- dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes_atleast1afscascritM)[1]
paste("- num_unique_genes_Same_Sign_Always_Yes_atleast1afscascritA : ",num_unique_genes_Same_Sign_Always_Yes_atleast1afscascritA,sep='')
paste("- num_unique_genes_Same_Sign_Always_Yes_atleast1afscascritQ : ",num_unique_genes_Same_Sign_Always_Yes_atleast1afscascritQ,sep='')
paste("- num_unique_genes_Same_Sign_Always_Yes_atleast1afscascritM : ",num_unique_genes_Same_Sign_Always_Yes_atleast1afscascritM,sep='')
#...- always same sign genes where all afsc had crit_A as 1 (num_unique_genes_Same_Sign_Always_Yes_allafscascritA)
#...- always same sign genes where all afsc had crit_Q as 1 (num_unique_genes_Same_Sign_Always_Yes_allafscascritQ)
#...- always same sign genes where all afsc had crit_M as 1 (num_unique_genes_Same_Sign_Always_Yes_allafscascritM)
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes_allafscascritA <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3[which((fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc == "Y")
                                                                                                                                                                &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Same_Sign_Always == "Y")
                                                                                                                                                                &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$All_afsc_were_critA == "Y")),]
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes_allafscascritQ <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3[which((fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc == "Y")
                                                                                                                                                           &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Same_Sign_Always == "Y")
                                                                                                                                                           &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$All_afsc_were_critQ == "Y")),]
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes_allafscascritM <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3[which((fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc == "Y")
                                                                                                                                                           &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Same_Sign_Always == "Y")
                                                                                                                                                           &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$All_afsc_were_critM == "Y")),]
num_unique_genes_Same_Sign_Always_Yes_allafscascritA <- dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes_allafscascritA)[1]
num_unique_genes_Same_Sign_Always_Yes_allafscascritQ <- dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes_allafscascritQ)[1]
num_unique_genes_Same_Sign_Always_Yes_allafscascritM <- dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes_allafscascritM)[1]
paste("- num_unique_genes_Same_Sign_Always_Yes_allafscascritA : ",num_unique_genes_Same_Sign_Always_Yes_allafscascritA,sep='')
paste("- num_unique_genes_Same_Sign_Always_Yes_allafscascritQ : ",num_unique_genes_Same_Sign_Always_Yes_allafscascritQ,sep='')
paste("- num_unique_genes_Same_Sign_Always_Yes_allafscascritM : ",num_unique_genes_Same_Sign_Always_Yes_allafscascritM,sep='')

# #>>>>>>>>>>>>> uncomment to use
# #...also we get the number of the rest : 
# #...- NOT always same sign genes where at least 1 afsc had crit_A as 1 (num_unique_genes_Same_Sign_Always_No_atleast1afscascritA) 
# #...- NOT always same sign genes where at least 1 afsc had crit_Q as 1 (num_unique_genes_Same_Sign_Always_No_atleast1afscascritQ) 
# #...- NOT always same sign genes where at least 1 afsc had crit_M as 1 (num_unique_genes_Same_Sign_Always_No_atleast1afscascritM) 
# fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_No_atleast1afscascritA <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3[which((fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc == "Y")
#                                                                                                                                                                 &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Same_Sign_Always == "N")
#                                                                                                                                                                 &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc_was_critA == "Y")),]
# fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_No_atleast1afscascritQ <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3[which((fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc == "Y")
#                                                                                                                                                                 &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Same_Sign_Always == "N")
#                                                                                                                                                                 &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc_was_critQ == "Y")),]
# fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_No_atleast1afscascritM <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3[which((fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc == "Y")
#                                                                                                                                                                 &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Same_Sign_Always == "N")
#                                                                                                                                                                 &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc_was_critM == "Y")),]
# num_unique_genes_Same_Sign_Always_No_atleast1afscascritA <- dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_No_atleast1afscascritA)[1]
# num_unique_genes_Same_Sign_Always_No_atleast1afscascritQ <- dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_No_atleast1afscascritQ)[1]
# num_unique_genes_Same_Sign_Always_No_atleast1afscascritM <- dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_No_atleast1afscascritM)[1]
# paste("- num_unique_genes_Same_Sign_Always_No_atleast1afscascritA : ",num_unique_genes_Same_Sign_Always_No_atleast1afscascritA,sep='')
# paste("- num_unique_genes_Same_Sign_Always_No_atleast1afscascritQ : ",num_unique_genes_Same_Sign_Always_No_atleast1afscascritQ,sep='')
# paste("- num_unique_genes_Same_Sign_Always_No_atleast1afscascritM : ",num_unique_genes_Same_Sign_Always_No_atleast1afscascritM,sep='')
# 
# #...- NOT always same sign genes where all afsc had crit_A as 1 (num_unique_genes_Same_Sign_Always_No_allafscascritA)
# #...- NOT always same sign genes where all afsc had crit_Q as 1 (num_unique_genes_Same_Sign_Always_No_allafscascritQ)
# #...- NOT always same sign genes where all afsc had crit_M as 1 (num_unique_genes_Same_Sign_Always_No_allafscascritM)
# fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_No_allafscascritA <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3[which((fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc == "Y")
#                                                                                                                                                            &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Same_Sign_Always == "N")
#                                                                                                                                                            &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$All_afsc_were_critA == "Y")),]
# fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_No_allafscascritQ <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3[which((fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc == "Y")
#                                                                                                                                                            &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Same_Sign_Always == "N")
#                                                                                                                                                            &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$All_afsc_were_critQ == "Y")),]
# fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_No_allafscascritM <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3[which((fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$At_least_1_afsc == "Y")
#                                                                                                                                                            &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Same_Sign_Always == "N")
#                                                                                                                                                            &(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$All_afsc_were_critM == "Y")),]
# num_unique_genes_Same_Sign_Always_No_allafscascritA <- dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_No_allafscascritA)[1]
# num_unique_genes_Same_Sign_Always_No_allafscascritQ <- dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_No_allafscascritQ)[1]
# num_unique_genes_Same_Sign_Always_No_allafscascritM <- dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_No_allafscascritM)[1]
# paste("- num_unique_genes_Same_Sign_Always_No_allafscascritA : ",num_unique_genes_Same_Sign_Always_No_allafscascritA,sep='')
# paste("- num_unique_genes_Same_Sign_Always_No_allafscascritQ : ",num_unique_genes_Same_Sign_Always_No_allafscascritQ,sep='')
# paste("- num_unique_genes_Same_Sign_Always_No_allafscascritM : ",num_unique_genes_Same_Sign_Always_No_allafscascritM,sep='')
# #<<<<<<<<<<<<< end of uncomment to use

# - WHen looking for the group of genes with the same sign always, we have differents groups the inquiry could be done for...
# with these 2 groups specially attractting our attention : 
# ...."fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes_atleast1afscascritM" : lowest stringency level
# ...."fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes_allafscascritA" : highest stringency level
# lets separate the two groups of genes that sort of sway the regression equation in opposite directions to sort of identify the 2 squad that sways the regression differently
#... "num_unique_genes_Same_Sign_Always_Yes_atleast1afscascritM_SquadofSameSignAsNeg"
#... "num_unique_genes_Same_Sign_Always_Yes_atleast1afscascritM_SquadofSameSignAsPos"
#... "num_unique_genes_Same_Sign_Always_Yes_allafscascritA_SquadofSameSignAsNeg"
#... "num_unique_genes_Same_Sign_Always_Yes_allafscascritA_SquadofSameSignAsPos"

# - the most reusable way to do this is to choose the table restricted to analyse for this and then do the analysis for it (this helps to repeat the analysis while only changing the input...)

# -- choosing the 2 opposing teams table (uncomment to use)
# # --- if it is for the lowest stringency level (D1)
# fs_table_2_opposing_teams_to_analyse <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes_atleast1afscascritM
# # --- if it is for the stringency level D2
# fs_table_2_opposing_teams_to_analyse <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes_atleast1afscascritQ
# # --- if it is for the stringency level D3
# fs_table_2_opposing_teams_to_analyse <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes_atleast1afscascritA
# # --- if it is for the stringency level E1
# fs_table_2_opposing_teams_to_analyse <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes_allafscascritM
# --- if it is for the stringency level E2
fs_table_2_opposing_teams_to_analyse <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes_allafscascritQ
# # --- if it is for the highest stringency level (E3)
# fs_table_2_opposing_teams_to_analyse <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes_allafscascritA

# -- carrying out the analysis of the 2 opposing teams table
fs_table_2_opposing_teams_to_analyse_SquadofSameSignAsNeg <- fs_table_2_opposing_teams_to_analyse[which((fs_table_2_opposing_teams_to_analyse$Same_Sign_Always_Sign == "Neg")),]
fs_table_2_opposing_teams_to_analyse_SquadofSameSignAsPos <- fs_table_2_opposing_teams_to_analyse[which((fs_table_2_opposing_teams_to_analyse$Same_Sign_Always_Sign == "Pos")),]


num_unique_genes_fs_table_2_opposing_teams_to_analyse_SquadofSameSignAsNeg <- dim(fs_table_2_opposing_teams_to_analyse_SquadofSameSignAsNeg)[1]
num_unique_genes_fs_table_2_opposing_teams_to_analyse_SquadofSameSignAsPos <- dim(fs_table_2_opposing_teams_to_analyse_SquadofSameSignAsPos)[1]
paste("- num_unique_genes_fs_table_2_opposing_teams_to_analyse_SquadofSameSignAsNeg : ",num_unique_genes_fs_table_2_opposing_teams_to_analyse_SquadofSameSignAsNeg,sep='')
paste("- num_unique_genes_fs_table_2_opposing_teams_to_analyse_SquadofSameSignAsPos : ",num_unique_genes_fs_table_2_opposing_teams_to_analyse_SquadofSameSignAsPos,sep='')
paste("- The ratio neg as a perc. here is : ",round(((num_unique_genes_fs_table_2_opposing_teams_to_analyse_SquadofSameSignAsNeg/(num_unique_genes_fs_table_2_opposing_teams_to_analyse_SquadofSameSignAsNeg+num_unique_genes_fs_table_2_opposing_teams_to_analyse_SquadofSameSignAsPos))*100),4),sep='')
paste("- The ratio pos as a perc. here is : ",round(((num_unique_genes_fs_table_2_opposing_teams_to_analyse_SquadofSameSignAsPos/(num_unique_genes_fs_table_2_opposing_teams_to_analyse_SquadofSameSignAsNeg+num_unique_genes_fs_table_2_opposing_teams_to_analyse_SquadofSameSignAsPos))*100),4),sep='')
paste("- The ratio #pos/#neg here is : ",round(((num_unique_genes_fs_table_2_opposing_teams_to_analyse_SquadofSameSignAsPos/num_unique_genes_fs_table_2_opposing_teams_to_analyse_SquadofSameSignAsNeg)),4),sep='')

# -- notes :  
# a difference of less than 5% is observed when opposing the ratio of pos and neg between the two groups ie 
# whatever level of stringency we choose, it is going towards a very similar constitution of genes in portion of pos and neg

# eof at 933      
  
  











