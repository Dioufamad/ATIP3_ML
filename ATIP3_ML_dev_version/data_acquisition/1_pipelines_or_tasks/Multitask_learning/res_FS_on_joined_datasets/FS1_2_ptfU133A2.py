
# Objective : do the FS idea1 thinking 2 for the platform "Affymetrix HG U133A 2.0"
'''
FS idea 1 : All 6 datasets, when they are joined keeping only the 12034 common features, form one dataset of 72204 features.
If we decide to use all the gallery of features in each implicated dataset, the max number of launchable features (46 340) force us to use only 3 datasets accounting for 36 102 features.
Q1 : How do we choose the 3 datasets to use ?
+ thinking “the dataset that are the closest in the making”, we can select at most 3 datasets of each platform

'''


#>>>>>>>>>>>imports
import pandas as pd
import matplotlib.pyplot as plt


#>>>>>>>>>>bring in the data
# - link for the common fts joined dataset to use as base and restrict
filepath_of_ml_dataset1= "/data_warehouse/outputs/atip3_unified_datasets/JoinNewDesign1CommonFtsof6_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"
local_link_to_csv_dataset = filepath_of_ml_dataset1
df = pd.read_csv(local_link_to_csv_dataset) # read the dataset in a df and an option is "sep_in_file = ","" to precise what was the separator in the file
# when the first column was kept because it was the previous index, we can put it back as index with this
df.rename(columns={"Unnamed: 0" : "samples_names"}, inplace=True)
df = df.set_index(list(df.columns)[0])

#>>>> restrict the df to only the 3 cohorts to keep
# - restrict on the rows (samples)
# list of cohorts present
list_of_cohorts_present = df["cohort"].unique()
print("- This is the list of cohorts present : ")
print(list_of_cohorts_present)
# from results of precedent manipulations, we know that there is only 2 cohorts for this platform
list_of_3_cohorts_with_most_samples = ["GSE41998","GSE63471"]
# lets restricted to only those cohorts (we are waiting for a total of 57+29 = 86 samples
df_restricted1 = df[df['cohort'].isin(list_of_3_cohorts_with_most_samples)] # has 85 samples ##: check later why the last dt has 28 samples instead of 29 samples as noted previously
# - restrict on the columns (features)
# idea : we could have remade a script that uses the only needed cohorts.
# but an easier way is to remove the features that dont contain in their names the designation of the cohorts to keep
list_all_cols_df_restricted1 = list(df_restricted1.columns)
# list_all_cols_df_restricted1.remove("Y_pCR") # not necessary
# list_all_cols_df_restricted1.remove("cohort") # not necessary
list_of_tags_for_cohorts_2keep_their_features = ["_in_GSE41998","_in_GSE63471"]
list_all_cols_df_with_fts_2keep_only = []
for ft_2keep_or_not in list_all_cols_df_restricted1:
    if any(a_tag_of_feature_2keep in ft_2keep_or_not for a_tag_of_feature_2keep in list_of_tags_for_cohorts_2keep_their_features):
        list_all_cols_df_with_fts_2keep_only.append(ft_2keep_or_not)
    # other ways but the .remove() method is not working with them
    # if all(a_tag_of_feature_2keep not in ft_2keep_or_not for a_tag_of_feature_2keep in list_of_tags_for_cohorts_2keep_their_features):
    # if not any(ft_2keep_or_not.endswith(a_tag_of_feature_2keep) for a_tag_of_feature_2keep in list_of_tags_for_cohorts_2keep_their_features): # endswith() method
    # if ('GSE41998' not in ft_2keep_or_not) and ('GSE26639' not in ft_2keep_or_not) and ('GSE20194' not in ft_2keep_or_not):
        # list_all_cols_df_with_fts_only.remove(ft_2keep_or_not)
# features restricted
# lets get the resulting df
list_all_cols_df_with_fts_2keep_only_plus2 = list_all_cols_df_with_fts_2keep_only + ["Y_pCR","cohort"]
df_restricted2 = df_restricted1[list_all_cols_df_with_fts_2keep_only_plus2]
# >>>> show an image of entire dataframe to have an overview of the zeros
list_all_cols_df_restricted2 = list(df_restricted2.columns)
list_all_cols_df_restricted2.remove("Y_pCR")
list_all_cols_df_restricted2.remove("cohort")
df_restricted2_4_image = df_restricted2.copy()
df_restricted2_4_image = df_restricted2_4_image[list_all_cols_df_restricted2]
df_restricted2_4_image[df_restricted2_4_image != 0.0] = 999
# Let's look at this new design matrix and check it's blocks in diagonal, with each data set features info forming one block
plt.imshow(df_restricted2_4_image, cmap='viridis', aspect='auto')
plt.colorbar()
# succession of cohorts on the Y axis is needed
list_of_cohorts_in_Yaxis_of_data_image = df_restricted2["cohort"].unique()
print("- This is the succession of cohorts on the Y axis of the data image : ")
print(list_of_cohorts_in_Yaxis_of_data_image)
# keep the image and use it as proof

# >>>>>> check the datatypes
df_restricted2.info()
# Index: 85 entries, GSM1030229 to GSM1550523
# Columns: 24070 entries, A1CF_in_GSE41998 to cohort
# dtypes: float64(24068), int64(1), object(1)
# memory usage: 15.6+ MB

#>>>> saving the df
fullname_file_of_df = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/JoinNewDesign1CommonFtsof6_FSidea1thinking2ptfU133A2_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"
df_restricted2.to_csv(fullname_file_of_df, header=True) # we keep the index for a future joining w tables of fts
print("File saved !")
#>>>>>>>>>>>>>>