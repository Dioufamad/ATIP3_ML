#!/usr/bin/env python
# coding: utf-8
# A script to create a unified matrix design for analysis of multiples populations that share the same response
# version for unifying 7 cohorts

# imports (needed)
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
# imports (not needed)
# import numpy as np
# from numpy import seterr,isneginf # used to manage the change into log2 o values in a np array
# from textwrap import wrap # to wrap plot titles
# from statannot import add_stat_annotation

#>>>> What we are building : datasets with all features across datasets, common features only, all samples from the datasets, 6 datasets joined
# Joining the type 1 datasets into one bigger dataset for multitalk learning
# Type1 = ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname in the filename
# contains :
# - n rows as samples
# - m cols as fts
# - 1 col as pCR response with the title "Y_pCR"
# - 1 col as the cohort name with the title "cohort"
# NB1 : along this code, we have to take in account these two last columns that not features columns and remove them before some manipulations
# NB2 ; previously all these datasets had cols that heped to restrict  to taxanes treated only samples

#>>>>> Where this precise number of datasets being loaded : we load 6/9 datasets type 1
# - the GSE25066 is the GSE25055 + the GSE20271. The GSE25066 is not very inspiring for supervisor 1. and the GSE20271 does not any of the 2 biomarker traits. so we only use the GSE25055 out of those 3
# hence 7 cohorts (out of 9)


#>>>>>>>>>>>>>> Loading type 1 datsets (7)
#---set the name of the sheet where the data of the cohort is
filepath_of_ml_dataset1= "/data_acquisition/1_pipelines_or_tasks/GSE41998_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
filepath_of_ml_dataset2= "/data_acquisition/1_pipelines_or_tasks/GSE26639_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
filepath_of_ml_dataset3= "/data_acquisition/1_pipelines_or_tasks/GSE32646_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
filepath_of_ml_dataset4= "/data_acquisition/1_pipelines_or_tasks/GSE25055_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
filepath_of_ml_dataset5= "/data_acquisition/1_pipelines_or_tasks/GSE20194_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
filepath_of_ml_dataset6= "/data_acquisition/1_pipelines_or_tasks/GSE23988_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
filepath_of_ml_dataset7= "/data_acquisition/1_pipelines_or_tasks/GSE63471_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
sep_in_file = ","
df_file1 = pd.read_csv(filepath_of_ml_dataset1, sep_in_file)
df_file2 = pd.read_csv(filepath_of_ml_dataset2, sep_in_file)
df_file3 = pd.read_csv(filepath_of_ml_dataset3, sep_in_file)
df_file4 = pd.read_csv(filepath_of_ml_dataset4, sep_in_file)
df_file5 = pd.read_csv(filepath_of_ml_dataset5, sep_in_file)
df_file6 = pd.read_csv(filepath_of_ml_dataset6, sep_in_file)
df_file7 = pd.read_csv(filepath_of_ml_dataset7, sep_in_file)
# rename the probes column before putting it as index (so that later we can have a nice titles for the probes)
df_file1.rename(columns={"Unnamed: 0" : "samples_names"}, inplace=True)
df_file2.rename(columns={"Unnamed: 0" : "samples_names"}, inplace=True)
df_file3.rename(columns={"Unnamed: 0" : "samples_names"}, inplace=True)
df_file4.rename(columns={"Unnamed: 0" : "samples_names"}, inplace=True)
df_file5.rename(columns={"Unnamed: 0" : "samples_names"}, inplace=True)
df_file6.rename(columns={"Unnamed: 0" : "samples_names"}, inplace=True)
df_file7.rename(columns={"Unnamed: 0" : "samples_names"}, inplace=True)
# put the rownames (genes) as index
df_file1 = df_file1.set_index(list(df_file1.columns)[0]) # because a csv from R has the rownames becoming the first col
df_file2 = df_file2.set_index(list(df_file2.columns)[0])
df_file3 = df_file3.set_index(list(df_file3.columns)[0])
df_file4 = df_file4.set_index(list(df_file4.columns)[0])
df_file5 = df_file5.set_index(list(df_file5.columns)[0])
df_file6 = df_file6.set_index(list(df_file6.columns)[0])
df_file7 = df_file7.set_index(list(df_file7.columns)[0])

# >>>>>> get the version of the datasets with only common cols
# get the list of cols
list_all_cols_df_file1 = list(df_file1.columns)
list_all_cols_df_file2 = list(df_file2.columns)
list_all_cols_df_file3 = list(df_file3.columns)
list_all_cols_df_file4 = list(df_file4.columns)
list_all_cols_df_file5 = list(df_file5.columns)
list_all_cols_df_file6 = list(df_file6.columns)
list_all_cols_df_file7 = list(df_file7.columns)
# get the list of common cols to all the datasets
p = [list_all_cols_df_file1,list_all_cols_df_file2,list_all_cols_df_file3,list_all_cols_df_file4,list_all_cols_df_file5,list_all_cols_df_file6,list_all_cols_df_file7]
result = set(p[0])
for s in p[1:]:
    result.intersection_update(s)
print("Number of features retained as common : ",len(result)) # 12036 ie 12304 fts
list_of_common_cols = list(result)
# putting the in previous order : fts in alphabetical, then Y_pCR, then cohort
list_of_common_cols.remove("Y_pCR")
list_of_common_cols.remove("cohort")
list_of_common_fts = sorted(list_of_common_cols)
list_of_common_cols = list_of_common_fts + ["Y_pCR","cohort"]
# restrict the loaded datasets to the common cols
common_of_df_file1 = df_file1[list_of_common_cols].copy()
common_of_df_file2 = df_file2[list_of_common_cols].copy()
common_of_df_file3 = df_file3[list_of_common_cols].copy()
common_of_df_file4 = df_file4[list_of_common_cols].copy()
common_of_df_file5 = df_file5[list_of_common_cols].copy()
common_of_df_file6 = df_file6[list_of_common_cols].copy()
common_of_df_file7 = df_file7[list_of_common_cols].copy()

# keep a copy of each single dataset for after operations comparisons
common_of_df_file1_b4_std = common_of_df_file1.copy()
common_of_df_file2_b4_std = common_of_df_file2.copy()
common_of_df_file3_b4_std = common_of_df_file3.copy()
common_of_df_file4_b4_std = common_of_df_file4.copy()
common_of_df_file5_b4_std = common_of_df_file5.copy()
common_of_df_file6_b4_std = common_of_df_file6.copy()
common_of_df_file7_b4_std = common_of_df_file7.copy()
list_of_common_of_dfs_b4_std = [common_of_df_file1_b4_std,common_of_df_file2_b4_std,common_of_df_file3_b4_std,common_of_df_file4_b4_std,common_of_df_file5_b4_std,common_of_df_file6_b4_std,common_of_df_file7_b4_std]
# >>>> standardize the values across samples for each feature
# introduce the naive scaler
scaler=StandardScaler()
# the model of common fts frame to use to fit the scaler : the dataset 1 is chosen because it has the most samples in order to make a learning from the largest pool possible
# (also, in the events of making this standization for all fts, this is the dataset that would be used as a master ie dataset we learn from for the fitting)
model_fts_frame_4_scaler = common_of_df_file1[list_of_common_fts].copy()
# fit the scaler to one dataset fts frame
scaler.fit(model_fts_frame_4_scaler)
# transform for each others dataset its fts frame
list_of_dfs_2_transform = [common_of_df_file1,common_of_df_file2,common_of_df_file3,common_of_df_file4,common_of_df_file5,common_of_df_file6,common_of_df_file7]
num_fts_frame_changed = 0
# - way 1 : replacing all fts cols at once
for a_full_df in list_of_dfs_2_transform:
    # for test : a_full_df = list_of_dfs_2_transform[0]
    fts_frame_2_change = a_full_df.loc[:, list_of_common_fts]
    fts_frame_scaled = scaler.transform(fts_frame_2_change)
    a_full_df.loc[:, list_of_common_fts] = fts_frame_scaled
    num_fts_frame_changed+=1
    print("number of feature frames changed :", num_fts_frame_changed)
# - way 2 : replacing column by column (not use or if using rework it again)
# for a_full_df in list_of_dfs_2_transform:
#     # for test : a_full_df = list_of_dfs_2_transform[0]
#     fts_frame_2_change = a_full_df.loc[:, list_of_common_fts]
#     fts_frame_scaled = scaler.transform(fts_frame_2_change)
#     for idx, col in enumerate(list_of_common_fts):
#         # for test : list_of_common_fts = [list_of_common_fts[0]]
#         a_full_df_keeper = a_full_df.copy()
#         a_full_df_keeper[col] = a_full_df_keeper.iloc[:,(len(list_of_common_cols)-1)] # put here the last column and do it also for the normal df
#         a_full_df_keeper[col] = a_full_df_keeper.iloc[:, (len(list_of_common_cols) - 1)]
#         # a_full_df[col] = fts_frame_scaled[:, idx]
#     num_fts_frame_changed+=1
#     print("number of feature frames change :", num_fts_frame_changed)

# rename the fts in each dataset (to later specify where each common fts is from
list_of_dfs_2_transform_new = []
num_fts_frame_names_changed = 0
for a_full_df_std in list_of_dfs_2_transform:
    # for the tests : a_full_df_std = list_of_dfs_2_transform[0]; a_full_df_std = list_of_dfs_2_transform[3]
    # get the cohort name
    list_of_cohorts_in_df_std = a_full_df_std["cohort"].unique()
    cohort_name_of_df_std = list_of_cohorts_in_df_std[0]
    # print(cohort_name_of_df_std)
    # rename the fts to know which cohort they are from
    list_all_fts_a_full_df_std = list(a_full_df_std.columns)
    list_all_fts_a_full_df_std.remove("Y_pCR")
    list_all_fts_a_full_df_std.remove("cohort")
    append_str = '_in_' + cohort_name_of_df_std
    list_all_fts_a_full_df_std_modded = [sub + append_str for sub in list_all_fts_a_full_df_std]
    list_all_fts_a_full_df_std_modded_completed = list_all_fts_a_full_df_std_modded + ["Y_pCR","cohort"]
    a_full_df_std_newfts = a_full_df_std.copy()
    a_full_df_std_newfts.columns = list_all_fts_a_full_df_std_modded_completed
    # a_full_df_std_newfts[list_all_fts_a_full_df_std] = a_full_df_std_newfts[list_all_fts_a_full_df_std].add_suffix('_in_' + cohort_name_of_df_std) # or also do df.columns = [str(col) + '_x' for col in df.columns]
    # put back the new df made inside the list of df
    list_of_dfs_2_transform_new.append(a_full_df_std_newfts)
    num_fts_frame_names_changed += 1
    print("number of feature frames where names have been changed :", num_fts_frame_names_changed, "; the cohort just done is : ", cohort_name_of_df_std)
    # index_of_elt_2_updt = list_of_dfs_2_transform.index(a_full_df_std)
    # list_of_dfs_2_transform[index_of_elt_2_updt] = a_full_df_std_newfts

#>>>> join the datasets (all features will be next to each other, all the responses will be in one column, all the cohort columns will be also made in one column same as the response)
# make a list of the df with only the fts (to make the resulting fts frame after concatenation)
# make a list of the df with only the response and the cohort cols (to make the resulting resp-cohort cols frame after concatenation)
list_of_dfs_2_divide_partof_fts_only = []
list_of_dfs_2_divide_partof_resp_only = []
for a_df_2_divide in list_of_dfs_2_transform_new:
    a_df_cut_2_resp_only = a_df_2_divide.loc[:, ["Y_pCR","cohort"]] # the resp col
    list_of_dfs_2_divide_partof_resp_only.append(a_df_cut_2_resp_only)
    a_df_2_divide.drop('Y_pCR', axis=1, inplace=True) # the fts cols only
    a_df_2_divide.drop('cohort', axis=1, inplace=True)
    a_df_cut_2_fts_only = a_df_2_divide.copy()
    list_of_dfs_2_divide_partof_fts_only.append(a_df_cut_2_fts_only)


# make the concatenated dfs
# - the concatenated df of features (by keeping all cols of features previously existing in each single df)
df_joined_fts_only = pd.concat(list_of_dfs_2_divide_partof_fts_only, axis=1, sort=False)
# make the nan cells into zeros values
df_joined_fts_only_zeroed = df_joined_fts_only.copy()
df_joined_fts_only_zeroed.fillna(0, inplace=True)
# - concatenante the df of the response column
df1_of_resp_only = list_of_dfs_2_divide_partof_resp_only[0]
df_joined_resp_only = df1_of_resp_only.append(list_of_dfs_2_divide_partof_resp_only[1:])
#>>> join the fts to the resp to make a full dataset
df_joined_new_design1 = pd.merge(df_joined_fts_only_zeroed, df_joined_resp_only, left_index=True, right_index=True)
# this can be used to output a plot of the dataframe so show the sections with zeros
# >>>> show an image of entire dataframe to have an overview of the zeros
list_all_cols_df_joined_new_design1 = list(df_joined_new_design1.columns)
list_all_cols_df_joined_new_design1.remove("Y_pCR")
list_all_cols_df_joined_new_design1.remove("cohort")
df_joined_new_design1_4_image = df_joined_new_design1.copy()
df_joined_new_design1_4_image = df_joined_new_design1_4_image[list_all_cols_df_joined_new_design1]
df_joined_new_design1_4_image[df_joined_new_design1_4_image != 0.0] = 999
# Let's look at this new design matrix and check it's blocks in diagonal, with each data set features info forming one block
plt.imshow(df_joined_new_design1_4_image, cmap='viridis', aspect='auto')
plt.colorbar()
# succession of cohorts on the Y axis is needed
list_of_cohorts_in_Yaxis_of_data_image = df_joined_new_design1["cohort"].unique()
print("- This is the succession of cohorts on the Y axis of the data image : ")
print(list_of_cohorts_in_Yaxis_of_data_image)
# keep the image and use it as proof of where the zeros are initially after the join

# >>>> There is a grouping required by SPAMS : in each dataset block of features, features must be sequenced in the same way so that different representations of the same feature are always at the same position
# we could have sorted the features to satisfy that sequencing, make a new version of the df that is following that grouping and keep the grouping to transfer it in out SPAMS scripts
# but we prefer to keep our joined dataset and such for simplicity of presentation and later, in the SPAMS scripts, create the grouping properly with the loaded dataset
# in the meantime, because all features from a dataset are sorted the same, the grouping that can be used for tests is the following :
# dict of values ntask and nftsbytask is : {0 : 12034, 1 : 12034, 2 : 12034, 3 : 12034, 4 : 12034, 5 : 12034}


# # - this can be used to make a version where the different representations of the same feature are always next to each other
# list_all_cols_df_joined_new_design1_sorted = sorted(list_all_cols_df_joined_new_design1)
# list_all_cols_df_joined_new_design1_sorted_plus2 = list_all_cols_df_joined_new_design1_sorted + ["Y_pCR","cohort"]
# df_joined_new_design1_ftssorted = df_joined_new_design1[list_all_cols_df_joined_new_design1_sorted_plus2]

# >>>>>> check the datatypes
df_joined_new_design1.info()
# Index: 233 entries, GSM1030229 to GSM1550523
# Columns: 84240 entries, A1CF_in_GSE41998 to cohort
# dtypes: float64(84238), int64(1), object(1)
# memory usage: 149.8+ MB

#>>>> saving the df
fullname_file_of_df_joined_new_design1 = "/data_acquisition/1_pipelines_or_tasks/JoinNewDesign1CommonFtsof7_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_7cohortname.csv"
df_joined_new_design1.to_csv(fullname_file_of_df_joined_new_design1, header=True) # we keep the index for a future joining w tables of fts
print("File saved !")
#>>>>>>>>>>>>>>
