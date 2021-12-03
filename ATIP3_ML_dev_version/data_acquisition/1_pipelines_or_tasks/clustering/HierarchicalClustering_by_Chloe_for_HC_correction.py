#!/usr/bin/env python
# coding: utf-8

# ## Exploring hierarchical clustering of REMAGUS02 cohort
#get_ipython().run_line_magic('pylab', 'inline')
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

# ### Loading data sent by Sylvie
df = pd.read_csv("r02_clustering_sylvie.csv", index_col=0, sep='\t')
#print(df.head())
#print(len(df))

# Rename last column with a more manageable name
df.rename(columns={df.columns[-1]:'ATIP3_classes'}, inplace=True)

# Names of the ATIP3 low samples
sylvie_atip3_low_names = df[df.ATIP3_classes==1].index

# Number of ATIP3 low samples
#print(len(sylvie_atip3_low_names))

# Extract data matrix
X = np.array(df.drop(columns=['ATIP3_classes', 'GROUPE']))
X.shape

# ## Data exploration

fig = plt.figure(figsize=(8, 8))
# Histograms for continuous features
for idx in range(X.shape[1]):
    # create a subplot in the (idx+1) position of a 2x2 grid
    ax = fig.add_subplot(2, 2, (idx+1))
    # plot the histogram of idx
    h = ax.hist(X[:, idx], bins=20, edgecolor='none')
    # use the name of the feature as a title for each histogram
    ax.set_title(df.columns[idx+2])
plt.title("Features")
# espacement entre les subplots
fig.tight_layout(pad=1.0)


# ### Scale features 
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
    ax.set_title(df.columns[idx+2])
# espacement entre les subplots
plt.title("Scaled features")
fig.tight_layout(pad=1.0)


# ## Hierarchical clustering with scipy
from scipy import cluster

# Perform clustering
link_matrix = cluster.hierarchy.linkage(X_scaled, method='average', metric='euclidean', optimal_ordering=True)

# Obtain 3 clusters
cluster_assignment = cluster.hierarchy.cut_tree(link_matrix, n_clusters=3)
cluster_assignment = cluster_assignment.reshape((cluster_assignment.shape[0], ))


# ## Visualization with seaborn
import seaborn as sns
#print(sns.__version__)

# Color palette
my_color_palette = sns.diverging_palette(20, 220, l=60, n=9, center="dark") 
sns.palplot(my_color_palette)

# Create a new data frame with scaled data
df_scaled = df.drop(columns=[df.columns[-1], 'GROUPE'])
for idx, col in enumerate(df_scaled.columns):
    df_scaled[col] = X_scaled[:, idx]

# Add cluster assignment to data frame
df_scaled['cluster'] = cluster_assignment

# Create a vector of colors corresponding to the 'cluster' column
my_palette = dict(zip(unique(df_scaled.cluster), ["darkorange", "khaki", "sienna"]))
cluster_row_colors = df_scaled.cluster.map(my_palette)

# Plot cluster heatmap + dendrogram
seaborn_cluster = sns.clustermap(df_scaled.drop(columns=['cluster']), 
                                 col_cluster=False, # do not cluster columns
                                 row_linkage=link_matrix, # use previously computed cluster assignment
                                 cbar_pos=(1.2, 0.7, 0.05, 0.1), # position of the colorbar
                                 cmap=my_color_palette,
                                 row_colors=cluster_row_colors, # use cluster colors to color rows on the left
                                 figsize=(5, 8))
seaborn_cluster.savefig('clustering_remagus02.png', bbox_inches='tight')


# The orange cluster (number 0) corresponds to low expression across all probes.

# ## Compare cluster 0 to the one identified by Sylvie
# Restrict df_scaled to the rows for which my cluster assignment is 0
my_atip3_low = df_scaled[df_scaled.cluster==0]
print("We found %d ATIP3 low samples" % len(my_atip3_low))

# Get their names
my_atip3_low_names = my_atip3_low.index
print("Our ATIP3 low samples:", my_atip3_low_names)

print("Sylvie's ATIP3 low samples:", sylvie_atip3_low_names)

print("The size of the intersection is:", len(set(my_atip3_low_names).intersection(set(sylvie_atip3_low_names))))

print("There are %d samples that differ" % len(set(my_atip3_low_names).difference(set(sylvie_atip3_low_names))))

