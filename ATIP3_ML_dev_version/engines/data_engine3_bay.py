###--------------------- This is the location of some functions to keep the datasets calls, paths, and manipulations at bay... in a bay-----------------------

###---------------------IMPORTS
import pandas as pd # for dataframes manipulation
import numpy as np
import locale
#====================================================================

# ---------------------Variables to initialise------------------------------------------
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') #for setting the characters format
#====================================================================


# >>>>>>>>>>>>> Library of links for datasets frequently used in the ATIP3 projects when called for learning tasks and datasets fusion/making

def local_link_to_csv_dataset_getter(tag_cohort): # you give it a specific string as the tag of a cohort and it gives you back the link to the dataset you want
	# - the general folder where the datasets are stored :
	source_base_folder_for_singletask_datasets ="/home/amad/PALADIN_2/3CEREBRO/garage/projects/ATIP3_ML/ATIP3_ML_dev_version/data_warehouse/outputs/atip3_ml_dataset_type1/"
	source_base_folder_for_multitask_datasets ="/home/amad/PALADIN_2/3CEREBRO/garage/projects/ATIP3_ML/ATIP3_ML_dev_version/data_warehouse/outputs/atip3_unified_datasets/"


	# - links for the datasets, each one for a specific tag_cohort
	if tag_cohort == "GSE41998" : # dt1
		filepath_of_ml_dataset = source_base_folder_for_singletask_datasets + "GSE41998_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
	elif tag_cohort == "GSE26639" : # dt2
		filepath_of_ml_dataset = source_base_folder_for_singletask_datasets + "GSE26639_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
	elif tag_cohort == "GSE32646" : # dt3
		filepath_of_ml_dataset= source_base_folder_for_singletask_datasets + "GSE32646_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
	elif tag_cohort == "GSE25055" : # dt4
		filepath_of_ml_dataset= source_base_folder_for_singletask_datasets + "GSE25055_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
	elif tag_cohort == "GSE20194" : # dt5
		filepath_of_ml_dataset= source_base_folder_for_singletask_datasets + "GSE20194_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
	elif tag_cohort == "GSE23988" : # to not use (cohort with too low number of samples : 4)-----------------<<<<<<<<<< ##! dt6
		filepath_of_ml_dataset= source_base_folder_for_singletask_datasets + "GSE23988_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
	elif tag_cohort == "GSE63471" : # dt7
		filepath_of_ml_dataset= source_base_folder_for_singletask_datasets + "GSE63471_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"

	# the joined datasets following a specific design
	elif tag_cohort == "JoinNewDesign1CommonFtsof6":  # idea of MT dataset 1 # never approved
		filepath_of_ml_dataset = source_base_folder_for_multitask_datasets + "JoinNewDesign1CommonFtsof6_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"
	elif tag_cohort == "JoinNewDesign2CommonFtsof6": # idea of MT dataset 2 # used in the MT spams trial 1 for L1
		filepath_of_ml_dataset = source_base_folder_for_multitask_datasets + "JoinNewDesign2CommonFtsof6_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"
	elif tag_cohort == "JoinNewDesign2CommonFtsof3oftop4FSsL1": # branching 1 of idea of MT dataset 2 # proposed while in the analysis of the signature from L1 MT # used in the L1 MT of 3 from top4 FSs of L1 run 1
		filepath_of_ml_dataset = source_base_folder_for_multitask_datasets + "JoinNewDesign2CommonFtsof3oftop4FSsL1_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"
	elif tag_cohort == "JoinNewDesign2AllFtsof6": # idea of MT dataset 3 for spams trials # never approved
		filepath_of_ml_dataset = source_base_folder_for_multitask_datasets + "JoinNewDesign2AllFtsof6_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"

	# the datasets created by using the JoinNewDesign1 and a feature selection on it
	elif tag_cohort == "JoinNewDesign1CommonFtsof6_FSidea1thinking1or3" :
		filepath_of_ml_dataset = source_base_folder_for_multitask_datasets + "JoinNewDesign1CommonFtsof6_FSidea1thinking1or3_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"
	elif tag_cohort == "JoinNewDesign1CommonFtsof6_FSidea1thinking2ptfU133A2" :
		filepath_of_ml_dataset= source_base_folder_for_multitask_datasets + "JoinNewDesign1CommonFtsof6_FSidea1thinking2ptfU133A2_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"
	elif tag_cohort == "JoinNewDesign1CommonFtsof6_FSidea1thinking2ptfU133plus2" :
		filepath_of_ml_dataset= source_base_folder_for_multitask_datasets + "JoinNewDesign1CommonFtsof6_FSidea1thinking2ptfU133plus2_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"
	elif tag_cohort == "JoinNewDesign1CommonFtsof6_FSidea1thinking2ptfU133A" :
		filepath_of_ml_dataset= source_base_folder_for_multitask_datasets + "JoinNewDesign1CommonFtsof6_FSidea1thinking2ptfU133A_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"
	elif tag_cohort == "JoinNewDesign1CommonFtsof6_FSidea2thinking1UTttest" :
		filepath_of_ml_dataset= source_base_folder_for_multitask_datasets + "JoinNewDesign1CommonFtsof6_FSidea2thinking1UTttest_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"

	# in the event where what has been supplied as tag_cohort is not recognized among what is available
	else :
		filepath_of_ml_dataset = ""
		print("Warning ! tag_cohort supplied for dataset file selection is not related to an existing file. ")
	# use this to create new entry faster
	# elif tag_cohort == "" : # not created yet
	# 	filepath_of_ml_dataset= ""
	return filepath_of_ml_dataset

# >>>>>>>>>>>>>>>>>>>>>> a function to use a given link and summon the dataset in almost all forms it will be need

def dataset_summoner(local_link_to_csv_dataset,resp_values_type,add_intercept="yes"):

	df = pd.read_csv(local_link_to_csv_dataset, sep=",")  # read the dataset in a df and an option is "sep_in_file = ","" to precise what was the separator in the file
	# - when the first column was kept because it was the previous index, we can put it back as index with this
	df.rename(columns={"Unnamed: 0": "samples_names"}, inplace=True)
	df = df.set_index(list(df.columns)[0])
	# - including or not a column at the first position for the intercept
	if add_intercept == "yes":
		df.insert(0, '_SyntheticFeat4Intercept', 1.0) # a column filled with value 1 on all its rows in inserted at first position # also 1 is put as 1.0 to stay in the floats theme of all the fts values
	# - lets separate our data
	# a df of the input (fts gallery)...
	df_input = df.drop(['Y_pCR', 'cohort'], axis=1)  # same as doing df_input = df.iloc[:, :-2] # recommended to use iloc to produce a slice # :-1 means all except the last one
	# ...and its array version
	X = np.array(df_input)  # same as X = df_input.values but with a possibility to force values to be floats
	# a df of the output (response column)...
	df_output = df['Y_pCR']
	# df_output = df['Y_pCR'] is a series here that has same content that the df df_ouput = df.iloc[:,-2] # -1 means select the last one only and it is the cohort (not a value analysed)
	# (correct later to get a real df with df_output = df[['Y_pCR']]) #  for solution, see (https://stackoverflow.com/questions/11285613/selecting-multiple-columns-in-a-pandas-dataframe)
	# ...and its array version
	if resp_values_type == "resp_val_type_as_float":
		y = np.array(df_output, dtype='float')  # same as  y = df_ouput.values but with a possibility to force values to be floats
	else: # leave the response values as ints
		y = np.array(df_output)
	# # get the list of the cohorts that were used to build the dataset  ## not needed
	# df_cohort_col = df['cohort']    # same as if column 'cohort' is the last column df.iloc[:, -1]
	# list_of_cohorts_used = list(df_cohort_col.unique())

	# - the list of the features in the same setup as input
	list_all_fts_df_input = list(df_input.columns)

	return df_input, df_output, X, y, list_all_fts_df_input


# >>>>>>>>>>>>>>>>>>>>>> same as previous dataset summoner (a function to use a given link and summon the dataset in almost all forms it will be need)
# but this difference is : a column is added at the start, filled with 1 value and it is the version od dataset to use for an intercept (1st coef is the intercept)