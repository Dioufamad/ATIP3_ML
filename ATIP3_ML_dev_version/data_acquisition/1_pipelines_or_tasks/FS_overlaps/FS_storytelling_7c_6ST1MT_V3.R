# this script is the test for counting and identifying the genes that tells the same story ie their differents coefs in regression works have the same sign
# Version 3 (after corrections of Chloé). This version gives you a table with 4 cols : strong_stringency_status, lenient_stringency_status, s_all, s_all_abs.
# when that table is ranked by s_abs_all, you have all the genes that have lenient_stringency_status as 1 and ranked by the s_all_abs.
# Issue here are : 
# - we need to remove the genes with s_all_abs = 0 (4 genes that have that because they passed every check but m_pos_all = m_neg_all). Solution : restrict later to s_all_abs = 1
# - we need to make a gene list for each FS to see historically what happened

# imports 
library(readxl) # for ability to read xlsx and xls files  
library(UpSetR) # for the upset plots
library(ggplot2) # for the attribute plots
library(dplyr) # for the operations on multiples frames using pipes in succession


# - defining collectors for the entry data to use (will be use to access the entire data through loops on these collectors)
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
tag_numcohort7 = "GSE41998_x_GSE26639_x_GSE32646_x_GSE25055_x_GSE20194_x_GSE63471" 
# tag_numcohort7 = "6GSEs" previously (changed to use it as an elt to split and get the compositional cohorts name for specific cols naming)
tag_nickname_cohort7 = "6_joined_dts"
list_paths2files_NNC <- c(list_paths2files_NNC,path2file7_NNC)
list_paths2files_RAW <- c(list_paths2files_RAW,path2file7_RAW)
list_tag_alg <- c(list_tag_alg,tag_alg7)
list_tag_numcohort <- c(list_tag_numcohort,tag_numcohort7)
list_tag_nickname_cohort <- c(list_tag_nickname_cohort,tag_nickname_cohort7)

# >>>>>>>>>> supply the colname where the selected features will be in each file
official_colname_of_selected_features_col = "Features"

# >>>>>>>>>>>> the ideas of scores
# we have a table with these cols to inform : 
# + m_0_st_seen, m_pos_st_seen, m_neg_st_seen, st_fs_where_seen,mt_cp_found, s_st_fs_ x i fs, s_mt_cp_ x i cp, s_all (initialized with 0) ,mt_cp_found, 
# we loop on the FSs : 
# for each FSs, we loop on the genes : 
# - for each gene, 
# + we get m_0_st_fs, m_pos_st_fs, m_neg_st_fs
# + we compute s_st_dt with the 3 fs values
# + we update these cols with them : m_0_st_seen, m_pos_st_seen, m_neg_st_seen
# + we update this cols : s_st_fs_ x i fs with i corresp to the fs being analysed if st fs (or s_mt_cp_ x i cp with i corresp to the cp being analysed if mt fs)
# + we update fs_seen with + 1
# all the FSs have been gone through and all the table cols are supplied with values
# we make each time a paragraph to compute one of the final rules : the result is a table from the inital table that has only the genes answering to the restriction 

# >>>>>>>>> Create a function to define score s.
score_s <- function(m_0,m_pos,m_neg) { 
  m = m_0 + m_pos + m_neg
  if ((m_0 >= (m-1)) | (m_pos == m_neg)) {
    result = 0
  }else{
    if (m_pos > m_neg) {
      result = 1*(m_pos/(m_pos+m_neg))
    }else if (m_neg > m_pos) {
      result = -1*(m_neg/(m_pos+m_neg))
    }
  }
  # result
  return(result)
}
# # for tests
# score_s(1,7,2)
# score_s(1,2,7)
# score_s(9,0,1)
# score_s(2,4,4)
# score_s(10,0,0)

# here was the not needed chunk 1

# here was the not needed chunk 1.5

# >>>>>>>>>>>> Ideas and remarks for the following steps: 
# - NB1:  some way to access the gene of each row using : 
# for (one_of_the_rownames in rownames(fs_table_raw_nnc_only)) {}
# but the column containing the features not usually the row names and we want to keep the number on the rownames as such to keep track of
# if the present list of features is from a discontinued or non discontued list of featurs by the previous restriction done
# hence we will access the rows using each name in the column Features


# - defining collectors for the raw data gathered or produced in order to keep track of whats is seen overall
list_fs_tables_retrieved_NNC = list() #needed
list_fs_tables_retrieved_RAW = list() #neeeded
list_fs_tables_retrieved_RAW_w_stats_and_marks = list() #needed
list_fs_tables_retrieved_RAW_marks_only_and_pruned = list() #needed
num_initial_sets_analysed <- 0 #needed
# output is fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs (a table with all unique genes, each one with its marks for storytelling) 



#>>>>>>>>>>> - for each alg (1 alg gives 1 specific FS with 1 table of raw coefs and 1 table of non nul coefs), lets load its needed csv files, makes the needed computations and stash them
for (index_of_an_alg in c(1:length(list_tag_alg))) { # for test use index_of_an_alg = 4 to restrict from more than 10k genes to 260 genes ; or index_of_an_alg = 7 for MT
  # - keep the tag of the present FS alg in case we need it later (for example to known what type of FS we are analysing)
  tag_alg_corresp_2_fs_retrieved = list_tag_alg[index_of_an_alg]
  # - keep the nickname of the cohort of the present FS alg in case we need it later
  tag_nickname_cohort_corresp_2_fs_retrieved = list_tag_nickname_cohort[index_of_an_alg]
  # - lets state the FS that will be analysed
  writeLines(paste("- FS ",index_of_an_alg," analysis started and it is for ",tag_alg_corresp_2_fs_retrieved,"_on_",tag_nickname_cohort_corresp_2_fs_retrieved, sep=''))
  # - keep the tag_numcohort for the present FS to later target the col to update for the score in ST or MT
  tag_numcohort_corresp_2_fs_retrieved = list_tag_numcohort[index_of_an_alg]
  # - get the path for each the 2 files needed (raw coefs table and non nuls coefs table)
  path2file_NNC = list_paths2files_NNC[index_of_an_alg]
  path2file_RAW = list_paths2files_RAW[index_of_an_alg]
  # - get the table corresponding to the path
  fs_table_nnc <- read.csv(file = path2file_NNC, header = TRUE)
  fs_table_raw <- read.csv(file = path2file_RAW, header = TRUE)
  # - add it to the collector of the fs_tables
  list_fs_tables_retrieved_NNC[[index_of_an_alg]] <- fs_table_nnc
  list_fs_tables_retrieved_RAW[[index_of_an_alg]] <- fs_table_raw
  # - check if the colname of the selected features column is in the colnames of the FS raw and NNC tables 
  #   (to be sure that there will be no surprises as to the colname we use to get the fts))
  colnames_in_fs_table_nnc = names(fs_table_nnc) # use it to also see the cols (to see which ones to keep)
  if (official_colname_of_selected_features_col %in% colnames_in_fs_table_nnc) { 
    paste("- the official_colname_of_selected_features_col IS in the colnames of the NON NULS COEFS FS table !", sep='')
  }else{
    paste("- Warning : the official_colname_of_selected_features_col IS NOT in the colnames of the NON NULS COEFS FS table.", sep='')
  }
  colnames_in_fs_table_raw = names(fs_table_raw) # use it to also see the cols (to see which ones to keep)
  if (official_colname_of_selected_features_col %in% colnames_in_fs_table_raw) { 
    paste("- the official_colname_of_selected_features_col IS in the colnames of the RAW COEFS FS table !", sep='')
  }else{
    paste("- Warning : the official_colname_of_selected_features_col IS NOT in the colnames of the RAW COEFS FS table.", sep='')
  }
  # - restrict the raw table using the nnc table
  # for a test, we shorten the nnc table to only the first 20 lines with this :
  # fs_table_nnc <- fs_table_nnc[1:20,]
  list_fts_in_nnc = unique(as.character(fs_table_nnc$Features))
  fs_table_raw_nnc_only = fs_table_raw[which(fs_table_raw$Features %in% list_fts_in_nnc),]
  
  ## Idea : utiliser une definition du score de qualité et recuperer pour chaque FS resultat d'un alg, les composants du score ainsi que le score
  # -----------------chunk 1
  # for the table of raw coefs that this FS has, we : 
  #...make a copy of the table that wont be modified and always available in its native form to get the values needed more easily in terms of code
  fs_table_raw_nnc_only_stash = fs_table_raw_nnc_only
  #...get the list of genes in the table in order to call it in the all the calls where we need a gene
  list_fts_in_raw_nnc_only = unique(as.character(fs_table_raw_nnc_only_stash$Features))
  #...add to the version of the table to modify the columns that will be supplied with values
  
  # here was the not needed chunk 2
  
  # + m_0_st_seen, m_pos_st_seen, m_neg_st_seen, fs_seen, s_st_fs_ x i fs, s_mt_cp_ x i cp (s_all will be created later on)  
  # the list of the elts for each score
  list_cols_to_create1 <- c("m_0_st_seen","m_pos_st_seen","m_neg_st_seen","m_0_mt_seen","m_pos_mt_seen","m_neg_mt_seen","st_fs_where_seen","mt_cp_found")
  # the list of all the scores s_st_fs_i and s_mt_cp_i
  list_cols_to_create2 <- c()
  # + go through the tag_alg and for each alg, get the scores names to create
  for (index_of_an_alg_bis in c(1:length(list_tag_alg))) { # for test use index_of_an_alg_bis = 4 for ST then index_of_an_alg_bis = 7 for MT
    tag_alg_corresp = list_tag_alg[index_of_an_alg_bis] 
    tag_numcohort_corresp = list_tag_numcohort[index_of_an_alg_bis]
    if (grepl("_ST_", tag_alg_corresp, fixed=TRUE)){ # one score name will be appended to list of scores names
      name_of_1_score_st_to_append = paste("s_st_fs_",tag_numcohort_corresp, sep='')
      list_cols_to_create2 <- c(list_cols_to_create2,name_of_1_score_st_to_append)
    } else if (grepl("_MT_", tag_alg_corresp, fixed=TRUE)){ # multiples score names will be appended to list of scores names
      suffixes_of_multiples_scores_mt_to_append = strsplit(tag_numcohort_corresp, "_x_")[[1]]
      for (suffix_i in suffixes_of_multiples_scores_mt_to_append){
        name_of_a_score_mt_to_append = paste("s_mt_cp_",suffix_i, sep='')
        # writeLines(name_of_a_score_mt_to_append) # for verifications 
        list_cols_to_create2 <- c(list_cols_to_create2,name_of_a_score_mt_to_append)
      }
      # also add a name_of_a_score_mt for the features unique that dont have a cohort name in their name
      list_cols_to_create2 <- c(list_cols_to_create2,"s_mt_cp_unikft")
    }
  }
  list_cols_to_create_all = c(list_cols_to_create1,list_cols_to_create2)
  # create all the new cols for elts of scores and scores (initialized all at zero not NA due to future sum between the tables collected)
  fs_table_raw_nnc_only[list_cols_to_create_all] = 0 
  
  # >>>>>>>>>>>>>> loop on the genes (precisely on the indexes of the list of genes) of the table of raw coefs and update the version of this table to modify
  for (index_of_a_gene in c(1:length(list_fts_in_raw_nnc_only))) { # index_of_a_gene = 4 # use this for tests 
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
    # we have the zeros, pos and neg numbers, we can compute and inform the table now for the gene
    
    # here was the not needed chunk 3
    
    # for each gene, update the values of the elts of the scores, were the gene have been found and one of the scores
    if (grepl("_ST_", tag_alg_corresp_2_fs_retrieved, fixed=TRUE)){
      # for the elts of the st score (to compute)
      fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"m_0_st_seen"] = Nzeros 
      fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"m_pos_st_seen"] = Npos
      fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"m_neg_st_seen"] = Nneg
      # for where the gene have been found
      fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"st_fs_where_seen"] = 1
      # for the score to compute
      value_score_s = score_s(Nzeros,Npos,Nneg)
      name_of_the_score_st_to_update = paste("s_st_fs_",tag_numcohort_corresp_2_fs_retrieved, sep='')
      fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),name_of_the_score_st_to_update] = value_score_s
    } else if (grepl("_MT_", tag_alg_corresp_2_fs_retrieved, fixed=TRUE)){
      # for the elts of the st score (to compute)
      fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"m_0_mt_seen"] = Nzeros 
      fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"m_pos_mt_seen"] = Npos
      fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"m_neg_mt_seen"] = Nneg
      # for where the gene have been found
      fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"mt_cp_found"] = 1
      # for the score to compute
      value_score_s = score_s(Nzeros,Npos,Nneg)
      pieces_MT_gene_name <- strsplit(present_gene, "_in_")[[1]] # NB : if the sep is not found, a vector of only the entire word is kept so getting the 1st elt gives it also
      if (length(pieces_MT_gene_name)==2){ # get the cohortname as the 2nd part of the name and use it to reconstruct the colname of the score to update
        suffix_to_find_in_name_of_the_score_mt_to_update <-pieces_MT_gene_name[2]
        name_of_the_score_mt_to_update = paste("s_mt_cp_",suffix_to_find_in_name_of_the_score_mt_to_update, sep='')
      }else if (length(pieces_MT_gene_name)==1){ # update the score "s_mt_cp_unikft"
        name_of_the_score_mt_to_update = "s_mt_cp_unikft"
      }
      fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),name_of_the_score_mt_to_update] = value_score_s
    }
    
    # here was the not needed chunk 4
    
    # end of the work on a gene (one row of a table of raw coefs)
  } 
  # end of the work on all genes in the present table of raw coefs
  
  
  # - lets add to a collector, this output table with stats and marks 
  list_fs_tables_retrieved_RAW_w_stats_and_marks[[index_of_an_alg]] <- fs_table_raw_nnc_only
  
  # - lets add to another collector, a version of this table that is: 
  # ... pruned (only a unique row is kept for each gene present multiple times) 
  # ... with only the marks cols
  # -- step 1 : lets produce a version with only the marks cols (ie the last length(list_cols_to_create_all) cols) ie last 20 cols # previously last 12 cols
  num_marks_cols = length(list_cols_to_create_all)
  set_of_cols_2_keep_for_marks <- c(colnames(fs_table_raw_nnc_only)[1],tail(colnames(fs_table_raw_nnc_only), num_marks_cols))
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
      # lets restrict the table with marks to only the rows that contain the correct gene name
      # fs_table_raw_nnc_only_marks_only_1_gene_rows <- fs_table_raw_nnc_only_marks_only[which(grepl(a_correct_gene_name, fs_table_raw_nnc_only_marks_only$Features, fixed=TRUE)), ] # deprecated
      fs_table_raw_nnc_only_marks_only_1_gene_rows <- fs_table_raw_nnc_only_marks_only[which(fs_table_raw_nnc_only_marks_only$Features %in% list_fts_MT_names_corresponding_to_a_correct_gene_name), ]
      # lets compute an added row that will contain the total of each column of marks
      fs_table_raw_nnc_only_marks_only_1_gene_rows_no_ft_col = fs_table_raw_nnc_only_marks_only_1_gene_rows[,2:(num_marks_cols+1)]
      fs_table_raw_nnc_only_marks_only_1_gene_rows_no_ft_col["Total" ,] <- colSums(fs_table_raw_nnc_only_marks_only_1_gene_rows_no_ft_col)
      # lets add the result row as a row in our matrix containing only the correct names of genes
      my_one_gene_copy_matrix[my_one_gene_copy_matrix$Features == a_correct_gene_name,2:(num_marks_cols+1)] <- fs_table_raw_nnc_only_marks_only_1_gene_rows_no_ft_col["Total",]
    }
    # keep the new table of one copy per gene wether it is ST or MT
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
  
  # end of the work on a table of raw coefs for one model
}
# end of work on all FSs ##!

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
# #>>>>>>>>>>>>>>version for 3 FSs analysis (uncomment to use)
# fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs <- bind_rows(list_fs_tables_retrieved_RAW_marks_only_and_pruned[[1]] %>% add_rownames(),
#                                                                  list_fs_tables_retrieved_RAW_marks_only_and_pruned[[2]] %>% add_rownames(),
#                                                                  list_fs_tables_retrieved_RAW_marks_only_and_pruned[[3]] %>% add_rownames()) %>%
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
colnames(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs)[1] <- "Features"   ##!  
# # -- Optional : with this line, we can remove the Feat4Intercept (_SyntheticFeat4Intercept) and call it table V1
# fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs$Features !="_SyntheticFeat4Intercept"),]
# make a stash in case of missteps in tests
final_table_0_stash = fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs


# the final table is V1 : 
final_table_V1 = fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs
# - lets make a version of the final unified table that will have this in addition : 
#... the high stringency and lenient stringency status ("y" or "n")
# - lets get the list of fts to loop on
list_fts_in_table_V1 = unique(as.character(final_table_V1$Features))
# - lets get the list of cols for the s_st_fs_i and the list of cols for the s_mt_cp_i
list_cols_for_all_s_st_fs_i = c()
list_cols_for_all_s_mt_cp_i = c()
list_of_cols_final_table_V1 = c(colnames(final_table_V1))
for (a_col_in_list_of_cols_final_table_V1 in list_of_cols_final_table_V1){
  if(startsWith(a_col_in_list_of_cols_final_table_V1, "s_st_fs_")){
    list_cols_for_all_s_st_fs_i = c(list_cols_for_all_s_st_fs_i,a_col_in_list_of_cols_final_table_V1)
  }else if(startsWith(a_col_in_list_of_cols_final_table_V1, "s_mt_cp_")){
    list_cols_for_all_s_mt_cp_i = c(list_cols_for_all_s_mt_cp_i,a_col_in_list_of_cols_final_table_V1)
  }
}
# - lets initialize the cols to inform
final_table_V1$high_string_status <- "_NOT_CHANGED_YET"
# final_table_V1$lenient_string_status <- "_NOT_CHANGED_YET"
final_table_V1$s_all <- 0
final_table_V1$s_all_abs <- 0
final_table_V1$SIG_status <- 0
final_table_V1$Class_of_SIG <- 0
# lets loop through the fts and get the stringency statuses
for (a_ft_in_table_V1 in list_fts_in_table_V1){ # for test use a_ft_in_table_V1 = list_fts_in_table_V1[3]
  # + lets get the elts to compute s_all (score_s_for across all st & all mt)
  val_m_0_st_seen = final_table_V1$m_0_st_seen[which(final_table_V1$Features == a_ft_in_table_V1)]
  val_m_pos_st_seen = final_table_V1$m_pos_st_seen[which(final_table_V1$Features == a_ft_in_table_V1)]
  val_m_neg_st_seen = final_table_V1$m_neg_st_seen[which(final_table_V1$Features == a_ft_in_table_V1)]
  val_m_0_mt_seen = final_table_V1$m_0_mt_seen[which(final_table_V1$Features == a_ft_in_table_V1)]
  val_m_pos_mt_seen = final_table_V1$m_pos_mt_seen[which(final_table_V1$Features == a_ft_in_table_V1)]
  val_m_neg_mt_seen = final_table_V1$m_neg_mt_seen[which(final_table_V1$Features == a_ft_in_table_V1)]
  val_st_fs_where_seen = final_table_V1$st_fs_where_seen[which(final_table_V1$Features == a_ft_in_table_V1)] # this line and the next one are not needed for s-all but to find the strigency statuses
  val_mt_cp_found = final_table_V1$mt_cp_found[which(final_table_V1$Features == a_ft_in_table_V1)]
  m_0_all = val_m_0_st_seen + val_m_0_mt_seen
  m_pos_all = val_m_pos_st_seen + val_m_pos_mt_seen
  m_neg_all = val_m_neg_st_seen + val_m_neg_mt_seen
  # + lets compute s_all and s_all_abs # (##! to be added to the column for it)
  s_all = score_s(m_0_all,m_pos_all,m_neg_all)
  s_all_abs = abs(s_all)
  # + lets get the row of values for the s_st_fs_i and the row of values for the s_mt_cp_i
  # # 3 easy ways to subset a table
  # row_values_for_all_s_st_fs_i_only <- subset(final_table_V1, Features == a_ft_in_table_V1, select = list_cols_for_all_s_st_fs_i)
  # row_values_for_all_s_st_fs_i_only<-final_table_V1[which(final_table_V1$Features %in% a_ft_in_table_V1),names(final_table_V1) %in% list_cols_for_all_s_st_fs_i]
  # row_values_for_all_s_st_fs_i_only<-final_table_V1[which(final_table_V1$Features %in% a_ft_in_table_V1),list_cols_for_all_s_st_fs_i]
  row_values_for_all_s_st_fs_i_only<-final_table_V1[which(final_table_V1$Features %in% a_ft_in_table_V1),list_cols_for_all_s_st_fs_i]
  row_values_for_all_s_mt_cp_i_only<-final_table_V1[which(final_table_V1$Features %in% a_ft_in_table_V1),list_cols_for_all_s_mt_cp_i]
  # + lets make each of these 2 rows as a space of values 
  space_values_for_all_s_st_fs_i_only <-as.numeric(as.vector(row_values_for_all_s_st_fs_i_only))
  space_values_for_all_s_mt_cp_i_only <-as.numeric(as.vector(row_values_for_all_s_mt_cp_i_only))
  # + lets distribute the values in these 2 spaces by quality
  list_s_st_values_high_string = c()
  list_s_mt_values_high_string = c()
  list_s_st_values_lenient_string_crit2 = c()
  list_s_mt_values_lenient_string_crit2 = c()
  for (a_val_in_space_values_for_all_s_st_fs_i_only in space_values_for_all_s_st_fs_i_only){ # for the st space of values
    if (abs(a_val_in_space_values_for_all_s_st_fs_i_only)==1){
      list_s_st_values_high_string = c(list_s_st_values_high_string,a_val_in_space_values_for_all_s_st_fs_i_only)
    }else if (abs(a_val_in_space_values_for_all_s_st_fs_i_only)>=0.9){
      list_s_st_values_lenient_string_crit2 = c(list_s_st_values_lenient_string_crit2,a_val_in_space_values_for_all_s_st_fs_i_only)
    }
  }
  for (a_val_in_space_values_for_all_s_mt_cp_i_only in space_values_for_all_s_mt_cp_i_only){ # for the mt space of values
    if (abs(a_val_in_space_values_for_all_s_mt_cp_i_only)==1){
      list_s_mt_values_high_string = c(list_s_mt_values_high_string,a_val_in_space_values_for_all_s_mt_cp_i_only)
    }else if (abs(a_val_in_space_values_for_all_s_mt_cp_i_only)>=0.9){
      list_s_mt_values_lenient_string_crit2 = c(list_s_mt_values_lenient_string_crit2,a_val_in_space_values_for_all_s_mt_cp_i_only)
    }
  }
  # + lets set the stringency statuses
  high_string_status = "_NOT_CHANGED_YET" # (##! to be added to the column for it)
  if ((length(list_s_st_values_high_string)==val_st_fs_where_seen)&(length(list_s_mt_values_high_string)==val_mt_cp_found)){
    high_string_status = "Y"
  }else{
    high_string_status = "N"
  }
  lenient_string_crit1 = "_NOT_CHANGED_YET"
  if ((length(list_s_st_values_high_string)>=(val_st_fs_where_seen-1))&(length(list_s_mt_values_high_string)>=(val_mt_cp_found-1))){
    lenient_string_crit1 = "Y"
  }else{
    lenient_string_crit1 = "N"
  }
  lenient_string_crit2 = "_NOT_CHANGED_YET"
  if ((length(list_s_st_values_lenient_string_crit2)==val_st_fs_where_seen)&(length(list_s_mt_values_lenient_string_crit2)==val_mt_cp_found)){
    lenient_string_crit2 = "Y"
  }else{
    lenient_string_crit2 = "N"
  }
  lenient_string_status = "_NOT_CHANGED_YET" # (##! to be added to the column for it)
  if ((lenient_string_crit1 == "Y") | (lenient_string_crit2 == "Y")){
    lenient_string_status = "Y"
  }else{
    lenient_string_status = "N"
  }
  # + lets set the SIG_status
  SIG_status = 0 # (##! to be added to the column for it)
  if ((high_string_status == "Y") & (s_all_abs == 1)){
    SIG_status = 1
  }else{
    SIG_status = 0
  }
  # + lets inform the cols (high_string_status,lenient_string_status,s_all, s_all_abs_,SIG_status in that order) 
  final_table_V1[which(final_table_V1$Features %in% a_ft_in_table_V1),"high_string_status"] = high_string_status
  # final_table_V1[which(final_table_V1$Features %in% a_ft_in_table_V1),"lenient_string_status"] = lenient_string_status # not needed
  final_table_V1[which(final_table_V1$Features %in% a_ft_in_table_V1),"s_all"] = s_all
  final_table_V1[which(final_table_V1$Features %in% a_ft_in_table_V1),"s_all_abs"] = s_all_abs
  final_table_V1[which(final_table_V1$Features %in% a_ft_in_table_V1),"SIG_status"] = SIG_status
  # NB : (Class_of_SIG will be informed later because it needs another table for existence of gene)
} 
# lets stash the obtained table in 2 fashions
final_table_V1_complete_stashed = final_table_V1 # full table stashed
# final_table_V1_restricted_to_cols_to_report = final_table_V1[c("Features","high_string_status","lenient_string_status","s_all","s_all_abs","SIG_status","Class_of_SIG")]
final_table_V1_restricted_to_cols_to_report = final_table_V1[c("Features","high_string_status","s_all","s_all_abs","SIG_status","Class_of_SIG")]

# >>>>>>>>>>> adding info of presence absence 1 (in FSs)
# - lets add columns to identify the FS were each ft has existed
final_table_V2 = final_table_V1_restricted_to_cols_to_report
# + lets load the table of presence/absence cols of fts across 7 FS by L1
path2file_pres_abs_fts_7_FSs2_L1Regr = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/presence_absence_table_for_FS_ST_L1_and_FS_MT_SGL1_7InitialSets_19535rows_8cols_GEX.csv"
table_pres_abs <- read.csv(file = path2file_pres_abs_fts_7_FSs2_L1Regr, header = TRUE)
# remove the first col that is just an ordered index (1 to end)
table_pres_abs[,1] <- NULL

names(table_pres_abs) # to see the cols

# + join the presence/absence cols and the SIGs tables on all 7 models
df_left <-final_table_V2
colref_left <- "Features"
df_right <- table_pres_abs
colref_right <- "Features_bis"
final_table_V2 <- merge(x = df_left, y = df_right, by.x = colref_left, by.y = colref_right)
final_table_V2_stash = final_table_V2

# >>>>>>>>>> adding info of presence absence 2 (in DSs)
# - lets add columns to identify the DS were each ft has existed
final_table_V3 = final_table_V2
# + lets load the table of presence/absence cols of fts across 7 FS by L1
path2file_pres_abs_fts_7_DSs = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/presence_absence_table_for_DS_ST_L1_and_DS_MT_SGL1_7InitialSets_19533rows_8cols_GEX.csv"
table_pres_abs_7_DSs <- read.csv(file = path2file_pres_abs_fts_7_DSs, header = TRUE)
# remove the first col that is just an ordered index (1 to end)
table_pres_abs_7_DSs[,1] <- NULL

names(table_pres_abs_7_DSs) # to see the cols

# + join the presence/absence cols and the SIGs tables on all 7 models
df_left <-final_table_V3
colref_left <- "Features"
df_right <- table_pres_abs_7_DSs
colref_right <- "Features_bis"
final_table_V3 <- merge(x = df_left, y = df_right, by.x = colref_left, by.y = colref_right)
final_table_V3_stash = final_table_V3




# -----------------lets make restrictions following questions and plot hist

# >>>>>>>>>>>>> restrcition for V4 (genes SIG_status_as_1)
final_table_V4 = final_table_V3
final_table_V4 <- final_table_V4[which(final_table_V4$SIG_status == 1),]
num_unique_genes_V4 <- dim(final_table_V4)[1]
paste("- Number of genes SIG_status_as_1 : ",num_unique_genes_V4,sep='')
final_table_V4_stashed = final_table_V4

# >>>>>>>>>>>>>> restriction by dataset analysed (genes SIG_status_as_1 in each dt)
final_table_V5 = final_table_V4
# + lets inform the col Class_of_SIG
list_all_SIGs_7FSs = unique(as.character(final_table_V5$Features))
names(final_table_V5) # to see the cols
cols_of_FSs_pres_abs = c("FS_Remagus04", "FS_MDAnderson_part1of2_310", "FS_MT_6_dts", "FS_BMS_Horak_2013", "FS_Osaka_Miyake_2012", "FS_Remagus02", "FS_Fudan_MAQC2BR")
cols_of_DSs_pres_abs = c("DS_Remagus04", "DS_MDAnderson_part1of2_310", "DS_MT_6_dts", "DS_BMS_Horak_2013", "DS_Osaka_Miyake_2012", "DS_Remagus02", "DS_Fudan_MAQC2BR")
for (a_SIG_anywhere in list_all_SIGs_7FSs){ # for test : a_SIG_anywhere = list_all_SIGs_7FSs[3]
  # values to reason on for selection
  row_values_for_selection<-final_table_V5[which(final_table_V5$Features %in% a_SIG_anywhere),cols_of_FSs_pres_abs]
  space_values_for_row_values_for_selection <-as.numeric(as.vector(row_values_for_selection))
  sum_fs_were_selected = sum(space_values_for_row_values_for_selection,na.rm = TRUE)
  # values to reason on for existence (in dt)
  row_values_for_existence<-final_table_V5[which(final_table_V5$Features %in% a_SIG_anywhere),cols_of_DSs_pres_abs]
  space_values_for_row_values_for_existence <-as.numeric(as.vector(row_values_for_existence))
  sum_fs_were_existed = sum(space_values_for_row_values_for_existence,na.rm = TRUE)
  # value to reason on for selection by MT
  val_selected_by_MT = final_table_V5[which(final_table_V5$Features %in% a_SIG_anywhere),"FS_MT_6_dts"]
  # lets define the classes of SIGS
  if ((sum_fs_were_selected ==7)&(val_selected_by_MT==1)){ # class 1
    final_table_V5[which(final_table_V5$Features %in% a_SIG_anywhere),"Class_of_SIG"] = "Class_1"
  } else if ((sum_fs_were_selected ==sum_fs_were_existed)&(val_selected_by_MT==0)){ # class 2
    final_table_V5[which(final_table_V5$Features %in% a_SIG_anywhere),"Class_of_SIG"] = "Class_2"
  } else if ((sum_fs_were_selected ==(sum_fs_were_existed-1))&(val_selected_by_MT==0)){ # class 3
    final_table_V5[which(final_table_V5$Features %in% a_SIG_anywhere),"Class_of_SIG"] = "Class_3"
  } else{ # class 4 ie the rest 
    final_table_V5[which(final_table_V5$Features %in% a_SIG_anywhere),"Class_of_SIG"] = "Class_4"
  }
}

# + the df of SIGs by dt and each class numbers (4 classes)
final_table_V6 = final_table_V5
# for fs ranked all : ie keep the whole previous table (allFSs)
final_table_V6_allFSs = final_table_V6
final_table_V6_allFSs <- final_table_V6_allFSs[order( final_table_V6_allFSs[,6] ),]
num_allclasses_final_table_V6_allFSs = dim(final_table_V6_allFSs)[1]
num_class1_final_table_V6_allFSs = dim(final_table_V6_allFSs[which(final_table_V6_allFSs$Class_of_SIG == "Class_1"),])[1]
num_class2_final_table_V6_allFSs = dim(final_table_V6_allFSs[which(final_table_V6_allFSs$Class_of_SIG == "Class_2"),])[1]
num_class3_final_table_V6_allFSs = dim(final_table_V6_allFSs[which(final_table_V6_allFSs$Class_of_SIG == "Class_3"),])[1]
num_class4_final_table_V6_allFSs = dim(final_table_V6_allFSs[which(final_table_V6_allFSs$Class_of_SIG == "Class_4"),])[1]
name_fs_allFSs = "All7FSs"
name_sheet_for_final_table_V6_allFSs = paste(name_fs_allFSs,"_",num_allclasses_final_table_V6_allFSs,"_",num_class1_final_table_V6_allFSs,
                                            "_",num_class2_final_table_V6_allFSs,"_",num_class3_final_table_V6_allFSs,"_",num_class4_final_table_V6_allFSs, sep='')
# for fs ranked 1 : "FS_Remagus04"
final_table_V6_rank1 = final_table_V6[which(final_table_V6$FS_Remagus04 == 1),]
final_table_V6_rank1 <- final_table_V6_rank1[order( final_table_V6_rank1[,6] ),]
num_allclasses_final_table_V6_rank1 = dim(final_table_V6_rank1)[1]
num_class1_final_table_V6_rank1 = dim(final_table_V6_rank1[which(final_table_V6_rank1$Class_of_SIG == "Class_1"),])[1]
num_class2_final_table_V6_rank1 = dim(final_table_V6_rank1[which(final_table_V6_rank1$Class_of_SIG == "Class_2"),])[1]
num_class3_final_table_V6_rank1 = dim(final_table_V6_rank1[which(final_table_V6_rank1$Class_of_SIG == "Class_3"),])[1]
num_class4_final_table_V6_rank1 = dim(final_table_V6_rank1[which(final_table_V6_rank1$Class_of_SIG == "Class_4"),])[1]
name_fs_rank1 = "FS_R04"
name_sheet_for_final_table_V6_rank1 = paste(name_fs_rank1,"_",num_allclasses_final_table_V6_rank1,"_",num_class1_final_table_V6_rank1,
                                            "_",num_class2_final_table_V6_rank1,"_",num_class3_final_table_V6_rank1,"_",num_class4_final_table_V6_rank1, sep='')
# for fs ranked 2 : "FS_MDAnderson_part1of2_310"
final_table_V6_rank2 = final_table_V6[which(final_table_V6$FS_MDAnderson_part1of2_310 == 1),]
final_table_V6_rank2 <- final_table_V6_rank2[order( final_table_V6_rank2[,6] ),]
num_allclasses_final_table_V6_rank2 = dim(final_table_V6_rank2)[1]
num_class1_final_table_V6_rank2 = dim(final_table_V6_rank2[which(final_table_V6_rank2$Class_of_SIG == "Class_1"),])[1]
num_class2_final_table_V6_rank2 = dim(final_table_V6_rank2[which(final_table_V6_rank2$Class_of_SIG == "Class_2"),])[1]
num_class3_final_table_V6_rank2 = dim(final_table_V6_rank2[which(final_table_V6_rank2$Class_of_SIG == "Class_3"),])[1]
num_class4_final_table_V6_rank2 = dim(final_table_V6_rank2[which(final_table_V6_rank2$Class_of_SIG == "Class_4"),])[1]
name_fs_rank2 = "FS_MDA"
name_sheet_for_final_table_V6_rank2 = paste(name_fs_rank2,"_",num_allclasses_final_table_V6_rank2,"_",num_class1_final_table_V6_rank2,
                                            "_",num_class2_final_table_V6_rank2,"_",num_class3_final_table_V6_rank2,"_",num_class4_final_table_V6_rank2, sep='')
# for fs ranked 3 : "FS_MT_6_dts"
final_table_V6_rank3 = final_table_V6[which(final_table_V6$FS_MT_6_dts == 1),]
final_table_V6_rank3 <- final_table_V6_rank3[order( final_table_V6_rank3[,6] ),]
num_allclasses_final_table_V6_rank3 = dim(final_table_V6_rank3)[1]
num_class1_final_table_V6_rank3 = dim(final_table_V6_rank3[which(final_table_V6_rank3$Class_of_SIG == "Class_1"),])[1]
num_class2_final_table_V6_rank3 = dim(final_table_V6_rank3[which(final_table_V6_rank3$Class_of_SIG == "Class_2"),])[1]
num_class3_final_table_V6_rank3 = dim(final_table_V6_rank3[which(final_table_V6_rank3$Class_of_SIG == "Class_3"),])[1]
num_class4_final_table_V6_rank3 = dim(final_table_V6_rank3[which(final_table_V6_rank3$Class_of_SIG == "Class_4"),])[1]
name_fs_rank3 = "FS_MT"
name_sheet_for_final_table_V6_rank3 = paste(name_fs_rank3,"_",num_allclasses_final_table_V6_rank3,"_",num_class1_final_table_V6_rank3,
                                            "_",num_class2_final_table_V6_rank3,"_",num_class3_final_table_V6_rank3,"_",num_class4_final_table_V6_rank3, sep='')
# for fs ranked 4 : "FS_BMS_Horak_2013"
final_table_V6_rank4 = final_table_V6[which(final_table_V6$FS_BMS_Horak_2013 == 1),]
final_table_V6_rank4 <- final_table_V6_rank4[order( final_table_V6_rank4[,6] ),]
num_allclasses_final_table_V6_rank4 = dim(final_table_V6_rank4)[1]
num_class1_final_table_V6_rank4 = dim(final_table_V6_rank4[which(final_table_V6_rank4$Class_of_SIG == "Class_1"),])[1]
num_class2_final_table_V6_rank4 = dim(final_table_V6_rank4[which(final_table_V6_rank4$Class_of_SIG == "Class_2"),])[1]
num_class3_final_table_V6_rank4 = dim(final_table_V6_rank4[which(final_table_V6_rank4$Class_of_SIG == "Class_3"),])[1]
num_class4_final_table_V6_rank4 = dim(final_table_V6_rank4[which(final_table_V6_rank4$Class_of_SIG == "Class_4"),])[1]
name_fs_rank4 = "FS_BMS_Horak"
name_sheet_for_final_table_V6_rank4 = paste(name_fs_rank4,"_",num_allclasses_final_table_V6_rank4,"_",num_class1_final_table_V6_rank4,
                                            "_",num_class2_final_table_V6_rank4,"_",num_class3_final_table_V6_rank4,"_",num_class4_final_table_V6_rank4, sep='')
# for fs ranked 5 : "FS_Osaka_Miyake_2012"
final_table_V6_rank5 = final_table_V6[which(final_table_V6$FS_Osaka_Miyake_2012 == 1),]
final_table_V6_rank5 <- final_table_V6_rank5[order( final_table_V6_rank5[,6] ),]
num_allclasses_final_table_V6_rank5 = dim(final_table_V6_rank5)[1]
num_class1_final_table_V6_rank5 = dim(final_table_V6_rank5[which(final_table_V6_rank5$Class_of_SIG == "Class_1"),])[1]
num_class2_final_table_V6_rank5 = dim(final_table_V6_rank5[which(final_table_V6_rank5$Class_of_SIG == "Class_2"),])[1]
num_class3_final_table_V6_rank5 = dim(final_table_V6_rank5[which(final_table_V6_rank5$Class_of_SIG == "Class_3"),])[1]
num_class4_final_table_V6_rank5 = dim(final_table_V6_rank5[which(final_table_V6_rank5$Class_of_SIG == "Class_4"),])[1]
name_fs_rank5 = "FS_Osaka"
name_sheet_for_final_table_V6_rank5 = paste(name_fs_rank5,"_",num_allclasses_final_table_V6_rank5,"_",num_class1_final_table_V6_rank5,
                                            "_",num_class2_final_table_V6_rank5,"_",num_class3_final_table_V6_rank5,"_",num_class4_final_table_V6_rank5, sep='')
# for fs ranked 6 : "FS_Remagus02"
final_table_V6_rank6 = final_table_V6[which(final_table_V6$FS_Remagus02 == 1),]
final_table_V6_rank6 <- final_table_V6_rank6[order( final_table_V6_rank6[,6] ),]
num_allclasses_final_table_V6_rank6 = dim(final_table_V6_rank6)[1]
num_class1_final_table_V6_rank6 = dim(final_table_V6_rank6[which(final_table_V6_rank6$Class_of_SIG == "Class_1"),])[1]
num_class2_final_table_V6_rank6 = dim(final_table_V6_rank6[which(final_table_V6_rank6$Class_of_SIG == "Class_2"),])[1]
num_class3_final_table_V6_rank6 = dim(final_table_V6_rank6[which(final_table_V6_rank6$Class_of_SIG == "Class_3"),])[1]
num_class4_final_table_V6_rank6 = dim(final_table_V6_rank6[which(final_table_V6_rank6$Class_of_SIG == "Class_4"),])[1]
name_fs_rank6 = "FS_R02"
name_sheet_for_final_table_V6_rank6 = paste(name_fs_rank6,"_",num_allclasses_final_table_V6_rank6,"_",num_class1_final_table_V6_rank6,
                                            "_",num_class2_final_table_V6_rank6,"_",num_class3_final_table_V6_rank6,"_",num_class4_final_table_V6_rank6, sep='')
# for fs ranked 7 : "FS_Fudan_MAQC2BR"
final_table_V6_rank7 = final_table_V6[which(final_table_V6$FS_Fudan_MAQC2BR == 1),]
final_table_V6_rank7 <- final_table_V6_rank7[order( final_table_V6_rank7[,6] ),]
num_allclasses_final_table_V6_rank7 = dim(final_table_V6_rank7)[1]
num_class1_final_table_V6_rank7 = dim(final_table_V6_rank7[which(final_table_V6_rank7$Class_of_SIG == "Class_1"),])[1]
num_class2_final_table_V6_rank7 = dim(final_table_V6_rank7[which(final_table_V6_rank7$Class_of_SIG == "Class_2"),])[1]
num_class3_final_table_V6_rank7 = dim(final_table_V6_rank7[which(final_table_V6_rank7$Class_of_SIG == "Class_3"),])[1]
num_class4_final_table_V6_rank7 = dim(final_table_V6_rank7[which(final_table_V6_rank7$Class_of_SIG == "Class_4"),])[1]
name_fs_rank7 = "FS_Fudan"
name_sheet_for_final_table_V6_rank7 = paste(name_fs_rank7,"_",num_allclasses_final_table_V6_rank7,"_",num_class1_final_table_V6_rank7,
                                            "_",num_class2_final_table_V6_rank7,"_",num_class3_final_table_V6_rank7,"_",num_class4_final_table_V6_rank7, sep='')

# >>>>>>> lets save now in a excel multiples sheets file
# # + Way 1
# library(xlsx)
# write.xlsx(dataframe1, file="filename.xlsx", sheetName="sheet1", row.names=FALSE)
# write.xlsx(dataframe2, file="filename.xlsx", sheetName="sheet2", append=TRUE, row.names=FALSE)
# + Way 2
require(openxlsx)

# list_of_datasets <- list(name_sheet_for_final_table_V6_allFSs = final_table_V6_allFSs, name_sheet_for_final_table_V6_rank1 = final_table_V6_rank1, 
#                          name_sheet_for_final_table_V6_rank2 = final_table_V6_rank2, name_sheet_for_final_table_V6_rank3 = final_table_V6_rank3,
#                          name_sheet_for_final_table_V6_rank4 = final_table_V6_rank4, name_sheet_for_final_table_V6_rank5 = final_table_V6_rank5,
#                          name_sheet_for_final_table_V6_rank6 = final_table_V6_rank6, name_sheet_for_final_table_V6_rank7 = final_table_V6_rank7)
list_of_datasets <- list("All7FSs_5845_0_10_5794_41" = final_table_V6_allFSs, "FS_R04_41_0_0_0_41" = final_table_V6_rank1, 
                         "FS_MDA_2_0_0_0_2" = final_table_V6_rank2, "FS_MT_7_0_0_0_7" = final_table_V6_rank3,
                         "FS_BMS_Horak_41_0_0_0_41" = final_table_V6_rank4, "FS_Osaka_10_0_10_0_0" = final_table_V6_rank5,
                         "FS_R02_5845_0_10_5794_41" = final_table_V6_rank6, "FS_Fudan_17_0_0_0_17" = final_table_V6_rank7)
write.xlsx(list_of_datasets, file = "SIG_genes_lists2.xlsx")

final_table_V6_stash = final_table_V6
# >>>>>>>>>>>>>>>>>>>>>>>>>> Proposition 2
# most of my interesting genes are in my Class 4
# the thing is its not about genes that can pass the harshest condittions of quality
# but its about genes that, when they are stable, they are stable in a lot of the datasets
final_table_V7 = final_table_V6
# - action 1 : get rid of the last 3 FSs in my present list of SIGs, and get rid of the classes
names(final_table_V7)
final_table_V7_top4FSs = final_table_V7[c("Features", "high_string_status", "s_all", "s_all_abs", "SIG_status", 
                     "FS_Remagus04", "FS_MDAnderson_part1of2_310", "FS_MT_6_dts", "FS_BMS_Horak_2013")]
names(final_table_V7_top4FSs)
# action 2 : add a col of %_#_times_selected_among_top4FSs
list_all_SIGs_top4FSs = unique(as.character(final_table_V7_top4FSs$Features))
cols_top4FSs = c("FS_Remagus04", "FS_MDAnderson_part1of2_310", "FS_MT_6_dts", "FS_BMS_Horak_2013")
for (a_SIG_in_top4FSs in list_all_SIGs_top4FSs){ # for test : a_SIG_in_top4FSs = list_all_SIGs_top4FSs[3]
  # num_times_selected_among_top4FSs
  row_values_for_top4FSs<-final_table_V7_top4FSs[which(final_table_V7_top4FSs$Features %in% a_SIG_in_top4FSs),cols_top4FSs]
  space_values_for_row_values_for_top4FSs <-as.numeric(as.vector(row_values_for_top4FSs))
  num_times_selected_among_top4FSs = sum(space_values_for_row_values_for_top4FSs,na.rm = TRUE)
  # add the col %_#_times_selected_among_top4FSs
  final_table_V7_top4FSs[which(final_table_V7_top4FSs$Features %in% a_SIG_in_top4FSs),"Percentage_selection_among_top4FSs"] = ((num_times_selected_among_top4FSs * 100) / 4)

}
final_table_V7_top4FSs_stashed = final_table_V7_top4FSs
# restriction to %_#_times_selected_among_top4FSs =! 0
final_table_V8_top4FSs = final_table_V7_top4FSs
final_table_V8_top4FSs_non_null_perc <-final_table_V8_top4FSs[which(final_table_V8_top4FSs$Percentage_selection_among_top4FSs > 0),]
# save it 
table_to_save1 <- final_table_V8_top4FSs_non_null_perc[order( -final_table_V8_top4FSs_non_null_perc[,10] ),]
filename_of_table_to_save1 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/SIGs_perc_selection_among_top4_FSs.xlsx"
library(openxlsx)
write.xlsx(table_to_save1, filename_of_table_to_save1)


######################### end of whats working


library(openxlsx)



# >>>> lets save a veen diagramm now 
set.seed(20190708)
genes <- paste("gene",1:1000,sep="")
x <- list(
  A = sample(genes,300), 
  B = sample(genes,525), 
  C = sample(genes,440),
  D = sample(genes,350)
)

if (!require(devtools)) install.packages("devtools")
devtools::install_github("gaospecial/ggVennDiagram")

library("ggVennDiagram")

# Changer les noms de catégories
# Changer la couleur de remplissage du dégradé
ggVennDiagram(
  x, label_alpha = 0,
  category.names = c("Stage 1","Stage 2","Stage 3", "Stage4")
) +
  ggplot2::scale_fill_gradient(low="blue",high = "yellow")


#----
a = c("FS_Remagus04", "FS_MDAnderson_part1of2_310", "FS_MT_6_dts", "FS_BMS_Horak_2013", "FS_Osaka_Miyake_2012", "FS_Remagus02", "FS_Fudan_MAQC2BR")
upsetplot_building_matrix = final_table_V6[c("Features",a)]
upset(upsetplot_building_matrix, sets = a, number.angles = 30, point.size = 3.5, line.size = 2, 
      mainbar.y.label = "Intersection size ", sets.x.label = "FS size", 
      text.scale = c(1.3, 1.3, 1, 1, 1.75, 1.35),mb.ratio = c(0.65, 0.35), 
      order.by = "freq", keep.order = TRUE, empty.intersections = "on")

###########################################

final_table_V6_allFSs_sorted <- final_table_V6_allFSs[order( final_table_V6_allFSs[,6] ),]




#################################################


#>>>>>>> restrict to only the genes with : high_string_status == "Y" (grp1)
final_table_V3_grp1 <- final_table_V3[which(final_table_V3$high_string_status == "Y"),]
num_unique_genes_grp1 <- dim(final_table_V3_grp1)[1]
paste("- Number of genes grp1 : ",num_unique_genes_grp1,sep='')
#>>>>>>> restrict to only the genes with : high_string_status == "N" but lenient_string_status == "Y" (grp2)
final_table_V3_grp2 <- final_table_V3[which((final_table_V3$high_string_status == "N")
                                            &(final_table_V3$lenient_string_status == "Y")),]
num_unique_genes_grp2 <- dim(final_table_V3_grp2)[1]
paste("- Number of genes grp2 : ",num_unique_genes_grp2,sep='')

#>>>>>>> restrict to only the genes with : lenient_string_status == "Y" (grp3=gr1+grp2)
final_table_V3_grp3 <- final_table_V3[which(final_table_V3$lenient_string_status == "Y"),]
num_unique_genes_grp3 <- dim(final_table_V3_grp3)[1]
paste("- Number of genes grp3 : ",num_unique_genes_grp3,sep='')
# small check : grp3 = grp1+ grp2 in values 

#>>>>>> the matrix with all num of genes by grp obtained from restriction
num_grps_for_now = 8 # num rows
num_FSs_for_now_plus1 = 7+1 # num cols
df_genes_grps = as.data.frame(matrix(NA, nrow = num_grps_for_now, ncol = num_FSs_for_now_plus1))
colnames(df_genes_grps) <- c("Groups",tail(colnames(final_table_V3), 7))
df_genes_grps[,"Groups"] = c("high strigency (grp1)","added by lenient stringency (grp2)","lenient stringency (grp3=grp1+grp2)", 
                             "Smax",
                             "Between SstrongV1 et Smax","Between SweakV1 et SstrongV1",
                             "Between SstrongV2 et Smax","Between SweakV2 et SstrongV2")

# - limit values for s_all_bs
Smax = 1
SstrongV1 = 0.9
SweakV1 = 0.7
# lets get the limits V2
list_values_s_abs_for_lenient <- final_table_V3_grp3[['s_all_abs']]
# using a 1st time the bimodal finding of a limit, we have limitV21 
limitV2_1 = 0.3639074 # computed with another script
# this being a limit too low compared to lowest limit given, we consider it as SweakV2 and we try to find now SstrongV2
list_values_s_abs_for_lenient_bis <- list_values_s_abs_for_lenient[list_values_s_abs_for_lenient>limitV2_1]
limitV2_2 = 0.813884 # computed with another script
# the final V2 limits values are : 
SstrongV2 = limitV2_2
SweakV2 = limitV2_1

# - supply the matrix
for (index_one_fs_ascolname in c(2:length(colnames(df_genes_grps)))) { # for test index_one_fs_ascolname = 2
  index_one_fs_ascolname_in_ori_table = index_one_fs_ascolname - 1 + 5 # Features is before the group of FS names and these ("Features","high_string_status","lenient_string_status","s_all","s_all_abs") were before it in V3
  # for grp1
  table_grp1 <- final_table_V3_grp1[final_table_V3_grp1[ ,index_one_fs_ascolname_in_ori_table] == 1, ]  # 1 is presence and 0 is absence of ft in the FS
  count_grp1 <- dim(table_grp1)[1]
  df_genes_grps[which(df_genes_grps$Groups == "high strigency (grp1)"),index_one_fs_ascolname] = count_grp1
  # for grp2
  table_grp2 <- final_table_V3_grp2[final_table_V3_grp2[ ,index_one_fs_ascolname_in_ori_table] == 1, ]
  count_grp2 <- dim(table_grp2)[1]
  df_genes_grps[which(df_genes_grps$Groups == "added by lenient stringency (grp2)"),index_one_fs_ascolname] = count_grp2
  # for grp3
  table_grp3 <- final_table_V3_grp3[final_table_V3_grp3[ ,index_one_fs_ascolname_in_ori_table] == 1, ]
  count_grp3 <- dim(table_grp3)[1]
  df_genes_grps[which(df_genes_grps$Groups == "lenient stringency (grp3=grp1+grp2)"),index_one_fs_ascolname] = count_grp3
  #----all below start from the table_grp3 because operate on the lenient situation
  # for grp4
  table_grp4 <- table_grp3[which(table_grp3$s_all_abs == Smax),]
  count_grp4 <- dim(table_grp4)[1]
  df_genes_grps[which(df_genes_grps$Groups == "Smax"),index_one_fs_ascolname] = count_grp4
  # for grp5
  table_grp5 <- table_grp3[which((table_grp3$s_all_abs >= SstrongV1)&(table_grp3$s_all_abs < Smax)),]
  count_grp5 <- dim(table_grp5)[1]
  df_genes_grps[which(df_genes_grps$Groups == "Between SstrongV1 et Smax"),index_one_fs_ascolname] = count_grp5
  # for grp6
  table_grp6 <- table_grp3[which((table_grp3$s_all_abs >= SweakV1)&(table_grp3$s_all_abs < SstrongV1)),]
  count_grp6 <- dim(table_grp6)[1]
  df_genes_grps[which(df_genes_grps$Groups == "Between SweakV1 et SstrongV1"),index_one_fs_ascolname] = count_grp6
  # for grp7
  table_grp7 <- table_grp3[which((table_grp3$s_all_abs >= SstrongV2)&(table_grp3$s_all_abs < Smax)),]
  count_grp7 <- dim(table_grp7)[1]
  df_genes_grps[which(df_genes_grps$Groups == "Between SstrongV2 et Smax"),index_one_fs_ascolname] = count_grp7
  # for grp8
  table_grp8 <- table_grp3[which((table_grp3$s_all_abs >= SweakV2)&(table_grp3$s_all_abs < SstrongV2)),]
  count_grp8 <- dim(table_grp8)[1]
  df_genes_grps[which(df_genes_grps$Groups == "Between SweakV2 et SstrongV2"),index_one_fs_ascolname] = count_grp8
  # end of all restrictions groups
}

# put the features col as rownames to have a matrix later
rownames(df_genes_grps) <- df_genes_grps[,1]
df_genes_grps[,1] <- NULL
df_genes_grps_stashed = df_genes_grps

# make the same table but with the proportions
df_genes_grps_props = df_genes_grps
size_cohorts_in_order_of_perfs = c(12151,12151,12304,12151,19417,19419,12151)
for (index_one_fs_ascolname2 in c(1:length(colnames(df_genes_grps_props)))) { # for test index_one_fs_ascolname2 = 2
  index_size_cohort_corresp = index_one_fs_ascolname2
  size_cohort_corresp = size_cohorts_in_order_of_perfs[index_size_cohort_corresp]
  df_genes_grps_props[,index_one_fs_ascolname2] = (df_genes_grps_props[,index_one_fs_ascolname2] / size_cohort_corresp) * 100
} 

# saving the df_genes_grps
prefix_path_until_folder_of_location = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/"
filename_of_table_to_save = paste(prefix_path_until_folder_of_location,"df_genes_grps.csv", sep='')
write.csv(df_genes_grps, filename_of_table_to_save, row.names=T)
# saving the df_genes_grps_props
prefix_path_until_folder_of_location = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/"
filename_of_table_to_save = paste(prefix_path_until_folder_of_location,"df_genes_grps_props.csv", sep='')
write.csv(df_genes_grps_props, filename_of_table_to_save, row.names=T)
# saving the table_grp1_sorted_on_s_abs_all
table_grp1_sorted_on_s_abs_all <- table_grp1[order( -table_grp1[,5] ),]
prefix_path_until_folder_of_location = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/"
filename_of_table_to_save = paste(prefix_path_until_folder_of_location,"table_grp1_sorted_on_s_abs_all.csv", sep='')
write.csv(table_grp1_sorted_on_s_abs_all, filename_of_table_to_save, row.names=T)

#~~~~~~~~~~~~~~~~~~~~~
# rownames(df_genes_grps_props) <- df_genes_grps_props[,1] # not neeeded
# df_genes_grps_props[,1] <- NULL  
#~~~~~~~~~~~~~~

# plot the bar plots 
# using something like barplot(t(as.matrix(df_genes_grps_props)),beside=TRUE)

# -  a bar plot for the numbers in 3 strigencies
df_used = df_genes_grps[c(1,2,3),]
barplot((as.matrix(df_used)),
        main = "Numbers of SIGs following the stringency criteria",
        xlab = "Feature selections (FS) from highest to lowest performance using F1",
        col = c("red","orange", "blue"),
        beside=TRUE)
legend("topleft",
       c("high strigency (grp1)","added by lenient stringency (grp2)","lenient stringency (grp3=grp1+grp2)"),
       fill = c("red","orange", "blue"))

# -  a bar plot for the props
df_used = df_genes_grps_props[c(1,2,3),]
barplot((as.matrix(df_used)),
        main = "Proportions of SIGs following the stringency criteria",
        xlab = "Feature selections (FS) from highest to lowest performance using F1",
        col = c("red","orange", "blue"),
        beside=TRUE)
legend("topleft",
       c("high strigency (grp1)","added by lenient stringency (grp2)","lenient stringency (grp3=grp1+grp2)"),
       fill = c("red","orange", "blue"))

# -  a bar plot for the numbers of each of the strigency crit
df_used = df_genes_grps[c(1),]
barplot((as.matrix(df_used)),
        main = "Numbers of SIGs for the high strigency criteria",
        xlab = "Feature selections (FS) from highest to lowest performance using F1",
        col = c("red","orange", "blue"),
        beside=TRUE)

df_used = df_genes_grps[c(2),]
barplot((as.matrix(df_used)),
        main = "Numbers of SIGs added by lenient stringency criteria",
        xlab = "Feature selections (FS) from highest to lowest performance using F1",
        col = c("red","orange", "blue"),
        beside=TRUE)

df_used = df_genes_grps[c(3),]
barplot((as.matrix(df_used)),
        main = "Numbers of SIGs for lenient stringency criteria",
        xlab = "Feature selections (FS) from highest to lowest performance using F1",
        col = c("red","orange", "blue"),
        beside=TRUE)

# -  a bar plot for the props of each of the strigency crit
df_used = df_genes_grps_props[c(1),]
barplot((as.matrix(df_used)),
        main = "Proportions of SIGs for the high strigency criteria",
        xlab = "Feature selections (FS) from highest to lowest performance using F1",
        col = c("red","orange", "blue"),
        beside=TRUE)

df_used = df_genes_grps_props[c(2),]
barplot((as.matrix(df_used)),
        main = "Proportions of SIGs added by lenient stringency criteria",
        xlab = "Feature selections (FS) from highest to lowest performance using F1",
        col = c("red","orange", "blue"),
        beside=TRUE)

df_used = df_genes_grps_props[c(3),]
barplot((as.matrix(df_used)),
        main = "Proportions of SIGs for lenient stringency criteria",
        xlab = "Feature selections (FS) from highest to lowest performance using F1",
        col = c("red","orange", "blue"),
        beside=TRUE)

# -  a bar plot for the numbers in smax and the limits
df_used = df_genes_grps[c(4,5,6),]
barplot((as.matrix(df_used)),
        main = "Numbers of SIGs between Max=1, LimitStrong = 0.9, and LimitWeak : 0.7",
        xlab = "Feature selections (FS) from highest to lowest performance using F1",
        col = c("green","orange", "red"),
        beside=TRUE)
legend("topleft",
       c("Smax","Between SstrongV1 and Smax","Between SweakV1 and SstrongV1"),
       fill = c("green","orange", "red"))

# -  a bar plot for the props in smax and the limits
df_used = df_genes_grps_props[c(4,5,6),]
barplot((as.matrix(df_used)),
        main = "Proportions of SIGs between Max=1, LimitStrong = 0.813884, and LimitWeak : 0.3639074",
        xlab = "Feature selections (FS) from highest to lowest performance using F1",
        col = c("green","orange", "red"),
        beside=TRUE)
legend("topleft",
       c("Smax","Between SstrongV2 and Smax","Between SweakV2 and SstrongV2"),
       fill = c("green","orange", "red"))




#######################



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













