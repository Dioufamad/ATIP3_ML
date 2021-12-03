#---------------------to get the normalised values of a gene and compare it following limits
#>>>>>>>>>>>>>>>>>>>>>>>>>>> IMPORTS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import pandas as pd
import numpy as np # linear algebra and exploit arrays faster and easier computations
import seaborn as sns
import matplotlib.pyplot as plt
from textwrap import wrap # to wrap plot titles

#>>>>>>>>>>>>>>>>>>>Choosing environnement values
# ----for the cohorts to implicate
# cohort_used = "REMAGUS02"
# cohort_used = "REMAGUS04"
cohort_used = "MDAnderson"
# ----Setting the type of probesets to kept
# part_of_probesets_kept = "allprobesets"
part_of_probesets_kept = "bestprobesetsonly"
# part_of_probesets_kept = "CDFsummarized"
# ----for the version of files to use
# version_of_fts = "probesnames"
version_of_fts = "genesnames"
# version_of_fts = "fullnames_GS_ACC_probe"
# the idea is to do it for 4 HKGs but we have the common HKGs also. Decision : Do it for the first 4 common HKGs and each first in a cohort
# ----choosing the pool where the HKG has been remarked
# std_ft_sourcepool = "common"
# std_ft_sourcepool = "R02"
# std_ft_sourcepool = "R04"
std_ft_sourcepool = "MDA"
# ----choosing the rank of the HKG in the pool where it has been remarked
# std_ft_rank = 1
# std_ft_rank = 2
# std_ft_rank = 3
std_ft_rank = 4

#>>>>>>>>>>>>>>>>>>>Setting environnement values
# ----Setting the standard feature

# >>>>>>>Task 3 : restrict the dataset to MTUS1 and one the 5 best HKG
#----paths to files of populations in cohorts
if part_of_probesets_kept == "allprobesets":
	file_path_R02 = "/data_warehouse/inputs/atip3_material/datasets_to_process_folder/R02_R04_MDA_GEOdatasets/allprobesets/Remagus02_GSE26639_allprobesets_probesnames_54675x226_GEX.csv"
	file_path_R04 = "/data_warehouse/inputs/atip3_material/datasets_to_process_folder/R02_R04_MDA_GEOdatasets/allprobesets/Remagus04_GSE63471_allprobesets_probesnames_22277x142_GEX.csv"
	file_path_MDA = "/data_warehouse/inputs/atip3_material/datasets_to_process_folder/R02_R04_MDA_GEOdatasets/allprobesets/MDAnderson_GSE25066_allprobesets_probesnames_22283x508_GEX.csv"
elif part_of_probesets_kept == "bestprobesetsonly":
	if version_of_fts == "probesnames": # to change later when got time to produce these versions of files
		file_path_R02 = "/data_warehouse/inputs/atip3_material/datasets_to_process_folder/R02_R04_MDA_GEOdatasets/bestprobesetsonly/probenames/Remagus02_GSE26639_bestprobesetsonly_probesnames_16814x226_GEX.csv"
		file_path_R04 = "/data_warehouse/inputs/atip3_material/datasets_to_process_folder/R02_R04_MDA_GEOdatasets/bestprobesetsonly/probenames/Remagus04_GSE63471_bestprobesetsonly_probesnames_12151x142_GEX.csv"
		file_path_MDA = "/data_warehouse/inputs/atip3_material/datasets_to_process_folder/R02_R04_MDA_GEOdatasets/bestprobesetsonly/probenames/MDAnderson_GSE25066_bestprobesetsonly_probesnames_12151x508_GEX.csv"
	elif version_of_fts == "genesnames":
		file_path_R02 = "/data_warehouse/inputs/atip3_material/datasets_to_process_folder/R02_R04_MDA_GEOdatasets/bestprobesetsonly/genenames/Remagus02_GSE26639_bestprobesetsonly_genesnames_16814x226_GEX.csv"
		file_path_R04 = "/data_warehouse/inputs/atip3_material/datasets_to_process_folder/R02_R04_MDA_GEOdatasets/bestprobesetsonly/genenames/Remagus04_GSE63471_bestprobesetsonly_genesnames_12151x142_GEX.csv"
		file_path_MDA = "/data_warehouse/inputs/atip3_material/datasets_to_process_folder/R02_R04_MDA_GEOdatasets/bestprobesetsonly/genenames/MDAnderson_GSE25066_bestprobesetsonly_genesnames_12151x508_GEX.csv"
elif part_of_probesets_kept == "CDFsummarized":
	file_path_R02 = ""
	file_path_R04 = ""
	file_path_MDA = ""

#---making the base dataset to use
sep_in_file = ","
if cohort_used == "REMAGUS02":
	df_file_R02 = pd.read_csv(file_path_R02, sep_in_file)
	df_file = df_file_R02
elif cohort_used == "REMAGUS04":
	df_file_R04 = pd.read_csv(file_path_R04, sep_in_file)
	df_file = df_file_R04
else : # cohort_used == "MDAnderson":
	df_file_MDA = pd.read_csv(file_path_MDA, sep_in_file)
	df_file = df_file_MDA


#>>>>>>>>>>>>>>>>>>>set up the df_file as it should (samples as rows and genes as fts)
# put the rownames (genes) as index
df_file = df_file.set_index(list(df_file.columns)[0]) # because a csv from R has the rownames becoming the first col
# transform the df to pu the genes as colnames
df_file_fts_only = df_file.transpose()
# remove the cols that are nan
list_good_cols = [i for i in list(df_file_fts_only.columns) if str(i) != 'nan']
df_file_fts_only = df_file_fts_only[list_good_cols]
# now we have the good setup  : kept all the cols except the responses (only fts and model remains)


#####-----checkpoint
print("----A checkpoint to check on joined table dtypes (first 5 columns and last 5 columns) in order to know what dtypes to convert...")
df_joined_preview = df_file_fts_only.iloc[:, list(range(6)) + [-5, -4, -3, -2, -1]]
print(df_joined_preview.info())  # on the model of df_joined[df_joined.columns[:10]].dtypes
####-----

#>>>>>>>>>>>>>>>>>>>making the restrictions to columns (genes) to use
# - find the std_ft name
# state the file already ordorered with std_ft in the first line
if std_ft_sourcepool == "common":
	file_path_full_info_HKGs = "/data_warehouse/inputs/atip3_material/datasets_to_process_folder/R02_R04_MDA_GEOdatasets/HKGs_bestprobesetsonly/common_to_R02_R04_MDA/HKGs_common_to_cohorts_MeanCVNoDup_sorted_report.csv"
elif std_ft_sourcepool == "R02":
	file_path_full_info_HKGs = "/data_warehouse/inputs/atip3_material/datasets_to_process_folder/R02_R04_MDA_GEOdatasets/HKGs_bestprobesetsonly/common_to_R02_R04_MDA/HKGs_common_to_cohorts_1cohort_R02_sorted_report.csv"
elif std_ft_sourcepool == "R04":
	file_path_full_info_HKGs = "/data_warehouse/inputs/atip3_material/datasets_to_process_folder/R02_R04_MDA_GEOdatasets/HKGs_bestprobesetsonly/common_to_R02_R04_MDA/HKGs_common_to_cohorts_1cohort_R04_sorted_report.csv"
elif std_ft_sourcepool == "MDA":
	file_path_full_info_HKGs = "/data_warehouse/inputs/atip3_material/datasets_to_process_folder/R02_R04_MDA_GEOdatasets/HKGs_bestprobesetsonly/common_to_R02_R04_MDA/HKGs_common_to_cohorts_1cohort_MDA_sorted_report.csv"
# load the file with HKGS full info (even info on common HKGS)
df_file_full_info_HKGs = pd.read_csv(file_path_full_info_HKGs, sep_in_file)
# get the std_ft name (entry 0 of col HK_features_common_to_cohorts)
std_ft = df_file_full_info_HKGs['HK_features_common_to_cohorts'].iloc[std_ft_rank-1]
# print("The std ft that will be used for normalisation is :",std_ft) # done later at the end
# list of cols to restrict on
list_of_cols_to_use = ["MTUS1",std_ft]
# restricting...
df_file_fts_only_restricted = df_file_fts_only[list_of_cols_to_use]

# Task 4 : make the normalised values column
df_file_fts_only_restricted['MTUS1_dividedby_std_ft'] = df_file_fts_only_restricted['MTUS1']/df_file_fts_only_restricted[std_ft]
# Task 5 : make the median value column
df_file_fts_only_restricted["median_MTUS1_dividedby_std_ft"] = df_file_fts_only_restricted['MTUS1_dividedby_std_ft'].median(axis=0, skipna=True) # axis = 0 means along the column and axis = 1 means working along the row
# Task 6 : make the columns of median/2 and medianx2
df_file_fts_only_restricted['median_dividedby_2'] = df_file_fts_only_restricted['median_MTUS1_dividedby_std_ft']/2
df_file_fts_only_restricted['median_times_2'] = df_file_fts_only_restricted['median_MTUS1_dividedby_std_ft']*2
# Task 7 : make the columns of median/3 and medianx3
df_file_fts_only_restricted['median_dividedby_3'] = df_file_fts_only_restricted['median_MTUS1_dividedby_std_ft']/3
df_file_fts_only_restricted['median_times_3'] = df_file_fts_only_restricted['median_MTUS1_dividedby_std_ft']*3
# Task 8 : make the column of predicted ATIP3 status from median (following low if MTUS1 < median/2, high if MTUS1 > medianx2 and med otherwise)
df_file_fts_only_restricted['Predicted_classes_med_and_2'] = "med" # intialise the col with the middle value...
df_file_fts_only_restricted.loc[df_file_fts_only_restricted['MTUS1_dividedby_std_ft'] < df_file_fts_only_restricted['median_dividedby_2'], 'Predicted_classes_med_and_2'] = "low" # ...and change it
df_file_fts_only_restricted.loc[df_file_fts_only_restricted['MTUS1_dividedby_std_ft'] > df_file_fts_only_restricted['median_times_2'], 'Predicted_classes_med_and_2'] = "high"
# Task 9 : make the column of predicted ATIP3 status from median (following low if < median/2, high if > medianx2 and med otherwise)
df_file_fts_only_restricted['Predicted_classes_med_and_3'] = "med" # intialise the col with the middle value...
df_file_fts_only_restricted.loc[df_file_fts_only_restricted['MTUS1_dividedby_std_ft'] < df_file_fts_only_restricted['median_dividedby_3'], 'Predicted_classes_med_and_3'] = "low" # ...and change it
df_file_fts_only_restricted.loc[df_file_fts_only_restricted['MTUS1_dividedby_std_ft'] > df_file_fts_only_restricted['median_times_3'], 'Predicted_classes_med_and_3'] = "high"
# Task 10 : get count of ATIP3 low numbers
count_class_low_with_med_and_2=df_file_fts_only_restricted.loc[df_file_fts_only_restricted['Predicted_classes_med_and_2'] == "low", 'Predicted_classes_med_and_2'].shape[0]
count_class_med_with_med_and_2=df_file_fts_only_restricted.loc[df_file_fts_only_restricted['Predicted_classes_med_and_2'] == "med", 'Predicted_classes_med_and_2'].shape[0]
count_class_high_with_med_and_2=df_file_fts_only_restricted.loc[df_file_fts_only_restricted['Predicted_classes_med_and_2'] == "high", 'Predicted_classes_med_and_2'].shape[0]
count_class_low_with_med_and_3=df_file_fts_only_restricted.loc[df_file_fts_only_restricted['Predicted_classes_med_and_3'] == "low", 'Predicted_classes_med_and_3'].shape[0]
count_class_med_with_med_and_3=df_file_fts_only_restricted.loc[df_file_fts_only_restricted['Predicted_classes_med_and_3'] == "med", 'Predicted_classes_med_and_3'].shape[0]
count_class_high_with_med_and_3=df_file_fts_only_restricted.loc[df_file_fts_only_restricted['Predicted_classes_med_and_3'] == "high", 'Predicted_classes_med_and_3'].shape[0]
# Task 11 : display the summary of ATIP3 numbers
print("Summary of the method only : ")
print("The std ft that will be used for normalisation is :",std_ft)
print("- With median and 2, predicted classes numbers : low (",count_class_low_with_med_and_2,"), med (",count_class_med_with_med_and_2,"), high (",count_class_high_with_med_and_2,")")
print("- With median and 3, predicted classes numbers : low (",count_class_low_with_med_and_3,"), med (",count_class_med_with_med_and_3,"), high (",count_class_high_with_med_and_3,")")
# Task  12 : get the min of MTUS1_dividedby_std_ft, the min of median_dividedby_2, median_dividedby_3 to explain the lack of ATIP3 samples if its the case
print("Situation of MTUS1_dividedby_std_ft and lower limits values : ")
print("- minimum of MTUS1_dividedby_std_ft : ",df_file_fts_only_restricted["MTUS1_dividedby_std_ft"].min(axis = 0))
print("- median_dividedby_2 is : ",df_file_fts_only_restricted["median_dividedby_2"].min(axis = 0))
print("- median_dividedby_3 is : ",df_file_fts_only_restricted["median_dividedby_3"].min(axis = 0))


# Task 13 : import and add the data about a previous grouping (sylvie's work) (done only if the cohort has correspondance of GEO sample names with Sylvie work sample names
if cohort_used in ["REMAGUS02","MDAnderson"]:
	# - in a copy of the results table, lets make a GSM_sample_name col from index
	df_file_fts_only_restricted_w_corresp = df_file_fts_only_restricted.rename_axis('GSM_sample_name').reset_index()
	# - state the proper file part to use
	file_path_previous_grouping = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/3_results/res_clustering/Clustering pour Amad 180520.xls"
	# sep_in_file = "\t" # not needed
	if cohort_used == "REMAGUS02":
		sheet_id = "R02"
	elif cohort_used == "MDAnderson":
		sheet_id = "MDA"
	else: # when no cohort is chosen
		sheet_id = "Unknown"
	# - load the file with HKGS full info (even info on common HKGS)
	df_previous_grouping = pd.read_excel(file_path_previous_grouping,sheet_id)
	# - rename the samples col and change it to str
	df_previous_grouping.rename(columns={df_previous_grouping.columns[0]:'sample_names_sylvie'}, inplace=True)
	df_previous_grouping[df_previous_grouping.columns[0]] = df_previous_grouping[df_previous_grouping.columns[0]].astype(str)
	# - rename last column with a more manageable name
	df_previous_grouping.rename(columns={df_previous_grouping.columns[-1]:'ATIP3_classes'}, inplace=True)
	# - join with a corresponding table
	if cohort_used == "REMAGUS02":
		filename_corresponding_table_for_names = "/data_warehouse/inputs/atip3_material/Sample_Names_correspondance/R02 pour Amad.xlsx"
		df_corresponding_table_for_names = pd.read_excel(filename_corresponding_table_for_names)
		df_corresponding_table_for_names["cletri"] = df_corresponding_table_for_names["cletri"].astype(str)
		df_joined_previous_grouping_corresponding_table = pd.merge(df_corresponding_table_for_names, df_previous_grouping, how="inner", left_on="cletri", right_on="sample_names_sylvie")
		df_joined_previous_grouping_corresponding_table = df_joined_previous_grouping_corresponding_table[["!Sample_geo_accession","ATIP3_classes"]]
		df_joined_previous_grouping_corresponding_table.rename(columns={df_joined_previous_grouping_corresponding_table.columns[0]: 'GSM_sample_name1'}, inplace=True)
	elif cohort_used == "MDAnderson":
		filename_corresponding_table_for_names = "/data_warehouse/inputs/atip3_material/Sample_Names_correspondance/MDA_pour_moi.csv"
		sep_in_file = ","
		df_corresponding_table_for_names = pd.read_csv(filename_corresponding_table_for_names, sep_in_file)
		df_corresponding_table_for_names["Title"] = df_corresponding_table_for_names["Title"].astype(str)
		df_corresponding_table_for_names.loc[df_corresponding_table_for_names['Title'] == "PERU12_14", 'Title'] = "PERU14"
		df_corresponding_table_for_names.loc[df_corresponding_table_for_names['Title'] == "PERU14_16", 'Title'] = "PERU16"
		df_joined_previous_grouping_corresponding_table = pd.merge(df_corresponding_table_for_names, df_previous_grouping, how="inner", left_on="Title", right_on="sample_names_sylvie")
		df_joined_previous_grouping_corresponding_table = df_joined_previous_grouping_corresponding_table[["Accession", "ATIP3_classes"]]
		df_joined_previous_grouping_corresponding_table.rename(columns={df_joined_previous_grouping_corresponding_table.columns[0]: 'GSM_sample_name1'}, inplace=True)
	# join our previous results restricted table with the joined with ATIP3_classes
	df_file_fts_only_restricted_w_corresp = pd.merge(df_file_fts_only_restricted_w_corresp, df_joined_previous_grouping_corresponding_table, how="inner", left_on="GSM_sample_name", right_on="GSM_sample_name1")
	# remove the GSM_sample_name1 col
	df_file_fts_only_restricted_w_corresp = df_file_fts_only_restricted_w_corresp.drop(['GSM_sample_name1'], axis=1)
	# make a column for to mark the samples that same low as in Sylvie's work
	df_file_fts_only_restricted_w_corresp['Same_ATIP3_low_than_Sylvie_w_med_and_2'] = "different_from_Sylvie_work" # intialise the col
	df_file_fts_only_restricted_w_corresp.loc[(df_file_fts_only_restricted_w_corresp['Predicted_classes_med_and_2'] == "low") & (df_file_fts_only_restricted_w_corresp['ATIP3_classes'] == 1), 'Same_ATIP3_low_than_Sylvie_w_med_and_2'] = "low_as_in_Sylvie_work"
	df_file_fts_only_restricted_w_corresp['Same_ATIP3_low_than_Sylvie_w_med_and_3'] = "different_from_Sylvie_work" # intialise the col
	df_file_fts_only_restricted_w_corresp.loc[(df_file_fts_only_restricted_w_corresp['Predicted_classes_med_and_3'] == "low") & (df_file_fts_only_restricted_w_corresp['ATIP3_classes'] == 1), 'Same_ATIP3_low_than_Sylvie_w_med_and_3'] = "low_as_in_Sylvie_work"
	# sort on the col ATIP3 classes (it is just to check very fast)
	df_file_fts_only_restricted_w_corresp = df_file_fts_only_restricted_w_corresp.sort_values('ATIP3_classes', ascending=True)
	df_file_fts_only_restricted_w_corresp = df_file_fts_only_restricted_w_corresp.reset_index(drop=True)
	# make the counts
	count_low_as_in_Sylvie_work_with_med_and_2=df_file_fts_only_restricted_w_corresp.loc[df_file_fts_only_restricted_w_corresp['Same_ATIP3_low_than_Sylvie_w_med_and_2'] == "low_as_in_Sylvie_work", 'Same_ATIP3_low_than_Sylvie_w_med_and_2'].shape[0]
	count_low_as_in_Sylvie_work_with_med_and_3=df_file_fts_only_restricted_w_corresp.loc[df_file_fts_only_restricted_w_corresp['Same_ATIP3_low_than_Sylvie_w_med_and_3'] == "low_as_in_Sylvie_work", 'Same_ATIP3_low_than_Sylvie_w_med_and_3'].shape[0]
	# make a summary
	print("Summary of the correspondance with Sylvie's results on ATIP3 low samples: ")
	print("- With median and 2, comparing with Sylvie's work, same ATIP3 low samples number is :",count_low_as_in_Sylvie_work_with_med_and_2)
	print("- With median and 3, comparing with Sylvie's work, same ATIP3 low samples number is :",count_low_as_in_Sylvie_work_with_med_and_3)
else: # cohort is Remagus04 that does not have a correspondance file for samples names
	print("The analysed cohort does not have correspondance file in order to compare predicted classes with previously obtained ones")







