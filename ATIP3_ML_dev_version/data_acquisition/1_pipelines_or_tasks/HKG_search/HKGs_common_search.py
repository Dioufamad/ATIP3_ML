#---------------------get the common HKGs across cohorts
#>>>>>>>>>>>>>>>>>>>>>>>>>>> IMPORTS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import pandas as pd
import numpy as np # linear algebra and exploit arrays faster and easier computations
import seaborn as sns
import matplotlib.pyplot as plt
from textwrap import wrap # to wrap plot titles

# load the HKGs report for each cohort (we choose the the full HKGs report ordered on the CV_no_dup
sep_in_file = ","
file_path_R02 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/HKGs_report/R02__HKGs/R02_HKGsCVnoDupRanked_report.csv"
file_path_R04 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/HKGs_report/R04__HKGs/R04_HKGsCVnoDupRanked_report.csv"
file_path_MDA = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/HKGs_report/MDA_HKGs/MDA_HKGsCVnoDupRanked_report.csv"
df_file_R02 = pd.read_csv(file_path_R02, sep_in_file)
df_file_R04 = pd.read_csv(file_path_R04, sep_in_file)
df_file_MDA = pd.read_csv(file_path_MDA, sep_in_file)

# restrict to needed columns
list_of_cols_to_remove = ["HKGs", "mean","std", "CV","CV_Rank"]
df_file_R02_restricted = df_file_R02.drop(list_of_cols_to_remove, axis=1)
df_file_R04_restricted = df_file_R04.drop(list_of_cols_to_remove, axis=1)
df_file_MDA_restricted = df_file_MDA.drop(list_of_cols_to_remove, axis=1)
# rename the columns to use
df_file_R02_restricted.rename(columns={"HKG_GS": "HKG_GS_R02"}, inplace=True)
df_file_R02_restricted.rename(columns={"CV_Rank_no_dup": "CV_Rank_no_dup_R02"}, inplace=True)
df_file_R04_restricted.rename(columns={"HKG_GS": "HKG_GS_R04"}, inplace=True)
df_file_R04_restricted.rename(columns={"CV_Rank_no_dup": "CV_Rank_no_dup_R04"}, inplace=True)
df_file_MDA_restricted.rename(columns={"HKG_GS": "HKG_GS_MDA"}, inplace=True)
df_file_MDA_restricted.rename(columns={"CV_Rank_no_dup": "CV_Rank_no_dup_MDA"}, inplace=True)

# join the dfs of two then the joined with the third # joined on the HKGs_GS columns # inner: use intersection of keys from both frames
df_joined_R02_R04 = pd.merge(df_file_R02_restricted, df_file_R04_restricted, how="inner", left_on="HKG_GS_R02", right_on="HKG_GS_R04")
df_joined_R02_R04_MDA = pd.merge(df_joined_R02_R04, df_file_MDA_restricted, how="inner", left_on="HKG_GS_R02", right_on="HKG_GS_MDA")

# drop the unecessary cols after the join
list_of_cols_to_remove2 = ["HKG_GS_R04", "HKG_GS_MDA"]
df_joined_R02_R04_MDA_restricted = df_joined_R02_R04_MDA.drop(list_of_cols_to_remove2, axis=1)
# rename the common HKGs column
df_joined_R02_R04_MDA_restricted.rename(columns={"HKG_GS_R02": "HKGs_GS_common_to_cohorts"}, inplace=True)
# create a copy that is alphabetical order on common HKGs
df_joined_R02_R04_MDA_restrictedInAlphabetOrder = df_joined_R02_R04_MDA_restricted.sort_values("HKGs_GS_common_to_cohorts", axis=0, ascending=True, kind='mergesort')
# some column have dates as GS (lets remove them) (use the indexes and then redo the index)
df_joined_R02_R04_MDA_restricted = df_joined_R02_R04_MDA_restricted.drop([335,224,1084])
df_joined_R02_R04_MDA_restrictedInAlphabetOrder = df_joined_R02_R04_MDA_restrictedInAlphabetOrder.drop([335,224,1084])
df_joined_R02_R04_MDA_restricted = df_joined_R02_R04_MDA_restricted.reset_index(drop=True)
df_joined_R02_R04_MDA_restrictedInAlphabetOrder = df_joined_R02_R04_MDA_restrictedInAlphabetOrder.reset_index(drop=True)


# save to a .csv file
HKGs_common_to_cohorts_report = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/HKGs_common_to_cohorts_report.csv"
df_joined_R02_R04_MDA_restricted.to_csv(HKGs_common_to_cohorts_report, index=None, header=True)
HKGs_common_to_cohortsInAlphabetOrder_report = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/HKGs_common_to_cohortsInAlphabetOrder_report.csv"
df_joined_R02_R04_MDA_restrictedInAlphabetOrder.to_csv(HKGs_common_to_cohortsInAlphabetOrder_report, index=None, header=True)

# get the df initials when stripped of the probes with dates (unknown probes)
df_file_R02 = df_file_R02.sort_values("HKG_GS", axis=0, ascending=True, kind='mergesort')
df_file_R02 = df_file_R02.reset_index(drop=True)
# R02 has 10 unamed as dates HKGs, numm all HKGs probes = 10832, remaining = 10822
df_file_R04 = df_file_R04.sort_values("HKG_GS", axis=0, ascending=True, kind='mergesort')
df_file_R04 = df_file_R04.reset_index(drop=True)
# R04 has 8 unamed as dates HKGs, numm all HKGs probes = 5410, remaining = 5402
df_file_MDA = df_file_MDA.sort_values("HKG_GS", axis=0, ascending=True, kind='mergesort')
df_file_MDA = df_file_MDA.reset_index(drop=True)
# MDA has 3 unamed as dates HKGs, numm all HKGs probes = 3137, remaining = 3134