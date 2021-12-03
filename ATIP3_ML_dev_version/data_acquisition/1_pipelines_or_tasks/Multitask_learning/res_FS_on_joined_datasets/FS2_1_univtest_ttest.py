# Objective : do the FS idea2 thinking 1 using a univariate test p-values (t-test)

'''
FS idea 2 : On SPAMS, the max amount of launchable features is 46340.
We could ignore the structuration in datasets of the features (if a common feature were to be used, all its versions on the others datasets would be used also).
Ignoring this means we can select the top 46 340 common features among the total 72204 common features.
Q1 : How do we choose those 46340 features among the 72 204 features ?
+	thinking 1 : on the joined dataset of common features, use a univariate test to rank all the features on the basis of
“how likely is it each one is related to the response values observed?” :
the lower the test p-value for a feature is, the more likely related it is) and the top 46340 features are our feature selection

'''

# >>> What is the statistical test used :
# values are floats so we use the student t-test is done instead of a fisher exact test on contigency table of fts var with response
# the T-test for the means of two independent samples of scores from Scipy (see : https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)
# This is a two-sided test for the null hypothesis that 2 independent samples have identical average (expected) values.
# NB : This test assumes that the populations have identical variances by default.
# But, we use equal_var = False because ttest_ind() suppose variance equals by default so underestimates p for unequal variances even if the t-statistic is the same

#>>>>>>>>>>>imports
import pandas as pd
import matplotlib.pyplot as plt
###---------------------IMPORTS FOR the univariate test
import numpy as np
import scipy
from operator import itemgetter # to sort lists of tuples using directly one position in the index elements
from sklearn.preprocessing import LabelEncoder # to change the Response values from string to classes 0 and 1


#>>>>>>>>>>bring in the data
# - link for the common fts joined dataset to use as base and restrict
filepath_of_ml_dataset1= "/data_warehouse/outputs/atip3_unified_datasets/JoinNewDesign1CommonFtsof6_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"
local_link_to_csv_dataset = filepath_of_ml_dataset1
df = pd.read_csv(local_link_to_csv_dataset) # read the dataset in a df and an option is "sep_in_file = ","" to precise what was the separator in the file
# when the first column was kept because it was the previous index, we can put it back as index with this
df.rename(columns={"Unnamed: 0" : "samples_names"}, inplace=True)
df = df.set_index(list(df.columns)[0])

# >>> we have to rank our features on how likely they are induavially contributing to the stratification of the response
# by using a univariate test and the p-values from the lowest to the highest gives us the most contributing to the less contributiing features
# then we restrict our dataset to the top 46340 features and saved it

# we use a previously used implementation of a function that execute one of two univariate tests following if the features values are categorical or floats

# >>> making the needed material for the function that execute one of two univariate tests
# - the frame of fts
df_frame_fts = df.iloc[:, :-2]
# the frame of resp
df_frame_resp = df.loc[:, ["Y_pCR"]]
# the feature_val_type
fts_val_type = "real" # it is just the strings "real" or "cat" to indicate floats or categorical values respectively
# the name of the resp col
resp_col_name = "Y_pCR"
# the encoded classes in the resp
RespClasses_sorted = sorted(df["Y_pCR"].unique())
binary_classes_le = LabelEncoder()  # the encoder
binary_classes_le.fit(RespClasses_sorted)  # encode the classes to memorize
my_encoded_classes = binary_classes_le.classes_

# #### execute these lines to test function of unvariate test
# frame_fts= df_frame_fts
# frame_resp=df_frame_resp
# feature_val_type=fts_val_type
# resp_col=resp_col_name
# encoded_classes=my_encoded_classes
# feat = list(frame_fts)[0]
# # feat = list(frame_fts)[1]
# # feat = list(frame_fts)[2]
# ####

# new versio of the ranker by pval function
def ranker_by_pval_v2(frame_fts,frame_resp,feature_val_type,resp_col,encoded_classes):
	dict_pvalues = {} # a col for all the pvalues computed
	res_indexes = frame_resp.index[frame_resp[resp_col] == encoded_classes[0]].tolist()  # isolate the uniques values for each group of the two response in the population
	sen_indexes = frame_resp.index[frame_resp[resp_col] == encoded_classes[1]].tolist()
	# considering one feature, the 2 groups values can be uniquely described by one unique value each : prfect p_value attributed if the 2 values are different; worst p_value attributed if the 2 values are identifical...
	p_val_top = -1  # ...the p_value value for the perfect differenciation then
	p_val_worst = 1  # ...the p_value value for the worst differenciation then
	if feature_val_type == "cat" : # cases of discrete values, do a fisher exact test on contigency table of fts var with response and extract pvalues
		for feat in list(frame_fts):
			the_resp_samples = frame_fts.loc[res_indexes, [feat]]
			the_sen_samples = frame_fts.loc[sen_indexes, [feat]]
			if (the_resp_samples[feat].nunique(dropna=True) == 1) & (the_sen_samples[feat].nunique(dropna=True) == 1) : # the 2 groups values are uniquely described
				if the_resp_samples[feat].unique()[0] != the_sen_samples[feat].unique()[0]: # by a different unique value
					dict_pvalues[feat] = p_val_top
				else:
					dict_pvalues[feat] = p_val_worst
			else : # not just one unique value exist in each group, the fisher exacttest is done then
				the_feat_col = pd.Categorical(frame_fts[feat],categories=[0,1])
				the_resp_col = pd.Categorical(frame_resp[resp_col],categories=encoded_classes) ## older ["Res","Sen"] is now encoded_classes (an array of shape (2,) ##!! externalise to the for loop to do it only one time ##!! use categories list instead of hard code
				contingency_table_filled = pd.crosstab(the_feat_col,the_resp_col,dropna=False) # dropna=False is used to tell to the system to still count classes that were not predicted
				oddsratio, p_value_f = scipy.stats.fisher_exact(contingency_table_filled, alternative="two-sided")
				dict_pvalues[feat] = p_value_f
	else : # case of reals values, find the two extreme situations of response segregation ability by the feature or do a t test
		for feat in list(frame_fts):
			the_resp_samples = frame_fts.loc[res_indexes,[feat]]
			the_sen_samples = frame_fts.loc[sen_indexes, [feat]]
			if (the_resp_samples[feat].nunique(dropna=True) == 1) & (the_sen_samples[feat].nunique(dropna=True) == 1) : # True is the 2 groups values are uniquely described by a different unique value each...
				if the_resp_samples[feat].unique()[0] != the_sen_samples[feat].unique()[0]: # ...True if those two values are not the same
					dict_pvalues[feat] = p_val_top
				else:					# ....case where those two values are the same
					dict_pvalues[feat] = p_val_worst
			else: # not just one unique value exist in each group, the t-test is done then
				# t_stat, p_value_t = scipy.stats.ttest_ind(the_resp_samples, the_sen_samples, equal_var=False) #old line 0
				# t_stat, p_value_t = scipy.stats.ttest_ind(the_resp_samples.dropna()[feat], the_sen_samples.dropna()[feat], equal_var=False) #old line 1.5
				# t_stat, p_value_t = scipy.stats.ttest_ind(the_resp_samples.iloc[:,0].tolist(),the_sen_samples.iloc[:,0].tolist(),equal_var = False,nan_policy='propagate') # old line 1
				t_stat, p_value_t = scipy.stats.ttest_ind(np.array(the_resp_samples.iloc[:, 0].tolist()), np.array(the_sen_samples.iloc[:, 0].tolist()), equal_var=False, nan_policy='omit')
				##!! transforming a column to an array is done by putting it as a list and then as a numpy array
				# ttest_ind suppose variance equals by default so underestimates p for unequal variances even if the t-statistic is the same (eg : case where size of samples are equals but on different scale :;
				# When n1 != n2, the equal variance t-statistic is no longer equal to the unequal variance t-statistic:
				# so we use  equal_var = False
				## !!! to try : make a condittion if variance and size are equals, use equal_var = True else use equal_var = False
				# nan_policy='propagate' to take into account the nan and 'omit' to not take them into account
				dict_pvalues[feat] = p_value_t
	# sorted_feats_by_pval = sorted(dict_pvalues, key=dict_pvalues.get, reverse=False) # deprecated as not working properly
	sorted_feats_by_pval = [key for key, value in sorted(dict_pvalues.items(), key=itemgetter(1), reverse=False)] # default is reverse = False so can omit it
	sorted_pvals = [value for key, value in sorted(dict_pvalues.items(), key=itemgetter(1), reverse=False)]  # to report later on results # default is reverse = False so can omit it
	return dict_pvalues,sorted_feats_by_pval,sorted_pvals

# execute the uvivariate test
fts_ranking_w_univtest = ranker_by_pval_v2(df_frame_fts, df_frame_resp, fts_val_type, resp_col_name,my_encoded_classes) # tuple of 3 : dict_pvalues,sorted_feats_by_pval,sorted_pvals
# list of top features
mc_2_keep = 46340 # model complexity to keep
topfeats = fts_ranking_w_univtest[1][0:mc_2_keep]
# - restrict df to list of top features
# df_restricted_mc2keepfts_only = df.loc[:, topfeats] # not good because sort features not from cohort memebrship but from lowest to highest p-value
list_all_cols_df_fts_only = list(df.columns)
list_all_cols_df_fts_only.remove("Y_pCR")
list_all_cols_df_fts_only.remove("cohort")
list_of_fts_in_top_feats = []
for feat_2_keep_or_not in list_all_cols_df_fts_only:
    if feat_2_keep_or_not in topfeats:
        list_of_fts_in_top_feats.append(feat_2_keep_or_not)
# adding the resp and cohort cols to have full gallery of cols to restrict the dataset on it
list_of_cols_of_df_w_fts_in_top_feats = list_of_fts_in_top_feats + ["Y_pCR","cohort"]
df_restricted_2_mc = df[list_of_cols_of_df_w_fts_in_top_feats]

# >>>> show an image of entire dataframe to have an overview of the zeros
list_all_cols_df_restricted_2_mc_fts_only = list(df_restricted_2_mc.columns)
list_all_cols_df_restricted_2_mc_fts_only.remove("Y_pCR")
list_all_cols_df_restricted_2_mc_fts_only.remove("cohort")
df_restricted_2_mc_fts_only_4_image = df_restricted_2_mc.copy()
df_restricted_2_mc_fts_only_4_image = df_restricted_2_mc_fts_only_4_image[list_all_cols_df_restricted_2_mc_fts_only]
df_restricted_2_mc_fts_only_4_image[df_restricted_2_mc_fts_only_4_image != 0.0] = 999
# Let's look at this new design matrix and check it's blocks in diagonal, with each data set features info forming one block
plt.imshow(df_restricted_2_mc_fts_only_4_image, cmap='viridis', aspect='auto')
plt.colorbar()
# succession of cohorts on the Y axis is needed
list_of_cohorts_in_Yaxis_of_data_image = df_restricted_2_mc["cohort"].unique()
print("- This is the succession of cohorts on the Y axis of the data image : ")
print(list_of_cohorts_in_Yaxis_of_data_image)
# keep the image and use it as proof

# >>>> find how much of each bucket has been kept in the FS by the unuvivariate test
# counters of the kept fts for each cohort
fts_kept_for_dt1 = 0 # GSE41998
fts_kept_for_dt2 = 0 # GSE26639
fts_kept_for_dt3 = 0 # GSE32646
fts_kept_for_dt4 = 0 # GSE25055
fts_kept_for_dt5 = 0 # GSE20194
fts_kept_for_dt6 = 0 # GSE63471
for ft_kept in list_of_fts_in_top_feats:
    if "GSE41998" in ft_kept:
        fts_kept_for_dt1+=1
    elif "GSE26639" in ft_kept:
        fts_kept_for_dt2+=1
    elif "GSE32646" in ft_kept:
        fts_kept_for_dt3+=1
    elif "GSE25055" in ft_kept:
        fts_kept_for_dt4+=1
    elif "GSE20194" in ft_kept:
        fts_kept_for_dt5+=1
    elif "GSE63471" in ft_kept:
        fts_kept_for_dt6+=1
print("count of the kept fts for each cohort is over")
print("- # fts of dt1 ie GSE41998 in the FS by univ test : ",fts_kept_for_dt1,"out of 12034 fts ie ",round((fts_kept_for_dt1/12034)*100, 2),"%")
print("- # fts of dt2 ie GSE26639 in the FS by univ test : ",fts_kept_for_dt2,"out of 12034 fts ie ",round((fts_kept_for_dt2/12034)*100, 2),"%")
print("- # fts of dt3 ie GSE32646 in the FS by univ test : ",fts_kept_for_dt3,"out of 12034 fts ie ",round((fts_kept_for_dt3/12034)*100, 2),"%")
print("- # fts of dt4 ie GSE25055 in the FS by univ test : ",fts_kept_for_dt4,"out of 12034 fts ie ",round((fts_kept_for_dt4/12034)*100, 2),"%")
print("- # fts of dt5 ie GSE20194 in the FS by univ test : ",fts_kept_for_dt5,"out of 12034 fts ie ",round((fts_kept_for_dt5/12034)*100, 2),"%")
print("- # fts of dt6 ie GSE63471 in the FS by univ test : ",fts_kept_for_dt6,"out of 12034 fts ie ",round((fts_kept_for_dt6/12034)*100, 2),"%")


# >>>>>> check the datatypes
df_restricted_2_mc.info()
# Index: 229 entries, GSM1030229 to GSM1550523
# Columns: 46342 entries, A2M_in_GSE41998 to cohort
# dtypes: float64(46340), int64(1), object(1)
# memory usage: 81.0+ MB

# >>>>>>>> saving the FS done with the unviriate t-test
dict_fts_pvalues = fts_ranking_w_univtest[0]
df_FS_made = pd.DataFrame(dict_fts_pvalues.items(), columns=['Features', 'p_value_t_test_equalvar_false'])
df_FS_made_sorted_on_p_val = df_FS_made.sort_values('p_value_t_test_equalvar_false', ascending=True)
df_FS_made_sorted_on_p_val = df_FS_made_sorted_on_p_val.reset_index(drop=True)
fullname_file_of_df_FS_made_sorted_on_p_val = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_FS_on_joined_datasets/FSidea2thinking1UTttest_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"
df_FS_made_sorted_on_p_val.to_csv(fullname_file_of_df_FS_made_sorted_on_p_val, header=True) # we keep the index for a future joining w tables of fts
print("File FS saved !")
#>>>>>>>>>>>>>>

#>>>> saving the df
fullname_file_of_df = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/JoinNewDesign1CommonFtsof6_FSidea2thinking1UTttest_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"
df_restricted_2_mc.to_csv(fullname_file_of_df, header=True) # we keep the index for a future joining w tables of fts
print("File df saved !")
#>>>>>>>>>>>>>>