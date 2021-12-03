#!/usr/bin/env python
# coding: utf-8

# ## Joining the type 1 datasets into one bigger datset for multitalk learning
# Type1 = ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname
# contains :
# - n rows as samples
# - m cols as fts
# - 1 cols as pCR response
# - and 1 col not appearing but previously used to restrict to taxanes treated only samples

# imports
import numpy as np
# from numpy import seterr,isneginf # used to manage the change into log2 o values in a np array
import matplotlib.pyplot as plt
from textwrap import wrap # to wrap plot titles
import pandas as pd
from statannot import add_stat_annotation

#>>>>> What do we load : 7/9 datasets type 1
# reason : the GSE25066 is the GSE25055 + the GSE20271. The GSE25066 is not very inspiring for supervisor 1. and the GSE20271 does not any of the 2 biomarker traits.
# so we only use the GSE25055 out of those 3
# hence 7 cohorts out of 9

#>>>>>>>>>>>>>> Loading type 1 datsets (7)
#---set the name of the sheet where the data of the cohort is
filepath_of_ml_dataset1= "/data_warehouse/outputs/atip3_ml_dataset_type1/GSE41998_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
filepath_of_ml_dataset2= "/data_warehouse/outputs/atip3_ml_dataset_type1/GSE26639_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
filepath_of_ml_dataset3= "/data_warehouse/outputs/atip3_ml_dataset_type1/GSE32646_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
filepath_of_ml_dataset4= "/data_warehouse/outputs/atip3_ml_dataset_type1/GSE25055_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
filepath_of_ml_dataset5= "/data_warehouse/outputs/atip3_ml_dataset_type1/GSE20194_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
filepath_of_ml_dataset6= "/data_warehouse/outputs/atip3_ml_dataset_type1/GSE23988_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
filepath_of_ml_dataset7= "/data_warehouse/outputs/atip3_ml_dataset_type1/GSE63471_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
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
print(len(result)) # 12036 ie 12304 fts
list_of_common_cols = list(result)
# putting the in previous order : fts in alphabetical, then Y_pCR, then cohort
list_of_common_cols.remove("Y_pCR")
list_of_common_cols.remove("cohort")
list_of_common_cols = sorted(list_of_common_cols)
list_of_common_cols = list_of_common_cols + ["Y_pCR","cohort"]
# restrict the loaded datasets to the common cols
common_of_df_file1 = df_file1[list_of_common_cols]
common_of_df_file2 = df_file2[list_of_common_cols]
common_of_df_file3 = df_file3[list_of_common_cols]
common_of_df_file4 = df_file4[list_of_common_cols]
common_of_df_file5 = df_file5[list_of_common_cols]
common_of_df_file6 = df_file6[list_of_common_cols]
common_of_df_file7 = df_file7[list_of_common_cols]

#>>>> join the loaded common versions of datasets
df_joined = pd.concat([common_of_df_file1,common_of_df_file2,common_of_df_file3,common_of_df_file4,common_of_df_file5,common_of_df_file6,common_of_df_file7]) # ignore_index=True not put to keep indexes
# 233 samples, 12036 fts

#>>>> create the response isolating each task (each cohort info)
list_of_cohorts = df_joined["cohort"].unique()
list_of_cohorts # show the list of cohorts
# colname strategy is Y_GSEnumber
df_joined['Y_GSE41998'] = np.where(df_joined['cohort'] == 'GSE41998', 1, 0)
df_joined['Y_GSE26639'] = np.where(df_joined['cohort'] == 'GSE26639', 1, 0)
df_joined['Y_GSE32646'] = np.where(df_joined['cohort'] == 'GSE32646', 1, 0)
df_joined['Y_GSE25055'] = np.where(df_joined['cohort'] == 'GSE25055', 1, 0)
df_joined['Y_GSE20194'] = np.where(df_joined['cohort'] == 'GSE20194', 1, 0)
df_joined['Y_GSE23988'] = np.where(df_joined['cohort'] == 'GSE23988', 1, 0)
df_joined['Y_GSE63471'] = np.where(df_joined['cohort'] == 'GSE63471', 1, 0)
# drop the col of cohort name
df_joined.drop('cohort', axis=1, inplace=True)
# check the datatypes (1st 5 cols and last 10 cols)
df_joined.info()
# # or this
# df_joined_preview_dtypes = df_joined.iloc[:, list(range(6)) + [-5, -4, -3, -2, -1]]
# print(df_aft_resp_preview.info())  # on the model of df_joined[df_joined.columns[:10]].dtypes

#>>>> saving the df
fullname_file_of_joined_type1_ml_dataset = "/data_acquisition/1_pipelines_or_tasks/Joinof7_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_7cohortname.csv"
df_joined.to_csv(fullname_file_of_joined_type1_ml_dataset, header=True) # we keep the index for a future joining w tables of fts
print("File saved !")
#>>>>>>>>>>>>>>
# repeated here is the filename of the joined7 with 8 responses
# "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Joinof7_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_7cohortname.csv"