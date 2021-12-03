#!/usr/bin/env python
# coding: utf-8

# ## Making a full datset for a cohort
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

#>>>>>setting the cohort name for later use
cohort_name = "GSE20271"

#>>>>>>>>>>>>>> Loading fts data
#---set the name of the sheet where the data of the cohort is
filepath_1cohort_gex_data_bestprobesets_genesnames= "/data_warehouse/outputs/atip3_ml_dataset_type1/GSE20271_bestprobesetsonly_genesnames_12151x178_GEX.csv"
sep_in_file = ","
df_file = pd.read_csv(filepath_1cohort_gex_data_bestprobesets_genesnames, sep_in_file)
# rename the probes column before putting it as index (so that later we can have a nice titles for the probes)
df_file.rename(columns={"Unnamed: 0" : "features_names"}, inplace=True)
# put the rownames (genes) as index
df_file = df_file.set_index(list(df_file.columns)[0]) # because a csv from R has the rownames becoming the first col
# transform the df to pu the genes as colnames
df_file_fts_only = df_file.transpose()

#####-----checkpoint to verify the data types
print("----A checkpoint to check on table dtypes (first 5 columns and last 5 columns) in order to know what dtypes to convert...")
print(df_file_fts_only.info())  # on the model of df_joined[df_joined.columns[:10]].dtypes
####-----
# Strategy : instead of loading the ph data file for the treatment col and also the clusters values, we only load a created file of the clusters value joined with the treatment when it was needed to restrict
# #>>>> Loading the treatment and response info
# filepath_1cohort_ph_data_ATIP3probesonly= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE41998_ATIP3probesetsonly_probesnames_279x7_ph.csv"
# sep_in_file = ","
# df_file_ph = pd.read_csv(filepath_1cohort_ph_data_ATIP3probesonly, sep_in_file)
# # put the rownames (genes) as index
# df_file_ph = df_file_ph.set_index(list(df_file_ph.columns)[0]) # because a csv from R has the rownames becoming the first col
# # df_file_ph.drop('treatment', axis=1, inplace=True) # keep this to make computations only on the Taxanes treated patients
# df_file_ph.columns # show the columns in order to copy past the names when renaming them
# # drop the not needed cols and rename the not so nicely written
# df_file_ph.drop(['geo_accession', 'ER_status', 'PR_status', 'HER2_status','TNBC'], axis=1, inplace=True)

#>>>> Loading the clusters info (w treatment info if needed to restrict)
filepath_1cohort_ph_data_ATIP3probesonly= "/data_warehouse/outputs/atip3_ml_dataset_type1/GSE20271_ATIP3probesetsonly_InfoTreatmentCluster.csv"
sep_in_file = ","
df_sup_file = pd.read_csv(filepath_1cohort_ph_data_ATIP3probesonly, sep_in_file)
# put the rownames (genes) as index
df_sup_file = df_sup_file.set_index(list(df_sup_file.columns)[0]) # because a csv from R has the rownames becoming the first col
# df_file_ph.drop('treatment', axis=1, inplace=True) # keep this to make computations only on the Taxanes treated patients
df_sup_file.columns # show the columns in order to copy past the names when renaming them
# keep only the needed cols
list_of_only_needed_cols = ['ATIP3_class_hm','treatment','RCH']
df_sup_file_restricted = df_sup_file[list_of_only_needed_cols]
# rename the not so nicely written among the kept cols
df_sup_file_restricted.rename(columns={"RCH":"Y_pCR"}, inplace=True)
# list the different values in the columns to see if additionnal repairs are needed
for col in df_sup_file_restricted:
    print(col)
    print(df_sup_file_restricted[col].unique())  # only clusters low, low med and high appear here (to keep in mind)

#>>>>optional steps
# # complementary formatting of the response
# df_sup_file_restricted["Y_pCR"].replace(["pcr: 0"], [0], inplace=True) # reencode the RCH as 0 and 1 (No and Yes previously)
# restricted to only taxanes treated samples
df_sup_file_restricted1 = df_sup_file_restricted[(df_sup_file_restricted.treatment=="treatment received (1=fac, 2=t/fac): 2")]
# drop the now uneeded col of treatment after all samples are for sure taxanes treated
df_sup_file_restricted1.drop('treatment', axis=1, inplace=True)
#>>>>
# df_sup_file_restricted1 = df_sup_file_restricted

#>>>> restrict to only the atip3 low
df_sup_file_restricted2 = df_sup_file_restricted1[(df_sup_file_restricted1.ATIP3_class_hm=="low")]
# drop the now uneeded col of treatment after all samples are for sure taxanes treated
df_sup_file_restricted2.drop('ATIP3_class_hm', axis=1, inplace=True)

#>>>>>joining the fts and response df
df_joined = pd.merge(df_file_fts_only, df_sup_file_restricted2, left_index=True, right_index=True)

#>>>> add a col with the cohort name (the GSE) to later use it to make the task response
df_joined['cohort']= cohort_name

#>>>> saving the df
fullname_file_of_ml_dataset = "/data_warehouse/outputs/atip3_ml_dataset_type1/GSE20271_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
df_joined.to_csv(fullname_file_of_ml_dataset, header=True) # we keep the index for a future joining w tables of fts
print("File saved !")
#>>>>>>>>>>>>>>