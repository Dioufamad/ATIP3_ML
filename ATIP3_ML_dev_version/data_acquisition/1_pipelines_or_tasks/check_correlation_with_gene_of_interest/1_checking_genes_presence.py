#---------------------check if the genes asked about are in datasets variables
#>>>>>>>>>>>>>>>>>>>>>>>>>>> IMPORTS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import pandas as pd
import numpy as np # linear algebra and exploit arrays faster and easier computations
import seaborn as sns
import matplotlib.pyplot as plt
from textwrap import wrap # to wrap plot titles

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

# list of genes to check their presence
list1 = ["HUWE1","HUWE11"]
list2 = ["RPL39","RPL2","RPL5","RPL28"] + ["RPL37A","RPL3","RPL6","RPL2"] + ["RPL41","RPL10","RPL7","RPL1"]
list3 = ["RPS27","RPS5","RPS9","RPS50"] + ["RPS16","RPS8","RPS54","RPS8"] + ["RPS18","RPS15","RPS23","RPS31"]
list4 = ["RP5-882O7.1", "RP11","RP10","RP5"]
list_of_genes_2_search = list1 + list2 + list3 + list4
list_of_genes_2_search = sorted(list_of_genes_2_search)
print("Here is the list of genes to search : ")
print(list_of_genes_2_search)

# get the list of columns
list_of_cols_R02 = sorted(list(df_file_R02_restricted.columns))
list_of_cols_R04 = sorted(list(df_file_R04_restricted.columns))
list_of_cols_MDA = sorted(list(df_file_MDA_restricted.columns))
# change the fts names in GS
# - a function to get the short gene name from the long column name
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
# - replace in the list the long name by the short name (GS)
list_of_lists_of_long_names = [list_of_cols_R02,list_of_cols_R04,list_of_cols_MDA]
for a_long_list in list_of_lists_of_long_names:
	for long_name in a_long_list:
		index_to_replace_into = a_long_list.index(long_name)
		new_short_name = full_name_ft2_short_name(long_name)
		a_long_list[index_to_replace_into] = new_short_name
	print("finished changing the list of features of a cohort")
print("finished going over the list of lists of features")

# make a dict for a dataframe with 7 cols : col1 : Inquired GS, col2 : R02_GS_where_it_is_found, col3 : R04_GS_where_it_is_found, col4 : MDA_GS_where_it_is_found,
# - create the list that receives results
# list_for_col1 = list_of_genes_2_search # the list of GS to inquire
list_of_lists_for_col2 = [] # for R02
list_of_lists_for_col3 = [] # for R04
list_of_lists_for_col4 = [] # for MDA
# - get only the unqiue in the lists where we have to search and sort the lists
list_of_cols_R02_new = sorted(list(set(list_of_lists_of_long_names[0])))
list_of_cols_R04_new = sorted(list(set(list_of_lists_of_long_names[1])))
list_of_cols_MDA_new = sorted(list(set(list_of_lists_of_long_names[2])))
# - make the search and stash the results
for a_inquired_GS in list_of_genes_2_search:
    list_of_R02_GS_where_it_is_found = []
    list_of_R04_GS_where_it_is_found = []
    list_of_MDA_GS_where_it_is_found = []
    for a_R02_GS in list_of_cols_R02_new:
        if a_inquired_GS in a_R02_GS:
            list_of_R02_GS_where_it_is_found.append(a_R02_GS)
    for a_R04_GS in list_of_cols_R04_new:
        if a_inquired_GS in a_R04_GS:
            list_of_R04_GS_where_it_is_found.append(a_R04_GS)
    for a_MDA_GS in list_of_cols_MDA_new:
        if a_inquired_GS in a_MDA_GS:
            list_of_MDA_GS_where_it_is_found.append(a_MDA_GS)
    # stash the results
    list_of_lists_for_col2.append(list_of_R02_GS_where_it_is_found)
    list_of_lists_for_col3.append(list_of_R04_GS_where_it_is_found)
    list_of_lists_for_col4.append(list_of_MDA_GS_where_it_is_found)
print("end of the search and result stashing")
# - make the dict
dict_for_df = {}
dict_for_df["GS_inquired"]=list_of_genes_2_search
dict_for_df["R02_GS_where_it_is_found"]=list_of_lists_for_col2
dict_for_df["R04_GS_where_it_is_found"]=list_of_lists_for_col3
dict_for_df["MDA_GS_where_it_is_found"]=list_of_lists_for_col4
# - make the df
df_search_results = pd.DataFrame(dict_for_df, columns=['GS_inquired', 'R02_GS_where_it_is_found',"R04_GS_where_it_is_found","MDA_GS_where_it_is_found"])

# # save the df of search results to a .csv file
# inquired_GS_search_results1_filename = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/inquired_GS_search_results1.csv"
# df_search_results.to_csv(inquired_GS_search_results1_filename, index=None, header=True)

#




