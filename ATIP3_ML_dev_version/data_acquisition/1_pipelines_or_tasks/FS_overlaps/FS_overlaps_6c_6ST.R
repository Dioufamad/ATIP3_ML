# this is a script to start doing the FS intersections as upset plots

# imports 
library(readxl) # for ability to read xlsx and xls files  
library(UpSetR) # for the upset plots
library(ggplot2) # for the attribute plots

# - supply the path of all FS to open here
# >>> FS 1
path2file1 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0061_NonNullCoefs.csv"
tag_alg1 = "FS_ST_L1"
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
# # >>> FS 7 aka MT
# path2file7 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/spams_sparse_group_lasso_l2__l1onlyused_6cohortes/Output_Regr_SPAMSSparseGroupL1LogReg_Allfts_Multitaskof6_BRCA_NACTaxanesBR_GEX_MA_Trial004_NonNullCoefs.csv"
# tag_alg7 = "FS_MT_SGL1"
# tag_numcohort7 = "6GSEs"
# tag_nickname_cohort7 = "6_joined_dts"
# >>>>>>>>>>> a list of paths to loop on and get the info needed
list_paths2files <- c(path2file1,path2file2,path2file3,path2file4,path2file5,path2file6)
# >>>>>>>>>>> a list of tag_alg
list_tag_alg <- c(tag_alg1,tag_alg2,tag_alg3,tag_alg4,tag_alg5,tag_alg6)
# >>>>>>>>>>> a list of tag_numcohort
list_tag_numcohort <- c(tag_numcohort1,tag_numcohort2,tag_numcohort3,tag_numcohort4,tag_numcohort5,tag_numcohort6)
# >>>>>>>>>>> a list of tag_nickname_cohort
list_tag_nickname_cohort <- c(tag_nickname_cohort1,tag_nickname_cohort2,tag_nickname_cohort3,tag_nickname_cohort4,tag_nickname_cohort5,tag_nickname_cohort6)
# >>>>>>>>>> the colname where the selected features will be in each file
# Features


# - a collector of the selected features
list_fs_tables_retrieved = list()
list_different_fs_retrieved = list() 
list_fts_across_all_fs_tables <- c()
list_of_fts_multiplicity_if_MT_FS_used <-c()
list_titles_initial_sets <- c()
num_initial_sets_analysed <- 0
# - lets load a csv for each FS and collect the list that is the FS in order to make a table telling with a boolean 0/1 on the presence of each ft in each FS
looping_index <- 0
for (a_path2afile in list_paths2files) {
  # update the looping index 
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
names(upsetplot_building_matrix) <- c("Unique features across all initial sets",list_titles_initial_sets) 

# put the Unique features in initial sets inside the 1st col
upsetplot_building_matrix$`Unique features across all initial sets` <- list_fts_unik_across_all_fs_tables

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
  upsetplot_building_matrix[which(upsetplot_building_matrix$`Unique features across all initial sets` %in% fs_retrieved_corresp_2_column),i] <- 1
}

###############  lets try the upset plots on our FS sets
#====> Trying the best proposition exemple: 
# lets display the initial sets retrieved
list_titles_initial_sets
# # lets put the list of sets into the order from best to worst performance (not including the MT)
# list_titles_initial_sets_in_order_best2worstperf = c("FS_ST_L1_On_Remagus04","FS_ST_L1_On_MDAnderson_part1of2_310","FS_ST_L1_On_BMS_Horak_2013","FS_ST_L1_On_Osaka_Miyake_2012","FS_ST_L1_On_Remagus02","FS_ST_L1_On_Fudan_MAQC2BR")
# lets put the list of sets into the order from best to worst performance (including the MT)
list_titles_initial_sets_in_order_best2worstperf = c("FS_ST_L1_On_Remagus04","FS_ST_L1_On_MDAnderson_part1of2_310","FS_ST_L1_On_BMS_Horak_2013","FS_ST_L1_On_Osaka_Miyake_2012","FS_ST_L1_On_Remagus02","FS_ST_L1_On_Fudan_MAQC2BR")
list_titles_initial_sets_in_order_best2worstperf

# testing the upset plot...
upset(upsetplot_building_matrix, sets = list_titles_initial_sets_in_order_best2worstperf, number.angles = 30, point.size = 3.5, line.size = 2, 
      mainbar.y.label = "Intersection size ", sets.x.label = "FS size", 
      text.scale = c(1.3, 1.3, 1, 1, 1.75, 1.35),mb.ratio = c(0.65, 0.35), 
      order.by = "freq", keep.order = TRUE, empty.intersections = "on")

# group.by = "sets" does not show the most efficient to observe ranking so we dont use it

#====> setting up the metadata (to be able to add metadata horizontal hists etc.)
# ....
# upsetplot_building_matrix[which(upsetplot_building_matrix$Multiplicity_if_MT_FS_used %in% fs_retrieved_corresp_2_column_multiplicity),index_col_Multiplicity_if_MT_FS_used] <- list_of_fts_multiplicity_if_MT_FS_used # not working

# --- the col for the names of the sets
sets_for_perfs <- list_titles_initial_sets_in_order_best2worstperf
# # --- the col for the perfs values (not including the MT)
# avgF1Score <- c(0.813,0.65,0.583,0.567,0.383,0.373)
# --- the col for the perfs values (including the MT)
avgF1Score <- c(0.813,0.65,0.583,0.567,0.383,0.373)
# ...check if the col containing perfs values is numeric (it is a factor so we coerce it to characters then change it to integers)

# # --- the col for the platforms names (not including the MT)
# Platforms_ID <-c("Affymetrix_HG_U133A_2_0","Affymetrix_HG_U133A","Affymetrix_HG_U133A_2_0",
#                 "Affymetrix_HG_U133_Plus_2_0","Affymetrix_HG_U133_Plus_2_0","Affymetrix_HG_U133A")
# --- the col for the platforms names (including the MT)
Platforms_ID <-c("Affymetrix_HG_U133A_2_0","Affymetrix_HG_U133A","Affymetrix_HG_U133A_2_0",
                 "Affymetrix_HG_U133_Plus_2_0","Affymetrix_HG_U133_Plus_2_0","Affymetrix_HG_U133A")
# # --- the col of the size of the initial pool of genes the platforms offers (not including the MT)
# PlatformsInitialPoolofGenes <-c("AffyHGU133A2 : 12151","AffyHGU133A : 12151","AffyHGU133A2 : 12151",
#                                 "AffyHGU133Plus2 : 19417","AffyHGU133Plus2 : 19419","AffyHGU133A : 12151")
# --- the col of the size of the initial pool of genes the platforms offers (including the MT)
PlatformsInitialPoolofGenes <-c("AffyHGU133A2 : 12151","AffyHGU133A : 12151","AffyHGU133A2 : 12151",
                                "AffyHGU133Plus2 : 19417","AffyHGU133Plus2 : 19419","AffyHGU133A : 12151")
# --- joining the cols
metadata <- as.data.frame(cbind(sets_for_perfs, avgF1Score,Platforms_ID,PlatformsInitialPoolofGenes))
names(metadata) <- c("FS_sets", "avgF1Score","Platform_ID", "Platform_and_size_initial_pool_of_genes") # Platform_and_size_initial_pool_of_genes or Platform : # genes
# -- formatting the cols
# ...check if the cols containing numbers as values are numeric 
# (they are most likely factors so we coerce to characters then change to integers)
is.numeric(metadata$avgF1Score)
metadata$avgF1Score <- as.numeric(as.character(metadata$avgF1Score))
is.numeric(metadata$avgF1Score)
metadata$Platform_and_size_initial_pool_of_genes <- as.character(metadata$Platform_and_size_initial_pool_of_genes)
metadata$Platform_ID <- as.character(metadata$Platform_ID)
# test it 
upset(upsetplot_building_matrix, 
      set.metadata = list(data = metadata, plots = list(list(type = "hist", column = "avgF1Score", assign = 20)))) # works
# # let's try to imitate it for our sets (not including the MT)...
# upset(upsetplot_building_matrix, 
#       sets = list_titles_initial_sets_in_order_best2worstperf, 
#       mainbar.y.label = "Intersection size ", sets.x.label = "FS size", 
#       number.angles = 30, point.size = 3.5, line.size = 2, text.scale = c(1.3, 1.3, 1, 1, 1.75, 1.35),mb.ratio = c(0.65, 0.35), 
#       order.by = "freq", keep.order = TRUE, empty.intersections = "on",
#       set.metadata = list(data = metadata, plots = list(list(type = "hist", column = "avgF1Score", assign = 20),
#                                                         list(type = "text", column = "Platform_and_size_initial_pool_of_genes", assign = 20),
#                                                         list(type = "matrix_rows", column = "Platform_ID", colors = c(Affymetrix_HG_U133A_2_0 = "light blue", Affymetrix_HG_U133A = "navy", Affymetrix_HG_U133_Plus_2_0 = "purple"), alpha = 0.5)
#                                                         )),
#       queries = list(list(query = intersects, params = list("FS_ST_L1_On_Remagus04"), color = "green", active = T, query.name = "Specific to best performing FS"),
#                      list(query = intersects, params = list("FS_ST_L1_On_Remagus04", "FS_ST_L1_On_MDAnderson_part1of2_310", "FS_ST_L1_On_BMS_Horak_2013"), color = "blue", active = T, query.name = "Intersection of top 3 performing FS"),
#                      list(query = intersects, params = list("FS_ST_L1_On_Remagus04","FS_ST_L1_On_MDAnderson_part1of2_310", "FS_ST_L1_On_BMS_Horak_2013","FS_ST_L1_On_Osaka_Miyake_2012","FS_ST_L1_On_Remagus02","FS_ST_L1_On_Fudan_MAQC2BR"), color = "red", active = T, query.name = "Intersection of all FS"),
#                      list(query = function(row, value){ data <- (row["FS_ST_L1_On_Remagus04"] == value)}, params = list(1), color="orange", active = T, query.name = "Intersection implicating best performing FS")
#                      ),
#       query.legend = "bottom"
#       ) # works 

# let's try to imitate it for our sets (including the MT)...
upset(upsetplot_building_matrix, 
      sets = list_titles_initial_sets_in_order_best2worstperf, 
      mainbar.y.label = "Intersection size ", sets.x.label = "FS size", 
      number.angles = 20, point.size = 3.5, line.size = 1, text.scale = c(1.3, 1.3, 1, 1, 1.55, 1.35),mb.ratio = c(0.65, 0.35), 
      order.by = "freq", keep.order = TRUE, empty.intersections = "on",
      set_size.show = TRUE,
      set_size.scale_max = 22000,
      set.metadata = list(data = metadata, plots = list(list(type = "hist", column = "avgF1Score", assign = 12),
                                                        list(type = "text", column = "Platform_and_size_initial_pool_of_genes", assign = 18),
                                                        list(type = "matrix_rows", column = "Platform_ID", colors = c(Affymetrix_HG_U133A_2_0 = "light blue", Affymetrix_HG_U133A = "navy", Affymetrix_HG_U133_Plus_2_0 = "purple",All_Platforms_Common_Genes = "grey"), alpha = 0.5)
      )),
      queries = list(list(query = intersects, params = list("FS_ST_L1_On_Remagus04"), color = "green", active = T, query.name = "Specific to the best performing FS"),
                     list(query = intersects, params = list("FS_ST_L1_On_Remagus04", "FS_ST_L1_On_MDAnderson_part1of2_310", "FS_ST_L1_On_BMS_Horak_2013"), color = "blue", active = T, query.name = "Intersection of top 3 performing FS"),
                     list(query = intersects, params = list("FS_ST_L1_On_Remagus04","FS_ST_L1_On_MDAnderson_part1of2_310","FS_ST_L1_On_BMS_Horak_2013","FS_ST_L1_On_Osaka_Miyake_2012","FS_ST_L1_On_Remagus02","FS_ST_L1_On_Fudan_MAQC2BR"), color = "red", active = T, query.name = "Intersection of all FS"),
                     list(query = function(row, value){ data <- (row["FS_ST_L1_On_Remagus04"] == value)}, params = list(1), color="orange", active = T, query.name = "Intersections implicating the best performing FS")
      ),
      query.legend = "bottom"
      #boxplot.summary = c("Multiplicity_if_MT_FS_used")
) # works but it dont have the boxplot of multiplicity (work on it later)

# list of top st vs 2nd best st
group_gsetop1 = rownames(ex1_bis_with_GS)
group_gsetop3 = rownames(ex1_bis_with_GS) # after launching the 2nd dt summoner script
in1notin3 = setdiff(group_gsetop1,group_gsetop3) # empty
in3notin1 = setdiff(group_gsetop1,group_gsetop3) # empty


# let's try to add a box plot for the multiplicity in the MT features...
upsetplot_building_matrix2 <- upsetplot_building_matrix
# -- adding the metadata col of multiplicity
index_fs_retrieved_corresp_2_column_multiplicity = 7
fs_retrieved_corresp_2_column_multiplicity <- list_different_fs_retrieved[[index_fs_retrieved_corresp_2_column_multiplicity]]
upsetplot_building_matrix2$Multiplicity_if_MT_FS_used <- 0
index_col_Multiplicity_if_MT_FS_used <- ncol(upsetplot_building_matrix2) ##
index_ft_in_fs_retrieved_corresp_2_column_multiplicity <- 0
for (a_ft in fs_retrieved_corresp_2_column_multiplicity) {
  index_ft_in_fs_retrieved_corresp_2_column_multiplicity <- index_ft_in_fs_retrieved_corresp_2_column_multiplicity + 1
  # upsetplot_building_matrix2[a_ft,index_col_Multiplicity_if_MT_FS_used] <- list_of_fts_multiplicity_if_MT_FS_used[index_ft_in_fs_retrieved_corresp_2_column_multiplicity]
  upsetplot_building_matrix2[a_ft,"Multiplicity_if_MT_FS_used"] <- list_of_fts_multiplicity_if_MT_FS_used[index_ft_in_fs_retrieved_corresp_2_column_multiplicity]
}
unique(upsetplot_building_matrix2$Multiplicity_if_MT_FS_used)
upset(upsetplot_building_matrix2, boxplot.summary = c("Multiplicity_if_MT_FS_used"))


# end of file
