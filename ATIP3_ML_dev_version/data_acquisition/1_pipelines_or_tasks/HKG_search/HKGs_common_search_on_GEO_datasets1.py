#---------------------get the common HKGs across cohorts
#>>>>>>>>>>>>>>>>>>>>>>>>>>> IMPORTS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import pandas as pd
import numpy as np # linear algebra and exploit arrays faster and easier computations
import seaborn as sns
import matplotlib.pyplot as plt
from textwrap import wrap # to wrap plot titles
#>>>>>>>>>>>>>>>>>>>Choosing environnement values
# ----Setting the type of probesets to kept
# part_of_probesets_kept = "allprobesets"
part_of_probesets_kept = "bestprobesetsonly"
# part_of_probesets_kept = "CDFsummarized"
# ----for the version of files to use
# version_of_fts = "probesnames"
version_of_fts = "genesnames"
# version_of_fts = "fullnames_GS_ACC_probe"
# ----for the column to rank on when we have the common
cohort_to_rank_on_the_common = "R02"
# cohort_to_rank_on_the_common = "R04"
# cohort_to_rank_on_the_common = "MDA"

#>>>>>>>>>>>>>>>>>>>Setting environnement values
# ----for the cohorts to implicate
tag_cohort_used1 = "R02"
tag_cohort_used2 = "R04"
tag_cohort_used3 = "MDA"

# load the HKGs report for each cohort (we choose the the full HKGs report ordered on the CV_no_dup
sep_in_file = ","
file_path_R02 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/atip3_material/datasets_to_process_folder/R02_R04_MDA_GEOdatasets/HKGs_bestprobesetsonly/R02/"+tag_cohort_used1+"_"+part_of_probesets_kept+"_"+version_of_fts+"_HKGsCVnoDupRanked_report.csv"
file_path_R04 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/atip3_material/datasets_to_process_folder/R02_R04_MDA_GEOdatasets/HKGs_bestprobesetsonly/R04/"+tag_cohort_used2+"_"+part_of_probesets_kept+"_"+version_of_fts+"_HKGsCVnoDupRanked_report.csv"
file_path_MDA = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/atip3_material/datasets_to_process_folder/R02_R04_MDA_GEOdatasets/HKGs_bestprobesetsonly/MDA/"+tag_cohort_used3+"_"+part_of_probesets_kept+"_"+version_of_fts+"_HKGsCVnoDupRanked_report.csv"
df_file_R02 = pd.read_csv(file_path_R02, sep_in_file)
df_file_R04 = pd.read_csv(file_path_R04, sep_in_file)
df_file_MDA = pd.read_csv(file_path_MDA, sep_in_file)

# restrict to needed columns
# list_of_cols_to_remove = ["HKGs", "mean","std", "CV","CV_Rank"] # use this if HKG_selected, mean, std and CV_Rank cols are not removed
list_of_cols_to_remove = ["CV"]
df_file_R02_restricted = df_file_R02.drop(list_of_cols_to_remove, axis=1)
df_file_R04_restricted = df_file_R04.drop(list_of_cols_to_remove, axis=1)
df_file_MDA_restricted = df_file_MDA.drop(list_of_cols_to_remove, axis=1)
# rename the columns to use
df_file_R02_restricted.rename(columns={"HK_features": "HK_features_R02"}, inplace=True)
df_file_R02_restricted.rename(columns={"CV_Rank_no_dup": "CV_Rank_no_dup_R02"}, inplace=True)
df_file_R04_restricted.rename(columns={"HK_features": "HK_features_R04"}, inplace=True)
df_file_R04_restricted.rename(columns={"CV_Rank_no_dup": "CV_Rank_no_dup_R04"}, inplace=True)
df_file_MDA_restricted.rename(columns={"HK_features": "HK_features_MDA"}, inplace=True)
df_file_MDA_restricted.rename(columns={"CV_Rank_no_dup": "CV_Rank_no_dup_MDA"}, inplace=True)

# join the dfs of two then the joined with the third # joined on the HKGs_GS columns # inner: use intersection of keys from both frames
df_joined_R02_R04 = pd.merge(df_file_R02_restricted, df_file_R04_restricted, how="inner", left_on="HK_features_R02", right_on="HK_features_R04")
df_joined_R02_R04_MDA = pd.merge(df_joined_R02_R04, df_file_MDA_restricted, how="inner", left_on="HK_features_R02", right_on="HK_features_MDA")


# drop the unecessary cols after the join
list_of_cols_to_remove2 = ["HK_features_R04", "HK_features_MDA"]
df_joined_R02_R04_MDA_restricted = df_joined_R02_R04_MDA.drop(list_of_cols_to_remove2, axis=1)
# rename the common HKGs column
df_joined_R02_R04_MDA_restricted.rename(columns={"HK_features_R02": "HK_features_common_to_cohorts"}, inplace=True)
# make a col of mean ranking across the three cohorts
df_joined_R02_R04_MDA_restricted["Mean_CV_Rank_no_dup"] = df_joined_R02_R04_MDA_restricted[["CV_Rank_no_dup_R02","CV_Rank_no_dup_R04","CV_Rank_no_dup_MDA"]].mean(axis=1, skipna=True) # axis = 0 means along the column and axis = 1 means working along the row

# - create a copy that is ordered on the mean CV no dup
df_joined_R02_R04_MDA_restricted_MeanCVNoDupsorted = df_joined_R02_R04_MDA_restricted.sort_values('Mean_CV_Rank_no_dup', ascending=True)
df_joined_R02_R04_MDA_restricted_MeanCVNoDupsorted = df_joined_R02_R04_MDA_restricted_MeanCVNoDupsorted.reset_index(drop=True)

# - create a copy that is ordered on the CV rank no dup of a cohort
df_joined_R02_R04_MDA_restricted_1cohortsorted = df_joined_R02_R04_MDA_restricted_MeanCVNoDupsorted
if cohort_to_rank_on_the_common == "R02":
    df_joined_R02_R04_MDA_restricted_1cohortsorted = df_joined_R02_R04_MDA_restricted_1cohortsorted.sort_values('CV_Rank_no_dup_R02', ascending=True)
elif cohort_to_rank_on_the_common == "R04":
    df_joined_R02_R04_MDA_restricted_1cohortsorted = df_joined_R02_R04_MDA_restricted_1cohortsorted.sort_values('CV_Rank_no_dup_R04', ascending=True)
elif cohort_to_rank_on_the_common == "MDA":
    df_joined_R02_R04_MDA_restricted_1cohortsorted = df_joined_R02_R04_MDA_restricted_1cohortsorted.sort_values('CV_Rank_no_dup_MDA', ascending=True)
df_joined_R02_R04_MDA_restricted_1cohortsorted = df_joined_R02_R04_MDA_restricted_1cohortsorted.reset_index(drop=True)

# - create a copy that is alphabetical order on common HKGs
df_joined_R02_R04_MDA_restrictedInAlphabetOrder = df_joined_R02_R04_MDA_restricted.sort_values("HK_features_common_to_cohorts", axis=0, ascending=True, kind='mergesort')


# # some column have dates as GS (lets remove them) (use the indexes and then redo the index)
# df_joined_R02_R04_MDA_restricted = df_joined_R02_R04_MDA_restricted.drop([335,224,1084])
# df_joined_R02_R04_MDA_restrictedInAlphabetOrder = df_joined_R02_R04_MDA_restrictedInAlphabetOrder.drop([335,224,1084])
# df_joined_R02_R04_MDA_restricted = df_joined_R02_R04_MDA_restricted.reset_index(drop=True)
# df_joined_R02_R04_MDA_restrictedInAlphabetOrder = df_joined_R02_R04_MDA_restrictedInAlphabetOrder.reset_index(drop=True)


# make the filenames of the reports to save
HKGs_common_to_cohorts_1cohortsorted_filename = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/HKGs_common_to_cohorts_1cohort_"+cohort_to_rank_on_the_common+"_sorted_report.csv"
HKGs_common_to_cohorts_MeanCVNoDupsorted_filename = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/HKGs_common_to_cohorts_MeanCVNoDup_sorted_report.csv"
HKGs_common_to_cohortsInAlphabetOrder_filename = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/HKGs_common_to_cohorts_Alphabet_sorted_report.csv"

# save to a .csv file
df_joined_R02_R04_MDA_restricted_1cohortsorted.to_csv(HKGs_common_to_cohorts_1cohortsorted_filename, index=None, header=True)
df_joined_R02_R04_MDA_restricted_MeanCVNoDupsorted.to_csv(HKGs_common_to_cohorts_MeanCVNoDupsorted_filename, index=None, header=True)
df_joined_R02_R04_MDA_restrictedInAlphabetOrder.to_csv(HKGs_common_to_cohortsInAlphabetOrder_filename, index=None, header=True)

# # get the df initials when stripped of the probes with dates (unknown probes)
# df_file_R02 = df_file_R02.sort_values("HKG_GS", axis=0, ascending=True, kind='mergesort')
# df_file_R02 = df_file_R02.reset_index(drop=True)
# # R02 has 10 unamed as dates HKGs, numm all HKGs probes = 10832, remaining = 10822
# df_file_R04 = df_file_R04.sort_values("HKG_GS", axis=0, ascending=True, kind='mergesort')
# df_file_R04 = df_file_R04.reset_index(drop=True)
# # R04 has 8 unamed as dates HKGs, numm all HKGs probes = 5410, remaining = 5402
# df_file_MDA = df_file_MDA.sort_values("HKG_GS", axis=0, ascending=True, kind='mergesort')
# df_file_MDA = df_file_MDA.reset_index(drop=True)
# # MDA has 3 unamed as dates HKGs, numm all HKGs probes = 3137, remaining = 3134