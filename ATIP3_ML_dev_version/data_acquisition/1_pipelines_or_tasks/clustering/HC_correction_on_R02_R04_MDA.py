#!/usr/bin/env python
# coding: utf-8

# ## Exploring hierarchical clustering of REMAGUS02 cohort
# imports
import numpy as np
from numpy import seterr,isneginf # used to manage the change into log2 o values in a np array
import matplotlib.pyplot as plt
import pandas as pd

# -------> choose method (ward or average)
linkage_method_chosen = "ward_section"
# linkage_method_chosen = "average_moyenne"
# -------> choose num clusters wanted
num_clusters_wanted = 3
# num_clusters_wanted = 4
# -------> choose to change matrix values in log2
change_in_log2_fts_values = "no"
# change_in_log2_fts_values = "yes"
# -------> choose the cohort to explore
cohort_used = "REMAGUS02"
# cohort_used = "REMAGUS04"
# cohort_used = "MDAnderson"
#>>>> rules that comes from cohort choice
#---set the name of the sheet where the data of the cohort is
all3cohorts_samplesOnTaxanesOnly_file_path = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/3_results/res_clustering/Clustering pour Amad 180520.xls"
sep_in_file = "\t"
if cohort_used == "REMAGUS02":
    sheet_id = "R02"
    sample_col_name = "CLETRI"
    list_additionnal_cols_to_drop_for_probes_only = ['GROUPE']
    filename_hm = "trial1_py_HCHM_R02.png"
    if num_clusters_wanted == 3 :
        low_expression_cluster_num_found = 0
    elif num_clusters_wanted == 4 :
        low_expression_cluster_num_found = 0
elif cohort_used == "REMAGUS04":
    sheet_id = "R04"
    sample_col_name = "cletri"
    list_additionnal_cols_to_drop_for_probes_only = []
    filename_hm = "trial1_py_HCHM_R04.png"
    if num_clusters_wanted == 3:
        low_expression_cluster_num_found = 1
    elif num_clusters_wanted == 4:
        low_expression_cluster_num_found = 1
elif cohort_used == "MDAnderson":
    sheet_id = "MDA"
    sample_col_name = "row.names"
    list_additionnal_cols_to_drop_for_probes_only = []
    filename_hm = "trial1_py_HCHM_MDA.png"
    if num_clusters_wanted == 3:
        if change_in_log2_fts_values == "yes":
            low_expression_cluster_num_found = 2
        else:
            low_expression_cluster_num_found = 1
    elif num_clusters_wanted == 4:
        if change_in_log2_fts_values == "yes":
            low_expression_cluster_num_found = 2
        else:
            low_expression_cluster_num_found = 1
else: # when no cohort is chosen
    sheet_id = "Unknown"
    sample_col_name = "Unknown"
    list_additionnal_cols_to_drop_for_probes_only = []
    filename_hm = "Unknown"
    low_expression_cluster_num_found = "Unknown"
    print("No cohort has been chosen for preprocessing")


# ### Loading data sent by Sylvie
# df = pd.read_csv("/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/heatmaps_correction/r02_clustering_sylvie.csv", index_col=0, sep='\t')
df = pd.read_excel(all3cohorts_samplesOnTaxanesOnly_file_path,sheet_id)
# rename the samples col and set it as index
df.rename(columns={df.columns[0]:'Samples'}, inplace=True)
df = df.set_index('Samples')

#print(df.head())
#print(len(df))

# Rename last column with a more manageable name
df.rename(columns={df.columns[-1]:'ATIP3_classes'}, inplace=True)

# Names of the ATIP3 low samples
sylvie_atip3_low_names = df[df.ATIP3_classes==1].index
sylvie_atip3_med_names = df[df.ATIP3_classes==2].index
sylvie_atip3_high_names = df[df.ATIP3_classes==3].index
# Number of ATIP3 low samples
#print(len(sylvie_atip3_low_names))

# Extract data matrix
X = np.array(df.drop(columns=["ATIP3_classes"]+list_additionnal_cols_to_drop_for_probes_only))
X.shape

# change the values of the matrix in log2
if change_in_log2_fts_values == "yes":
    #####--------> special operation : change all values here in log2 because they are not
    seterr(divide='ignore')
    X = np.log2(X)
    seterr(divide='warn')
    X[isneginf(X)] = 0
    #####--------> special operation (end)


# ## Data exploration

fig = plt.figure(figsize=(8, 8))
# Histograms for continuous features
for idx in range(X.shape[1]):
    # create a subplot in the (idx+1) position of a 2x2 grid
    ax = fig.add_subplot(2, 2, (idx+1))
    # plot the histogram of idx
    h = ax.hist(X[:, idx], bins=20, edgecolor='none')
    # use the name of the feature as a title for each histogram
    if cohort_used == "REMAGUS02":
        ax.set_title(df.columns[idx+1])
    else:
        ax.set_title(df.columns[idx])
# title for the entire figure
fig.suptitle('ATIP3 probes values distribution of cohort '+cohort_used)
# espacement entre les subplots
# fig.tight_layout(pad=1.0)


# ### Scale features  ##! to check in R : if scaling fts is really doing standardization (x-u/std)
from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)

fig = plt.figure(figsize=(8, 8))
# Histograms for continuous features
for idx in range(X_scaled.shape[1]):
    # create a subplot in the (idx+1) position of a 2x2 grid
    ax = fig.add_subplot(2, 2, (idx+1))
    # plot the histogram of idx
    h = ax.hist(X_scaled[:, idx], bins=20, edgecolor='none')
    # use the name of the feature as a title for each histogram
    if cohort_used == "REMAGUS02":
        ax.set_title(df.columns[idx + 1])
    else:
        ax.set_title(df.columns[idx])
# title for the entire figure
fig.suptitle('Scaled ATIP3 probes values distribution of cohort '+cohort_used)
# espacement entre les subplots
# fig.tight_layout(pad=1.0)


# ## Hierarchical clustering with scipy
from scipy import cluster

# Perform clustering
if linkage_method_chosen == "ward_section":
    link_matrix = cluster.hierarchy.linkage(X_scaled, method='ward', metric='euclidean', optimal_ordering=True)  ##! to check in R : optimal ordering for a better view
elif linkage_method_chosen == "average_moyenne":
    link_matrix = cluster.hierarchy.linkage(X_scaled, method='average', metric='euclidean', optimal_ordering=True) ##! to check in R : optimal ordering for a better view

# Obtain 3 clusters
cluster_assignment = cluster.hierarchy.cut_tree(link_matrix, n_clusters=num_clusters_wanted) # num_clusters_wanted is the num of clusters (3 or 4)
cluster_assignment = cluster_assignment.reshape((cluster_assignment.shape[0], ))


# ## Visualization with seaborn
import seaborn as sns
#print(sns.__version__)

# Color palette
my_color_palette = sns.diverging_palette(20, 220, l=60, n=9, center="dark") # by Chloé
# my_color_palette = sns.diverging_palette(150, 10, l=60, n=9, center="dark") # proposed to compare better with Sylvies's hm
sns.palplot(my_color_palette)

# Create a new data frame with scaled data
df_scaled = df.drop(columns=[df.columns[-1]]+list_additionnal_cols_to_drop_for_probes_only)
for idx, col in enumerate(df_scaled.columns):
    df_scaled[col] = X_scaled[:, idx]

# Add cluster assignment to data frame
df_scaled['cluster'] = cluster_assignment

# Create a vector of colors corresponding to the 'cluster' column
# my_palette = dict(zip(np.unique(df_scaled.cluster), ["darkorange", "khaki", "sienna"])) # by Chloé
if num_clusters_wanted == 3:
    my_palette = dict(zip(np.unique(df_scaled.cluster), ["green", "blue", "red"])) # proposed because easir to use when discussing the cluster that is ATIP3 low
elif num_clusters_wanted == 4:
    my_palette = dict(zip(np.unique(df_scaled.cluster), ["green", "blue", "red","khaki"]))  # proposed because easir to use when discussing the cluster that is ATIP3 low
cluster_row_colors = df_scaled.cluster.map(my_palette)

# Plot cluster heatmap + dendrogram ##! at the start make sure samples are in index from col titled CLETRI and only number as sample name
seaborn_cluster = sns.clustermap(df_scaled.drop(columns=['cluster']),
                                 col_cluster=False, # do not cluster columns
                                 row_linkage=link_matrix, # use previously computed cluster assignment
                                 cbar_pos=(1.2, 0.7, 0.05, 0.1), # position of the colorbar
                                 cmap=my_color_palette,
                                 row_colors=cluster_row_colors, # use cluster colors to color rows on the left
                                 figsize=(5, 8))
seaborn_cluster.savefig(filename_hm, bbox_inches='tight')


# For Remagus02, the orange cluster (number 0) corresponds to low expression across all probes.
# For Remagus04, the khaki cluster (number 1) corresponds to low expression across all probes.
# For MDAnderson, the khaki cluster (number 1) corresponds to low expression across all probes.
# >>>>>>> For the cohort analysed, give a report
# a reminder of the cohort analysed :
print("The cohort analysed is :",cohort_used)
print("we found : ")
for a_cluster_num in range(num_clusters_wanted):
    print("- a cluster of size :",len(df_scaled[df_scaled.cluster==a_cluster_num]))
print("whereas Sylvie's results found : ")
print("- a low values cluster of size : ",len(sylvie_atip3_low_names))
print("- a med values cluster of size : ",len(sylvie_atip3_med_names))
print("- a high values cluster of size : ",len(sylvie_atip3_high_names))
# ## Compare cluster 0 to the one identified by Sylvie
# Restrict df_scaled to the rows for which my cluster assignment is 0 and report on its size, members, intersection, and difference with Sylvie finding
my_atip3_low = df_scaled[df_scaled.cluster==low_expression_cluster_num_found]

# get the size
print("We found %d ATIP3 low samples" % len(my_atip3_low))
# Get their names
my_atip3_low_names = my_atip3_low.index
print("Our ATIP3 low samples:", my_atip3_low_names)

# get the size (sylvie's finding)
print("Sylvie has found %d ATIP3 low samples" % len(sylvie_atip3_low_names))
# get the names (sylvie's finding)
print("Sylvie's ATIP3 low samples:", sylvie_atip3_low_names)

print("The size of the intersection is:", len(set(my_atip3_low_names).intersection(set(sylvie_atip3_low_names))))

print("There are %d samples that differ" % (len(set(my_atip3_low_names).difference(set(sylvie_atip3_low_names)))+len(set(sylvie_atip3_low_names).difference(set(my_atip3_low_names)))))

