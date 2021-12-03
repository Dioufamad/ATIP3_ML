# Version : Vranksasentallftsselectedornot & WE KEEP ALL THE GENES NO MATTER THE SIG_STATUS to wait at the end to have an overview of all the genes ranking and stability states


# this script is the test for counting and identifying the genes that tells the same story ie their differents coefs in regression works have the same sign
# Version 4 (after corrections of Chloé). This version is what is used after Chloe corrected us on the use of the coefs 
# (the idea is that you get ranks from the coefs of each seed and then afterwards you get a mean rank from that)


# imports 
library(readxl) # for ability to read xlsx and xls files  
library(UpSetR) # for the upset plots
library(ggplot2) # for the attribute plots
library(dplyr) # for the operations on multiples frames using pipes in succession
library(openxlsx)

# - defining collectors for the entry data to use (will be use to access the entire data through loops on these collectors)
list_paths2files_NNC <- c() # >>>>>>>>>>> a list of paths (non nul coefs fts tables)
list_paths2files_RAW <- c() # >>>>>>>>>>> a list of paths (raw coefs values for fts tables)
list_paths2files_MCR <- c() # >>>>>>>>>>> a list of paths (mean coefs rank  fts tables)
list_tag_alg <- c() # >>>>>>>>>>> a list of tag_alg
list_tag_numcohort <- c() # >>>>>>>>>>> a list of tag_numcohort
list_tag_nickname_cohort <- c() # >>>>>>>>>>> a list of tag_nickname_cohort

# - supply the path of all FS to open here and add their respective info to the previous collectors

# >>> FS 1new
path2file6_NNC = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0066_NonNullCoefs.csv"
path2file6_RAW = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0066_RawListOfCoefs.csv"
path2file6_MCR = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0066_MeanRank10SeedsFtsAndRanksOnlyVranksasentallftsselectedornot.csv"
tag_alg6 = "FS_ST_L1"
tag_numcohort6 = "GSE63471"
tag_nickname_cohort6 = "Remagus04"
list_paths2files_NNC <- c(list_paths2files_NNC,path2file6_NNC)
list_paths2files_RAW <- c(list_paths2files_RAW,path2file6_RAW)
list_paths2files_MCR <- c(list_paths2files_MCR,path2file6_MCR)
list_tag_alg <- c(list_tag_alg,tag_alg6)
list_tag_numcohort <- c(list_tag_numcohort,tag_numcohort6)
list_tag_nickname_cohort <- c(list_tag_nickname_cohort,tag_nickname_cohort6)

# >>> FS 2new
path2file4_NNC = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0064_NonNullCoefs.csv"
path2file4_RAW = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0064_RawListOfCoefs.csv"
path2file4_MCR = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0064_MeanRank10SeedsFtsAndRanksOnlyVranksasentallftsselectedornot.csv"
tag_alg4 = "FS_ST_L1"
tag_numcohort4 = "GSE25055"
tag_nickname_cohort4 = "MDAnderson_part1of2_310"
list_paths2files_NNC <- c(list_paths2files_NNC,path2file4_NNC)
list_paths2files_RAW <- c(list_paths2files_RAW,path2file4_RAW)
list_paths2files_MCR <- c(list_paths2files_MCR,path2file4_MCR)
list_tag_alg <- c(list_tag_alg,tag_alg4)
list_tag_numcohort <- c(list_tag_numcohort,tag_numcohort4)
list_tag_nickname_cohort <- c(list_tag_nickname_cohort,tag_nickname_cohort4)

# >>> FS 3new
path2file1_NNC = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0061_NonNullCoefs.csv"
path2file1_RAW = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0061_RawListOfCoefs.csv"
path2file1_MCR = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0061_MeanRank10SeedsFtsAndRanksOnlyVranksasentallftsselectedornot.csv"
tag_alg1 = "FS_ST_L1"
tag_numcohort1 = "GSE41998"
tag_nickname_cohort1 = "BMS_Horak_2013"
list_paths2files_NNC <- c(list_paths2files_NNC,path2file1_NNC)
list_paths2files_RAW <- c(list_paths2files_RAW,path2file1_RAW)
list_paths2files_MCR <- c(list_paths2files_MCR,path2file1_MCR)
list_tag_alg <- c(list_tag_alg,tag_alg1)
list_tag_numcohort <- c(list_tag_numcohort,tag_numcohort1)
list_tag_nickname_cohort <- c(list_tag_nickname_cohort,tag_nickname_cohort1)


# >>> FS 4new aka MTof3
path2file7_NNC = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/spams_sparse_group_lasso_l2_l1onlyused_3oftop4FSsL1/Output_Regr_SPAMSSparseGroupL1L2LogReg_CommonFtsMT3ofTop4FSsL1_BRCA_NACTaxanesBR_GEX_MA_Trial1MT3ofTop4FSsL1_NonNullCoefs.csv"
path2file7_RAW = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/spams_sparse_group_lasso_l2_l1onlyused_3oftop4FSsL1/Output_Regr_SPAMSSparseGroupL1L2LogReg_CommonFtsMT3ofTop4FSsL1_BRCA_NACTaxanesBR_GEX_MA_Trial1MT3ofTop4FSsL1_RawListOfCoefs.csv"
path2file7_MCR = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/spams_sparse_group_lasso_l2_l1onlyused_3oftop4FSsL1/Output_Regr_SPAMSSparseGroupL1L2LogReg_CommonFtsMT3ofTop4FSsL1_BRCA_NACTaxanesBR_GEX_MA_Trial1MT3ofTop4FSsL1_MeanRank10SeedsFtsAndRanksOnlyVranksasentallftsselectedornot.csv"
tag_alg7 = "FS_MT_SGL1"
tag_numcohort7 = "GSE63471_x_GSE25055_x_GSE41998" 
# tag_numcohort7 = "6GSEs" previously (changed to use it as an elt to split and get the compositional cohorts name for specific cols naming)
tag_nickname_cohort7 = "6_joined_dts"
list_paths2files_NNC <- c(list_paths2files_NNC,path2file7_NNC)
list_paths2files_RAW <- c(list_paths2files_RAW,path2file7_RAW)
list_paths2files_MCR <- c(list_paths2files_MCR,path2file7_MCR)
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
list_fs_tables_retrieved_MCR = list()
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
  path2file_MCR = list_paths2files_MCR[index_of_an_alg]
  # - get the table corresponding to the path
  fs_table_nnc <- read.csv(file = path2file_NNC, header = TRUE)
  fs_table_raw <- read.csv(file = path2file_RAW, header = TRUE)
  fs_table_mcr <- read.csv(file = path2file_MCR, header = TRUE)
  
  # - check if the colname of the selected features column is in the colnames of the tables with have to go through their rows 
  #   (to be sure that there will be no surprises as to the colname we use to get the fts))
  colnames_in_fs_table_nnc = names(fs_table_nnc) # use it to also see the cols (to see which ones to keep)
  colnames_in_fs_table_raw = names(fs_table_raw)
  colnames_in_fs_table_mcr = names(fs_table_mcr)
  if ((official_colname_of_selected_features_col %in% colnames_in_fs_table_nnc)&(official_colname_of_selected_features_col %in% colnames_in_fs_table_raw)&(official_colname_of_selected_features_col %in% colnames_in_fs_table_mcr)) { 
    paste("- the official_colname_of_selected_features_col IS in the colnames of the tables with have to go through their list of fts !", sep='')
  }else{
    paste("- Warning : the official_colname_of_selected_features_col IS NOT in one of the colnames of the tables with have to go through their list of fts.", sep='')
  }
  
  # - restrictions to only non nuls coefs of the tables to use later
  # for a test, we shorten the nnc table to only the first 20 lines with this : # fs_table_nnc <- fs_table_nnc[1:20,]
  list_fts_in_nnc = unique(as.character(fs_table_nnc$Features))
  # restrict raw table to nnc
  fs_table_raw_nnc_only = fs_table_raw[which(fs_table_raw$Features %in% list_fts_in_nnc),]
  # # restrict mcr table to nnc # not needed
  # fs_table_mcr_only = fs_table_mcr[which(fs_table_mcr$Features %in% list_fts_in_nnc),]
  
  # - add it to the collector of the fs_tables
  list_fs_tables_retrieved_NNC[[index_of_an_alg]] <- fs_table_nnc
  list_fs_tables_retrieved_RAW[[index_of_an_alg]] <- fs_table_raw_nnc_only
  list_fs_tables_retrieved_MCR[[index_of_an_alg]] <- fs_table_mcr # later, we will need the ranks in this table but only for the non nul genes
  
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
#>>>>>>>>>>>>>>version for 4 FSs analysis (uncomment to use)
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs <- bind_rows(list_fs_tables_retrieved_RAW_marks_only_and_pruned[[1]] %>% add_rownames(),
                                                                 list_fs_tables_retrieved_RAW_marks_only_and_pruned[[2]] %>% add_rownames(),
                                                                 list_fs_tables_retrieved_RAW_marks_only_and_pruned[[3]] %>% add_rownames(),
                                                                 list_fs_tables_retrieved_RAW_marks_only_and_pruned[[4]] %>% add_rownames()) %>%
  # evaluate following calls for each value in the rowname column
  group_by(rowname) %>%
  # add all non-grouping variables
  summarise_all(sum)
#<<<<<<<<<<<<<<<<<<<<<<
# #>>>>>>>>>>>>>>version for 7 FSs analysis (uncomment to use)
# fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs <- bind_rows(list_fs_tables_retrieved_RAW_marks_only_and_pruned[[1]] %>% add_rownames(),
#                                                                  list_fs_tables_retrieved_RAW_marks_only_and_pruned[[2]] %>% add_rownames(),
#                                                                  list_fs_tables_retrieved_RAW_marks_only_and_pruned[[3]] %>% add_rownames(),
#                                                                  list_fs_tables_retrieved_RAW_marks_only_and_pruned[[4]] %>% add_rownames(),
#                                                                  list_fs_tables_retrieved_RAW_marks_only_and_pruned[[5]] %>% add_rownames(),
#                                                                  list_fs_tables_retrieved_RAW_marks_only_and_pruned[[6]] %>% add_rownames(),
#                                                                  list_fs_tables_retrieved_RAW_marks_only_and_pruned[[7]] %>% add_rownames()) %>%
#   # evaluate following calls for each value in the rowname column
#   group_by(rowname) %>%
#   # add all non-grouping variables
#   summarise_all(sum)
# #<<<<<<<<<<<<<<<<<<<<<<
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
# final_table_V1$Class_of_SIG <- 0 # not needed
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
  # NB : (Class_of_SIG will be informed later because it needs another table for existence of gene) # not needed
} 
# lets stash the obtained table in 2 fashions
final_table_V1_complete_stashed = final_table_V1 # full table stashed
# final_table_V1_restricted_to_cols_to_report = final_table_V1[c("Features","high_string_status","lenient_string_status","s_all","s_all_abs","SIG_status","Class_of_SIG")]
# final_table_V1_restricted_to_cols_to_report = final_table_V1[c("Features","high_string_status","s_all","s_all_abs","SIG_status","Class_of_SIG")] # not needed
final_table_V1_restricted_to_cols_to_report = final_table_V1[c("Features","high_string_status","s_all","s_all_abs","SIG_status")]

# >>>>>>>>>>> adding info of presence absence 1 (in FSs) # changed to implicate top 4 FSs only
# - lets add columns to identify the FS were each ft has existed
final_table_V2 = final_table_V1_restricted_to_cols_to_report
# + lets load the table of presence/absence cols of fts across 7 FS by L1
path2file_pres_abs_fts_7_FSs2_L1Regr = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/presence_absence_tables/presence_absence_table_for_FS_ST_L1_and_FS_MT_SGL1_4InitialSets_12152rows_5cols_GEX.csv"
table_pres_abs <- read.csv(file = path2file_pres_abs_fts_7_FSs2_L1Regr, header = TRUE)
names(table_pres_abs) # to see the cols
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

# # >>>>>>>>>> adding info of presence absence 2 (in DSs) # not needed
# # - lets add columns to identify the DS were each ft has existed
# final_table_V3 = final_table_V2
# # + lets load the table of presence/absence cols of fts across 7 FS by L1
# path2file_pres_abs_fts_7_DSs = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/presence_absence_table_for_DS_ST_L1_and_DS_MT_SGL1_7InitialSets_19533rows_8cols_GEX.csv"
# table_pres_abs_7_DSs <- read.csv(file = path2file_pres_abs_fts_7_DSs, header = TRUE)
# # remove the first col that is just an ordered index (1 to end)
# table_pres_abs_7_DSs[,1] <- NULL
# 
# names(table_pres_abs_7_DSs) # to see the cols
# 
# # + join the presence/absence cols and the SIGs tables on all 7 models
# df_left <-final_table_V3
# colref_left <- "Features"
# df_right <- table_pres_abs_7_DSs
# colref_right <- "Features_bis"
# final_table_V3 <- merge(x = df_left, y = df_right, by.x = colref_left, by.y = colref_right)
# final_table_V3_stash = final_table_V3


# >>>>>>>>>>>>>>>> action 2 : add a col of %_#_times_selected_among_top4FSs
final_table_V3 = final_table_V2
list_all_SIGs_top4FSs = unique(as.character(final_table_V3$Features))
names(final_table_V3)
cols_top4FSs = c("FS_Remagus04", "FS_MDAnderson_part1of2_310", "FS_BMS_Horak_2013", "FS_MT_3_dts")
for (a_SIG_in_top4FSs in list_all_SIGs_top4FSs){ # for test : a_SIG_in_top4FSs = list_all_SIGs_top4FSs[3]
  # num_times_selected_among_top4FSs
  row_values_for_top4FSs<-final_table_V3[which(final_table_V3$Features %in% a_SIG_in_top4FSs),cols_top4FSs]
  space_values_for_row_values_for_top4FSs <-as.numeric(as.vector(row_values_for_top4FSs))
  num_times_selected_among_top4FSs = sum(space_values_for_row_values_for_top4FSs,na.rm = TRUE)
  # add the col %_#_times_selected_among_top4FSs
  final_table_V3[which(final_table_V3$Features %in% a_SIG_in_top4FSs),"Percentage_selection_among_top4FSs"] = ((num_times_selected_among_top4FSs * 100) / 4)
  
}


# # UNCOMMENT TO USE : WE DONT TO THIS BECAUSE WE KEEP ALL THE GENES NO MATTER THE SIG_STATUS
# # -----------------lets make restrictions following questions (SIG status and % repreentations in FS) and plot hist
# # >>>>>>>>>>>>> restrcition for V4 (only genes SIG_status_as_1 remain)
# final_table_V4 = final_table_V3
# final_table_V4 <- final_table_V4[which(final_table_V4$SIG_status == 1),]
# num_unique_genes_V4 <- dim(final_table_V4)[1]
# paste("- Number of genes SIG_status_as_1 : ",num_unique_genes_V4,sep='')
# final_table_V4_stashed = final_table_V4

# # UNCOMMENT TO USE : WE DONT TO THIS BECAUSE WE KEEP ALL THE GENES NO MATTER THE SIG_STATUS
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TAKE A KNEE MOMENT : Situation of genes that did not pass
# # 192 genes have SIG status
# # Q : are they different from the list of last time ? We just want to know what happened from this point to those genes
# # lets load the table of previous meeting SIG list and restricte the final_table_V3 to it
# path2file_previousSIGlist = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/SIGs_perc_selection_among_top4_FSs.xlsx"
# # library("readxl") # already called at the start of the script
# table_previous_SIGs_only <- read_excel(path2file_previousSIGlist)
# # - lets get the list of previous SIGs
# list_previous_SIGs_only = unique(as.character(table_previous_SIGs_only$Features))
# # - a version of V3 before limiting to out present SIGs) restrcted to previous SIGs and sorted by the descending order of s_all_abs
# final_table_V3_previous_SIGs_only <- final_table_V3[which(final_table_V3$Features %in% list_previous_SIGs_only),]
# final_table_V3_previous_SIGs_only_sorted_desc_sig_status <- final_table_V3_previous_SIGs_only[order( final_table_V3_previous_SIGs_only[,5] ),] ##! to save
# # - a version of V3 before limiting to out present SIGs) restrcted to previous SIGs that did not pass the SIGs status this time (6 revious SIGS genes)
# final_table_V3_previous_SIGs_not_passed <- final_table_V3_previous_SIGs_only[which(final_table_V3_previous_SIGs_only$SIG_status != 1),] ##! to save
# # - a version of V1 (table with the score stats) restrcted to previous SIGs that did not pass the SIGs status this time
# list_previous_SIGs_not_passed = unique(as.character(final_table_V3_previous_SIGs_not_passed$Features))
# final_table_V1_complete_stashed_previous_SIGs_not_passed <- final_table_V1_complete_stashed[which(final_table_V1_complete_stashed$Features %in% list_previous_SIGs_not_passed),] ##! to save
# # - lets save those 3
# require(openxlsx)
# list_of_tables_for_previous_SIGs_not_passed <- list("Previous_41_SIGs_present_situation" = final_table_V3_previous_SIGs_only_sorted_desc_sig_status,
#                                                     "Previous_SIGs_not_passed" = final_table_V3_previous_SIGs_not_passed, 
#                                                     "Previous_SIGs_causes_not_passing" = final_table_V1_complete_stashed_previous_SIGs_not_passed)
# write.xlsx(list_of_tables_for_previous_SIGs_not_passed, file = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/Previous_41_SIGs_situation_after_SIGs_comp_with_Top4FSsVranksasentallftsselectedornot.xlsx")
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~END OF KNEE MOMENT

# # UNCOMMENT TO USE : WE DONT TO THIS BECAUSE WE KEEP ALL THE GENES NO MATTER THE SIG_STATUS
# # >>>>>>>>>>>>>>>> restriction to %_#_times_selected_among_top4FSs =! 0
# 
# # final_table_V4 is used as base
# final_table_V4_bis <-final_table_V4[which(final_table_V4$Percentage_selection_among_top4FSs > 0),]
# # save it 
# table_to_save_final_table_V4_bis <- final_table_V4_bis[order( -final_table_V4_bis$Percentage_selection_among_top4FSs ),]
# filename_table_to_save_final_table_V4_bis = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/SIGs_perc_selection_among_top4_FSsVranksasentallftsselectedornot.xlsx"
# write.xlsx(table_to_save_final_table_V4_bis, filename_table_to_save_final_table_V4_bis)

final_table_V4_bis = final_table_V3
# >>>>>>>>> lets start adding the Mean of Coefs ranks for each gene
final_table_V5 = final_table_V4_bis
final_table_V5$Mean_coefs_rank_for_R04 <- NA
final_table_V5$Mean_coefs_rank_for_MDA <- NA
final_table_V5$Mean_coefs_rank_for_BMS <- NA
final_table_V5$Mean_coefs_rank_for_MT_all_3_copies <- NA
final_table_V5$Mean_coefs_rank_for_MT_copy_of_the_gene_from_R04 <- NA # _in_GSE63471 has been added to the name of the gene
final_table_V5$Mean_coefs_rank_for_MT_copy_of_the_gene_from_MDA <- NA # _in_GSE25055 has been added to the name of the gene
final_table_V5$Mean_coefs_rank_for_MT_copy_of_the_gene_from_BMS <- NA # _in_GSE41998 has been added to the name of the gene
# the tables where we get the mean coefs rank from
table_mcr_FS1 = list_fs_tables_retrieved_MCR[[1]] # lets get the table of coef per gene in each fs  
table_mcr_FS2 = list_fs_tables_retrieved_MCR[[2]]
table_mcr_FS3 = list_fs_tables_retrieved_MCR[[3]]
table_mcr_FS4 = list_fs_tables_retrieved_MCR[[4]]
names(table_mcr_FS1) # to know the name of the col containing traditionally the rank
# lets get the list of fts to loop on
list_fts_final_table_V5 = unique(as.character(final_table_V5$Features)) # to loop through the rows of the table to supply
list_fts_table_mcr_FS1 = unique(as.character(table_mcr_FS1$Features)) # lets get the list of fts in each FS (in order to go get a value only if it existed in the FS)
list_fts_table_mcr_FS2 = unique(as.character(table_mcr_FS2$Features))
list_fts_table_mcr_FS3 = unique(as.character(table_mcr_FS3$Features))
list_fts_table_mcr_FS4 = unique(as.character(table_mcr_FS4$Features))
# lets supply the cols
for (a_ft_in_final_table_V5 in list_fts_final_table_V5){ # for test a_ft_in_final_table_V5 = list_fts_final_table_V5[1]
  # + lets supply the val of the rank for the present gene in all 3 single-tasks FSs (step 1 : we get the vale, step 2 : we put the val in place)
  if(a_ft_in_final_table_V5 %in% list_fts_table_mcr_FS1){ # for FS1
    mean_coefs_rank_for_R04 = table_mcr_FS1[which(table_mcr_FS1$Features %in% a_ft_in_final_table_V5),"Mean_of_rank_across_10_seeds"]
    final_table_V5[which(final_table_V5$Features %in% a_ft_in_final_table_V5),"Mean_coefs_rank_for_R04"] = mean_coefs_rank_for_R04
  }
  if(a_ft_in_final_table_V5 %in% list_fts_table_mcr_FS2){ # for FS2
    mean_coefs_rank_for_MDA = table_mcr_FS2[which(table_mcr_FS2$Features %in% a_ft_in_final_table_V5),"Mean_of_rank_across_10_seeds"]
    final_table_V5[which(final_table_V5$Features %in% a_ft_in_final_table_V5),"Mean_coefs_rank_for_MDA"] = mean_coefs_rank_for_MDA
  }
  if(a_ft_in_final_table_V5 %in% list_fts_table_mcr_FS3){ # for FS3
    mean_coefs_rank_for_BMS = table_mcr_FS3[which(table_mcr_FS3$Features %in% a_ft_in_final_table_V5),"Mean_of_rank_across_10_seeds"]
    final_table_V5[which(final_table_V5$Features %in% a_ft_in_final_table_V5),"Mean_coefs_rank_for_BMS"] = mean_coefs_rank_for_BMS
  }
  # + lets supply the val of the rank for the present gene in 4 ways : 1-as a mean of all 3 ranks given for 3 copies of the gene, 2-as a rank for each copy of the gene (3 copies)
  MT_name_start = paste(a_ft_in_final_table_V5,"_in_",sep='') # we get the name of all the copies of the genes in the multi-task
  list_MT_names_corresponding = c()
  for (a_MT_name_known in list_fts_table_mcr_FS4){
    if(startsWith(a_MT_name_known, MT_name_start)){
      list_MT_names_corresponding = c(list_MT_names_corresponding,a_MT_name_known)
    }
  }
  # focusing on the copies of a gene if it has copies in the multitask
  table_mcr_FS4_rows_w_MT_name_start = table_mcr_FS4[which(table_mcr_FS4$Features %in% list_MT_names_corresponding),] # we get a short table with only the 3 copies of the present gene (to get mean and the copies of the presentgene)
  numrows_table_mcr_FS4_rows_w_MT_name_start = nrow(table_mcr_FS4_rows_w_MT_name_start)
  if(numrows_table_mcr_FS4_rows_w_MT_name_start > 0){
    mean_coefs_rank_for_MT_all_3_copies=mean(table_mcr_FS4_rows_w_MT_name_start$Mean_of_rank_across_10_seeds, na.rm = TRUE) # get val of the mean of the copies
    final_table_V5[which(final_table_V5$Features %in% a_ft_in_final_table_V5),"Mean_coefs_rank_for_MT_all_3_copies"] = mean_coefs_rank_for_MT_all_3_copies # val of mean of the copies added
    for (one_of_list_MT_names_corresponding in list_MT_names_corresponding){
      # get the val of the rank of the copy, whatever copy it is...
      mean_coefs_rank_for_MT_copy_of_the_gene = table_mcr_FS4[which(table_mcr_FS4$Features %in% one_of_list_MT_names_corresponding),"Mean_of_rank_across_10_seeds"] 
      # ...report that value for the proper col of the copy 
      if(grepl("_in_GSE63471", one_of_list_MT_names_corresponding, fixed=TRUE)){
        final_table_V5[which(final_table_V5$Features %in% a_ft_in_final_table_V5),"Mean_coefs_rank_for_MT_copy_of_the_gene_from_R04"] = mean_coefs_rank_for_MT_copy_of_the_gene
      }else if (grepl("_in_GSE25055", one_of_list_MT_names_corresponding, fixed=TRUE)){
        final_table_V5[which(final_table_V5$Features %in% a_ft_in_final_table_V5),"Mean_coefs_rank_for_MT_copy_of_the_gene_from_MDA"] = mean_coefs_rank_for_MT_copy_of_the_gene
      }else if(grepl("_in_GSE41998", one_of_list_MT_names_corresponding, fixed=TRUE)){
        final_table_V5[which(final_table_V5$Features %in% a_ft_in_final_table_V5),"Mean_coefs_rank_for_MT_copy_of_the_gene_from_BMS"] = mean_coefs_rank_for_MT_copy_of_the_gene
      }
    } # all copies of the present gene have their value added
  } # cond of having at least one copy of the present gene in the multi-task is close
} # all present genes in the final table have been supplied with proper values of ranks
final_table_V5_stashed = final_table_V5


# >>>> lets add a col of mean of rank across the top4FSs
# - get a version full table with all ranks
final_table_V6 = final_table_V5
names(final_table_V6)
final_table_V6$Mean_coefs_rank_for_all_3_STs <- rowMeans(subset(final_table_V6, select = c(Mean_coefs_rank_for_R04, Mean_coefs_rank_for_MDA,Mean_coefs_rank_for_BMS)), na.rm = TRUE)
names(final_table_V6) #  reorder the table to have the full table 

# final_table_V6_sorted_summary = final_table_V6_sorted[c("Features", "s_all", 
#                                                         "MEAN_OF_RANKS_ACROSS_THE_TOP_4_FSs", 
#                                                         "Percentage_selection_among_top4FSs", "FS_Remagus04","FS_MDAnderson_part1of2_310", "FS_BMS_Horak_2013","FS_MT_3_dts")]

# final_table_V6$MEAN_OF_RANKS_ACROSS_THE_TOP_4_FSs <- rowMeans(subset(final_table_V6, select = c(Mean_coefs_rank_for_R04, Mean_coefs_rank_for_MDA,Mean_coefs_rank_for_BMS,Mean_coefs_rank_for_MT_all_3_copies)), na.rm = TRUE)
# final_table_V6$FINAL_RANK_ACROSS_THE_TOP_4_FSs[order(final_table_V6$MEAN_OF_RANKS_ACROSS_THE_TOP_4_FSs)] <- 1:nrow(final_table_V6) # not added because the rank are ent already
# final_table_V6_sorted <- final_table_V6[order( final_table_V6$MEAN_OF_RANKS_ACROSS_THE_TOP_4_FSs ),] # to save
# get a version sorted on the final rank
# names(final_table_V6_sorted)
final_table_V6_reordered_cols = final_table_V6[c("Features",
                                                 "FS_Remagus04","FS_MDAnderson_part1of2_310","FS_BMS_Horak_2013","FS_MT_3_dts","Percentage_selection_among_top4FSs",
                                                 "high_string_status","s_all","s_all_abs","SIG_status",
                                                 "Mean_coefs_rank_for_R04","Mean_coefs_rank_for_MDA","Mean_coefs_rank_for_BMS","Mean_coefs_rank_for_all_3_STs",
                                                 "Mean_coefs_rank_for_MT_all_3_copies","Mean_coefs_rank_for_MT_copy_of_the_gene_from_R04",
                                                 "Mean_coefs_rank_for_MT_copy_of_the_gene_from_MDA","Mean_coefs_rank_for_MT_copy_of_the_gene_from_BMS")] # changed to not include an added final rank # to save
# we sorted on a the mean of the ST and on the mean of all MT copies
final_table_V6_reordered_cols_sorted_on_mean_STs <- final_table_V6_reordered_cols[order( final_table_V6_reordered_cols$Mean_coefs_rank_for_all_3_STs ),]
final_table_V6_reordered_cols_sorted_on_mean_MTcopies <- final_table_V6_reordered_cols[order( final_table_V6_reordered_cols$Mean_coefs_rank_for_MT_all_3_copies ),]

# we restrict those to only the important cols
final_table_V6_reordered_cols_sorted_on_mean_STs_res = final_table_V6_reordered_cols_sorted_on_mean_STs[c("Features",
                                                                                                          "FS_Remagus04","FS_MDAnderson_part1of2_310","FS_BMS_Horak_2013","FS_MT_3_dts","Percentage_selection_among_top4FSs",
                                                                                                          "high_string_status","s_all","s_all_abs","SIG_status",
                                                                                                          "Mean_coefs_rank_for_all_3_STs", "Mean_coefs_rank_for_MT_all_3_copies")]
final_table_V6_reordered_cols_sorted_on_mean_MTcopies_res = final_table_V6_reordered_cols_sorted_on_mean_MTcopies[c("Features",
                                                                                                          "FS_Remagus04","FS_MDAnderson_part1of2_310","FS_BMS_Horak_2013","FS_MT_3_dts","Percentage_selection_among_top4FSs",
                                                                                                          "high_string_status","s_all","s_all_abs","SIG_status",
                                                                                                          "Mean_coefs_rank_for_all_3_STs", "Mean_coefs_rank_for_MT_all_3_copies")]


# now lets save em all in one sheet
require(openxlsx)
list_of_tables_from_ranks_of_coefs <- list("All_sortedby_STmean1" = final_table_V6_reordered_cols_sorted_on_mean_STs,
                                           "All_sortedby_MTmean1" = final_table_V6_reordered_cols_sorted_on_mean_MTcopies, 
                                           "All_sortedby_STmean2" = final_table_V6_reordered_cols_sorted_on_mean_STs_res,
                                           "All_sortedby_MTmean2" = final_table_V6_reordered_cols_sorted_on_mean_MTcopies_res)
write.xlsx(list_of_tables_from_ranks_of_coefs, file = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/Tables_of_all_genes_with_stability_and_ranks_no_restriction_V2.xlsx")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~END OF FILE







############################################################"
###################################################""""
#################################################""

# end of file