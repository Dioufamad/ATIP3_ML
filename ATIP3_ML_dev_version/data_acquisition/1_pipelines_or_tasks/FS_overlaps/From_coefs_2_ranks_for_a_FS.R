# this is a script to make a ranking of the fts in a FS based on the coefs at each seed

# uncomment if you prefer to use excel files instead of 
# library(openxlsx) # to save excel format
# library("readxl") # to read excel format

# uncomment 1 group info to analyse 1 FS

# # >>> FS 1new
# path2file_RAW = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0066_RawListOfCoefs.csv"
# tag_alg = "FS_ST_L1"
# tag_numcohort = "GSE63471"
# tag_nickname_cohort = "Remagus04"

# # >>> FS 2new
# path2file_RAW = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0064_RawListOfCoefs.csv"
# tag_alg = "FS_ST_L1"
# tag_numcohort = "GSE25055"
# tag_nickname_cohort = "MDAnderson_part1of2_310"
# 
# # >>> FS 3new
# path2file_RAW = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn/Output_Regr_SklearnL1LogReg_Allfts_Singletask_BRCA_NACTaxanesBR_GEX_MA_Trial0061_RawListOfCoefs.csv"
# tag_alg = "FS_ST_L1"
# tag_numcohort = "GSE41998"
# tag_nickname_cohort = "BMS_Horak_2013"
# # 
# 
# >>> FS 4new aka MTof3
path2file_RAW = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/spams_sparse_group_lasso_l2_l1onlyused_3oftop4FSsL1/Output_Regr_SPAMSSparseGroupL1L2LogReg_CommonFtsMT3ofTop4FSsL1_BRCA_NACTaxanesBR_GEX_MA_Trial1MT3ofTop4FSsL1_RawListOfCoefs.csv"
tag_alg = "FS_MT_SGL1"
tag_numcohort = "GSE63471_x_GSE25055_x_GSE41998"
tag_nickname_cohort = "6_joined_dts"

fs_table_raw <- read.csv(file = path2file_RAW, header = TRUE)
names(fs_table_raw)

# lets create the 10 cols for each of the 10 seeds ranking
fs_table_raw$Abs_val_coef_seed_0 <- abs(fs_table_raw$Coefficient.Estimate.Seed.0)
fs_table_raw$Abs_val_coef_seed_1 <- abs(fs_table_raw$Coefficient.Estimate.Seed.1)
fs_table_raw$Abs_val_coef_seed_2 <- abs(fs_table_raw$Coefficient.Estimate.Seed.2)
fs_table_raw$Abs_val_coef_seed_3 <- abs(fs_table_raw$Coefficient.Estimate.Seed.3)
fs_table_raw$Abs_val_coef_seed_4 <- abs(fs_table_raw$Coefficient.Estimate.Seed.4)
fs_table_raw$Abs_val_coef_seed_5 <- abs(fs_table_raw$Coefficient.Estimate.Seed.5)
fs_table_raw$Abs_val_coef_seed_6 <- abs(fs_table_raw$Coefficient.Estimate.Seed.6)
fs_table_raw$Abs_val_coef_seed_7 <- abs(fs_table_raw$Coefficient.Estimate.Seed.7)
fs_table_raw$Abs_val_coef_seed_8 <- abs(fs_table_raw$Coefficient.Estimate.Seed.8)
fs_table_raw$Abs_val_coef_seed_9 <- abs(fs_table_raw$Coefficient.Estimate.Seed.9)

# lets restrict the table to only the rows where the abs value of the coef is non null for all the coefs
fs_table_raw = fs_table_raw[which((fs_table_raw$Abs_val_coef_seed_0 != 0)
                                  |(fs_table_raw$Abs_val_coef_seed_1 != 0)
                                  |(fs_table_raw$Abs_val_coef_seed_2 != 0)
                                  |(fs_table_raw$Abs_val_coef_seed_3 != 0)
                                  |(fs_table_raw$Abs_val_coef_seed_4 != 0)
                                  |(fs_table_raw$Abs_val_coef_seed_5 != 0)
                                  |(fs_table_raw$Abs_val_coef_seed_6 != 0)
                                  |(fs_table_raw$Abs_val_coef_seed_7 != 0)
                                  |(fs_table_raw$Abs_val_coef_seed_8 != 0)
                                  |(fs_table_raw$Abs_val_coef_seed_9 != 0)),]

# lets create the 10 cols for each of the 10 seeds ranking
fs_table_raw$Rank_coef_seed_0[order(-fs_table_raw$Abs_val_coef_seed_0)] <- (1:nrow(fs_table_raw))/nrow(fs_table_raw)
fs_table_raw$Rank_coef_seed_1[order(-fs_table_raw$Abs_val_coef_seed_1)] <- (1:nrow(fs_table_raw))/nrow(fs_table_raw)
fs_table_raw$Rank_coef_seed_2[order(-fs_table_raw$Abs_val_coef_seed_2)] <- (1:nrow(fs_table_raw))/nrow(fs_table_raw)
fs_table_raw$Rank_coef_seed_3[order(-fs_table_raw$Abs_val_coef_seed_3)] <- (1:nrow(fs_table_raw))/nrow(fs_table_raw)
fs_table_raw$Rank_coef_seed_4[order(-fs_table_raw$Abs_val_coef_seed_4)] <- (1:nrow(fs_table_raw))/nrow(fs_table_raw)
fs_table_raw$Rank_coef_seed_5[order(-fs_table_raw$Abs_val_coef_seed_5)] <- (1:nrow(fs_table_raw))/nrow(fs_table_raw)
fs_table_raw$Rank_coef_seed_6[order(-fs_table_raw$Abs_val_coef_seed_6)] <- (1:nrow(fs_table_raw))/nrow(fs_table_raw)
fs_table_raw$Rank_coef_seed_7[order(-fs_table_raw$Abs_val_coef_seed_7)] <- (1:nrow(fs_table_raw))/nrow(fs_table_raw)
fs_table_raw$Rank_coef_seed_8[order(-fs_table_raw$Abs_val_coef_seed_8)] <- (1:nrow(fs_table_raw))/nrow(fs_table_raw)
fs_table_raw$Rank_coef_seed_9[order(-fs_table_raw$Abs_val_coef_seed_9)] <- (1:nrow(fs_table_raw))/nrow(fs_table_raw)

# lets make a mean rank col
fs_table_raw$Mean_of_rank_across_10_seeds <- rowMeans(subset(fs_table_raw, select = c(Rank_coef_seed_0, Rank_coef_seed_1,Rank_coef_seed_2,Rank_coef_seed_3,Rank_coef_seed_4,
                                                                                      Rank_coef_seed_5,Rank_coef_seed_6,Rank_coef_seed_7,Rank_coef_seed_8,Rank_coef_seed_9)), na.rm = TRUE)
# lets reorder the cols to easily check out if all rankings have been properly done 
# we want for each seed, this order : the raw value of the coef, the abs val of the coef, the ranking
names(fs_table_raw)
fs_table_raw_full_table = fs_table_raw[c("Features",                     
                                         "Coefficient.Estimate.Seed.0", "Abs_val_coef_seed_0", "Rank_coef_seed_0",
                                         "Coefficient.Estimate.Seed.1", "Abs_val_coef_seed_1", "Rank_coef_seed_1", 
                                         "Coefficient.Estimate.Seed.2", "Abs_val_coef_seed_2", "Rank_coef_seed_2",
                                         "Coefficient.Estimate.Seed.3",  "Abs_val_coef_seed_3", "Rank_coef_seed_3",
                                         "Coefficient.Estimate.Seed.4", "Abs_val_coef_seed_4", "Rank_coef_seed_4",
                                         "Coefficient.Estimate.Seed.5",  "Abs_val_coef_seed_5", "Rank_coef_seed_5",
                                         "Coefficient.Estimate.Seed.6",  "Abs_val_coef_seed_6", "Rank_coef_seed_6",
                                         "Coefficient.Estimate.Seed.7",  "Abs_val_coef_seed_7", "Rank_coef_seed_7",
                                         "Coefficient.Estimate.Seed.8",  "Abs_val_coef_seed_8", "Rank_coef_seed_8",
                                         "Coefficient.Estimate.Seed.9",  "Abs_val_coef_seed_9", "Rank_coef_seed_9",
                                         "Mean_of_rank_across_10_seeds")]
fs_table_raw_full_table_sorted = fs_table_raw_full_table[order( fs_table_raw_full_table$Mean_of_rank_across_10_seeds ),]

#~~~~~~ for a version of the table restricted to only the features and their mean rank, use this
fs_table_raw_full_table_sorted_restricted = fs_table_raw_full_table_sorted[c("Features","Mean_of_rank_across_10_seeds")]    

#~~~~~~~~~~~~~~~~
# lets define the table(s) to save
table_to_save1 = fs_table_raw_full_table_sorted
table_to_save2 = fs_table_raw_full_table_sorted_restricted
# lets define the filename(s) to use for saving
start_of_filename_to_use = strsplit(path2file_RAW, "_RawListOfCoefs")[[1]][1]
filename1 = paste(start_of_filename_to_use,"_MeanRank10SeedsFullTable.csv", sep='')
filename2 = paste(start_of_filename_to_use,"_MeanRank10SeedsFtsAndRanksOnly.csv", sep='')
# lets get to saving
write.csv(table_to_save1, filename1, row.names=F) # the rownames have not been kept so when you load it no need to remove 1st col
write.csv(table_to_save2, filename2, row.names=F)
# fs_test <- read.csv(file = filename, header = TRUE) # you can load it with this


# for excel format
# write.xlsx(table_to_save, filename) # use this if you want a excel format
