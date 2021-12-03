#---------------------check if the genes inquired are correlated
#>>>>>>>>>>>>>>>>>>>>>>>>>>> IMPORTS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import pandas as pd
import numpy as np # linear algebra and exploit arrays faster and easier computations
import seaborn as sns
import matplotlib.pyplot as plt
from textwrap import wrap # to wrap plot titles
from ast import literal_eval # to put back string of list as lists
from sklearn.preprocessing import StandardScaler # to scale fts and give them normal distributions for pearson correlation computation

# load the HKGs report for each cohort (we choose the the full HKGs report ordered on the CV_no_dup
sep_in_file = ","
file_path_R02 = "/data_warehouse/inputs/atip3_material/datasets_to_process_folder/R02/BRCA_Treatment11_REMAGUS02xNACx226Sx54675Fx4RasRCH3HSall_GEX.csv"
file_path_R04 = "/data_warehouse/inputs/atip3_material/datasets_to_process_folder/R04/BRCA_Treatment12_REMAGUS04xNACx142Sx22277Fx4RasRCH3HSall_GEX.csv"
file_path_MDA = "/data_warehouse/inputs/atip3_material/datasets_to_process_folder/MDA/BRCA_Treatment13_MDAndersonxNACx133Sx22283Fx4RasRCH3HSall_GEX.csv"
df_file_R02 = pd.read_csv(file_path_R02, sep_in_file)
df_file_R04 = pd.read_csv(file_path_R04, sep_in_file)
df_file_MDA = pd.read_csv(file_path_MDA, sep_in_file)

# restrict to needed columns
list_of_cols_to_remove = ["BestResCat_as_RCH","BestResCat_as_RO","BestResCat_as_RP","BestResCat_as_HER2","Model"]
df_file_R02_restricted = df_file_R02.drop(list_of_cols_to_remove, axis=1)
df_file_R04_restricted = df_file_R04.drop(list_of_cols_to_remove, axis=1)
df_file_MDA_restricted = df_file_MDA.drop(list_of_cols_to_remove, axis=1)

# rename the columns GS_withprobe_P
list_of_cols_R02 = list(df_file_R02_restricted.columns)
list_of_cols_R04 = list(df_file_R04_restricted.columns)
list_of_cols_MDA = list(df_file_MDA_restricted.columns)
# change the fts names into GS_withprobe_P
# - a function to shorten the name (eg : 'GSasDDR1 /// MIR4640wGBANasU48705wPSIas1007_s_at' into 'DDR1 /// MIR4640_withprobe_1007_s_at'
def longer_name_2_shorter_name(longer_name):
	list_from_split1 = longer_name.split("GSas")
	if len(list_from_split1)==1:
		new_shorter_name = "NA"
	else :
		kept_from_list1 = list_from_split1[1]
		list_from_split2 = kept_from_list1.split("wGBANas")
		GSpart = list_from_split2[0]
		kept_from_list2 = list_from_split2[1]
		list_from_split3 = kept_from_list2.split("wPSIas")
		Probepart = list_from_split3[1]
		new_shorter_name = GSpart + "_withprobe_" + Probepart
	return new_shorter_name

# change the name of cols
for old_col_name in list_of_cols_R02:
	index_to_replace_into = list_of_cols_R02.index(old_col_name)
	new_short_name = longer_name_2_shorter_name(old_col_name)
	list_of_cols_R02[index_to_replace_into] = new_short_name
print("finished changing the list of features of a cohort")
for old_col_name in list_of_cols_R04:
	index_to_replace_into = list_of_cols_R04.index(old_col_name)
	new_short_name = longer_name_2_shorter_name(old_col_name)
	list_of_cols_R04[index_to_replace_into] = new_short_name
print("finished changing the list of features of a cohort")
for old_col_name in list_of_cols_MDA:
	index_to_replace_into = list_of_cols_MDA.index(old_col_name)
	new_short_name = longer_name_2_shorter_name(old_col_name)
	list_of_cols_MDA[index_to_replace_into] = new_short_name
print("finished changing the list of features of a cohort")

# reassign the new col names
df_file_R02_restricted.columns = list_of_cols_R02
df_file_R04_restricted.columns = list_of_cols_R04
df_file_MDA_restricted.columns = list_of_cols_MDA

# we have to restrict the columns to only the fts to compute correlations for
# - list of genes to check their presence
list0_probes_to_compare_with = ["MTUS1"]
list1 = ["HUWE1","HUWE11"]
list2 = ["RPL39","RPL2","RPL5","RPL28"] + ["RPL37A","RPL3","RPL6","RPL2"] + ["RPL41","RPL10","RPL7","RPL1"]
list3 = ["RPS27","RPS5","RPS9","RPS50"] + ["RPS16","RPS8","RPS54","RPS8"] + ["RPS18","RPS15","RPS23","RPS31"]
list4 = ["RP5-882O7.1", "RP11","RP10","RP5"]
list1_probes_of_inquiry = list1 + list2 + list3 + list4
list_of_genes_2_search = list0_probes_to_compare_with + sorted(list(set(list1_probes_of_inquiry)))
print("Here is the list of genes to search : ")
print(list_of_genes_2_search)
# - create the list that cols to keep
list_of_R02_cols_with_GS_2keep = []
list_of_R04_cols_with_GS_2keep = []
list_of_MDA_cols_with_GS_2keep = []
# - supply the lists of cols to keep
for g in list_of_genes_2_search:
	for i in sorted(list(df_file_R02_restricted.columns)):
		if g in i:
			if i not in list_of_R02_cols_with_GS_2keep:
				list_of_R02_cols_with_GS_2keep.append(i)
for g in list_of_genes_2_search:
	for i in sorted(list(df_file_R04_restricted.columns)):
		if g in i:
			if i not in list_of_R04_cols_with_GS_2keep:
				list_of_R04_cols_with_GS_2keep.append(i)
for g in list_of_genes_2_search:
	for i in sorted(list(df_file_MDA_restricted.columns)):
		if g in i:
			if i not in list_of_MDA_cols_with_GS_2keep:
				list_of_MDA_cols_with_GS_2keep.append(i)

# verify if all probes of a GS have been captured
# - for R02
mtsu1_probes_for_R02 = []
for elt in list_of_R02_cols_with_GS_2keep:
	if "MTUS1" in elt:
		mtsu1_probes_for_R02.append(elt)
# - for R04
mtsu1_probes_for_R04 = []
for elt in list_of_R04_cols_with_GS_2keep:
	if "MTUS1" in elt:
		mtsu1_probes_for_R04.append(elt)
# - for MDA
mtsu1_probes_for_MDA = []
for elt in list_of_MDA_cols_with_GS_2keep:
	if "MTUS1" in elt:
		mtsu1_probes_for_MDA.append(elt)

# get the df to use for computation of correlations
df_file_R02_for_corr = df_file_R02_restricted[list_of_R02_cols_with_GS_2keep]
df_file_R04_for_corr = df_file_R04_restricted[list_of_R04_cols_with_GS_2keep]
df_file_MDA_for_corr = df_file_MDA_restricted[list_of_MDA_cols_with_GS_2keep]

# Create a new data frame with scaled data
# - Pearson’s correlation requires that each dataset be normally distributed so we scale features # scaling fts does standardization (x-u/std)
X_R02_scaled = StandardScaler().fit_transform(df_file_R02_for_corr.values) # for R02
X_R04_scaled = StandardScaler().fit_transform(df_file_R04_for_corr.values) # for R04
X_MDA_scaled = StandardScaler().fit_transform(df_file_MDA_for_corr.values) # for MDA
# - make new data frame
df_file_R02_for_corr_scaled = pd.DataFrame(X_R02_scaled, index=df_file_R02_for_corr.index, columns=df_file_R02_for_corr.columns)
df_file_R04_for_corr_scaled = pd.DataFrame(X_R04_scaled, index=df_file_R04_for_corr.index, columns=df_file_R04_for_corr.columns)
df_file_MDA_for_corr_scaled = pd.DataFrame(X_MDA_scaled, index=df_file_MDA_for_corr.index, columns=df_file_MDA_for_corr.columns)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<           THE PLOTS                 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>> - make the plot for a heatmap of the correlation coefficients : for ALL genes probes
df_file_R02_with_corr_val = df_file_R02_for_corr_scaled.corr()
df_file_R04_with_corr_val = df_file_R04_for_corr_scaled.corr()
df_file_MDA_with_corr_val = df_file_MDA_for_corr_scaled.corr()
# - for R02
list_of_GS_desired_on_plot_R02 = list_of_genes_2_search
list_cols_with_GS_desired_on_plot_R02 = []
for g in list_of_GS_desired_on_plot_R02:
	for i in df_file_R02_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_R02:
				list_cols_with_GS_desired_on_plot_R02.append(i)
df_all_genes_R02 = df_file_R02_for_corr_scaled[list_cols_with_GS_desired_on_plot_R02]
data_all_genes_R02 = df_all_genes_R02.corr()
ax = sns.heatmap(data_all_genes_R02.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30)
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/HUWE_all_probes_corr_with_MTUS1_R02.png')

#>>>>>>>>>>>> - make the plot for a heatmap of the correlation coefficients : for HUWE genes probes
# - for R02
list_of_GS_desired_on_plot_R02 = ["MTUS1"] + ["HUWE1"]
list_cols_with_GS_desired_on_plot_R02 = []
for g in list_of_GS_desired_on_plot_R02:
	for i in df_file_R02_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_R02:
				list_cols_with_GS_desired_on_plot_R02.append(i)
df_huwe_genes_R02 = df_file_R02_for_corr_scaled[list_cols_with_GS_desired_on_plot_R02]
data_huwe_genes_R02 = df_huwe_genes_R02.corr()
ax = sns.heatmap(data_huwe_genes_R02.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30)
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list1_genes_probes_corr_with_MTUS1_R02.png')
# - for R04
list_of_GS_desired_on_plot_R04 = ["MTUS1"] + ["HUWE1"]
list_cols_with_GS_desired_on_plot_R04 = []
for g in list_of_GS_desired_on_plot_R04:
	for i in df_file_R04_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_R04:
				list_cols_with_GS_desired_on_plot_R04.append(i)
df_huwe_genes_R04 = df_file_R04_for_corr_scaled[list_cols_with_GS_desired_on_plot_R04]
data_huwe_genes_R04 = df_huwe_genes_R04.corr()
ax = sns.heatmap(data_huwe_genes_R04.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30)
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list1_genes_probes_corr_with_MTUS1_R04.png')
# - for MDA
list_of_GS_desired_on_plot_MDA = ["MTUS1"] + ["HUWE1"]
list_cols_with_GS_desired_on_plot_MDA = []
for g in list_of_GS_desired_on_plot_MDA:
	for i in df_file_MDA_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_MDA:
				list_cols_with_GS_desired_on_plot_MDA.append(i)
df_huwe_genes_MDA = df_file_MDA_for_corr_scaled[list_cols_with_GS_desired_on_plot_MDA]
data_huwe_genes_MDA = df_huwe_genes_MDA.corr()
ax = sns.heatmap(data_huwe_genes_MDA.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30) 
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list1_genes_probes_corr_with_MTUS1_MDA.png')

#>>>>>>>>>>>> - make the plot for a heatmap of the correlation coefficients : for list2 genes probes
# - for R02
list_of_GS_desired_on_plot_R02 = ["MTUS1"] + ["RPL39 ","RPL2 ","RPL5 ","RPL28 ","RPL39_","RPL2_","RPL5_","RPL28_"] # done to restrict the search
list_cols_with_GS_desired_on_plot_R02 = []
for g in list_of_GS_desired_on_plot_R02:
	for i in df_file_R02_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_R02:
				list_cols_with_GS_desired_on_plot_R02.append(i)
df_huwe_genes_R02 = df_file_R02_for_corr_scaled[list_cols_with_GS_desired_on_plot_R02]
data_huwe_genes_R02 = df_huwe_genes_R02.corr()
ax = sns.heatmap(data_huwe_genes_R02.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30)
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list2_genes_probes_corr_with_MTUS1_R02.png')
# - for R04
list_of_GS_desired_on_plot_R04 = ["MTUS1"] + ["RPL39 ","RPL2 ","RPL5 ","RPL28 ","RPL39_","RPL2_","RPL5_","RPL28_"] # issue with : 'RPL5 /// SNORA66 /// SNORD21_withprobe_210035_s_at' it has the same value for all samples
list_cols_with_GS_desired_on_plot_R04 = []
for g in list_of_GS_desired_on_plot_R04:
	for i in df_file_R04_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_R04:
				list_cols_with_GS_desired_on_plot_R04.append(i)
df_huwe_genes_R04 = df_file_R04_for_corr_scaled[list_cols_with_GS_desired_on_plot_R04]
data_huwe_genes_R04 = df_huwe_genes_R04.corr()
ax = sns.heatmap(data_huwe_genes_R04.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30)
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list2_genes_probes_corr_with_MTUS1_R04.png')
# - for MDA
list_of_GS_desired_on_plot_MDA = ["MTUS1"] + ["RPL39 ","RPL2 ","RPL5 ","RPL28 ","RPL39_","RPL2_","RPL5_","RPL28_"]
list_cols_with_GS_desired_on_plot_MDA = []
for g in list_of_GS_desired_on_plot_MDA:
	for i in df_file_MDA_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_MDA:
				list_cols_with_GS_desired_on_plot_MDA.append(i)
df_huwe_genes_MDA = df_file_MDA_for_corr_scaled[list_cols_with_GS_desired_on_plot_MDA]
data_huwe_genes_MDA = df_huwe_genes_MDA.corr()
ax = sns.heatmap(data_huwe_genes_MDA.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30) 
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list2_genes_probes_corr_with_MTUS1_MDA.png')

#>>>>>>>>>>>> - make the plot for a heatmap of the correlation coefficients : for list3 genes probes
# - for R02
list_of_GS_desired_on_plot_R02 = ["MTUS1"] + ["RPL37A ","RPL37A_","RPL3 ","RPL3_","RPL6 ","RPL6_","RPL2 ", "RPL2_"] # done to restrict the search
list_cols_with_GS_desired_on_plot_R02 = []
for g in list_of_GS_desired_on_plot_R02:
	for i in df_file_R02_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_R02:
				list_cols_with_GS_desired_on_plot_R02.append(i)
df_huwe_genes_R02 = df_file_R02_for_corr_scaled[list_cols_with_GS_desired_on_plot_R02]
data_huwe_genes_R02 = df_huwe_genes_R02.corr()
ax = sns.heatmap(data_huwe_genes_R02.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30)
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list3_genes_probes_corr_with_MTUS1_R02.png')
# - for R04
list_of_GS_desired_on_plot_R04 = ["MTUS1"] + ["RPL37A ","RPL37A_","RPL3 ","RPL3_","RPL6 ","RPL6_","RPL2 ", "RPL2_"]
list_cols_with_GS_desired_on_plot_R04 = []
for g in list_of_GS_desired_on_plot_R04:
	for i in df_file_R04_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_R04:
				list_cols_with_GS_desired_on_plot_R04.append(i)
df_huwe_genes_R04 = df_file_R04_for_corr_scaled[list_cols_with_GS_desired_on_plot_R04]
data_huwe_genes_R04 = df_huwe_genes_R04.corr()
ax = sns.heatmap(data_huwe_genes_R04.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30)
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list3_genes_probes_corr_with_MTUS1_R04.png')
# - for MDA
list_of_GS_desired_on_plot_MDA = ["MTUS1"] + ["RPL37A ","RPL37A_","RPL3 ","RPL3_","RPL6 ","RPL6_","RPL2 ", "RPL2_"]
list_cols_with_GS_desired_on_plot_MDA = []
for g in list_of_GS_desired_on_plot_MDA:
	for i in df_file_MDA_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_MDA:
				list_cols_with_GS_desired_on_plot_MDA.append(i)
df_huwe_genes_MDA = df_file_MDA_for_corr_scaled[list_cols_with_GS_desired_on_plot_MDA]
data_huwe_genes_MDA = df_huwe_genes_MDA.corr()
ax = sns.heatmap(data_huwe_genes_MDA.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30) 
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list3_genes_probes_corr_with_MTUS1_MDA.png')

#>>>>>>>>>>>> - make the plot for a heatmap of the correlation coefficients : for list4 genes probes
# - for R02
list_of_GS_desired_on_plot_R02 = ["MTUS1"] + ["RPS27 ","RPS5 ","RPS9 ", "RPS27_","RPS5_","RPS9_"] # done to restrict the search
list_cols_with_GS_desired_on_plot_R02 = []
for g in list_of_GS_desired_on_plot_R02:
	for i in df_file_R02_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_R02:
				list_cols_with_GS_desired_on_plot_R02.append(i)
df_huwe_genes_R02 = df_file_R02_for_corr_scaled[list_cols_with_GS_desired_on_plot_R02]
data_huwe_genes_R02 = df_huwe_genes_R02.corr()
ax = sns.heatmap(data_huwe_genes_R02.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30)
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list4_genes_probes_corr_with_MTUS1_R02.png')
# - for R04
list_of_GS_desired_on_plot_R04 = ["MTUS1"] + ["RPS27 ","RPS5 ","RPS9 ", "RPS27_","RPS5_","RPS9_"]
list_cols_with_GS_desired_on_plot_R04 = []
for g in list_of_GS_desired_on_plot_R04:
	for i in df_file_R04_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_R04:
				list_cols_with_GS_desired_on_plot_R04.append(i)
df_huwe_genes_R04 = df_file_R04_for_corr_scaled[list_cols_with_GS_desired_on_plot_R04]
data_huwe_genes_R04 = df_huwe_genes_R04.corr()
ax = sns.heatmap(data_huwe_genes_R04.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30)
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list4_genes_probes_corr_with_MTUS1_R04.png')
# - for MDA
list_of_GS_desired_on_plot_MDA = ["MTUS1"] + ["RPS27 ","RPS5 ","RPS9 ", "RPS27_","RPS5_","RPS9_"]
list_cols_with_GS_desired_on_plot_MDA = []
for g in list_of_GS_desired_on_plot_MDA:
	for i in df_file_MDA_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_MDA:
				list_cols_with_GS_desired_on_plot_MDA.append(i)
df_huwe_genes_MDA = df_file_MDA_for_corr_scaled[list_cols_with_GS_desired_on_plot_MDA]
data_huwe_genes_MDA = df_huwe_genes_MDA.corr()
ax = sns.heatmap(data_huwe_genes_MDA.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30) 
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list4_genes_probes_corr_with_MTUS1_MDA.png')

#>>>>>>>>>>>> - make the plot for a heatmap of the correlation coefficients : for list5 genes probes
# - for R02
list_of_GS_desired_on_plot_R02 = ["MTUS1"] + ["RPS16 ","RPS16_","RPS8 ","RPS8_"] # done to restrict the search # reordered to keep the same GS probes close to each other
list_cols_with_GS_desired_on_plot_R02 = []
for g in list_of_GS_desired_on_plot_R02:
	for i in df_file_R02_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_R02:
				list_cols_with_GS_desired_on_plot_R02.append(i)
df_huwe_genes_R02 = df_file_R02_for_corr_scaled[list_cols_with_GS_desired_on_plot_R02]
data_huwe_genes_R02 = df_huwe_genes_R02.corr()
ax = sns.heatmap(data_huwe_genes_R02.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30)
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list5_genes_probes_corr_with_MTUS1_R02.png')
# - for R04
list_of_GS_desired_on_plot_R04 = ["MTUS1"] + ["RPS16 ","RPS16_","RPS8 ","RPS8_"]
list_cols_with_GS_desired_on_plot_R04 = []
for g in list_of_GS_desired_on_plot_R04:
	for i in df_file_R04_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_R04:
				list_cols_with_GS_desired_on_plot_R04.append(i)
df_huwe_genes_R04 = df_file_R04_for_corr_scaled[list_cols_with_GS_desired_on_plot_R04]
data_huwe_genes_R04 = df_huwe_genes_R04.corr()
ax = sns.heatmap(data_huwe_genes_R04.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30)
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list5_genes_probes_corr_with_MTUS1_R04.png')
# - for MDA
list_of_GS_desired_on_plot_MDA = ["MTUS1"] + ["RPS16 ","RPS16_","RPS8 ","RPS8_"]
list_cols_with_GS_desired_on_plot_MDA = []
for g in list_of_GS_desired_on_plot_MDA:
	for i in df_file_MDA_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_MDA:
				list_cols_with_GS_desired_on_plot_MDA.append(i)
df_huwe_genes_MDA = df_file_MDA_for_corr_scaled[list_cols_with_GS_desired_on_plot_MDA]
data_huwe_genes_MDA = df_huwe_genes_MDA.corr()
ax = sns.heatmap(data_huwe_genes_MDA.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30) 
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list5_genes_probes_corr_with_MTUS1_MDA.png')

#>>>>>>>>>>>> - make the plot for a heatmap of the correlation coefficients : for list6 genes probes
# - for R02
list_of_GS_desired_on_plot_R02 = ["MTUS1"] + ["RPL41 ","RPL41_","RPL10 ","RPL10_","RPL7 ","RPL7_","RPL1 ","RPL1_"] # done to restrict the search # reordered to keep the same GS probes close to each other
list_cols_with_GS_desired_on_plot_R02 = []
for g in list_of_GS_desired_on_plot_R02:
	for i in df_file_R02_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_R02:
				list_cols_with_GS_desired_on_plot_R02.append(i)
df_huwe_genes_R02 = df_file_R02_for_corr_scaled[list_cols_with_GS_desired_on_plot_R02]
data_huwe_genes_R02 = df_huwe_genes_R02.corr()
ax = sns.heatmap(data_huwe_genes_R02.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30)
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list6_genes_probes_corr_with_MTUS1_R02.png')
# - for R04
list_of_GS_desired_on_plot_R04 = ["MTUS1"] + ["RPL41 ","RPL41_","RPL10 ","RPL10_","RPL7 ","RPL7_","RPL1 ","RPL1_"]
list_cols_with_GS_desired_on_plot_R04 = []
for g in list_of_GS_desired_on_plot_R04:
	for i in df_file_R04_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_R04:
				list_cols_with_GS_desired_on_plot_R04.append(i)
df_huwe_genes_R04 = df_file_R04_for_corr_scaled[list_cols_with_GS_desired_on_plot_R04]
data_huwe_genes_R04 = df_huwe_genes_R04.corr()
ax = sns.heatmap(data_huwe_genes_R04.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30)
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list6_genes_probes_corr_with_MTUS1_R04.png')
# - for MDA
list_of_GS_desired_on_plot_MDA = ["MTUS1"] + ["RPL41 ","RPL41_","RPL10 ","RPL10_","RPL7 ","RPL7_","RPL1 ","RPL1_"]
list_cols_with_GS_desired_on_plot_MDA = []
for g in list_of_GS_desired_on_plot_MDA:
	for i in df_file_MDA_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_MDA:
				list_cols_with_GS_desired_on_plot_MDA.append(i)
df_huwe_genes_MDA = df_file_MDA_for_corr_scaled[list_cols_with_GS_desired_on_plot_MDA]
data_huwe_genes_MDA = df_huwe_genes_MDA.corr()
ax = sns.heatmap(data_huwe_genes_MDA.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30) 
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list6_genes_probes_corr_with_MTUS1_MDA.png')

#>>>>>>>>>>>> - make the plot for a heatmap of the correlation coefficients : for list7 genes probes
# - for R02
list_of_GS_desired_on_plot_R02 = ["MTUS1"] + ["RP5-882O7.1 ", "RP5-882O7.1_", "RP11 ", "RP11_","RP10 ","RP10_","RP5 ","RP5_"] # done to restrict the search # reordered to keep the same GS probes close to each other
list_cols_with_GS_desired_on_plot_R02 = []
for g in list_of_GS_desired_on_plot_R02:
	for i in df_file_R02_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_R02:
				list_cols_with_GS_desired_on_plot_R02.append(i)
df_huwe_genes_R02 = df_file_R02_for_corr_scaled[list_cols_with_GS_desired_on_plot_R02]
data_huwe_genes_R02 = df_huwe_genes_R02.corr()
ax = sns.heatmap(data_huwe_genes_R02.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30)
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list7_genes_probes_corr_with_MTUS1_R02.png')
# - for R04
list_of_GS_desired_on_plot_R04 = ["MTUS1"] + ["RP5-882O7.1 ", "RP5-882O7.1_", "RP11 ", "RP11_","RP10 ","RP10_","RP5 ","RP5_"]
list_cols_with_GS_desired_on_plot_R04 = []
for g in list_of_GS_desired_on_plot_R04:
	for i in df_file_R04_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_R04:
				list_cols_with_GS_desired_on_plot_R04.append(i)
df_huwe_genes_R04 = df_file_R04_for_corr_scaled[list_cols_with_GS_desired_on_plot_R04]
data_huwe_genes_R04 = df_huwe_genes_R04.corr()
ax = sns.heatmap(data_huwe_genes_R04.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30)
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list7_genes_probes_corr_with_MTUS1_R04.png')
# - for MDA
list_of_GS_desired_on_plot_MDA = ["MTUS1"] + ["RP5-882O7.1 ", "RP5-882O7.1_", "RP11 ", "RP11_","RP10 ","RP10_","RP5 ","RP5_"]
list_cols_with_GS_desired_on_plot_MDA = []
for g in list_of_GS_desired_on_plot_MDA:
	for i in df_file_MDA_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_MDA:
				list_cols_with_GS_desired_on_plot_MDA.append(i)
df_huwe_genes_MDA = df_file_MDA_for_corr_scaled[list_cols_with_GS_desired_on_plot_MDA]
data_huwe_genes_MDA = df_huwe_genes_MDA.corr()
ax = sns.heatmap(data_huwe_genes_MDA.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30) 
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list7_genes_probes_corr_with_MTUS1_MDA.png')

#>>>>>>>>>>>> - make the plot for a heatmap of the correlation coefficients : for list8 genes probes
# - for R02
list_of_GS_desired_on_plot_R02 = ["MTUS1"] + ["RPS18 ","RPS18_","RPS15 ","RPS15_","RPS23 ","RPS23_","RPS31 ","RPS31_"] # done to restrict the search # reordered to keep the same GS probes close to each other
list_cols_with_GS_desired_on_plot_R02 = []
for g in list_of_GS_desired_on_plot_R02:
	for i in df_file_R02_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_R02:
				list_cols_with_GS_desired_on_plot_R02.append(i)
df_huwe_genes_R02 = df_file_R02_for_corr_scaled[list_cols_with_GS_desired_on_plot_R02]
data_huwe_genes_R02 = df_huwe_genes_R02.corr()
ax = sns.heatmap(data_huwe_genes_R02.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30)
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list8_genes_probes_corr_with_MTUS1_R02.png')
# - for R04
list_of_GS_desired_on_plot_R04 = ["MTUS1"] + ["RPS18 ","RPS18_","RPS15 ","RPS15_","RPS23 ","RPS23_","RPS31 ","RPS31_"]
list_cols_with_GS_desired_on_plot_R04 = []
for g in list_of_GS_desired_on_plot_R04:
	for i in df_file_R04_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_R04:
				list_cols_with_GS_desired_on_plot_R04.append(i)
df_huwe_genes_R04 = df_file_R04_for_corr_scaled[list_cols_with_GS_desired_on_plot_R04]
data_huwe_genes_R04 = df_huwe_genes_R04.corr()
ax = sns.heatmap(data_huwe_genes_R04.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30)
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list8_genes_probes_corr_with_MTUS1_R04.png')
# - for MDA
list_of_GS_desired_on_plot_MDA = ["MTUS1"] + ["RPS18 ","RPS18_","RPS15 ","RPS15_","RPS23 ","RPS23_","RPS31 ","RPS31_"]
list_cols_with_GS_desired_on_plot_MDA = []
for g in list_of_GS_desired_on_plot_MDA:
	for i in df_file_MDA_for_corr_scaled.columns:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_MDA:
				list_cols_with_GS_desired_on_plot_MDA.append(i)
df_huwe_genes_MDA = df_file_MDA_for_corr_scaled[list_cols_with_GS_desired_on_plot_MDA]
data_huwe_genes_MDA = df_huwe_genes_MDA.corr()
ax = sns.heatmap(data_huwe_genes_MDA.T) # --plot heatmap
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 30) 
plt.savefig('/home/khamasiga/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/outputs/list8_genes_probes_corr_with_MTUS1_MDA.png')

# a df of the probes with the same value across samples
# - for R02
list_of_GS_desired_on_plot_R02 = ["SNORA66 ","MRPL41_","SNORA70"]
list_cols_with_GS_desired_on_plot_R02 = []
for g in list_of_GS_desired_on_plot_R02:
	for i in df_file_R02_for_corr_scaled:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_R02:
				list_cols_with_GS_desired_on_plot_R02.append(i)
df_file_R02_faulty_in_corr = df_file_R02_for_corr_scaled[list_cols_with_GS_desired_on_plot_R02]
# - for R04
list_of_GS_desired_on_plot_R04 = ["SNORA66 ","MRPL41_","SNORA70"]
list_cols_with_GS_desired_on_plot_R04 = []
for g in list_of_GS_desired_on_plot_R04:
	for i in df_file_R04_for_corr_scaled:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_R04:
				list_cols_with_GS_desired_on_plot_R04.append(i)
df_file_R04_faulty_in_corr = df_file_R04_for_corr_scaled[list_cols_with_GS_desired_on_plot_R04]
# - for MDA
list_of_GS_desired_on_plot_MDA = ["SNORA66 ","MRPL41_","SNORA70"]
list_cols_with_GS_desired_on_plot_MDA = []
for g in list_of_GS_desired_on_plot_MDA:
	for i in df_file_MDA_for_corr_scaled:
		if g in i:
			if i not in list_cols_with_GS_desired_on_plot_MDA:
				list_cols_with_GS_desired_on_plot_MDA.append(i)
df_file_MDA_faulty_in_corr = df_file_MDA_for_corr_scaled[list_cols_with_GS_desired_on_plot_MDA]


# sources for pearson corr:
# - https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.pearsonr.html
# - the corr matrix : https://stackoverflow.com/questions/42579908/use-corr-to-get-the-correlation-between-two-columns
# - the heatmap : https://stackoverflow.com/questions/35788626/how-to-plot-a-heatmap-from-pandas-dataframe/35793415#35793415