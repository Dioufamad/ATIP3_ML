


# >>>> lets take a knee and strategize for a min :
# - sitrep : we have 1 set of 7 datasets (dt1-7) and we want to standardize not just the common cols but all cols
# - to do it in a secure way, we have to :
# - - find the buckets of fts across all the datasets
# - - designated a dataset that has all these buckets
# - - split that master dataset into versions (one version contain only the fts in a bucket)
# - - fit a scaler on each version of the master dataset
# - - split each dataset into the same versions than the master one until no fts is left out
# - - transform, for each dataset, the version created using the scalers created from the master dataset
# - - stitch back the versions of each dataset into the original dataset
# now go on with our script of making the full dataset of

# str="amad"
# if "a" in str :
# 	print("ok_a")
# if "m" in str :
# 	print("ok_m")
# if "d" in str :
# 	print("ok_d")

# list_of_all_possible_use_of_a_ft_tidy = [] # a list where
# list_of_all_possible_uses_tidy_dict_use_ftslist = {}
# for a_use_as_list in list_of_all_possible_use_of_a_ft:
# 	a_sorted_version_of_the_use = sorted(a_use_as_list)
# 	if a_sorted_version_of_the_use not in list_of_all_possible_use_of_a_ft_tidy:
# 		list_of_all_possible_use_of_a_ft_tidy.append(a_sorted_version_of_the_use)


#
# # lets find the different types of lists that exists by making a tidy list (no duplicates of the use lists) and reporting the info
# list_of_all_possible_use_of_a_ft_tidy = []
# for a_use_as_list in list(dict_ft_listofdtiwhereused.values()):
# 	a_sorted_version_of_the_use = sorted(a_use_as_list)
# 	if a_sorted_version_of_the_use not in list_of_all_possible_use_of_a_ft_tidy:
# 		list_of_all_possible_use_of_a_ft_tidy.append(a_sorted_version_of_the_use)
# print("lets the reveal the possible unique use lists we have across the datasets : ")
# print("- number of use lists : ", len(list_of_all_possible_use_of_a_ft_tidy))
# for an_ordered_list_of_dt_as_a_unique_use in list_of_all_possible_use_of_a_ft_tidy:
# 	print(an_ordered_list_of_dt_as_a_unique_use)
# # lets get for each unique use list, the list of fts to
# # + we have to make a new dict as {unique_string_of_use_list : list_of_fts_set_like_that}
# dict_uniquestrofuselist_listofftssetlikethat = {}
# list_of_uniquestrofuselist = []
# for a_unique_use_list in list_of_all_possible_use_of_a_ft_tidy:
# 	a_str_version_of_present_unique_use_list = '-'.join(a_unique_use_list)
# 	list_of_uniquestrofuselist.append(a_str_version_of_present_unique_use_list)
# # list_of_uniquestrofuselist has 4 elements
# print("There are",len(list_of_uniquestrofuselist),"keys to features grouping across datasets are : ")
# for a_str_of_dti in list_of_uniquestrofuselist:
# 	print(a_str_of_dti)
# for one_of_the_possible_use_list in list(dict_ft_listofdtiwhereused.keys()):
#
# 	if '-'.join(sorted(dict_ft_listofdtiwhereused[one_of_the_possible_use_list])) == :             # the value obtained is a list, we sort it, we join it into a str,
#
# for a, b in dict_Vparts.items():
# 	for c, d in dict_Vparts.items():
# 		print("intersection of", a, "and", c, "has count : ", len(list(set(b) & set(d))))
#
#
# # + we have to make a new dict as {unique_use_list : list_of_fts_set_like_that}
# dict_uniqueuselist_listofftssetlikethat = {}
# # list_of_all_possible_use_of_a_ft is the list(dict_ft_listofdtiwhereused.values()) so no need to make it again
# list_of_all_possible_use_of_a_ft = list(dict_ft_listofdtiwhereused.values()) # each use is a list of dti (used to loop on the differents use list and make a tidy list of them by removing duplicates lists)
# list_of_all_possible_ft_sorted_in_use_order = list(dict_ft_listofdtiwhereused.keys()) # a list of the fts in the same order than the use lists that will be used later to get for each use the
# for an_unordered_possible_use_list in list_of_all_possible_use_of_a_ft: # ie in  list(dict_ft_listofdtiwhereused.values())
# 	# for test : an_unordered_possible_use_list = list_of_all_possible_use_of_a_ft[0]
# 	# - lets make the key to store
# 	the_sorted_version_of_an_unordered_possible_use_list = sorted(an_unordered_possible_use_list)
# 	a_string_made_of_the_sorted_version_of_an_unordered_possible_use_list = '-'.join(the_sorted_version_of_an_unordered_possible_use_list)
# 	# - mets make the value to store
# 	index_an_ordered_possible_use_list = list_of_all_possible_use_of_a_ft.index(an_unordered_possible_use_list)
# 	an_unordered_possible_use_list_corresponding_ft = list_of_all_possible_ft_sorted_in_use_order[index_an_ordered_possible_use_list]
# 	# - lets store
# 	add_entry_in_dict(dict_uniqueuselist_listofftssetlikethat, a_string_made_of_the_sorted_version_of_an_unordered_possible_use_list, an_unordered_possible_use_list_corresponding_ft)
#


# - - the fts common to the commons groups of  platform1 and plaftorm 2 (version 1 aka Vpart1)
# - - the fts of the common group of platform1 that are not in the common group of platform2 (version 1b aka Vpart1b)
# - - the fts of the group platform2 that are common to the dataset2 and dataset3, and we remove the fts that were in platform1 (version 2 aka Vpart2)
# - - We know that the datasets 2 and 3 are setup like this : dataset2 = "common fts with dataset3 ie all fts of dataset3" + 2 fts.
# so this part is the fts of the dt2 not in dt3 and we remove the fts that were in platform1 (version 3 aka Vpart3)
# = >>> we have 3 versions maximum to make for each data set as such :
# - datasets 1, 4-7 will only have Vpart1 and Vpart1b
# - dataset 2 will have Vpart1, Vpart2 and Vpart3
# - dataset 3 will have Vpart1 and Vpart2
# summary of tasks for this part : (write it later)


# # >>>> get the list of common cols to all the datasets
# # - "list_of_common_cols_platform1 intersection with list_of_common_cols_platform2" is for the sorted list of common cols between the 2 platforms : we make it a list and to be sure, we sort it again
# list_of_fts_Vpart1 = sorted(list(set(list_of_common_cols_platform1) & set(list_of_common_cols_platform2)))
# # - "list_of_common_cols_platform1 and we remove from it the list_of_fts_Vpart1" is the sorted list of cols in platform1 and not in plaftorfor the Vpart1b : we make it a list and to be sure, we sort it again
# list_of_fts_Vpart1b = sorted(list(set(list_of_common_cols_platform1) - set(list_of_fts_Vpart1)))
# # - "list_of_common_cols_platform2 and we remove from it the list_of_common_cols_platform1 and sort again" will give us the sorted list of cols being fts only for the Vpart2
# # (no need to remove the non fts cols manually because they areare common hence they will be removed). we make it a list and just sort again to be sure
# list_of_fts_Vpart2 = sorted(list(set(list_of_common_cols_platform2) - set(list_of_common_cols_platform1)))
# # - "fts_only_in_df2" is the sorted list of cols for the Vpart3. its already a list of fts only so no removing anything. we just sort again to be sure
# list_of_fts_Vpart3 = ((set(list_all_cols_df_file2) - set(list_all_cols_df_file3)) - set(["Y_pCR", "cohort"])) - set(list_of_common_cols_platform1)
# # small verification if all the Vpart are distincs
# dict_Vparts = {"Vpart1" : list_of_fts_Vpart1,"Vpart1b" : list_of_fts_Vpart1b,"Vpart2" :list_of_fts_Vpart2 ,"Vpart3" : list_of_fts_Vpart3}
# for a,b in dict_Vparts.items():
# 	for c,d in dict_Vparts.items() :
# 		print("intersection of",a,"and",c,"has count : ",len(list(set(b) & set(d))))
#
# ((set(list_of_fts_Vpart1) & set(list_of_fts_Vpart1b)) & set(list_of_fts_Vpart2)) & set(list_of_fts_Vpart3)





# #========================
# # >>>> scaling the Vpart1bs across all datasets
# # - restrict the loaded datasets
# df_file1_Vpart1b = df_file1[list_of_fts_Vpart1b].copy()
# df_file2_Vpart1b = df_file2[list_of_fts_Vpart1b].copy()
# df_file3_Vpart1b = df_file3[list_of_fts_Vpart1b].copy()
# df_file4_Vpart1b = df_file4[list_of_fts_Vpart1b].copy()
# df_file5_Vpart1b = df_file5[list_of_fts_Vpart1b].copy()
# df_file6_Vpart1b = df_file6[list_of_fts_Vpart1b].copy()
# df_file7_Vpart1b = df_file7[list_of_fts_Vpart1b].copy()
# # - keep a copy of each single dataset for after operations comparisons
# list_of_dfs_Vpart1b_b4_std = [df_file1_Vpart1b.copy(),df_file2_Vpart1b.copy(),df_file3_Vpart1b.copy(),df_file4_Vpart1b.copy(),df_file5_Vpart1b.copy(),df_file6_Vpart1b.copy(),df_file7_Vpart1b.copy()]
# # introduce the naive scaler
# scaler_Vpart1b=StandardScaler()
# # the model of common fts frame to use to fit the scaler (the dataset 2 is chosen because in the events of making the standization for all fts, this is the dataset that would be used as base for fitting)
# model_fts_frame_4_scaler_Vpart1b = df_file2_Vpart1b.copy()
# # fit the scaler to one dataset fts frame
# scaler_Vpart1b.fit(model_fts_frame_4_scaler_Vpart1b)
# # transform for each others dataset its fts frame
# list_of_dfs_2_transform_Vpart1b = [df_file1_Vpart1b,df_file2_Vpart1b,df_file3_Vpart1b,df_file4_Vpart1b,df_file5_Vpart1b,df_file6_Vpart1b,df_file7_Vpart1b]
# num_fts_frame_changed = 0
# # replacing all fts cols at once
# for a_full_df in list_of_dfs_2_transform_Vpart1b:
# 	# for test : a_full_df = list_of_dfs_2_transform_Vpart1b[0]
# 	fts_frame_2_change = a_full_df.loc[:, list_of_fts_Vpart1b]
# 	fts_frame_scaled = scaler_Vpart1b.transform(fts_frame_2_change)
# 	a_full_df.loc[:, list_of_fts_Vpart1b] = fts_frame_scaled
# 	num_fts_frame_changed+=1
# 	print("number of feature frames changed for the Vpart1 :", num_fts_frame_changed)
# #=========================
#
# # >>>> scaling the Vpart2s across all datasets
# # - restrict the loaded datasets
# df_file2_Vpart2 = df_file2[list_of_fts_Vpart2].copy()
# df_file3_Vpart2 = df_file3[list_of_fts_Vpart2].copy()
# # - keep a copy of each single dataset for after operations comparisons
# list_of_dfs_Vpart2_b4_std = [df_file2_Vpart2.copy(),df_file3_Vpart2.copy()]
# # introduce the naive scaler
# scaler_Vpart2=StandardScaler()
# # the model of common fts frame to use to fit the scaler (the dataset 2 is chosen because in the events of making the standization for all fts, this is the dataset that would be used as base for fitting)
# model_fts_frame_4_scaler_Vpart2 = df_file2_Vpart2.copy()
# # fit the scaler to one dataset fts frame
# scaler_Vpart2.fit(model_fts_frame_4_scaler_Vpart2)
# # transform for each others dataset its fts frame
# list_of_dfs_2_transform_Vpart2 = [df_file2_Vpart2,df_file3_Vpart2]
# num_fts_frame_changed = 0
# # replacing all fts cols at once
# for a_full_df in list_of_dfs_2_transform_Vpart2:
# 	# for test : a_full_df = list_of_dfs_2_transform_Vpart2[0]
# 	fts_frame_2_change = a_full_df.loc[:, list_of_fts_Vpart2]
# 	fts_frame_scaled = scaler_Vpart2.transform(fts_frame_2_change)
# 	a_full_df.loc[:, list_of_fts_Vpart2] = fts_frame_scaled
# 	num_fts_frame_changed+=1
# 	print("number of feature frames changed for the Vpart2 :", num_fts_frame_changed)
# # >>>> scaling the Vpart3s across all datasets
# # - restrict the loaded datasets
# df_file2_Vpart3 = df_file2[list_of_fts_Vpart3].copy()
# # - keep a copy of each single dataset for after operations comparisons
# list_of_dfs_Vpart3_b4_std = [df_file2_Vpart3.copy()]
# # introduce the naive scaler
# scaler_Vpart3=StandardScaler()
# # the model of common fts frame to use to fit the scaler (the dataset 2 is chosen because in the events of making the standization for all fts, this is the dataset that would be used as base for fitting)
# model_fts_frame_4_scaler_Vpart3 = df_file2_Vpart3.copy()
# # fit the scaler to one dataset fts frame
# scaler_Vpart3.fit(model_fts_frame_4_scaler_Vpart3)
# # transform for each others dataset its fts frame
# list_of_dfs_2_transform_Vpart3 = [df_file2_Vpart3]
# num_fts_frame_changed = 0
# # replacing all fts cols at once
# for a_full_df in list_of_dfs_2_transform_Vpart3:
# 	# for test : a_full_df = list_of_dfs_2_transform_Vpart3[0]
# 	fts_frame_2_change = a_full_df.loc[:, list_of_fts_Vpart3]
# 	fts_frame_scaled = scaler_Vpart3.transform(fts_frame_2_change)
# 	a_full_df.loc[:, list_of_fts_Vpart3] = fts_frame_scaled
# 	num_fts_frame_changed+=1
# 	print("number of feature frames changed for the Vpart3 :", num_fts_frame_changed)


# from sklearn.utils.estimator_checks import check_estimator
# from sklearn.svm import LinearSVC
# check_estimator(LinearSVC())  # passes
#
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.datasets import load_iris
#
#
#
# iris = load_iris()
# X = iris.data
# y = iris.target
#
# plt.scatter(X[:, 0], X[:, 1], c=y, alpha=0.8)
#
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=5) ##!
#
# print('Train set:', X_train.shape)
# print('Test set:', X_test.shape)


# #==========================================++++CONTENTS OF OLD "C1_gridsearchcv_sklearn.py" script (the script before validation inclusion) (the corrected version is same name with corr at the end
# # making an estimator that will use the 7 cohorts joint dataset (common fts)
#
# # Choices made for the tests of the scikit-learn LogisticRegression :
# # - The solver used : The ‘newton-cg’, ‘sag’, and ‘lbfgs’ solvers support only L2 regularization with primal formulation, or no regularization. The ‘liblinear’ solver supports both L1 and L2 regularization, with a dual formulation only for the L2 penalty.
# # => the liblinear is used for L1 and L2.
# # The Elastic-Net regularization is only supported by the ‘saga’ solver. => the saga solver is used for the elasticnet
# # - dualbool, default=False
# # Dual or primal formulation. Dual formulation is only implemented for l2 penalty with liblinear solver. Prefer dual=False when n_samples > n_features.
# # - tolfloat, default=1e-4
# # Tolerance for stopping criteria.
# # - Cfloat, default=1.0
# # Inverse of regularization strength; must be a positive float. Like in support vector machines, smaller values specify stronger regularization.
# # - fit_interceptbool, default=True
# # Specifies if a constant (a.k.a. bias or intercept) should be added to the decision function.
# # - intercept_scalingfloat, default=1
# # Useful only when the solver ‘liblinear’ is used and self.fit_intercept is set to True. In this case, x becomes [x, self.intercept_scaling], i.e. a “synthetic” feature with constant value equal to intercept_scaling is appended to the instance vector.
# # The intercept becomes intercept_scaling * synthetic_feature_weight. # Note! the synthetic feature weight is subject to l1/l2 regularization as all other features.
# # To lessen the effect of regularization on synthetic feature weight (and therefore on the intercept) intercept_scaling has to be increased.
# # - New in version 0.17: class_weight=’balanced’
# # The “balanced” mode uses the values of y to automatically adjust weights inversely proportional to class frequencies in the input data as n_samples / (n_classes * np.bincount(y))
# # - random_stateint, RandomState instance, default=None
# # from the sklearn page of RandomizedLogisticRegression, we pull "If None, the random number generator is the RandomState instance used by np.random."
#
# # - NB : error when computing MCC as a scoring in GridSearchCV :
# # error is  :  /home/amad/anaconda3/envs/atip3_1_from_old_slate_env5/lib/python3.7/site-packages/sklearn/metrics/_classification.py:846: RuntimeWarning: invalid value encountered in double_scalars
# #   mcc = cov_ytyp / np.sqrt(cov_ytyt * cov_ypyp)
# # Explanation here : https://github.com/ThilinaRajapakse/simpletransformers/issues/4 ie the rule in the sklearn API for whats returned as mcc value is : if nor defined value (nan as mcc) return 0
# # Means that at some point, some of the 4 values of the confusion matrix were zero and made the MCC undefined. so sometimes, mcc is nan and we have an error showed and mcc value is 0
#
# # Used when solver == ‘sag’, ‘saga’ or ‘liblinear’ to shuffle the data.
# #>>>>>>>>>>>imports
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# #>>>>>>>>>>bring in the data
# # - link for the common fts dataset
# filepath_of_ml_dataset1= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE41998_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
# filepath_of_ml_dataset2= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE26639_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
# filepath_of_ml_dataset3= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE32646_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
# filepath_of_ml_dataset4= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE25055_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
# filepath_of_ml_dataset5= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE20194_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
# filepath_of_ml_dataset6= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE23988_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
# filepath_of_ml_dataset7= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE63471_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
# local_link_to_csv_dataset = filepath_of_ml_dataset3
# df = pd.read_csv(local_link_to_csv_dataset) # read the dataset in a df and an option is "sep_in_file = ","" to precise what was the separator in the file
# # when the first column was kept because it was the previous index, we can put it back as index with this
# df.rename(columns={"Unnamed: 0" : "samples_names"}, inplace=True)
# df = df.set_index(list(df.columns)[0])
#
# # # lets find the n_samples_per_task list
# # dict_cht_nsamples_in_order = {}
# # col_cohort_list = list(df["cohort"])
# # for a_cohort in col_cohort_list:
# #     if a_cohort not in list(dict_cht_nsamples_in_order.keys()) :
# #         count_samples_from_cohort = df.loc[df['cohort'] == a_cohort].shape[0]
# #         dict_cht_nsamples_in_order[a_cohort] = count_samples_from_cohort
# # n_samples_per_task = list(dict_cht_nsamples_in_order.values())
#
# # lets separate our data
# # input
# df_input = df.iloc[:, :-2] # recommended to iloc to produce a slice # :-1 means all except the last one
# X = df_input.values
# # output
# df_ouput = df.iloc[:,-2] # -1 means select the last one only and it is the cohort (not a value analysed)
# y = df_ouput.values
# # get the tag_of_cohort to mark the cohort used :
# df_cohort_col = df.iloc[:,-1]
# sorted_list_of_cohorts = sorted(df_cohort_col.unique())
# tag_cohort = sorted_list_of_cohorts[0]
#
# # >>>>>>>>>>>> Separate single - task l1 - regularized logistic regressions on each dataset with sklearn on 10 seeds
# #     Let 's run an l1-regularized logistic regression
# regularization_used = "L1"
#
# from sklearn import linear_model
# from sklearn import model_selection
# from sklearn.metrics import matthews_corrcoef # define the scoring to use
# from sklearn.metrics import make_scorer
# list_seeds=[0,1,2,3,4,5,6,7,8,9]
# n_features = X.shape[1]
# # single_task_lasso_coefs = np.zeros(shape=(len(list_tasks), n_features)) # initialize a empty grid for the coefs
# single_task_lasso_coefs = pd.DataFrame()
# single_task_lasso_coefs["Features"] = df_input.columns
# single_task_lasso_scores = []
# single_task_lasso_hp_of_interest = []
# # go through the seeds and get :
# # 1- the coef od the fts for the best model
# # 2-the best params for that best model
# for a_seed in list_seeds:  # test aseed = 0
#     # - fixate the actual seed
#     np.random.seed(a_seed)
#     # - define the grid of params to explore
#     param_grid = {'C': np.logspace(-3, 2, num=100)}  # define the grid of params and params values to explore
#     # the array of value to test for C : is returned here a list of values evenly spaced, log10(start value is -3 ie start val is 0,001) and log10(end value is 2 ie start val is 100)
#     # this is to be able to have non nul values evenly spaced that goes from 0,OO1 to 100 (from the lowest without being zero to the very high like 100)
#     # - define the gridsearchcv
#     # lasso_gs = model_selection.GridSearchCV(linear_model.LogisticRegression(penalty='l1', solver='liblinear'), param_grid, scoring="f1",cv=10, n_jobs=-1) # old scoring="f1" line (alpha)
#     # my_scoring1 = {'mcc': make_scorer(matthews_corrcoef)}  # 'roc_auc_score':make_scorer(roc_auc_score) # mcc scoring line beta 1
#     # lasso_gs = model_selection.GridSearchCV(linear_model.LogisticRegression(penalty='l1', solver='liblinear'), param_grid, scoring=my_scoring1, refit="mcc", cv=10, n_jobs=-1)  # new scoring="mcc" with a "refit declared as using the mcc" line beta 1
#     mcc_as_scorer = make_scorer(matthews_corrcoef) # mcc scoring line beta 2
#     lasso_gs = model_selection.GridSearchCV(linear_model.LogisticRegression(penalty='l1', solver='liblinear'), param_grid, scoring=mcc_as_scorer, cv=10, n_jobs=-1) # same as before but without stating the refit (beta 2)
#     # - fit lasso
#     lasso_gs.fit(X, y)
#     # - keep coefficients
#     colname_coefs_values = "Coefficient Estimate Seed " + str(a_seed)
#     # best_estimator_.coef_ is here the a 1D array of same numbers of values (coefs) as the number of fts. so need to flatten to make it usable as a column
#     A = lasso_gs.best_estimator_.coef_
#     B = A.flatten()
#     single_task_lasso_coefs[colname_coefs_values] = pd.Series(B)
#     # - keep scores
#     single_task_lasso_scores.append(lasso_gs.best_score_)
#     # - keep hp of interest
#     single_task_lasso_hp_of_interest.append(list(lasso_gs.best_params_.values())[0])
#     # - show hp of interest and best score
#     print("Best estimator for seed %d: %s " % (a_seed, lasso_gs.best_estimator_))
#     print("Best lambda for seed %d: %s with a score of %s" % (a_seed, lasso_gs.best_params_,lasso_gs.best_score_)) # best params give me a dict of key as a param and value as best value for the param
#
# # get the averages :
# # - for the perf
# average_scores = np.nanmedian(single_task_lasso_scores)
# print("the average score from the 10 seeds is : %s" % (average_scores))
# # - for the hp of interest :
# average_hp_of_interest = np.nanmean(single_task_lasso_hp_of_interest)
# print("the average hp of interest from the 10 seeds is : %s" % (average_hp_of_interest))
# # - for the coef :
# list_of_cols_coefs = ['Coefficient Estimate Seed 0','Coefficient Estimate Seed 1','Coefficient Estimate Seed 2',
#                       'Coefficient Estimate Seed 3','Coefficient Estimate Seed 4','Coefficient Estimate Seed 5',
#                       'Coefficient Estimate Seed 6','Coefficient Estimate Seed 7','Coefficient Estimate Seed 8','Coefficient Estimate Seed 9']
# single_task_lasso_coefs_abs = single_task_lasso_coefs
# single_task_lasso_coefs_abs[list_of_cols_coefs] = single_task_lasso_coefs[list_of_cols_coefs].abs()
# # make a col of mean coefs across the 10 seeds cols of coefs
# single_task_lasso_coefs_abs["Mean Coefficient Estimate 10 Seeds"] = single_task_lasso_coefs_abs[list_of_cols_coefs].mean(axis=1, skipna=True) # axis = 0 means along the column and axis = 1 means working along the row
# single_task_lasso_coefs_abs_mean_only = single_task_lasso_coefs_abs[["Features","Mean Coefficient Estimate 10 Seeds"]]
# single_task_lasso_coefs_abs_mean_only_nonnull_fts = single_task_lasso_coefs_abs_mean_only[single_task_lasso_coefs_abs_mean_only["Mean Coefficient Estimate 10 Seeds"] != 0]
# number_of_nuls_coefs_fts = single_task_lasso_coefs_abs_mean_only.shape[0] - single_task_lasso_coefs_abs_mean_only_nonnull_fts.shape[0]
# print("Out of %s , number of features with null coefs is %s and number of non null is %s " %(single_task_lasso_coefs_abs_mean_only.shape[0],number_of_nuls_coefs_fts,single_task_lasso_coefs_abs_mean_only_nonnull_fts.shape[0]))
# # lets sort by mean coef value the remaining fts (they have non null coefs)
# single_task_lasso_coefs_abs_mean_only_nonnull_fts_sorted = single_task_lasso_coefs_abs_mean_only_nonnull_fts.sort_values("Mean Coefficient Estimate 10 Seeds", axis=0, ascending=False, kind='mergesort') # axis=0 ie sort the rows
#
#
# # - saving the list of non null coefs features
# name_coefs_report = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_singletask_sklearn/non_null_coefs_sklearn_"+ regularization_used +"_10seeds_"+ tag_cohort +".csv"
# single_task_lasso_coefs_abs_mean_only_nonnull_fts_sorted.to_csv(name_coefs_report, index=None, header=True)
# print("File with non nul coefs saved into following path file : ")
# print(name_coefs_report)
#
# # end
#
# #==========================================++++

# #==========================================++++tuto learning curves found here : https://scikit-learn.org/stable/auto_examples/model_selection/plot_learning_curve.html#sphx-glr-auto-examples-model-selection-plot-learning-curve-py
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.naive_bayes import GaussianNB
# from sklearn.svm import SVC
# from sklearn.datasets import load_digits
# from sklearn.model_selection import learning_curve
# from sklearn.model_selection import ShuffleSplit
#
#
# def plot_learning_curve(estimator, title, X, y, axes=None, ylim=None, cv=None,
#                         n_jobs=None, train_sizes=np.linspace(.1, 1.0, 5)):
#
#     if axes is None:
#         _, axes = plt.subplots(1, 3, figsize=(20, 5))
#
#     axes[0].set_title(title)
#     if ylim is not None:
#         axes[0].set_ylim(*ylim)
#     axes[0].set_xlabel("Training examples")
#     axes[0].set_ylabel("Score")
#
#     train_sizes, train_scores, test_scores, fit_times, _ =learning_curve(estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes,return_times=True)
#     train_scores_mean = np.mean(train_scores, axis=1)
#     train_scores_std = np.std(train_scores, axis=1)
#     test_scores_mean = np.mean(test_scores, axis=1)
#     test_scores_std = np.std(test_scores, axis=1)
#     fit_times_mean = np.mean(fit_times, axis=1)
#     fit_times_std = np.std(fit_times, axis=1)
#
#     # Plot learning curve
#     axes[0].grid()
#     axes[0].fill_between(train_sizes, train_scores_mean - train_scores_std,
#                          train_scores_mean + train_scores_std, alpha=0.1,
#                          color="r")
#     axes[0].fill_between(train_sizes, test_scores_mean - test_scores_std,
#                          test_scores_mean + test_scores_std, alpha=0.1,
#                          color="g")
#     axes[0].plot(train_sizes, train_scores_mean, 'o-', color="r",
#                  label="Training score")
#     axes[0].plot(train_sizes, test_scores_mean, 'o-', color="g",
#                  label="Cross-validation score")
#     axes[0].legend(loc="best")
#
#     # Plot n_samples vs fit_times
#     axes[1].grid()
#     axes[1].plot(train_sizes, fit_times_mean, 'o-')
#     axes[1].fill_between(train_sizes, fit_times_mean - fit_times_std,
#                          fit_times_mean + fit_times_std, alpha=0.1)
#     axes[1].set_xlabel("Training examples")
#     axes[1].set_ylabel("fit_times")
#     axes[1].set_title("Scalability of the model")
#
#     # Plot fit_time vs score
#     axes[2].grid()
#     axes[2].plot(fit_times_mean, test_scores_mean, 'o-')
#     axes[2].fill_between(fit_times_mean, test_scores_mean - test_scores_std,
#                          test_scores_mean + test_scores_std, alpha=0.1)
#     axes[2].set_xlabel("fit_times")
#     axes[2].set_ylabel("Score")
#     axes[2].set_title("Performance of the model")
#
#     return plt
#
#
# fig, axes = plt.subplots(3, 10, figsize=(150, 15))
#
# X, y = load_digits(return_X_y=True)
#
# title = "Learning Curves (Naive Bayes)"
# # Cross validation with 10 iterations, each time with 20% data randomly selected as a validation set.
# cv = ShuffleSplit(n_splits=10, test_size=0.1, random_state=0)
#
# estimator = GaussianNB()
# plot_learning_curve(estimator, title, X, y, axes=axes[:, 0], ylim=(0.7, 1.01),
#                     cv=cv, n_jobs=4)
#
# plt.show()
#
# #==========================================++++

# # ==========================================++++ learning curve adapted for end of script : C1_gridsearchcv_sklearn_corr1
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.naive_bayes import GaussianNB
# from sklearn.svm import SVC
# from sklearn.datasets import load_digits
# from sklearn.model_selection import learning_curve
# from sklearn.model_selection import ShuffleSplit
#
#
# def plot_learning_curve(estimator, title, X, y, axes=None, ylim=None, cv=None, n_jobs=None, train_sizes=np.linspace(.1, 1.0, 5)):
#
#     if axes is None:
#         _, axes = plt.subplots(1, 3, figsize=(20, 5))
#
#     axes[0].set_title(title)
#     if ylim is not None:
#         axes[0].set_ylim(*ylim)
#     axes[0].set_xlabel("Training examples")
#     axes[0].set_ylabel("Score")
#
#     train_sizes, train_scores, test_scores, fit_times, _ =learning_curve(estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes,return_times=True) # _ is put for the uneeded score_times and is 5th return
#     train_scores_mean = np.mean(train_scores, axis=1)
#     train_scores_std = np.std(train_scores, axis=1)
#     test_scores_mean = np.mean(test_scores, axis=1)
#     test_scores_std = np.std(test_scores, axis=1)
#     fit_times_mean = np.mean(fit_times, axis=1)
#     fit_times_std = np.std(fit_times, axis=1)
#
#     # Plot learning curve
#     axes[0].grid()
#     axes[0].fill_between(train_sizes, train_scores_mean - train_scores_std,
#                          train_scores_mean + train_scores_std, alpha=0.1,
#                          color="r")
#     axes[0].fill_between(train_sizes, test_scores_mean - test_scores_std,
#                          test_scores_mean + test_scores_std, alpha=0.1,
#                          color="g")
#     axes[0].plot(train_sizes, train_scores_mean, 'o-', color="r",
#                  label="Training score")
#     axes[0].plot(train_sizes, test_scores_mean, 'o-', color="g",
#                  label="Cross-validation score")
#     axes[0].legend(loc="best")
#
#     # Plot n_samples vs fit_times
#     axes[1].grid()
#     axes[1].plot(train_sizes, fit_times_mean, 'o-')
#     axes[1].fill_between(train_sizes, fit_times_mean - fit_times_std,
#                          fit_times_mean + fit_times_std, alpha=0.1)
#     axes[1].set_xlabel("Training examples")
#     axes[1].set_ylabel("fit_times")
#     axes[1].set_title("Scalability of the model")
#
#     # Plot fit_time vs score
#     axes[2].grid()
#     axes[2].plot(fit_times_mean, test_scores_mean, 'o-')
#     axes[2].fill_between(fit_times_mean, test_scores_mean - test_scores_std,
#                          test_scores_mean + test_scores_std, alpha=0.1)
#     axes[2].set_xlabel("fit_times")
#     axes[2].set_ylabel("Score")
#     axes[2].set_title("Performance of the model")
#
#     return plt
#
#
# fig, axes = plt.subplots(3, 2, figsize=(150, 15))
#
# X, y = X_train, y_train
#
# for a_new_seed in list_seeds[:2]: # to test: a_new_seed = 0 , a_new_seed = 1
#     # - fixate the actual seed
#     np.random.seed(a_seed)
#     # - make the curve title
#     title = "Learning Curves of best validation model on seed %d" % (a_new_seed)
#     # - for the cv, we give n int for  stratifiedkfold instead of a randomizedsplit generator
#     # Cross validation with 10 iterations, each time with 20% data randomly selected as a validation set.
#     # cv = ShuffleSplit(n_splits=10, test_size=0.1, random_state=a_new_seed)
#     cv=10
#     estimator = model_retained_asbest
#     plot_learning_curve(estimator, title, X, y, axes=axes[:, a_new_seed], ylim=(0.7, 1.01), cv=cv, n_jobs=-1)
#
# plt.show()
# # ==========================================++++




# ==========================================++++
# #>>>>>>>>> trial of lambda search space
# # c values from 0,1 to 10000 ie lambda values from 10 to 0.0001 ##! use these values for C param
# # - the tested space for lambda values in  SPAMS (uses proper lambda values)
# A_space2 = np.logspace(-4, 1, num=30) # a space of values from 0,0001 to 10 (30 values)
# A_space2_2 = np.logspace(-4, 1, num=100) # a space of values from 0,0001 to 10 (100 values) ##! use these values for lambda param
# #>>>>>>>>>


#
# #>>>>>>>>>>>imports
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn import linear_model
# from sklearn import model_selection
# from sklearn.metrics import matthews_corrcoef # define the scoring to use
# from sklearn.metrics import make_scorer
# from sklearn.model_selection import learning_curve
#
# #>>>>>>>>>>bring in the data
# # - link for the common fts dataset
# filepath_of_ml_dataset1= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE41998_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
# filepath_of_ml_dataset2= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE26639_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
# filepath_of_ml_dataset3= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE32646_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
# filepath_of_ml_dataset4= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE25055_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
# filepath_of_ml_dataset5= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE20194_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
# filepath_of_ml_dataset6= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE23988_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
# filepath_of_ml_dataset7= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE63471_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
# local_link_to_csv_dataset = filepath_of_ml_dataset1
# df = pd.read_csv(local_link_to_csv_dataset) # read the dataset in a df and an option is "sep_in_file = ","" to precise what was the separator in the file
# # when the first column was kept because it was the previous index, we can put it back as index with this
# df.rename(columns={"Unnamed: 0" : "samples_names"}, inplace=True)
# df = df.set_index(list(df.columns)[0])
#
# # - lets separate our data
# # input
# df_input = df.iloc[:, :-2] # recommended to iloc to produce a slice # :-1 means all except the last one
# X = df_input.values
# # output
# df_ouput = df.iloc[:,-2] # -1 means select the last one only and it is the cohort (not a value analysed)
# y = df_ouput.values
# # get the tag_of_cohort to mark the cohort used :
# df_cohort_col = df.iloc[:,-1]
# sorted_list_of_cohorts = sorted(df_cohort_col.unique())
# tag_cohort = sorted_list_of_cohorts[0]
#
#
# # >>>>>>>>>>>> Let 's run a Separate single - task l1 - regularized logistic regressions on each dataset with sklearn on 10 seeds
# # - the variation parmas of the alg
# regularization_used = "L1"
# list_seeds=[0,1,2,3,4,5,6,7,8,9]
# # - the results collectors
# single_task_lasso_coefs = pd.DataFrame()
# single_task_lasso_coefs["Features"] = df_input.columns
# single_task_lasso_val_scores = []
# single_task_lasso_test_scores = []
# single_task_lasso_val_bestval_hp_of_interest = []
# # go through the seeds and get :
# # 1- define the data splits in train and test to use
# # 2- get the coef of the fts for the best model in validation, the best model in validation hp of intesrest value, the best model in val test score
# # 3- for each of those, keep it in one of the collectors
# for a_seed in list_seeds:  # test aseed = 0
#     # - fixate the actual seed
#     np.random.seed(a_seed)
#     # - get the different train and test part of our data
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=a_seed)
#     # - define the grid of params to explore
#     param_grid = {'C': np.logspace(-3, 2, num=100)}  # define the grid of params and params values to explore
#     # the array of value to test for C : is returned here a list of values evenly spaced, log10(start value is -3 ie start val is 0,001) and log10(end value is 2 ie start val is 100)
#     # this is to be able to have non nul values evenly spaced that goes from 0,OO1 to 100 (from the lowest without being zero to the very high like 100)
#     # - define the gridsearchcv
#     # lasso_gs = model_selection.GridSearchCV(linear_model.LogisticRegression(penalty='l1', solver='liblinear'), param_grid, scoring="f1",cv=10, n_jobs=-1) # old scoring="f1" line (alpha)
#     # my_scoring1 = {'mcc': make_scorer(matthews_corrcoef)}  # 'roc_auc_score':make_scorer(roc_auc_score) # mcc scoring line beta 1
#     # lasso_gs = model_selection.GridSearchCV(linear_model.LogisticRegression(penalty='l1', solver='liblinear'), param_grid, scoring=my_scoring1, refit="mcc", cv=10, n_jobs=-1)  # new scoring="mcc" with a "refit declared as using the mcc" line beta 1
#     mcc_as_scorer = make_scorer(matthews_corrcoef) # mcc scoring line beta 2
#     lasso_gs = model_selection.GridSearchCV(linear_model.LogisticRegression(penalty='l1', solver='liblinear'), param_grid, scoring=mcc_as_scorer, cv=10, n_jobs=-1) # same as before but without stating the refit (beta 2)
#     # - fit lasso
#     lasso_gs.fit(X_train, y_train)
#     # - keep coefficients
#     colname_coefs_values = "Coefficient Estimate Seed " + str(a_seed)
#     # best_estimator_.coef_ is here the a 1D array of same numbers of values (coefs) as the number of fts. so need to flatten to make it usable as a column
#     A = lasso_gs.best_estimator_.coef_
#     B = A.flatten()
#     single_task_lasso_coefs[colname_coefs_values] = pd.Series(B)
#     # - keep val scores
#     single_task_lasso_val_scores.append(lasso_gs.best_score_)
#     # - keep hp of interest
#     single_task_lasso_val_bestval_hp_of_interest.append(list(lasso_gs.best_params_.values())[0])
#     # - keep test scores with hp of interest value
#     model_retained_asbest = lasso_gs.best_estimator_
#     model_retained_asbest_testscore = matthews_corrcoef(y_test, model_retained_asbest.predict(X_test))
#     single_task_lasso_test_scores.append(model_retained_asbest_testscore)
#
# print("Summary of model selection analysis : ")
# num_seeds = len(list_seeds)
# if (len(single_task_lasso_val_scores) ==num_seeds) & (len(single_task_lasso_val_bestval_hp_of_interest) ==num_seeds) & (len(single_task_lasso_test_scores) ==num_seeds) & (single_task_lasso_coefs.shape[1] ==(num_seeds+1)) :
#     print("- All results are accounted for!")
# else :
#     print("- Attention! At least one collector have missing values !")
# for a_seed in list_seeds :
#     index_present_seed = list_seeds.index(a_seed)
#     seed_best_model_val_params = single_task_lasso_val_bestval_hp_of_interest[index_present_seed]
#     seed_best_model_val_score = single_task_lasso_val_scores[index_present_seed]
#     seed_best_model_test_score = single_task_lasso_test_scores[index_present_seed]
#     print("- Seed %d best model in validation had best params as %s with validation score as %s and test score as %s." % (a_seed,seed_best_model_val_params,seed_best_model_val_score,seed_best_model_test_score))
#
# # get the averages :
# # - for the perf across seeds
# average_test_scores_as_median = np.nanmedian(single_task_lasso_test_scores)
# average_test_scores_as_mean = np.nanmean(single_task_lasso_test_scores)
# print("- The average test score from the 10 seeds is median %s and mean %s" % (average_test_scores_as_median,average_test_scores_as_mean))
# # - for the hp of interest across seeds
# average_hp_of_interest = np.nanmean(single_task_lasso_val_bestval_hp_of_interest)
# print("- The average value of the hp of interest from the 10 seeds is : %s" % (average_hp_of_interest))
# # - for the coef :
# list_of_cols_coefs = ['Coefficient Estimate Seed 0','Coefficient Estimate Seed 1','Coefficient Estimate Seed 2',
#                       'Coefficient Estimate Seed 3','Coefficient Estimate Seed 4','Coefficient Estimate Seed 5',
#                       'Coefficient Estimate Seed 6','Coefficient Estimate Seed 7','Coefficient Estimate Seed 8','Coefficient Estimate Seed 9']
# single_task_lasso_coefs_abs = single_task_lasso_coefs
# single_task_lasso_coefs_abs[list_of_cols_coefs] = single_task_lasso_coefs[list_of_cols_coefs].abs()
# # make a col of mean coefs across the 10 seeds cols of coefs
# single_task_lasso_coefs_abs["Mean Coefficient Estimate 10 Seeds"] = single_task_lasso_coefs_abs[list_of_cols_coefs].mean(axis=1, skipna=True) # axis = 0 means along the column and axis = 1 means working along the row
# single_task_lasso_coefs_abs_mean_only = single_task_lasso_coefs_abs[["Features","Mean Coefficient Estimate 10 Seeds"]]
# single_task_lasso_coefs_abs_mean_only_nonnull_fts = single_task_lasso_coefs_abs_mean_only[single_task_lasso_coefs_abs_mean_only["Mean Coefficient Estimate 10 Seeds"] != 0]
# number_of_nuls_coefs_fts = single_task_lasso_coefs_abs_mean_only.shape[0] - single_task_lasso_coefs_abs_mean_only_nonnull_fts.shape[0]
# print("- Out of %s , number of features with null coefs is %s and number of non null is %s " %(single_task_lasso_coefs_abs_mean_only.shape[0],number_of_nuls_coefs_fts,single_task_lasso_coefs_abs_mean_only_nonnull_fts.shape[0]))
# # lets sort by mean coef value the remaining fts (they have non null coefs)
# single_task_lasso_coefs_abs_mean_only_nonnull_fts_sorted = single_task_lasso_coefs_abs_mean_only_nonnull_fts.sort_values("Mean Coefficient Estimate 10 Seeds", axis=0, ascending=False, kind='mergesort') # axis=0 ie sort the rows
#
#
# # - saving the list of non null coefs features
# name_coefs_report = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_singletask_sklearn/non_null_coefs_sklearn_"+ regularization_used +"_10seeds_"+ tag_cohort +".csv"
# single_task_lasso_coefs_abs_mean_only_nonnull_fts_sorted.to_csv(name_coefs_report, index=None, header=True)
# print("- File with non nul coefs saved into following path file : ")
# print(name_coefs_report)


#---------an debut of trial of the regression part from chloé's notebook tuto
# import numpy as np
# n_tasks = 3
# n_features = 20
# n_samples_per_task = [30, 30, 40]
# n_samples = np.sum(n_samples_per_task)
#
# n_causal_features = 5 # first n_causal_features have non-zero weights
#
# epsilon = 0.3 # noise level
#
# import spams
# r = 0
# start_idx = 0
# end_idx = 0
# end_idx += n_samples_per_task[r]
# X_asfa = np.asfortranarray(X[start_idx:end_idx, :])
# y_asfa = np.asfortranarray(y[start_idx:end_idx].reshape((n_samples_per_task[r], 1)))
# w_init = np.zeros((n_features, 1), order="F")
# print(X_asfa.shape, y_asfa.shape, w_init.shape)
# w1 = spams.fistaFlat(y_asfa, X_asfa, W0=w_init,
#                     loss='square', regul='l1',
#                     lambda1=10)
# w2 = spams.fistaFlat(y_asfa, X_asfa, W0=w_init,
#                     loss='square', regul='l1',
#                     lambda1=1e-3)


########################