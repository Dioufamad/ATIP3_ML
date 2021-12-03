#----------get the mean limits
#---------------------get the HKGs
#>>>>>>>>>>>>>>>>>>>>>>>>>>> IMPORTS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import pandas as pd
import numpy as np # linear algebra and exploit arrays faster and easier computations
from math import sqrt # need to compute mcc
import seaborn as sns
import matplotlib.pyplot as plt
from textwrap import wrap # to wrap plot titles

#>>>>>>>>>>>>>>>>>>>Choosing the environnement values
# ----for the task to do
task_2do = "select_cols_based_on_medians"
# ----for the response strategy
resp_used = "RCH3HSall"
resp_used_in_full = "All the samples with -defined or not RCH and 3 hormonals status, are kept"
# resp_used = "RCH3HSdefined"
# resp_used_in_full = "Only defined -RCH and the 3 hormonals status- samples are kept"
# resp_used = "RCHdefined"
# resp_used_in_full = "Only defined RCH samples are kept"
# resp_used = "TNBCdefined"
# resp_used_in_full = "Only defined TNBC samples are kept"
# resp_used = "RCHandTNBCdefined"
# resp_used_in_full = "Only defined RCH and TNBC samples are kept"
print("For population restriction, the response strategy chosen is",resp_used_in_full,"(",resp_used,")...")
# ----for the cohorts to implicate
cohort_used = "REMAGUS02"
# cohort_used = "REMAGUS04"
# cohort_used = "MDAnderson"
# ----for the origin of the top 20 HKGs to use to compute Std in the cohort we are predicting on
origin_of_top20_HKGs = "the_cohort_only"
# origin_of_top20_HKGs = "common_to_cohorts"
# ----for the Ath origin in terms of top20 HKGs
# ath_top20_aspect_origin = "the_cohort_only"
ath_top20_aspect_origin = "common_to_cohorts"
# ----for the Ath to use to predict
# ath_origin = "Aexp_R02"
ath_origin = "Aexp_R04"
# ath_origin = "Aexp_MDA"
if ath_origin == "Aexp_R02":
	if ath_top20_aspect_origin == "the_cohort_only":
		ath_mtus1_probe1 = 0.321904360625095
		ath_mtus1_probe2 = 0.350056987276414
		ath_mtus1_probe3 = 0.653212849897016
		ath_mtus1_probe4 = 0.50194726128412
	else: # ath_top20_aspect_origin == "common_to_cohorts"
		ath_mtus1_probe1 = 0.313928929360514
		ath_mtus1_probe2 = 0.340353034010916
		ath_mtus1_probe3 = 0.635712177457833
		ath_mtus1_probe4 = 0.488092284240476
elif ath_origin == "Aexp_R04":
	if ath_top20_aspect_origin == "the_cohort_only":
		ath_mtus1_probe1 = 0.439682035430134
		ath_mtus1_probe2 = 0.241507440470879
		ath_mtus1_probe3 = 0.715313199384631
	else:  # ath_top20_aspect_origin == "common_to_cohorts"
		ath_mtus1_probe1 = 0.419447546923098
		ath_mtus1_probe2 = 0.230393091612411
		ath_mtus1_probe3 = 0.682393963333242
else: # ath_origin == "Aexp_MDA"
	if ath_top20_aspect_origin == "the_cohort_only":
		ath_mtus1_probe1 = 0.600719188222076
		ath_mtus1_probe2 = 0.613977067098925
		ath_mtus1_probe3 = 0.613038636134454
	else:  # ath_top20_aspect_origin == "common_to_cohorts"
		ath_mtus1_probe1 = 0.603200908099517
		ath_mtus1_probe2 = 0.620596077841658
		ath_mtus1_probe3 = 0.613071962822774

# ----a list to go over for the probe to use to compute Mg
if cohort_used == "REMAGUS02":
	list_mtus1_probe_2_focus_on = ["GSasMTUS1wGBANasAI695017wPSIas212093_s_at", "GSasMTUS1wGBANasBE552421wPSIas212095_s_at", "GSasMTUS1wGBANasAL096842wPSIas212096_s_at", "GSasMTUS1wGBANasAI028661wPSIas239576_at"]
else:
	list_mtus1_probe_2_focus_on = ["GSasMTUS1wGBANasAI695017wPSIas212093_s_at", "GSasMTUS1wGBANasBE552421wPSIas212095_s_at", "GSasMTUS1wGBANasAL096842wPSIas212096_s_at"]
#>>>>>>>>Setting up the environnement values
# ----for the location of the datasets
# command_center = "Gustave_Roussy"
command_center = "Home"
if command_center == "Gustave_Roussy":
	rest_of_abs_path_b4_content_root = "/home/amad/PycharmProjects/ATIP3_in_GR/"
else : # command_center = "Home"
	rest_of_abs_path_b4_content_root = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/"
print("command center used recognized...")
# ----making the dataset to use when the cohort(s) to manipulate is(are) known
#----paths to files of populations in cohorts
R02_ds_folder_path = rest_of_abs_path_b4_content_root + "ATIP3_ML/ATIP3_ML_dev_version/atip3_material/datasets_to_process_folder/R02/"
R04_ds_folder_path = rest_of_abs_path_b4_content_root + "ATIP3_ML/ATIP3_ML_dev_version/atip3_material/datasets_to_process_folder/R04/"
MDA_ds_folder_path = rest_of_abs_path_b4_content_root + "ATIP3_ML/ATIP3_ML_dev_version/atip3_material/datasets_to_process_folder/MDA/"
if resp_used == "RCH3HSall":
	file_path_R02 = R02_ds_folder_path + "BRCA_Treatment11_REMAGUS02xNACx226Sx54675Fx4RasRCH3HSall_GEX.csv"
	file_path_R04 = R04_ds_folder_path + "BRCA_Treatment12_REMAGUS04xNACx142Sx22277Fx4RasRCH3HSall_GEX.csv"
	file_path_MDA = MDA_ds_folder_path + "BRCA_Treatment13_MDAndersonxNACx133Sx22283Fx4RasRCH3HSall_GEX.csv"
elif resp_used == "RCH3HSdefined":
	file_path_R02 = R02_ds_folder_path + "BRCA_Treatment11_REMAGUS02xNACx218Sx54675Fx4RasRCH3HSdefined_GEX.csv"
	file_path_R04 = R04_ds_folder_path + "BRCA_Treatment12_REMAGUS04xNACx139Sx22277Fx4RasRCH3HSdefined_GEX.csv"
	file_path_MDA = MDA_ds_folder_path + "BRCA_Treatment13_MDAndersonxNACx129Sx22283Fx4RasRCH3HSdefined_GEX.csv"
elif resp_used == "RCHdefined":
	file_path_R02 = R02_ds_folder_path + "BRCA_Treatment11_REMAGUS02xNACx221Sx54675Fx1RasRCHdefined_GEX.csv"
	file_path_R04 = R04_ds_folder_path + "BRCA_Treatment12_REMAGUS04xNACx139Sx22277Fx1RasRCHdefined_GEX.csv"
	file_path_MDA = MDA_ds_folder_path + "BRCA_Treatment13_MDAndersonxNACx133Sx22283Fx1RasRCHdefined_GEX.csv"
elif resp_used == "TNBCdefined":
	file_path_R02 = R02_ds_folder_path + "BRCA_Treatment11_REMAGUS02xNACx226Sx54675Fx1RasTNBCdefined_GEX.csv"
	file_path_R04 = R04_ds_folder_path + "BRCA_Treatment12_REMAGUS04xNACx142Sx22277Fx1RasTNBCdefined_GEX.csv"
	file_path_MDA = MDA_ds_folder_path + "BRCA_Treatment13_MDAndersonxNACx133Sx22283Fx1RasTNBCdefined_GEX.csv"
else:  # resp_used == "RCHandTNBCdefined":
	file_path_R02 = R02_ds_folder_path + "BRCA_Treatment11_REMAGUS02xNACx221Sx54675Fx2RasRCHandTNBCdefined_GEX.csv"
	file_path_R04 = R04_ds_folder_path + "BRCA_Treatment12_REMAGUS04xNACx139Sx22277Fx2RasRCHandTNBCdefined_GEX.csv"
	file_path_MDA = MDA_ds_folder_path + "BRCA_Treatment13_MDAndersonxNACx133Sx22283Fx2RasRCHandTNBCdefined_GEX.csv"
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

# #---add to the dataset a column having the cohort name for each sample
# if cohort_used == "REMAGUS02":
#     df_file.insert(len(list(df_file.columns)), 'Cohort', 'Remagus02')
# elif cohort_used == "REMAGUS04":
#     df_file.insert(len(list(df_file.columns)), 'Cohort', 'Remagus04')
# else:  # cohort_used == "MDAnderson":
#     df_file.insert(len(list(df_file.columns)), 'Cohort', 'MDAnderson')

#>>>>>>>>>>>>>>>>>>>restrict the dataset to the columns of interest
# df_file = df_file.set_index('Model')
# ----for the columns to keep in all 3 cohorts df
# we will keep all the cols except the responses (only fts and model remains)
if resp_used == "RCH3HSall":
	list_of_cols_to_remove = ["BestResCat_as_RCH", "BestResCat_as_RO","BestResCat_as_RP", "BestResCat_as_HER2"]
elif resp_used == "RCH3HSdefined":
	list_of_cols_to_remove = ["BestResCat_as_RCH", "BestResCat_as_RO","BestResCat_as_RP", "BestResCat_as_HER2"]
elif resp_used == "RCHdefined":
	list_of_cols_to_remove = ["BestResCat_as_RCH"]
elif resp_used == "TNBCdefined":
	list_of_cols_to_remove = ["BestResCat_as_TNBC"]
else : # resp_used == "RCHandTNBCdefined":
	list_of_cols_to_remove = ["BestResCat_as_RCH", "BestResCat_as_TNBC"]

# ---- making the df with full info to use
df_file_fts_model_only = df_file.drop(list_of_cols_to_remove, axis=1)

# the base df
df_base = df_file_fts_model_only
#---make df for the file from HM of clustering
all3cohorts_samplesOnTaxanesOnly_file_path = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/heatmaps_correction/Clustering pour Amad 180520.xls"
if cohort_used == "REMAGUS02":
	sheet_id = "R02"
elif cohort_used == "REMAGUS04":
	sheet_id = "R02"
else : # cohort_used == "MDAnderson":
	sheet_id = "MDA"

df_clusters_cohort = pd.read_excel(all3cohorts_samplesOnTaxanesOnly_file_path,sheet_id)
df_clusters_cohort[df_clusters_cohort.columns[0]] = "CLETRI" + "_" + df_clusters_cohort[df_clusters_cohort.columns[0]].astype(str) # sample_name is a string ColumnName_IdInColumn
df_clusters_cohort.rename(columns={df_clusters_cohort.columns[0]:'Model_bis'}, inplace=True)
df_clusters_cohort.rename(columns={df_clusters_cohort.columns[-1]:'Clusters'}, inplace=True) # rename with simpler name like ATIP3_classes or Clusters
df_clusters_cohort = df_clusters_cohort[["Model_bis","Clusters"]] # restrict to only columns needed
# df_clusters_cohort.drop(labels=["GROUPE"], axis=1, inplace=True) # drop the uneeded cols
# join the df to get big on on which to compute after restricted
df_joined = pd.merge(df_base, df_clusters_cohort, how="inner", left_on="Model", right_on="Model_bis")
df_joined.drop(labels=["Model_bis"], axis=1, inplace=True)
#---making the column of real clusters
df_joined.rename(columns={"Clusters": "Real_Clusters"}, inplace=True)
# change the name for easier future references ie 1 is low and 2 and 3 are high (high here means high or medium)
df_joined["Real_Clusters"].replace([1,2,3], ["low", "high","high"], inplace=True)





# # #>>>>>>>>>>>>>>>>>>>>not needed
# #==========> computing the Mg each probe and make a new col with it to join in
# # - copy the dataset, find the columns for the probes of ATIP3 and compute the mean expr for all row (samples) then rejoin with df we had before
# # make a copy
# df_Mg_start_low_end_only = df_joined
# # they all have MTUS1 in the colname (they are 4 for R02 and 3 for R04 and MDA)
# # a list of the column of the probes
# full_list_of_cols = list(df_Mg_start_low_end_only.columns)
# list_of_probes2keep_colnames = []
# for colname in full_list_of_cols:
# 	if "MTUS1" in colname:
# 		list_of_probes2keep_colnames.append(colname)
# list_of_cols2keep = list_of_probes2keep_colnames + ["Model"]
# df_Mg_start_low_end_cols_restricted = df_Mg_start_low_end_only[list_of_cols2keep]
# # go over the list of mtus1 probes and keep for each one in a dict the value of Mg
# for mtus1_probe in list_mtus1_probe_2_focus_on:
# 	# sort as descending on the col of the mean
# 	df_Mg_start_low_end_cols_restricted= df_Mg_start_low_end_cols_restricted.sort_values(mtus1_probe, axis=0, ascending=False, kind='mergesort')
# 	# drop index in order to use new ordered index to adress the first line as index 0
# 	df_Mg_start_low_end_cols_restricted = df_Mg_start_low_end_cols_restricted.reset_index(drop=True)
# 	# The value of Mg for the probe across all samples
# 	Mg = df_Mg_start_low_end_cols_restricted.at[0, mtus1_probe]
# 	# create a col with the Mg of the probe
# 	new_colname_for_Mg_probe = "Mg" + "_" + mtus1_probe
# 	df_Mg_start_low_end_cols_restricted[new_colname_for_Mg_probe] = Mg
#
# # restrict on columns to keep for the joining
# cols_2keep_for_joining_after_Mg = []
# cols_2keep_for_joining_after_Mg.append("Model")
# for a_col in df_Mg_start_low_end_cols_restricted.columns:
# 	if a_col.startswith("Mg_"):
# 		cols_2keep_for_joining_after_Mg.append(a_col)
# df_Mg_start_low_end_cols_restricted_with_Mgs = df_Mg_start_low_end_cols_restricted[cols_2keep_for_joining_after_Mg]
# df_Mg_start_low_end_cols_restricted_with_Mgs.rename(columns={"Model": "Model_bis2"}, inplace=True)
# # now do the joining
# df_joined = pd.merge(df_joined, df_Mg_start_low_end_cols_restricted_with_Mgs, how="inner", left_on="Model", right_on="Model_bis2")
# df_joined.drop(labels=["Model_bis2"], axis=1, inplace=True)
# ##>>>>>>>>>>>>>>>> not needed




# -----mean for top 20s HKGs (for each sample)
# make a copy
df_Std_start = df_joined
# put the col of samples content aside (into the index) and then bring it back later
df_Std_start_restricted = df_Std_start.set_index('Model')
# - restrict the df
# ---get the cols to keep
#---make df for the file from HKGs selection
sep_in_file = ","
if cohort_used == "REMAGUS02":
	if origin_of_top20_HKGs == "common_to_cohorts":
		file_path_HKGs_cohort = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/HKGs_report/Common_HKGs_w_probes/HKGs_common_to_cohorts_report_w_probes_top20.csv"
	else :
		file_path_HKGs_cohort = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/HKGs_report/R02__HKGs/R02_Top20HKGsCVnoDupRanked_report.csv"
elif cohort_used == "REMAGUS04":
	if origin_of_top20_HKGs == "common_to_cohorts":
		file_path_HKGs_cohort = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/HKGs_report/Common_HKGs_w_probes/HKGs_common_to_cohorts_report_w_probes_top20.csv"
	else :
		file_path_HKGs_cohort = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/HKGs_report/R04__HKGs/R04_Top20HKGsCVnoDupRanked_report.csv"
else : # cohort_used == "MDAnderson":
	if origin_of_top20_HKGs == "common_to_cohorts":
		file_path_HKGs_cohort = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/HKGs_report/Common_HKGs_w_probes/HKGs_common_to_cohorts_report_w_probes_top20.csv"
	else :
		file_path_HKGs_cohort = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/HKGs_report/MDA_HKGs/MDA_Top20HKGsCVnoDupRanked_report.csv"
df_HKGs_cohort = pd.read_csv(file_path_HKGs_cohort, sep_in_file)
# a list of the colnames found in the df of HKGs and to use to restrict
if origin_of_top20_HKGs == "common_to_cohorts":
	if cohort_used == "REMAGUS02":
		list_colnames_asHKGs = df_HKGs_cohort['HKGs_R02'].tolist()
	elif cohort_used == "REMAGUS04":
		list_colnames_asHKGs = df_HKGs_cohort['HKGs_R04'].tolist()
	else : # cohort_used == "MDAnderson":
		list_colnames_asHKGs = df_HKGs_cohort['HKGs_MDA'].tolist()
else : # origin_of_top20_HKGs == "the_cohort_only"
	list_colnames_asHKGs = df_HKGs_cohort['HKGs'].tolist()
# restrict on cols that are the HKGs
df_Std_start_restricted = df_Std_start_restricted[list_colnames_asHKGs]
# compute the mean and keep it in a col
df_Std_start_restricted["Std_as_mean_top20_HKGs_by_sample"] = df_Std_start_restricted.mean(axis=1) # default is skipna=True
# bring back the samples col
df_Std_start_restricted = df_Std_start_restricted.rename_axis('Model').reset_index()
# restrict on columns to keep for the joining
columns_need_to_have_when_joining2 = ["Model","Std_as_mean_top20_HKGs_by_sample"]
df_Std_start_restricted_with_Std_col = df_Std_start_restricted[columns_need_to_have_when_joining2]
df_Std_start_restricted_with_Std_col.rename(columns={"Model": "Model_bis3"}, inplace=True)
# now do the joining
df_joined = pd.merge(df_joined, df_Std_start_restricted_with_Std_col, how="inner", left_on="Model", right_on="Model_bis3")
df_joined.drop(labels=["Model_bis3"], axis=1, inplace=True)

#--------restrict the cols for clarity before making the cols of predictions
list_of_cols_to_keep_going_towards_predictions = []
list_of_cols_to_keep_going_towards_predictions.append("Model")
list_of_mtus1_probes_cols = []
for a_col in df_joined.columns:
	if "MTUS1" in a_col:
		list_of_mtus1_probes_cols.append(a_col)
list_of_cols_to_keep_going_towards_predictions = list_of_cols_to_keep_going_towards_predictions + list_of_mtus1_probes_cols
list_of_cols_to_keep_going_towards_predictions.append("Std_as_mean_top20_HKGs_by_sample")
list_of_cols_to_keep_going_towards_predictions.append("Real_Clusters")
df_joined = df_joined[list_of_cols_to_keep_going_towards_predictions]

# produce 4 or 3 columns with Mg from ath (Mg by probe)
if cohort_used == "REMAGUS02":
	df_joined['Mg_mtus1_probe1_from_Ath_x_Std_top20_HKGs'] = ath_mtus1_probe1 * df_joined["Std_as_mean_top20_HKGs_by_sample"]
	df_joined['Mg_mtus1_probe2_from_Ath_x_Std_top20_HKGs'] = ath_mtus1_probe2 * df_joined["Std_as_mean_top20_HKGs_by_sample"]
	df_joined['Mg_mtus1_probe3_from_Ath_x_Std_top20_HKGs'] = ath_mtus1_probe3 * df_joined["Std_as_mean_top20_HKGs_by_sample"]
	df_joined['Mg_mtus1_probe4_from_Ath_x_Std_top20_HKGs'] = ath_mtus1_probe4 * df_joined["Std_as_mean_top20_HKGs_by_sample"]
else:
	df_joined['Mg_mtus1_probe1_from_Ath_x_Std_top20_HKGs'] = ath_mtus1_probe1 * df_joined["Std_as_mean_top20_HKGs_by_sample"]
	df_joined['Mg_mtus1_probe2_from_Ath_x_Std_top20_HKGs'] = ath_mtus1_probe2 * df_joined["Std_as_mean_top20_HKGs_by_sample"]
	df_joined['Mg_mtus1_probe3_from_Ath_x_Std_top20_HKGs'] = ath_mtus1_probe3 * df_joined["Std_as_mean_top20_HKGs_by_sample"]

# produce the col of predictions
# - get the cols name of Mg probe to use
# -- set up a function to create the colu of predicted cluster
if cohort_used == "REMAGUS02":
	colname_mtus1_probe1 = list_of_mtus1_probes_cols[0]
	colname_mtus1_probe2 = list_of_mtus1_probes_cols[1]
	colname_mtus1_probe3 = list_of_mtus1_probes_cols[2]
	colname_mtus1_probe4 = list_of_mtus1_probes_cols[3]
	def compute_predicted_clusters(df_joined):
		if (df_joined[colname_mtus1_probe1] < df_joined['Mg_mtus1_probe1_from_Ath_x_Std_top20_HKGs']) and (df_joined[colname_mtus1_probe2] < df_joined['Mg_mtus1_probe2_from_Ath_x_Std_top20_HKGs']) and (df_joined[colname_mtus1_probe3] < df_joined['Mg_mtus1_probe3_from_Ath_x_Std_top20_HKGs']) and (df_joined[colname_mtus1_probe4] < df_joined['Mg_mtus1_probe4_from_Ath_x_Std_top20_HKGs']):
			return "low"
		else:
			return "high"
else:
	colname_mtus1_probe1 = list_of_mtus1_probes_cols[0]
	colname_mtus1_probe2 = list_of_mtus1_probes_cols[1]
	colname_mtus1_probe3 = list_of_mtus1_probes_cols[2]
	def compute_predicted_clusters(df_joined):
		if (df_joined[colname_mtus1_probe1] < df_joined['Mg_mtus1_probe1_from_Ath_x_Std_top20_HKGs']) and (df_joined[colname_mtus1_probe2] < df_joined['Mg_mtus1_probe2_from_Ath_x_Std_top20_HKGs']) and (df_joined[colname_mtus1_probe3] < df_joined['Mg_mtus1_probe3_from_Ath_x_Std_top20_HKGs']):
			return "low"
		else:
			return "high"
# create the col of the predicted values
df_joined['Pred_Clusters'] = df_joined.apply(compute_predicted_clusters, axis=1)
#---------get the mcc for the total operation
TP = 0
TN = 0
FP = 0
FN = 0
list_of_the_samples = df_joined['Model'].tolist() # get a list of the samples to loop through them (they will be unavailable later because used as index)
print("Predicting the cluster of this number of samples:",len(list_of_the_samples))
df_joined = df_joined.set_index('Model') # make an index out of the col of the samples
for a_sample in list_of_the_samples:
	real_cluster_sample = df_joined.at[a_sample,"Real_Clusters"]
	predicted_cluster_sample = df_joined.at[a_sample, "Pred_Clusters"]
	if predicted_cluster_sample=="high": # cases where the negative class  is predicted
		if predicted_cluster_sample==real_cluster_sample:
			TN+=1
		else : # not predicted_cluster_sample==real_cluster_sample
			FN+=1
	elif predicted_cluster_sample=="low": # cases where the positive class  is predicted
		if predicted_cluster_sample==real_cluster_sample:
			TP+=1
		else : # not predicted_cluster_sample==real_cluster_sample
			FP+=1

# computation of a mcc
mcc_numerator = (TP*TN)-(FP*FN)
candidate_for_mcc_denominateur = sqrt((TP+FP)*(FP+TN)*(TN+FN)*(FN+TP))
if candidate_for_mcc_denominateur == 0: # condittion of existence of mcc mathematically
	mcc_denominateur = 1
else:
	mcc_denominateur = candidate_for_mcc_denominateur
mcc_df_joined = mcc_numerator / mcc_denominateur

# A summary of the prediction analysis done here :
print("summary of the prediction analysis done here :")
print("- cohort being predicted on :",cohort_used)
print("- origin of top 20 HKGs used to get Std :",origin_of_top20_HKGs)
print("- origin of Ath : ",ath_origin)
print("- aspect of top 20 HKGs origin for Ath used :",ath_top20_aspect_origin)
print("MCC : ",mcc_df_joined)
print("FP :",FP)
print("FN :",FN)
print("TP :",TP)
print("TN :",TN)









