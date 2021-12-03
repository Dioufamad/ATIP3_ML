#!/usr/bin/env python
# coding: utf-8

# ## Exploring hierarchical clustering of REMAGUS02 cohort
# imports
import numpy as np
# from numpy import seterr,isneginf # used to manage the change into log2 o values in a np array
import matplotlib.pyplot as plt
from textwrap import wrap # to wrap plot titles
import pandas as pd
from statannot import add_stat_annotation

# -------> choose method (ward or average)
linkage_method_chosen = "ward_section"
# linkage_method_chosen = "average_moyenne"
# -------> choose num clusters wanted
# num_clusters_wanted = 3
num_clusters_wanted = 4
# num_clusters_wanted = 5

# ### Loading data sent by Sylvie
#---set the name of the sheet where the data of the cohort is
filepath_1cohort_gex_data_ATIP3probesonly= "/data_warehouse/outputs/atip3_ml_dataset_type1/GSE23988_ATIP3probesetsonly_probesnames_3x61_GEX.csv"
sep_in_file = ","
df_file = pd.read_csv(filepath_1cohort_gex_data_ATIP3probesonly, sep_in_file)
# rename the probes column before putting it as index (so that later we can have a nice titles for the probes)
df_file.rename(columns={"Unnamed: 0" : "MTUS1 probes"}, inplace=True)
# put the rownames (genes) as index
df_file = df_file.set_index(list(df_file.columns)[0]) # because a csv from R has the rownames becoming the first col
# transform the df to pu the genes as colnames
df_file_fts_only = df_file.transpose()

#####-----checkpoint to verify the data types
print("----A checkpoint to check on joined table dtypes (first 5 columns and last 5 columns) in order to know what dtypes to convert...")
print(df_file_fts_only.info())  # on the model of df_joined[df_joined.columns[:10]].dtypes
####-----

# Extract data matrix
X = np.array(df_file_fts_only)
X.shape

# ### Scale features  ##! to check in R : if scaling fts is really doing standardization (x-u/std)
from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)

# ## Hierarchical clustering with scipy
from scipy import cluster

# Perform clustering
if linkage_method_chosen == "ward_section":
    link_matrix = cluster.hierarchy.linkage(X_scaled, method='ward', metric='euclidean', optimal_ordering=True)  ##! to check in R : optimal ordering for a better view
elif linkage_method_chosen == "average_moyenne":
    link_matrix = cluster.hierarchy.linkage(X_scaled, method='average', metric='euclidean', optimal_ordering=True) ##! to check in R : optimal ordering for a better view

# Obtain the column of clusters in order to add them as a column later
cluster_assignment = cluster.hierarchy.cut_tree(link_matrix, n_clusters=num_clusters_wanted) # num_clusters_wanted is the num of clusters (3 or 4)
cluster_assignment = cluster_assignment.reshape((cluster_assignment.shape[0], ))

# ## Visualization with seaborn
import seaborn as sns
#print(sns.__version__)

# Create a new data frame with scaled data
df_X_scaled = df_file_fts_only
for idx, col in enumerate(df_X_scaled.columns):
    df_X_scaled[col] = X_scaled[:, idx]

# Add cluster assignment to data frame
df_X_scaled['cluster'] = cluster_assignment

# Color palette used inside the heatmap ()
my_heatmap_color_palette = sns.diverging_palette(20, 220, l=60, n=9, center="dark") # by Chloé
# my_heatmap_color_palette = sns.diverging_palette(150, 10, l=60, n=9, center="dark") # proposed to compare better with Sylvies's hm
# sns.palplot(my_color_palette) # use this line to show the heatmap inside colors color palette

# Create a vector of colors corresponding to the 'cluster' column
# my_palette = dict(zip(np.unique(df_scaled.cluster), ["darkorange", "khaki", "sienna"])) # by Chloé
if num_clusters_wanted == 3:
    my_list_of_clusters_colors = ["green", "blue", "red"]
    my_palette_for_row_colors = dict(zip(np.unique(df_X_scaled.cluster), my_list_of_clusters_colors)) # proposed because easir to use when discussing the cluster that is ATIP3 low
elif num_clusters_wanted == 4:
    my_list_of_clusters_colors = ["green", "blue", "red","khaki"]
    my_palette_for_row_colors = dict(zip(np.unique(df_X_scaled.cluster), my_list_of_clusters_colors))  # proposed because easir to use when discussing the cluster that is ATIP3 low
elif num_clusters_wanted == 5:
    my_list_of_clusters_colors = ["green", "blue", "red","khaki","orange"]
    my_palette_for_row_colors = dict(zip(np.unique(df_X_scaled.cluster), my_list_of_clusters_colors))  # proposed because easir to use when discussing the cluster that is ATIP3 low
cluster_row_colors = df_X_scaled.cluster.map(my_palette_for_row_colors)


# Plot cluster heatmap + dendrogram ##! at the start make sure samples are in index from col titled CLETRI and only number as sample name
list_of_cols_to_drop_from_df_X_scaled = ['cluster']
seaborn_cluster = sns.clustermap(df_X_scaled.drop(columns=list_of_cols_to_drop_from_df_X_scaled),
                                 col_cluster=False, # do not cluster columns
                                 row_linkage=link_matrix, # use previously computed cluster assignment
                                 cbar_pos=(0.8,0.015,0.05, 0.1), # position of the colorbar cbar_pos(left, bottom, width, height), optional # old values cbar_pos=(1.2, 0.7, 0.05, 0.1)
                                 cmap=my_heatmap_color_palette,
                                 row_colors=cluster_row_colors, # use cluster colors to color rows on the left
                                 figsize=(5, 8))
# seaborn_cluster.savefig(filename_hm, bbox_inches='tight') ##! not needed due to screenshots are taken

# add a column of the clusters names (low, med, high or low,low_med, med_high, high) # choosen clusters following what we see
print("The attributed colors to clusters were : ",my_palette_for_row_colors) # shows {0: 'green', 1: 'blue', 2: 'red', 3: 'khaki'}
# clusters_placement_dictionary ={0 : "med", 1 : "low", 2 : "high"} # use this for 3 clusters
clusters_placement_dictionary ={3 : "low", 0 : "low_med", 1 : "med_high", 2 : "high"} # use this for 4 clusters {0: 'green', 1: 'blue', 2: 'red', 3: 'khaki'}
# NB : the low half of the cluster 2/4 can be added to the cluster 1 is we do 5 clusters
# clusters_placement_dictionary ={4 : "low", 0 : "low", 2 : "low_med", 3 : "med_high", 1 : "high"} # use this for 5 clusters {0: 'green', 1: 'blue', 2: 'red', 3: 'khaki', 4: 'orange'}
df_X_scaled['ATIP3_class_hm'] = df_X_scaled['cluster'].map(clusters_placement_dictionary)
# add the columns of the hormonal profiles
filepath_1cohort_ph_data_ATIP3probesonly= "/data_warehouse/outputs/atip3_ml_dataset_type1/GSE23988_ATIP3probesetsonly_probesnames_61x3_ph.csv"
sep_in_file = ","
df_file_ph = pd.read_csv(filepath_1cohort_ph_data_ATIP3probesonly, sep_in_file)
# put the rownames (genes) as index
df_file_ph = df_file_ph.set_index(list(df_file_ph.columns)[0]) # because a csv from R has the rownames becoming the first col
# drop the not needed cols and rename the not so nicely written
df_file_ph.drop('geo_accession', axis=1, inplace=True)
# df_file_ph.drop('treatment', axis=1, inplace=True)
df_file_ph.columns # show the columns in order to copy past the names when renaming them
old_cols_list = ["ER_status","pCR_status"]
new_cols_list = ["RO_status","RCH"]
dict2renamecols = dict(zip(old_cols_list, new_cols_list))
df_file_ph.rename(columns=dict2renamecols, inplace=True)
df_file_ph["RCH"].replace(["No","Yes"], [0, 1], inplace=True) # reencode the RCH as 0 and 1 (No and Yes previously)
# #----exceptional addition of the info of pCR status
# supporting_file_path = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/atip3_material/Sample_Names_correspondance/R02 pour Amad.xlsx"
# sheet_id = 1
# df_sup_file = pd.read_excel(supporting_file_path) # get a table containing the pCR status (RCH)
# list_of_cols_to_keep = ["!Sample_geo_accession","RCH"]
# df_sup_file = df_sup_file[list_of_cols_to_keep]
# print(df_sup_file.info())
# pcr0 = df_sup_file[df_sup_file.RCH==0] # 185
# pcr1 = df_sup_file[df_sup_file.RCH==1] # 36
# pcr_not_defined = df_sup_file[(df_sup_file.RCH !=0) & (df_sup_file.RCH !=1)] # 5
# df_sup_file = df_sup_file.set_index(list(df_sup_file.columns)[0]) # because a csv from R has the rownames becoming the first col
# df_file_ph = pd.merge(df_file_ph, df_sup_file, left_index=True, right_index=True)
# #----end of exceptional addition

# join the ph info table with the gex table
df_X_scaled_joined = pd.merge(df_X_scaled, df_file_ph, left_index=True, right_index=True)
# make the new row colors
RO_row_colors = df_X_scaled_joined.RO_status.map({"negative": 'red', "positive": 'green'})
# PR_row_colors = df_X_scaled_joined.PR_status.map({"negative": 'red', "positive": 'green'})
# HER2_row_colors = df_X_scaled_joined.HER2_status.map({"negative": 'red', "positive": 'green'})
# TN_row_colors = df_X_scaled_joined.TN_status.map({"no": 'green', "yes": 'red'})
pCR_row_colors = df_X_scaled_joined.RCH.map({0: 'grey', 1: 'skyblue'})
all_row_colors1 = pd.concat([RO_row_colors,pCR_row_colors,cluster_row_colors],axis=1) # ,RO_row_colors,PR_row_colors,HER2_row_colors removed to be added for more info on hormonal statuses
# Plot the cluster heatmap + dendrogram again but this time with the additional hormonal row colors
list_of_cols_to_drop_from_joined_table = ['cluster',"ATIP3_class_hm","RO_status","RCH"]
seaborn_cluster = sns.clustermap(df_X_scaled_joined.drop(columns=list_of_cols_to_drop_from_joined_table),
                                 col_cluster=False, # do not cluster columns
                                 row_linkage=link_matrix, # use previously computed cluster assignment,
                                 cbar_pos=(0.8,0.015,0.05, 0.1), # position of the colorbar cbar_pos(left, bottom, width, height), optional # old values cbar_pos=(1.2, 0.7, 0.05, 0.1)
                                 cmap=my_heatmap_color_palette,
                                 row_colors=all_row_colors1, # use a df of row colors as cols or a list (of max 3) row_colors to color rows on the left
                                 figsize=(5, 8))
# #>>>>>>>>>>>>>> optional saving to get a file with the clusters and the treatment if present
# df_X_scaled_joined_full = df_X_scaled_joined
# fullname_file_w_treatment_and_clusters = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE23988_ATIP3probesetsonly_InfoTreatmentCluster.csv"
# df_X_scaled_joined_full.to_csv(fullname_file_w_treatment_and_clusters, header=True) # we keep the index for a future joining w tables of fts
# print("File saved !")
# #>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>special restriction on the samples from taxanes treated patients only
df_X_scaled_joined_all = df_X_scaled_joined
# df_X_scaled_joined = df_X_scaled_joined[(df_X_scaled_joined.treatment=="treatment arm: Paclitaxel")]
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>> For the cohort analysed, give a report
print("For the cohort analysed, we found :")
for a_cluster_num in range(num_clusters_wanted):
    print("- a cluster of size :",len(df_X_scaled_joined[df_X_scaled_joined.cluster==a_cluster_num]),"colored in",my_list_of_clusters_colors[a_cluster_num])
print("For the cohort analysed, the population stratification is :")
tab_pCR = df_X_scaled_joined[df_X_scaled_joined.RCH==1] # the pCR status (2 groups)
tab_NpR = df_X_scaled_joined[df_X_scaled_joined.RCH==0]
tab_pCR_low = df_X_scaled_joined[(df_X_scaled_joined.RCH==1) &(df_X_scaled_joined.ATIP3_class_hm=="low")] # the pCR=1 for each of the 4 clusters
tab_pCR_low_med = df_X_scaled_joined[(df_X_scaled_joined.RCH==1) &(df_X_scaled_joined.ATIP3_class_hm=="low_med")]
tab_pCR_med_high = df_X_scaled_joined[(df_X_scaled_joined.RCH==1) &(df_X_scaled_joined.ATIP3_class_hm=="med_high")]
tab_pCR_high = df_X_scaled_joined[(df_X_scaled_joined.RCH==1) &(df_X_scaled_joined.ATIP3_class_hm=="high")]
tab_NpR_low = df_X_scaled_joined[(df_X_scaled_joined.RCH==0) &(df_X_scaled_joined.ATIP3_class_hm=="low")] # the pCR=0 for each of the 4 clusters
tab_NpR_low_med = df_X_scaled_joined[(df_X_scaled_joined.RCH==0) &(df_X_scaled_joined.ATIP3_class_hm=="low_med")]
tab_NpR_med_high = df_X_scaled_joined[(df_X_scaled_joined.RCH==0) &(df_X_scaled_joined.ATIP3_class_hm=="med_high")]
tab_NpR_high = df_X_scaled_joined[(df_X_scaled_joined.RCH==0) &(df_X_scaled_joined.ATIP3_class_hm=="high")]
tab_TN_low = df_X_scaled_joined[(df_X_scaled_joined.RO_status=="negative") &(df_X_scaled_joined.ATIP3_class_hm=="low")] # the TNBC & low  (IN ALL THE FOLLOWING INSTEAD OF THE TNBC WE DID THE ER_STATUS)
tab_TN_low_med = df_X_scaled_joined[(df_X_scaled_joined.RO_status=="negative") &(df_X_scaled_joined.ATIP3_class_hm=="low_med")] # the TNBC & low_med
tab_TN_med_high = df_X_scaled_joined[(df_X_scaled_joined.RO_status=="negative") &(df_X_scaled_joined.ATIP3_class_hm=="med_high")] # the TNBC & med_high
tab_TN_high = df_X_scaled_joined[(df_X_scaled_joined.RO_status=="negative") &(df_X_scaled_joined.ATIP3_class_hm=="high")] # the TNBC & high
tab_TN_low_pCR = df_X_scaled_joined[(df_X_scaled_joined.RCH==1) &(df_X_scaled_joined.RO_status=="negative") &(df_X_scaled_joined.ATIP3_class_hm=="low")] # the TNBC & low with pCR
tab_TN_low_med_pCR = df_X_scaled_joined[(df_X_scaled_joined.RCH==1) &(df_X_scaled_joined.RO_status=="negative") &(df_X_scaled_joined.ATIP3_class_hm=="low_med")] # the TNBC & low_med with pCR
tab_TN_low_NpR = df_X_scaled_joined[(df_X_scaled_joined.RCH==0) &(df_X_scaled_joined.RO_status=="negative") &(df_X_scaled_joined.ATIP3_class_hm=="low")] # the TNBC & low with NpR
tab_TN_low_med_NpR = df_X_scaled_joined[(df_X_scaled_joined.RCH==0) &(df_X_scaled_joined.RO_status=="negative") &(df_X_scaled_joined.ATIP3_class_hm=="low_med")] # the TNBC & low_med with NpR
print("- Number of pCR :",len(tab_pCR)) # the pCR status (2 groups)
print("- Number of NpR :",len(tab_NpR))
print("- Number of pCR & low :",len(tab_pCR_low)) # the pCR=1 for each of the 4 clusters
print("- Number of pCR & low-med :",len(tab_pCR_low_med))
print("- Number of pCR & med-high :",len(tab_pCR_med_high))
print("- Number of pCR & high :",len(tab_pCR_high))
print("- Number of NpR & low :",len(tab_NpR_low)) # the pCR=0 for each of the 4 clusters
print("- Number of NpR & low-med :",len(tab_NpR_low_med))
print("- Number of NpR & med-high :",len(tab_NpR_med_high))
print("- Number of NpR & high :",len(tab_NpR_high))
print("- Number of TN & low :",len(tab_TN_low)) # the TNBC & low
print("- Number of TN & low-med :",len(tab_TN_low_med)) # the TNBC & low_med
print("- Number of TN & med-high :",len(tab_TN_med_high)) # the TNBC & med_high
print("- Number of TN & high :",len(tab_TN_high)) # the TNBC & high
print("- Number of TN & low & pCR :",len(tab_TN_low_pCR)) # the TNBC & low with pCR
print("- Number of TN & low_med & pCR :",len(tab_TN_low_med_pCR)) # the TNBC & low_med with pCR
print("- Number of TN & low & NpR :",len(tab_TN_low_NpR)) # the TNBC & low with NpR
print("- Number of TN & low_med & NpR :",len(tab_TN_low_med_NpR)) # the TNBC & low_med with NpR
# print("- Number of TN & low+low-med :",len(tab_TN_low)+len(tab_TN_low_med)) # the TNBC on the low & low_med together

# >>>>>>>>>>>plot all on one

# line 1 points
x1 = ["high","med-high","low-med","low"]
y1 = [len(tab_pCR_high),len(tab_pCR_med_high),len(tab_pCR_low_med),len(tab_pCR_low)]
# plotting the line 1 points
plt.plot(x1, y1, label = "# pCR samples",marker='o', markerfacecolor='blue', markersize=6)
# labelling the line 1 points
for x,y in zip(x1,y1):
    label = "{}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 color='blue',
                 textcoords="offset points", # how to position the text
                 xytext=(5,-12), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# line 2 points
x2 = ["high","med-high","low-med","low"]
y2 = [len(tab_NpR_high),len(tab_NpR_med_high),len(tab_NpR_low_med),len(tab_NpR_low)]
# plotting the line 2 points
plt.plot(x2, y2, label = "# NpR samples",marker='o', markerfacecolor='orange', markersize=6)
# labelling the line 2 points
for x,y in zip(x2,y2):
    label = "{}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 color='orange',
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# # line 3 points (the TNBC across the clusters)
# x3 = ["high","med-high","low-med","low"]
# y3 = [len(tab_TN_high),len(tab_TN_med_high),len(tab_TN_low_med),len(tab_TN_low)]
# # plotting the line 3 points
# plt.plot(x3, y3, label = "# TNBC samples",marker='^', markerfacecolor='olive', markersize=6, color='olive', linewidth=2, linestyle='dashed')
# # labelling the line 3 points
# for x,y in zip(x3,y3):
#     label = "{}".format(y)
#     plt.annotate(label, # this is the text
#                  (x,y), # this is the point to label
#                  color='olive',
#                  textcoords="offset points", # how to position the text
#                  xytext=(-5,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center
plt.xlabel('ATIP3 clusters ')
# Set the y axis label of the current axis.
plt.ylabel('Numbers of samples')
# Set a title of the current axes.
# plt.title('Stratification following 4 clusters of ATIP3 expression and the pCR status.')
plt.title("\n".join(wrap("Stratification following 4 clusters of ATIP3 expression and the pCR status.")), fontsize=12)
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()

#>>>>>>>>>>>>>>>>>>>>>make the boxplot
df_X_scaled_joined_all.columns # show to the columns of the full table
list_of_cols_for_boxplots_of_expressions = ["212093_s_at","212095_s_at","212096_s_at","ATIP3_class_hm" ]
df_X_scaled_joined_for_boxplot = df_X_scaled_joined_all[list_of_cols_for_boxplots_of_expressions]
df_X_scaled_joined_for_boxplot.rename(columns={"212096_s_at":"212096_s_at_(best_probeset)","ATIP3_class_hm":"ATIP3_classes_from_heatmap"}, inplace=True)
df_X_scaled_joined_for_boxplot_mdf = pd.melt(df_X_scaled_joined_for_boxplot,id_vars=['ATIP3_classes_from_heatmap'], var_name=['Probesets']) # MELT
chosen_data = df_X_scaled_joined_for_boxplot_mdf
chosen_x = "Probesets"
chosen_x_order = ["212093_s_at","212095_s_at","212096_s_at_(best_probeset)"]
chosen_y = "value"
chosen_hue = "ATIP3_classes_from_heatmap"
chosen_hue_order = ["low", "low_med", "med_high","high"]
chosen_box_pairs=[
    (("212093_s_at", "low"), ("212093_s_at", "low_med")),
    (("212093_s_at", "med_high"), ("212093_s_at", "high")),
    (("212095_s_at", "low"), ("212095_s_at", "low_med")),
    (("212095_s_at", "med_high"), ("212095_s_at", "high")),
    (("212096_s_at_(best_probeset)", "low"), ("212096_s_at_(best_probeset)", "low_med")),
    (("212096_s_at_(best_probeset)", "med_high"), ("212096_s_at_(best_probeset)", "high")),
    ]
ax = sns.boxplot(data=chosen_data, x=chosen_x, order=chosen_x_order, y=chosen_y, hue=chosen_hue, hue_order=chosen_hue_order)  # df_file_phRUN PLOT
ax, test_results = add_stat_annotation(ax, data=chosen_data, x=chosen_x, y=chosen_y, order=chosen_x_order,hue=chosen_hue, hue_order=chosen_hue_order,
                                   box_pairs=chosen_box_pairs, test='Mann-Whitney', text_format='star', loc='inside', verbose=2)
# plt.legend(loc='upper left', bbox_to_anchor=(1.03, 1))
# plt.show()
#>>>>>>>>>>>>>>>>>>>>>

