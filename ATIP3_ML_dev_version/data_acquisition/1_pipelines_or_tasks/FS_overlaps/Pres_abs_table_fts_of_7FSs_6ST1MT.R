# this is a script to make the presence absence table to use as : 
# - an upsetplot building matrix
# - or a file to later use as a presence absence information table
# Version : for the 7 FS of LASSO (L1) 

# imports 
library(readxl) # for ability to read xlsx and xls files  
library(UpSetR) # for the upset plots
library(ggplot2) # for the attribute plots

# - supply the path of all FS to open here
# >>> FS 1
path2file1 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0061_NonNullCoefs.csv"
tag_alg1 = "FS_ST_L1" # needed to see if it is a dataset towards ST or MT (if MT, the fts name ahas to be analysed to get real name)
tag_numcohort1 = "GSE41998"
tag_nickname_cohort1 = "BMS_Horak_2013"
# >>> FS 2
path2file2 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0062_NonNullCoefs.csv"
tag_alg2 = "FS_ST_L1"
tag_numcohort2 = "GSE26639"
tag_nickname_cohort2 = "Remagus02"
# >>> FS 3
path2file3 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0063_NonNullCoefs.csv"
tag_alg3 = "FS_ST_L1"
tag_numcohort3 = "GSE32646"
tag_nickname_cohort3 = "Osaka_Miyake_2012"
# >>> FS 4
path2file4 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0064_NonNullCoefs.csv"
tag_alg4 = "FS_ST_L1"
tag_numcohort4 = "GSE25055"
tag_nickname_cohort4 = "MDAnderson_part1of2_310"
# >>> FS 5
path2file5 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0065_NonNullCoefs.csv"
tag_alg5 = "FS_ST_L1"
tag_numcohort5 = "GSE20194"
tag_nickname_cohort5 = "Fudan_MAQC2BR"
# >>> FS 6
path2file6 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0066_NonNullCoefs.csv"
tag_alg6 = "FS_ST_L1"
tag_numcohort6 = "GSE63471"
tag_nickname_cohort6 = "Remagus04"
# >>> FS 7 aka MT
path2file7 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/spams_sparse_group_lasso_l2__l1onlyused_6cohortes/Output_Regr_SPAMSSparseGroupL1LogReg_Allfts_Multitaskof6_BRCA_NACTaxanesBR_GEX_MA_Trial004_NonNullCoefs.csv"
tag_alg7 = "FS_MT_SGL1"
tag_numcohort7 = "6GSEs"
tag_nickname_cohort7 = "6_joined_dts"
# >>>>>>>>>>> a list of paths to loop on and get the info needed
list_paths2files <- c(path2file1,path2file2,path2file3,path2file4,path2file5,path2file6,path2file7) # needed
# >>>>>>>>>>> a list of tag_alg
list_tag_alg <- c(tag_alg1,tag_alg2,tag_alg3,tag_alg4,tag_alg5,tag_alg6,tag_alg7)
# >>>>>>>>>>> a list of tag_numcohort
list_tag_numcohort <- c(tag_numcohort1,tag_numcohort2,tag_numcohort3,tag_numcohort4,tag_numcohort5,tag_numcohort6,tag_numcohort7)
# >>>>>>>>>>> a list of tag_nickname_cohort
list_tag_nickname_cohort <- c(tag_nickname_cohort1,tag_nickname_cohort2,tag_nickname_cohort3,tag_nickname_cohort4,tag_nickname_cohort5,tag_nickname_cohort6,tag_nickname_cohort7)
# >>>>>>>>>> the colname where the selected features will be in each file
# Features


# - defining collectors
list_fs_tables_retrieved = list() # needed (just for info) 
list_different_fs_retrieved = list() # needed
list_fts_across_all_fs_tables <- c() # needed
list_of_fts_multiplicity_if_MT_FS_used <-c() # needed (just for info) ##! get the unique values and make a print to display them at the end
list_titles_initial_sets <- c() # needed
num_initial_sets_analysed <- 0 # needed
# - lets load a csv for each FS and collect the list that is the FS in order to make a table telling with a boolean 0/1 on the presence of each ft in each FS
looping_index <- 0
for (a_path2afile in list_paths2files) { # for test : a_path2afile = list_paths2files[1]
  # update the looping index (to later get what we want for the present step from the lists created while entering the data paths)
  looping_index <- looping_index + 1
  # - get the table corresponding to the path
  fs_table <- read.csv(file = a_path2afile, header = TRUE)
  # - add it to the collector of the fs_tables
  list_fs_tables_retrieved[[looping_index]] <- fs_table
  # - check if the colname of the selected features column is in the colnames of the FS table (to be sure that there will be no surprises as to the colname we use to get the fts))
  colnames_in_fs_table = names(fs_table) # to see the cols (to see which ones to keep)
  if ("Features" %in% colnames_in_fs_table) { 
    paste("- the known colname of the selected features column is in the colnames of the FS table !", sep='')
  }else{
    paste("- Warning : the known colname of the selected features column IS NOT in the colnames of the FS table.", sep='')
  }
  # - get a list of the elements in the FS following if there is a MT FS or not in the groups of sets analysed
  # get the tag_alg and see if tag has an indication of MT
  tag_alg_corresp_2_fs_retrieved = list_tag_alg[looping_index]
  if (grepl("MT", tag_alg_corresp_2_fs_retrieved, fixed=TRUE)) { #...case where the analysed FS comes from a MT
    list_fts_unik_in_fs_table_as_MT_names = unique(as.character(fs_table$Features))
    # - check if the list unique features got for this initial set does not have redundancies in it
    if (length(list_fts_unik_in_fs_table_as_MT_names) == nrow(fs_table)) { # !isNA(bestprobe = is not NA (a best probe has been found) 
      paste("- no redundancy in the selected features list !", sep='')
    }else{
      paste("- Warning : there is redundancy in the selected features list : num unique selected features list is different from num features in the table of the FS.", sep='')
    }
    # lets split the MT features names to get the correct initial names of the fts
    list_fts_all_in_fs_table_as_correct_names <- c()
    for (a_MT_ft_name in list_fts_unik_in_fs_table_as_MT_names){
      pieces_of_ftname_as_MT_name <- strsplit(a_MT_ft_name, "_in_")[[1]] # NB : if the sep is not found, a vector of only the entire word is kept so getting the 1st elt gives it also
      ftname_as_correct_initial_name <-pieces_of_ftname_as_MT_name[1]
      list_fts_all_in_fs_table_as_correct_names <- c(list_fts_all_in_fs_table_as_correct_names,ftname_as_correct_initial_name)
    }
    list_fts_unik_in_fs_table = unique(list_fts_all_in_fs_table_as_correct_names)
    # lets get the multiplicity of each correct name in the set of MT names
    for (a_correct_ft_name in list_fts_unik_in_fs_table) {
      value_multiplicity <- length(which(list_fts_all_in_fs_table_as_correct_names == a_correct_ft_name))
      list_of_fts_multiplicity_if_MT_FS_used <- c(list_of_fts_multiplicity_if_MT_FS_used,value_multiplicity)
    }
  }else{ #...case where the analysed FS comes from a ST
    list_fts_unik_in_fs_table = unique(as.character(fs_table$Features))
    # - check if the list unique features got for this initial set does not have redundancies in it
    if (length(list_fts_unik_in_fs_table) == nrow(fs_table)) { # !isNA(bestprobe = is not NA (a best probe has been found) 
      paste("- no redundancy in the selected features list !", sep='')
    }else{
      paste("- Warning : there is redundancy in the selected features list : num unique selected features list is different from num features in the table of the FS.", sep='')
    }
  }
  
  # - add it to the collector of selected features
  list_fts_across_all_fs_tables <- c(list_fts_across_all_fs_tables,list_fts_unik_in_fs_table) 
  # add it to the collector of FS lists
  list_different_fs_retrieved[[looping_index]] <- list_fts_unik_in_fs_table
  # - choose a title for this FS
  title_initial_set_in_fs_table <- paste(list_tag_alg[looping_index],list_tag_nickname_cohort[looping_index], sep='_On_') # elements of list_tag_numcohort were not used
  # --add the title of the FS to a collector ie the vector of cols name for the upset building matrix
  list_titles_initial_sets <-c(list_titles_initial_sets,title_initial_set_in_fs_table)
  # update the number of initial sets
  num_initial_sets_analysed <- num_initial_sets_analysed + 1
}

# from the collector of the selected features, make a list of unique selected features (used to build the 1st col of the upset matrix)
list_fts_unik_across_all_fs_tables <-unique(list_fts_across_all_fs_tables)

# make a new table with the previous list as its 1st col and the remaining cols being each one for an initial set
upsetplot_building_matrix <- data.frame(matrix(NA,    # Create empty data frame
                                               nrow = length(list_fts_unik_across_all_fs_tables),
                                               ncol = (num_initial_sets_analysed+1)))
# rename the cols 
names(upsetplot_building_matrix) <- c("Unique_features_across_all_initial_sets",list_titles_initial_sets) 

# put the Unique features in initial sets inside the 1st col
upsetplot_building_matrix$Unique_features_across_all_initial_sets <- list_fts_unik_across_all_fs_tables

# put the boolean 0/1 in each of the col that is for a FS (0 = this ft is not in this FS, 1 = this ft is in this FS)
for (i  in 2:ncol(upsetplot_building_matrix)) { # looping through the cols in list_titles_initial_sets
  # - put 0 as an initial value so that ,the fts that wont be seen later in the initial set, will be already 0
  upsetplot_building_matrix[,i] <- 0
  # - in the upset building matrix, on the rows where the element of the unique features across all initial sets was in the initial set considered, 
  # change the col of the related initial set into 1
  # -- get the index of the specific FS retrieved that was corresponding to the column to change
  index_fs_retrieved_corresp_2_column = i - 1
  # -- get the FS retrieved that was corresponding to the column to change
  fs_retrieved_corresp_2_column <- list_different_fs_retrieved[[index_fs_retrieved_corresp_2_column]]
  # make the change to 1 in the cells of the cols that have to get the change
  upsetplot_building_matrix[which(upsetplot_building_matrix$Unique_features_across_all_initial_sets %in% fs_retrieved_corresp_2_column),i] <- 1
}


# we sort the table cols for future easier reading and reporting of results
# the idea is : see the titles of the cols, place each one where we want to see it, and see them again to check if all is okay
names(upsetplot_building_matrix)
# >>>>>>>>>>>> sort by dts performance
upsetplot_building_matrix_cols_by_perf_order = upsetplot_building_matrix[c("Unique_features_across_all_initial_sets","FS_ST_L1_On_Remagus04","FS_ST_L1_On_MDAnderson_part1of2_310","FS_MT_SGL1_On_6_joined_dts",
                                  "FS_ST_L1_On_BMS_Horak_2013","FS_ST_L1_On_Osaka_Miyake_2012","FS_ST_L1_On_Remagus02","FS_ST_L1_On_Fudan_MAQC2BR")]

# <<<<<<<<<<<<

# we rename columns for easier names
names(upsetplot_building_matrix_cols_by_perf_order) # to see the cols titles (for copy pasting)
names(upsetplot_building_matrix_cols_by_perf_order) <- c("Features_bis","FS_Remagus04","FS_MDAnderson_part1of2_310","FS_MT_6_dts",
                                                         "FS_BMS_Horak_2013","FS_Osaka_Miyake_2012","FS_Remagus02","FS_Fudan_MAQC2BR")
names(upsetplot_building_matrix_cols_by_perf_order) # to see the cols titles (for verification)

# + Optionnaly, we can restrict to only some cols needed (use this example for it)

# # #>>>>>>>>>>>>> for 7 FSs (all FSs as the pattern to modify)
# table_pres_abs = table_pres_abs[c("Features_bis","FS_Remagus04","FS_MDAnderson_part1of2_310","FS_MT_6_dts",
#                                   "FS_BMS_Horak_2013","FS_Osaka_Miyake_2012","FS_Remagus02","FS_Fudan_MAQC2BR")]
# #<<<<<<<<<<<<

# >>>>>>>>>>>>>>>> chunk used to save the upsetplot_building_matrix_cols_by_perf_order for a table with presence and absence of all fts across the FS of the L1 lasso
# - the file name definition (using list_tag_alg and upsetplot_building_matrix_cols_by_perf_order)

list_tag_initial_sets_analysed = unique(as.character(list_tag_alg))
str_for_algs_analysed = paste(list_tag_initial_sets_analysed, collapse = '_and_')
num_intitial_sets_analysed = length(list_tag_alg)
num_rows = dim(upsetplot_building_matrix_cols_by_perf_order)[1]
num_cols = dim(upsetplot_building_matrix_cols_by_perf_order)[2]
type_of_values = "GEX"
# # a good place to save for L1 Regr is ...
# "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/Summary_results_L1_lasso_runs.xlsx"
prefix_path_until_folder_of_location = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/"
filename_of_table_to_save = paste(prefix_path_until_folder_of_location,"presence_absence_table_for_",str_for_algs_analysed,"_",num_intitial_sets_analysed,"InitialSets_",num_rows,"rows_",num_cols,"cols_",type_of_values,".csv", sep='')
# - if okay , save now in .csv
table_to_save = upsetplot_building_matrix_cols_by_perf_order
write.csv(table_to_save, filename_of_table_to_save, row.names=T)


# end of file


