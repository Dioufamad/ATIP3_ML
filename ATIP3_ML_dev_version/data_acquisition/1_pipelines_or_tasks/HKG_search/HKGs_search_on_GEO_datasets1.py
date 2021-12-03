#---------------------get the HKGs sorted on the stabily list, from a dataset extracted from GEO
#>>>>>>>>>>>>>>>>>>>>>>>>>>> IMPORTS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import pandas as pd
import numpy as np # linear algebra and exploit arrays faster and easier computations
import seaborn as sns
import matplotlib.pyplot as plt
from textwrap import wrap # to wrap plot titles

#>>>>>>>>>>>>>>>>>>>Choosing the environnement values
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

#>>>>>>>>Setting up the environnement values
# # ----for the location of the datasets
# # command_center = "Gustave_Roussy"
# command_center = "Home"
# if command_center == "Gustave_Roussy":
# 	rest_of_abs_path_b4_content_root = "/home/amad/PycharmProjects/ATIP3_in_GR/"
# else : # command_center = "Home"
# 	rest_of_abs_path_b4_content_root = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/"
# print("command center used recognized...")
# ----making the dataset to use when the cohort(s) to manipulate is(are) known
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

#>>>>>>>>>>>>>>>>>>>getting to the HKGs selection
# I - setting criteria 1
# 1-additionnal requirements
# make df with new col as median intensity for all gene
df_file_fts_only_w_median = df_file_fts_only
df_file_fts_only_w_median["median_all_fts"] = df_file_fts_only_w_median.median(axis=1, skipna=True) # axis = 0 means along the column and axis = 1 means working along the row


# 2-make new line as for a gene, top_HKG_criteria_1 (for all samples, Y if sample value > new col val of the sample, else N)
# a dict to collect the Y or N affected for each gene
dict_ft_topHKGcriteria1={}
# make a list of the cols that are fts (genes) to loop on it and affect Y or N
list_of_cols_being_fts = list(df_file_fts_only.columns) # or use list_of_cols_being_fts = list_of_cols[:len(list(df_file_fts_only_w_median.columns))-1]
# keep the number of samples to check for a if the number of times we have a Y by samples is equal to num of samples in order to put the final Y to the gene
num_of_samples = len(df_file_fts_only) #
# lets loop on the genes and attribute the Y or N
for a_ft in list_of_cols_being_fts:
	num_of_samples_w_criteria1_valid = (df_file_fts_only_w_median[a_ft] > df_file_fts_only_w_median['median_all_fts']).sum()
	# dict_ft_topHKGcriteria1[a_ft] = num_of_samples_w_criteria1_valid # to test
	if num_of_samples_w_criteria1_valid == num_of_samples:
		dict_ft_topHKGcriteria1[a_ft]="Y"
	else:
		dict_ft_topHKGcriteria1[a_ft] = "N"
# make a new df with the criteria 1 result as row and the fts as fts
df_crit1_lineonly = pd.DataFrame(dict_ft_topHKGcriteria1, index=['top_HKG_criteria_1'])

# II - setting criteria 2
# 3-make new line as, mean across samples for each gene
df_crit2 = df_file_fts_only[list_of_cols_being_fts] # restart from the df with fts only for the criteria 2
df_crit2.loc["mean"] = df_file_fts_only[list_of_cols_being_fts].mean(axis=0) # axis = 0 means along the column and axis = 1 means working along the row
# make new line as for a gene, sd related to mean
df_crit2.loc["std"] = df_file_fts_only[list_of_cols_being_fts].std(axis=0, skipna=True)
# make new line as for a gene, CV
df_crit2.loc['CV'] = df_crit2.loc['std'] / df_crit2.loc['mean']
# make new line as for a gene, top_HKG_criteria_2 (Y, if CV < 0.35, else N)
dict_ft_topHKGcriteria2={}
# we loop on the list of the fts (already made from previous criteria 1 computations) and attribute a status of criteria 2 following CV < 0.35 or not (Y or N)
for a_ft in list_of_cols_being_fts:
	limit_val_of_CV = 0.35
	if df_crit2.at["CV",a_ft] < limit_val_of_CV:
		dict_ft_topHKGcriteria2[a_ft] = "Y"
	else:
		dict_ft_topHKGcriteria2[a_ft] = "N"
# make a new df with the criteria 2 result as row and the fts as fts
df_crit2_lineonly = pd.DataFrame(dict_ft_topHKGcriteria2, index=['top_HKG_criteria_2'])

# 4-make new line as for a gene, top_HKG_status, (Y, if top_HKG_criteria_1 =Y & top_HKG_criteria_2 =Y, else N)
dict_ft_topHKGstatus={}
# we loop on the list of the fts and attribute the HKG_status Y (both criteria valid) or N
for a_ft in list_of_cols_being_fts:
	if (df_crit1_lineonly.at["top_HKG_criteria_1",a_ft] == "Y") & (df_crit2_lineonly.at["top_HKG_criteria_2",a_ft] == "Y"):
		dict_ft_topHKGstatus[a_ft] = "Y"
	else:
		dict_ft_topHKGstatus[a_ft] = "N"
# the new df with top_HKG_status as row and fts as cols
df_topHKGstatus_lineonly = pd.DataFrame(dict_ft_topHKGstatus, index=['top_HKG_status'])

# 5-get list of cols/genes and df with only top_HKG_status=Y
list_of_cols_being_top_HKGs = []
list_of_cols = list(df_topHKGstatus_lineonly.columns)
for a_ft in list_of_cols:
	if df_topHKGstatus_lineonly.at["top_HKG_status",a_ft] == "Y":
		list_of_cols_being_top_HKGs.append(a_ft)
# the df with only cols as top_HKG_status=Y
df_topHKGs_cols = df_topHKGstatus_lineonly[list_of_cols_being_top_HKGs]
# list_of_cols_being_top_HKGs counts for best probesetsonly (R02 : 4023, R04: x, MDA : x)

# 6-make overall df of results by restricting the df with all fts as cols and the mean std and CV rows (keep only HKGs as cols and rows are mean across samples, sd related to mean, top_HKG_status)
df_mean_sd_CV_of_HKGs = df_crit2[list_of_cols_being_top_HKGs].loc[["mean","std","CV"],:]
# transform cols in rows in previous df, sort rows by the col CV, and add col rank
df_mean_sd_CV_of_HKGs_to_sort = df_mean_sd_CV_of_HKGs.transpose()
df_mean_sd_CV_of_HKGs_sortedOnCV= df_mean_sd_CV_of_HKGs_to_sort.sort_values("CV", axis=0, ascending=True, kind='mergesort') # axis = 0 means along the column and axis = 1 means working along the row
# df3_sorted_cv_then_std = df3.sort_values(["CV","std"], axis=0, ascending=[True,True]) #  not working to order using 2 cols
# change the fts/genes from an index to a col named "HKGs" ("HKGs" here are the HKGs from our 2 criterias)
df_topHKGs_sorted = df_mean_sd_CV_of_HKGs_sortedOnCV.rename_axis('HKers_selected').reset_index() # this column can be named probes or genes so we name it HK_features
# get a new col "rank of CV" with the ranking of CV in ascending
df_topHKGs_sorted['CV_Rank'] = df_topHKGs_sorted['CV'].rank(ascending=1)
df_topHKGs_sorted['CV_Rank'] = df_topHKGs_sorted['CV_Rank'].astype(int) # this is just to make the new col values as int like 132 instead of float like 132.0

# 7 - make a new col HK_features from HKers_selected if HKers_selected is to be changed
if version_of_fts == "fullnames_GS_ACC_probe" :
	# a function to get the short gene name from the long column name
	def full_name_ft2_short_name(full_name):
		list_from_split1 = full_name.split("GSas")
		if len(list_from_split1)==1:
			short_name = "NA"
		else :
			kept_from_list1 = list_from_split1[1]
			list_from_split2 = kept_from_list1.split("wGBANas")
			kept_from_list2 = list_from_split2[0]
			short_name = kept_from_list2
		return short_name
	# get a new col "HKG_GS", remove the rows where "HKG_GS" = "NA", redo the index
	df_topHKGs_sorted["HK_features"] = df_topHKGs_sorted["HKers_selected"].apply(lambda x: full_name_ft2_short_name(x))
elif (version_of_fts == "genesnames") | (version_of_fts == "probesnames") : # 2nd condittion was (version_of_fts == "genesnames") changed into (version_of_fts == "probesnames")
	df_topHKGs_sorted["HK_features"] = df_topHKGs_sorted["HKers_selected"]

# remove the rows with NA in HK_features col
len_b4_removal_NA_as_GS_probes = len(df_topHKGs_sorted)
indexes2drop = df_topHKGs_sorted[df_topHKGs_sorted['HK_features'] == "NA"].index
df_topHKGs_sorted_noNAasGS = df_topHKGs_sorted.drop(indexes2drop , inplace=False)
df_topHKGs_sorted_noNAasGS = df_topHKGs_sorted_noNAasGS.reset_index(drop=True)
len_after_removal_NA_as_GS_probes = len(df_topHKGs_sorted_noNAasGS)
num_probes_wo_GS = len_b4_removal_NA_as_GS_probes - len_after_removal_NA_as_GS_probes
print("Number of HK features which GS is known :", num_probes_wo_GS)
# get the first mentions only, in the CV ranking (for security mesures we rank using the ranks)
df_topHKGs_sorted_1stmentions_only = df_topHKGs_sorted_noNAasGS.sort_values('CV_Rank', ascending=True).drop_duplicates('HK_features').sort_index()
# full resultings dfs of the first mentions (using a corrected rank of CV) (2 dfs : 1 sorted on CV_Rank_no_dup, 1 sorted on alphabetical order of HKG_GS)
df_topHKGs_sorted_1stmentions_only['CV_Rank_no_dup'] = df_topHKGs_sorted_1stmentions_only['CV_Rank'].rank(ascending=1)
df_topHKGs_sorted_1stmentions_only['CV_Rank_no_dup'] = df_topHKGs_sorted_1stmentions_only['CV_Rank_no_dup'].astype(int) # this is just to make the new col values as int like 132 instead of float like 132.0
# restrict to only the needed columns
list_of_cols2keep_in_good_order = ["HK_features","CV","CV_Rank_no_dup"]
df_topHKGs_sorted_1stmentions_only = df_topHKGs_sorted_1stmentions_only[list_of_cols2keep_in_good_order]
# back with the regular scheduled program (making the others tables and all)
df_topHKGs_sorted_1stmentions_only_genesInAlphabetOrder = df_topHKGs_sorted_1stmentions_only.sort_values("HK_features", axis=0, ascending=True, kind='mergesort') # axis = 0 means along the column and axis = 1 means working along the row
# resultings dfs restricted to the top 20 of the first mentions (using a corrected rank of CV) (2 dfs : 1 sorted on CV_Rank_no_dup, 1 sorted on alphabetical order of HKG_GS)
df_topHKGs_sorted_1stmentions_only_top20 = df_topHKGs_sorted_1stmentions_only.head(20)
df_topHKGs_sorted_1stmentions_only_top20_genesInAlphabetOrder = df_topHKGs_sorted_1stmentions_only_top20.sort_values("HK_features", axis=0, ascending=True, kind='mergesort') # axis = 0 means along the column and axis = 1 means working along the row
# save the report df
if cohort_used == "REMAGUS02":
	tag_cohort_name = "R02"
elif cohort_used == "REMAGUS04":
	tag_cohort_name = "R04"
else : # cohort_used == "MDAnderson":
	tag_cohort_name = "MDA"
# make the filenames
ourHKGsCVnoDupRanked_report_filename = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/"+tag_cohort_name+"_"+part_of_probesets_kept+"_"+version_of_fts+"_HKGsCVnoDupRanked_report.csv"
ourHKGsAlphabetOrder_report_filename = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/"+tag_cohort_name+"_"+part_of_probesets_kept+"_"+version_of_fts+"_HKGsAlphabetOrder_report.csv"
ourTop20HKGsCVnoDupRanked_report_filename = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/"+tag_cohort_name+"_"+part_of_probesets_kept+"_"+version_of_fts+"_Top20HKGsCVnoDupRanked_report.csv"
ourTop20HKGsAlphabetOrder_report_filename = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/"+tag_cohort_name+"_"+part_of_probesets_kept+"_"+version_of_fts+"_Top20HKGsAlphabetOrder.csv"
# saving in .csv files
df_topHKGs_sorted_1stmentions_only.to_csv(ourHKGsCVnoDupRanked_report_filename, index=None, header=True)
df_topHKGs_sorted_1stmentions_only_genesInAlphabetOrder.to_csv(ourHKGsAlphabetOrder_report_filename, index=None, header=True)
df_topHKGs_sorted_1stmentions_only_top20.to_csv(ourTop20HKGsCVnoDupRanked_report_filename, index=None, header=True)
df_topHKGs_sorted_1stmentions_only_top20_genesInAlphabetOrder.to_csv(ourTop20HKGsAlphabetOrder_report_filename, index=None, header=True)

# dont use following part (just modify it later when needing to compare with list of genes)
# # >>>>>>>>>>>>>>>>7- summary comparison of our our HKGs vs the top 2O HKGs advised for experiments
# # make a dictionnary keys as cols and values as content of cols to create a summarizing df
# dict_HKGs_advised_for_exp = {}
# # create the 1st column of the future df
# dict_HKGs_advised_for_exp["HKGs_advised"] = ["CALR","ACTG1","GAPDH","RPS27A","ACTB","RPS20","HNRPD","NACA","NONO","UBC",
# 											 "RPL38","RPL11","PTMAP7","GFRA4","RPL7","CDC42","EIF3H","RPS11","RPL26L1","UBE2D3"]
# # create the 2nd column of the future df
# dict_HKGs_advised_for_exp["Mean_Rank"] = list(range(1,21)) # value is a list from 1 to 20, step 1
# # - making the two lists containing positions and names of our HKGs that are similar to one of the advised top 20 HKGs
# # a list as container of lists of positions (1 list in it is for one advised HKG)
# list_of_lists_of_ranks_of_advised_HKGs_found = []
# # a list as container of lists of similar in our HKGs (1 list in it is for one advised HKG)
# list_of_lists_of_similars_of_advised_HKGs_found = []
# # the lists to explore in our HKGs (one is the HKGs and other is their respective CV_Rank_no_dup
# topHKGs_sorted_1stmentions_only_as_list = df_topHKGs_sorted_1stmentions_only['HKG_GS'].tolist()
# CVrank_of_topHKGs_sorted_1stmentions_only_as_list = df_topHKGs_sorted_1stmentions_only['CV_Rank_no_dup'].tolist()
# # for each of the advised HKGs, make the search in our HKGs and keep similars and their ranks
# for an_HKG_advised in dict_HKGs_advised_for_exp["HKGs_advised"]:
# 	list_of_ranks_of_the_advised_HKG=[]
# 	list_of_similars_of_the_advised_HKGs=[]
# 	for one_of_our_top_HKGs_1stmentions in topHKGs_sorted_1stmentions_only_as_list:
# 		if an_HKG_advised in one_of_our_top_HKGs_1stmentions:
# 			index_of_the_top_HKG_where_its_found = topHKGs_sorted_1stmentions_only_as_list.index(one_of_our_top_HKGs_1stmentions)
# 			CVrank_to_keep = CVrank_of_topHKGs_sorted_1stmentions_only_as_list[index_of_the_top_HKG_where_its_found]
# 			list_of_ranks_of_the_advised_HKG.append(CVrank_to_keep) # keep the position in our CVranks
# 			list_of_similars_of_the_advised_HKGs.append(one_of_our_top_HKGs_1stmentions)  # keep the similar HKG where the advised HKG has been found
# 	# keep all the list of all positions where the advised HKG has been found in our CVranks
# 	list_of_lists_of_ranks_of_advised_HKGs_found.append(list_of_ranks_of_the_advised_HKG)
# 	# keep all the list of similars HKGs where the advised HKG has been found in our CVranks
# 	list_of_lists_of_similars_of_advised_HKGs_found.append(list_of_similars_of_the_advised_HKGs)
#
# # create the 3rd column of the future df
# dict_HKGs_advised_for_exp["CvrankNoDup_where_advised_HKG_been_found"] = list_of_lists_of_ranks_of_advised_HKGs_found
# # create the 4th column of the future df
# dict_HKGs_advised_for_exp["Similar_HKGs_where_advised_HKG_been_found"] = list_of_lists_of_similars_of_advised_HKGs_found
# # create the report df on the advised HKGs positions
# df_HKGs_advised_for_exp = pd.DataFrame(dict_HKGs_advised_for_exp)
# # save the report df
# if cohort_used == "REMAGUS02":
# 	name_report = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/R02_advised_HKGs_report.csv"
# elif cohort_used == "REMAGUS04":
# 	name_report = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/R04_advised_HKGs_report.csv"
# else : # cohort_used == "MDAnderson":
# 	name_report = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/MDA_advised_HKGs_report.csv"
#
# df_HKGs_advised_for_exp.to_csv(name_report, index=None, header=True)
#
# # END OF PART>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
