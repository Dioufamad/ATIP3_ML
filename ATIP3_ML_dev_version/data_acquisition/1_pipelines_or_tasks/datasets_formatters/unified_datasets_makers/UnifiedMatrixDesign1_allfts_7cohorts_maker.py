#!/usr/bin/env python
# coding: utf-8
# A script to create a unified matrix design for analysis of multiples populations that share the same response

# imports
import numpy as np
# from numpy import seterr,isneginf # used to manage the change into log2 o values in a np array
import matplotlib.pyplot as plt
from textwrap import wrap # to wrap plot titles
import pandas as pd
from statannot import add_stat_annotation
from sklearn.preprocessing import StandardScaler

#>>>>>>>>>>>>>>>>> With all features across datasets, common only

# ## Joining the type 1 datasets into one bigger datset for multitalk learning
# Type1 = ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname
# contains :
# - n rows as samples
# - m cols as fts
# - 1 cols as pCR response
# - and 1 col not appearing but previously used to restrict to taxanes treated only samples

#>>>>> What do we load : 7/9 datasets type 1
# reason : the GSE25066 is the GSE25055 + the GSE20271. The GSE25066 is not very inspiring for supervisor 1. and the GSE20271 does not any of the 2 biomarker traits.
# so we only use the GSE25055 out of those 3
# hence 7 cohorts out of 9

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

# >>>> lets take a knee and strategize for a min :
# - sitrep : we have 1 set of 7 datasets (dt1-7) and we want to standardize not just the common cols but all cols
# - to do it in a secure way, we have to :
# - - find the buckets of fts across all the datasets
# - - designated a dataset that has all these buckets
# - - split that master dataset into versions (one version contain only the fts in a bucket)
# - - fit a scaler on each version of the master dataset
# - - split each dataset into the same versions than the master one until no fts is left out
# - - transform, for each dataset, the version created using the scalers created from the master dataset
# - - stitch back the versions of each dataset into the original dataset
# now go on with our script of making the full dataset of

# >>>>> find the buckets of fts across all the datasets
# - get the list of cols
list_all_cols_df_file1 = list(df_file1.columns) # a list of 12151 elts + 2 cols (resp & cohortname)
list_all_cols_df_file2 = list(df_file2.columns) # a list of 19419 elts + 2 cols (resp & cohortname)
list_all_cols_df_file3 = list(df_file3.columns) # a list of 19417 elts + 2 cols (resp & cohortname)
list_all_cols_df_file4 = list(df_file4.columns) # a list of 12151 elts + 2 cols (resp & cohortname)
list_all_cols_df_file5 = list(df_file5.columns) # a list of 12151 elts + 2 cols (resp & cohortname)
list_all_cols_df_file6 = list(df_file6.columns) # a list of 12151 elts + 2 cols (resp & cohortname)
list_all_cols_df_file7 = list(df_file7.columns) # a list of 12151 elts + 2 cols (resp & cohortname)
# behind the scenes, we known that the datasets with 12151 fts have been made using the same platform [Affy U133 A (GPL571 for the U133A 2.0 and GPL96 for the U133A)] : we call them group platform 1 (5 dts)
# and the datsets with ~19417 fts have been made using the same platform (Affy U133 PLus 2.0 (GPL 570)) : we call them group platform 2 (2 dts)
# =>>>> hence we can deduce that we have two groups of datasets

# - lets check if the group platform 1 have all their fts in common
p_platform1 = [list_all_cols_df_file1,list_all_cols_df_file4,list_all_cols_df_file5,list_all_cols_df_file6,list_all_cols_df_file7]
result_platform1 = set(p_platform1[0])
for s_platform1 in p_platform1[1:]:
	result_platform1.intersection_update(s_platform1)
result_platform1 = result_platform1 - set(["Y_pCR", "cohort"])
print("Number of features retained as common : ",len(result_platform1)) # 12151 elts + 2 cols (resp & cohortname)
list_of_common_cols_platform1 = sorted(list(result_platform1))
# =>>>> all fts of the plaform 1 has the fts in common

# - lets check if the group platform 2 have all their fts in common
p_platform2 = [list_all_cols_df_file2,list_all_cols_df_file3]
result_platform2 = set(p_platform2[0])
for s_platform2 in p_platform2[1:]:
	result_platform2.intersection_update(s_platform2)
result_platform2 = result_platform2 - set(["Y_pCR", "cohort"])
print("Number of features retained as common : ",len(result_platform2)) # 19417 elts + 2 cols (resp & cohortname) =>>>> all fts of the plaform 1 has the fts in common
list_of_common_cols_platform2 = sorted(list(result_platform2))

fts_only_in_df2 = sorted(list(set(list_all_cols_df_file2).difference(list_all_cols_df_file3)))
print("Number of features only in dataset2 : ",len(fts_only_in_df2), "and are : ",fts_only_in_df2) # a list of 2 elts : "GAPDH", "ACTB"
fts_only_in_df3 = sorted(list(set(list_all_cols_df_file3).difference(list_all_cols_df_file2)))
print("Number of features only in dataset2 : ",len(fts_only_in_df3), "and are : ",fts_only_in_df3) # a list of 0 elts
# =>>>> the dataset 2 and 3 have 19417 fts in common and the dataset 2 have 2 fts more
# Those 2 fts specific to the dataset 2 are "GAPDH", "ACTB". They does not pose a problem of needing to go back to the making of the datset 3 to see if we missed something because :
# 1- those 2 fts are HKGs so they are pretty stable across samples and then will not be likely among the fts that will define a structuration of the population (see She et al., 2009)
# 2- we can check if they are present in dataset2 but in different writting of the fts name :
print("these are the fts with ACTB in dataset2 : ")
for x in list_all_cols_df_file2:
	if "ACTB" in x :
		print(x)
# these are the fts with "ACTB" in dataset2
# ACTB /// ACTG1
# LACTB2
# LACTB
# ACTB
print("these are the fts with ACTB in dataset3 : ")
for x in list_all_cols_df_file3:
	if "ACTB" in x :
		print(x)
# these are the fts with "ACTB" in dataset3
# ACTB /// ACTG1
# LACTB2
# LACTB
# =>>>> ACTB is in fact present in dataset 3 so no need to make a fuss about it
print("these are the fts with GAPDH in dataset2 : ")
for x in list_all_cols_df_file2:
	if "GAPDH" in x :
		print(x)
# these are the fts with "GAPDH" in dataset2
# GAPDHS
# GAPDH
print("these are the fts with GAPDH in dataset3 : ")
for x in list_all_cols_df_file3:
	if "GAPDH" in x :
		print(x)
# these are the fts with "GAPDH" in dataset3
# GAPDHS
# =>>> GAPDH is textually not in dataset2. but we do not make a fuss about is because it is quite stable across samples.

# >>> lets find out the pools of fts we have :
dict_dti_listallcolsdffilei = {"dt1" : list_all_cols_df_file1 ,
							   "dt2" : list_all_cols_df_file2 ,
							   "dt3" : list_all_cols_df_file3 ,
							   "dt4" : list_all_cols_df_file4 ,
							   "dt5" : list_all_cols_df_file5 ,
							   "dt6" : list_all_cols_df_file6 ,
							   "dt7" : list_all_cols_df_file7}
list_of_all_possible_fts = [item for sublist in list(dict_dti_listallcolsdffilei.values()) for item in sublist] # 99605 including resp and cohortname
list_of_all_possible_fts_unik_only = sorted(list(set(list_of_all_possible_fts) - set(["Y_pCR", "cohort"]))) # 19534 without resp and cohortname
dict_ft_listofdtiwhereused = {}
# a function to update very well a dict of key as ft and value as list of all the dt where found
def add_entry_in_dict(dict_to_supply,key,value):
	try:
		dict_to_supply[key].append(value)
	except KeyError:  # if the key does not exit (case of the first append for a key) # except means "in case of this following event, do this : # maybe change later by "if key not if list of keys of the dict"
		dict_to_supply[key] = [value]
	return
for a_possible_ft in list_of_all_possible_fts_unik_only: # test : a_possible_ft = "ACTB"
	# use_list_of_dti_for_present_possible_ft = []
	if a_possible_ft in list(dict_dti_listallcolsdffilei.values())[0]:
		# use_list_of_dti_for_present_possible_ft.append(list(dict_dti_listallcolsdffilei.keys())[0])
		add_entry_in_dict(dict_ft_listofdtiwhereused, a_possible_ft, list(dict_dti_listallcolsdffilei.keys())[0])
	if a_possible_ft in list(dict_dti_listallcolsdffilei.values())[1]:
		# use_list_of_dti_for_present_possible_ft.append(list(dict_dti_listallcolsdffilei.keys())[1])
	    add_entry_in_dict(dict_ft_listofdtiwhereused, a_possible_ft, list(dict_dti_listallcolsdffilei.keys())[1])
	if a_possible_ft in list(dict_dti_listallcolsdffilei.values())[2]:
		# use_list_of_dti_for_present_possible_ft.append(list(dict_dti_listallcolsdffilei.keys())[2])
	    add_entry_in_dict(dict_ft_listofdtiwhereused, a_possible_ft, list(dict_dti_listallcolsdffilei.keys())[2])
	if a_possible_ft in list(dict_dti_listallcolsdffilei.values())[3]:
		# use_list_of_dti_for_present_possible_ft.append(list(dict_dti_listallcolsdffilei.keys())[3])
	    add_entry_in_dict(dict_ft_listofdtiwhereused, a_possible_ft, list(dict_dti_listallcolsdffilei.keys())[3])
	if a_possible_ft in list(dict_dti_listallcolsdffilei.values())[4]:
		# use_list_of_dti_for_present_possible_ft.append(list(dict_dti_listallcolsdffilei.keys())[4])
	    add_entry_in_dict(dict_ft_listofdtiwhereused, a_possible_ft, list(dict_dti_listallcolsdffilei.keys())[4])
	if a_possible_ft in list(dict_dti_listallcolsdffilei.values())[5]:
		# use_list_of_dti_for_present_possible_ft.append(list(dict_dti_listallcolsdffilei.keys())[5])
	    add_entry_in_dict(dict_ft_listofdtiwhereused, a_possible_ft, list(dict_dti_listallcolsdffilei.keys())[5])
	if a_possible_ft in list(dict_dti_listallcolsdffilei.values())[6]:
		# use_list_of_dti_for_present_possible_ft.append(list(dict_dti_listallcolsdffilei.keys())[6])
		add_entry_in_dict(dict_ft_listofdtiwhereused, a_possible_ft, list(dict_dti_listallcolsdffilei.keys())[6])
	# dict_ft_listofdtiwhereused[a_possible_ft] = use_list_of_dti_for_present_possible_ft

# lets tidy it up
# now we have in the newly supplied dict the values being all the different list of dt where a ft is used
# lets find the different types of lists of list of datasets that shares a feature. Also for each of those lists, what is the full list of fts shared. then we will be reporting the info
dict_ft_listofdtiwhereused_tidy = {}
for a_unique_ft_across_all_dt, a_possible_list_dt_sharing_the_ft in dict_ft_listofdtiwhereused.items():
	# - lets make the key
	new_key_as_str_of_dti_sharing_the_ft = '-'.join(sorted(a_possible_list_dt_sharing_the_ft))
	# - the value to make is a_unique_ft_across_all_dt
	add_entry_in_dict(dict_ft_listofdtiwhereused_tidy, new_key_as_str_of_dti_sharing_the_ft, a_unique_ft_across_all_dt)
print("Number of possible unique use lists we have across the datasets : ",len(list(dict_ft_listofdtiwhereused_tidy.keys())))
print("They are : ")
for an_ordered_list_of_dt_as_a_unique_use in sorted(list(dict_ft_listofdtiwhereused_tidy.keys())):
	print(an_ordered_list_of_dt_as_a_unique_use, "unique uses in the case of :",len(list(dict_ft_listofdtiwhereused_tidy[an_ordered_list_of_dt_as_a_unique_use])),"features")

# - we clearly know now that we have 4 pools of fts. We have to decide for each pool of fts, which dataset to use as a master for the fit befire the transform :
# Rule of choice : the master is always choosen as being the largest dataset that have all the features in the use but also is limited to only those features (because we risk creating values for column that are not to be implicated)
# we choose the largest dt because it is more training samples for the model to adapt in the transform (because it is really that in reality)
# - - the use "dt1-dt2-dt3-dt4-dt5-dt6-dt7" is the group of fts common to both platforms : we use the dt1 as master (version 1 aka Vpart1)---------12034 fts
# - - the use "dt1-dt2-dt4-dt5-dt6-dt7" is the group of fts that exists only on the platform1 but somehow dt2 has them while being made using platform2 : we use the dt1 as master (version 2 aka Vpart2)--------2 fts
# - - the use "dt1-dt4-dt5-dt6-dt7" is the group of the fts that exists only on the plaform1 : we use the dt1 as master (version 3 aka Vpart3)--------115 fts
# - - the use "dt2-dt3" is the group of fts that exists only on the plaform1 : we use dt2 as master (version 4 aka Vpart4)-----7383 fts

# = >>> we have 4 versions maximum to make for each data set as such :
# - datasets 1-7 will have Vpart1 : make a fit on dt1 and transform on those
# - datasets 1,2,4-7 will have Vpart2 : make a fit on dt1 and transform on those
# - datasets 1,4-7 will have Vpart3 : make a fit on dt1 and transform on those
# - dataset 2,3 will have Vpart4 : make a fit on dt2 and transform on those
# summary of tasks for this part : (write it later)
# Verifications :


dict_Vparts = {"Vpart1" : dict_ft_listofdtiwhereused_tidy[sorted(list(dict_ft_listofdtiwhereused_tidy.keys()))[0]],
			   "Vpart2" : dict_ft_listofdtiwhereused_tidy[sorted(list(dict_ft_listofdtiwhereused_tidy.keys()))[1]],
			   "Vpart3" : dict_ft_listofdtiwhereused_tidy[sorted(list(dict_ft_listofdtiwhereused_tidy.keys()))[2]],
			   "Vpart4" : dict_ft_listofdtiwhereused_tidy[sorted(list(dict_ft_listofdtiwhereused_tidy.keys()))[3]]}

print("Verification 1 : Counts of each Vparti and checking if all the Vpart have 0 duplicates in terms of features contained : ")
for a_vpart,a_sorted_list_of_fts in dict_Vparts.items():
	print(" - number of duplicates among the",len(list(a_sorted_list_of_fts)),"of",a_vpart," is : ", len(list(a_sorted_list_of_fts)) - len(list(set(a_sorted_list_of_fts))))

print("Verification 2 : if all the Vpart are distincs in terms of features contained : ")
for a_vpart,a_sorted_list_of_fts in dict_Vparts.items():
	for a_vpart_bis,a_sorted_list_of_fts_bis in dict_Vparts.items() :
		if a_vpart != a_vpart_bis:
			print("intersection of",a_vpart,"and",a_vpart_bis,"has count : ",len(list(set(a_sorted_list_of_fts) & set(a_sorted_list_of_fts_bis))))

# >>>> scaling the Vpart1s across all datasets concerned
# - restrict the loaded datasets
df_file1_Vpart1 = df_file1[dict_Vparts["Vpart1"]].copy()
df_file2_Vpart1 = df_file2[dict_Vparts["Vpart1"]].copy()
df_file3_Vpart1 = df_file3[dict_Vparts["Vpart1"]].copy()
df_file4_Vpart1 = df_file4[dict_Vparts["Vpart1"]].copy()
df_file5_Vpart1 = df_file5[dict_Vparts["Vpart1"]].copy()
df_file6_Vpart1 = df_file6[dict_Vparts["Vpart1"]].copy()
df_file7_Vpart1 = df_file7[dict_Vparts["Vpart1"]].copy()
# - keep a copy of each single dataset for after operations comparisons
list_of_dfs_Vpart1_b4_std = [df_file1_Vpart1.copy(),df_file2_Vpart1.copy(),df_file3_Vpart1.copy(),df_file4_Vpart1.copy(),df_file5_Vpart1.copy(),df_file6_Vpart1.copy(),df_file7_Vpart1.copy()]
# introduce the naive scaler
scaler_Vpart1=StandardScaler()
# the model of common fts frame to use to fit the scaler (the dataset 2 is chosen because in the events of making the standization for all fts, this is the dataset that would be used as base for fitting)
model_fts_frame_4_scaler_Vpart1 = df_file1_Vpart1.copy()
# fit the scaler to one dataset fts frame
scaler_Vpart1.fit(model_fts_frame_4_scaler_Vpart1)
# transform for each others dataset its fts frame
list_of_dfs_2_transform_Vpart1 = [df_file1_Vpart1,df_file2_Vpart1,df_file3_Vpart1,df_file4_Vpart1,df_file5_Vpart1,df_file6_Vpart1,df_file7_Vpart1]
num_fts_frame_changed = 0
# replacing all fts cols at once
for a_full_df in list_of_dfs_2_transform_Vpart1:
	# for test : a_full_df = list_of_dfs_2_transform_Vpart1[0]
	fts_frame_2_change = a_full_df.loc[:, dict_Vparts["Vpart1"]]
	fts_frame_scaled = scaler_Vpart1.transform(fts_frame_2_change)
	a_full_df.loc[:, dict_Vparts["Vpart1"]] = fts_frame_scaled
	num_fts_frame_changed+=1
	print("number of feature frames changed for the Vpart1 :", num_fts_frame_changed)

# >>>> scaling the Vpart2s across all datasets concerned
# - restrict the loaded datasets
df_file1_Vpart2 = df_file1[dict_Vparts["Vpart2"]].copy()
df_file2_Vpart2 = df_file2[dict_Vparts["Vpart2"]].copy()
df_file4_Vpart2 = df_file4[dict_Vparts["Vpart2"]].copy()
df_file5_Vpart2 = df_file5[dict_Vparts["Vpart2"]].copy()
df_file6_Vpart2 = df_file6[dict_Vparts["Vpart2"]].copy()
df_file7_Vpart2 = df_file7[dict_Vparts["Vpart2"]].copy()
# - keep a copy of each single dataset for after operations comparisons
list_of_dfs_Vpart2_b4_std = [df_file1_Vpart2.copy(),df_file2_Vpart2.copy(),df_file4_Vpart2.copy(),df_file5_Vpart2.copy(),df_file6_Vpart2.copy(),df_file7_Vpart2.copy()]
# introduce the naive scaler
scaler_Vpart2=StandardScaler()
# the model of common fts frame to use to fit the scaler (the dataset 2 is chosen because in the events of making the standization for all fts, this is the dataset that would be used as base for fitting)
model_fts_frame_4_scaler_Vpart2 = df_file1_Vpart2.copy()
# fit the scaler to one dataset fts frame
scaler_Vpart2.fit(model_fts_frame_4_scaler_Vpart2)
# transform for each others dataset its fts frame
list_of_dfs_2_transform_Vpart2 = [df_file1_Vpart2,df_file2_Vpart2,df_file4_Vpart2,df_file5_Vpart2,df_file6_Vpart2,df_file7_Vpart2]
num_fts_frame_changed = 0
# replacing all fts cols at once
for a_full_df in list_of_dfs_2_transform_Vpart2:
	# for test : a_full_df = list_of_dfs_2_transform_Vpart2[0]
	fts_frame_2_change = a_full_df.loc[:, dict_Vparts["Vpart2"]]
	fts_frame_scaled = scaler_Vpart2.transform(fts_frame_2_change)
	a_full_df.loc[:, dict_Vparts["Vpart2"]] = fts_frame_scaled
	num_fts_frame_changed+=1
	print("number of feature frames changed for the Vpart2 :", num_fts_frame_changed)


# >>>> scaling the Vpart3s across all datasets concerned
# - restrict the loaded datasets
df_file1_Vpart3 = df_file1[dict_Vparts["Vpart3"]].copy()
df_file4_Vpart3 = df_file4[dict_Vparts["Vpart3"]].copy()
df_file5_Vpart3 = df_file5[dict_Vparts["Vpart3"]].copy()
df_file6_Vpart3 = df_file6[dict_Vparts["Vpart3"]].copy()
df_file7_Vpart3 = df_file7[dict_Vparts["Vpart3"]].copy()
# - keep a copy of each single dataset for after operations comparisons
list_of_dfs_Vpart3_b4_std = [df_file1_Vpart3.copy(),df_file4_Vpart3.copy(),df_file5_Vpart3.copy(),df_file6_Vpart3.copy(),df_file7_Vpart3.copy()]
# introduce the naive scaler
scaler_Vpart3=StandardScaler()
# the model of common fts frame to use to fit the scaler (the dataset 2 is chosen because in the events of making the standization for all fts, this is the dataset that would be used as base for fitting)
model_fts_frame_4_scaler_Vpart3 = df_file1_Vpart3.copy()
# fit the scaler to one dataset fts frame
scaler_Vpart3.fit(model_fts_frame_4_scaler_Vpart3)
# transform for each others dataset its fts frame
list_of_dfs_2_transform_Vpart3 = [df_file1_Vpart3,df_file4_Vpart3,df_file5_Vpart3,df_file6_Vpart3,df_file7_Vpart3]
num_fts_frame_changed = 0
# replacing all fts cols at once
for a_full_df in list_of_dfs_2_transform_Vpart3:
	# for test : a_full_df = list_of_dfs_2_transform_Vpart3[0]
	fts_frame_2_change = a_full_df.loc[:, dict_Vparts["Vpart3"]]
	fts_frame_scaled = scaler_Vpart3.transform(fts_frame_2_change)
	a_full_df.loc[:, dict_Vparts["Vpart3"]] = fts_frame_scaled
	num_fts_frame_changed+=1
	print("number of feature frames changed for the Vpart3 :", num_fts_frame_changed)



# >>>> scaling the Vpart4s across all datasets concerned
# - restrict the loaded datasets
df_file2_Vpart4 = df_file2[dict_Vparts["Vpart4"]].copy()
df_file3_Vpart4 = df_file3[dict_Vparts["Vpart4"]].copy()

# - keep a copy of each single dataset for after operations comparisons
list_of_dfs_Vpart4_b4_std = [df_file2_Vpart4.copy(),df_file3_Vpart4.copy()]
# introduce the naive scaler
scaler_Vpart4=StandardScaler()
# the model of common fts frame to use to fit the scaler (the dataset 2 is chosen because in the events of making the standization for all fts, this is the dataset that would be used as base for fitting)
model_fts_frame_4_scaler_Vpart4 = df_file2_Vpart4.copy()
# fit the scaler to one dataset fts frame
scaler_Vpart4.fit(model_fts_frame_4_scaler_Vpart4)
# transform for each others dataset its fts frame
list_of_dfs_2_transform_Vpart4 = [df_file2_Vpart4,df_file3_Vpart4]
num_fts_frame_changed = 0
# replacing all fts cols at once
for a_full_df in list_of_dfs_2_transform_Vpart4:
	# for test : a_full_df = list_of_dfs_2_transform_Vpart4[0]
	fts_frame_2_change = a_full_df.loc[:, dict_Vparts["Vpart4"]]
	fts_frame_scaled = scaler_Vpart4.transform(fts_frame_2_change)
	a_full_df.loc[:, dict_Vparts["Vpart4"]] = fts_frame_scaled
	num_fts_frame_changed+=1
	print("number of feature frames changed for the Vpart4 :", num_fts_frame_changed)


# >>>>> Next : we have to stitch back the Vparts together and restore them the full dfs we have for each dataset
# - composition of each dataset :
# - - dt1 : Vpart1, Vpart2, Vpart3, non fts cols
# - - dt2 : Vpart1, Vpart2, Vpart4, non fts cols
# - - dt3 : Vpart1, Vpart4, non fts cols
# - - dt4 : Vpart1, Vpart2, Vpart3, non fts cols
# - - dt5 : Vpart1, Vpart2, Vpart3, non fts cols
# - - dt6 : Vpart1, Vpart2, Vpart3, non fts cols
# - - dt7 : Vpart1, Vpart2, Vpart3, non fts cols

# >>>> stitch back the Vparts
list_of_dfs_2_transform_stitched = []
list_of_non_fts_cols = ["Y_pCR","cohort"]
# df1
df_file1_stitched = pd.concat([list_of_dfs_2_transform_Vpart1[0],list_of_dfs_2_transform_Vpart2[0],list_of_dfs_2_transform_Vpart3[0],df_file1[list_of_non_fts_cols].copy()], axis=1, sort=False)
list_of_dfs_2_transform_stitched.append(df_file1_stitched)
# df2
df_file2_stitched = pd.concat([list_of_dfs_2_transform_Vpart1[1],list_of_dfs_2_transform_Vpart2[1],list_of_dfs_2_transform_Vpart4[0],df_file2[list_of_non_fts_cols].copy()], axis=1, sort=False)
list_of_dfs_2_transform_stitched.append(df_file2_stitched)
# df3
df_file3_stitched = pd.concat([list_of_dfs_2_transform_Vpart1[2],list_of_dfs_2_transform_Vpart4[1],df_file3[list_of_non_fts_cols].copy()], axis=1, sort=False)
list_of_dfs_2_transform_stitched.append(df_file3_stitched)
# df4
df_file4_stitched = pd.concat([list_of_dfs_2_transform_Vpart1[3],list_of_dfs_2_transform_Vpart2[2],list_of_dfs_2_transform_Vpart3[1],df_file4[list_of_non_fts_cols].copy()], axis=1, sort=False)
list_of_dfs_2_transform_stitched.append(df_file4_stitched)
# df5
df_file5_stitched = pd.concat([list_of_dfs_2_transform_Vpart1[4],list_of_dfs_2_transform_Vpart2[3],list_of_dfs_2_transform_Vpart3[2],df_file5[list_of_non_fts_cols].copy()], axis=1, sort=False)
list_of_dfs_2_transform_stitched.append(df_file5_stitched)
# df6
df_file6_stitched = pd.concat([list_of_dfs_2_transform_Vpart1[5],list_of_dfs_2_transform_Vpart2[4],list_of_dfs_2_transform_Vpart3[3],df_file6[list_of_non_fts_cols].copy()], axis=1, sort=False)
list_of_dfs_2_transform_stitched.append(df_file6_stitched)
# df7
df_file7_stitched = pd.concat([list_of_dfs_2_transform_Vpart1[6],list_of_dfs_2_transform_Vpart2[5],list_of_dfs_2_transform_Vpart3[4],df_file7[list_of_non_fts_cols].copy()], axis=1, sort=False)
list_of_dfs_2_transform_stitched.append(df_file7_stitched)


# rename the fts in each dataset (to later specify where each common fts is from
list_of_dfs_2_transform_new = []
num_fts_frame_names_changed = 0
for a_full_df_std in list_of_dfs_2_transform_stitched:
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

#>>>> join the datasets by keeping all that you can keep
# make a list of the df with only the fts (this will bee the resulting fts frame after concatenation
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
# >>>> sort the fts cols and make a sorted version of the cols
list_all_cols_df_joined_new_design1 = list(df_joined_new_design1.columns)
list_all_cols_df_joined_new_design1.remove("Y_pCR")
list_all_cols_df_joined_new_design1.remove("cohort")
list_all_cols_df_joined_new_design1_sorted = sorted(list_all_cols_df_joined_new_design1)
list_all_cols_df_joined_new_design1_sorted_plus2 = list_all_cols_df_joined_new_design1_sorted + ["Y_pCR","cohort"]
df_joined_new_design1_ftssorted = df_joined_new_design1.copy()
df_joined_new_design1_ftssorted.columns = list_all_cols_df_joined_new_design1_sorted_plus2


# >>>>>> check the datatypes
df_joined_new_design1_ftssorted.info()
# Index: 233 entries, GSM1030229 to GSM1550523
# Columns: 99593 entries, A1BG-AS1_in_GSE26639 to cohort
# dtypes: float64(99591), int64(1), object(1)
# memory usage: 177.1+ MB
#>>>> saving the df
fullname_file_of_df_joined_new_design1 = "/data_acquisition/1_pipelines_or_tasks/JoinNewDesign1AllFtsof7_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_7cohortname.csv"
df_joined_new_design1_ftssorted.to_csv(fullname_file_of_df_joined_new_design1, header=True) # we keep the index for a future joining w tables of fts
print("File saved !")
#>>>>>>>>>>>>>>
