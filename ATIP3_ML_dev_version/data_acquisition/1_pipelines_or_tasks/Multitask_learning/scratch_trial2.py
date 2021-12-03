#-------------a model script for SPAMS tests inspired from the script "C1_gridsearchcv_sklearn_corr1" used previously from sklearn tests

#>>>>>>>>>>>imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn import model_selection
from sklearn.metrics import matthews_corrcoef # define the scoring to use
from sklearn.metrics import make_scorer
from sklearn.model_selection import learning_curve
from engines.watcher_engine import timer_started,duration_from,bcolors # for duration of operations and display colors
import spams # for SPAMS API workings
from scipy import sparse # to convert arrays

globalstart = timer_started() # start a clock to get the time after all the analysis
#>>>>>>>>>>bring in the data
# - link for the common fts dataset
filepath_of_ml_dataset1= "/data_warehouse/outputs/atip3_unified_datasets/JoinNewDesign1CommonFtsof6_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"
# filepath_of_ml_dataset2= "" # add later the 4 other joined datasets
# filepath_of_ml_dataset3= ""
# filepath_of_ml_dataset4= ""
local_link_to_csv_dataset = filepath_of_ml_dataset1
# Name of the trial that will be run for this exact analysis
tag_num_trial = "trial1" # = "Trial_test" for testing
df = pd.read_csv(local_link_to_csv_dataset) # read the dataset in a df and an option is "sep_in_file = ","" to precise what was the separator in the file
# when the first column was kept because it was the previous index, we can put it back as index with this
df.rename(columns={"Unnamed: 0" : "samples_names"}, inplace=True)
df = df.set_index(list(df.columns)[0])

# - lets separate our data
# input
df_input_primary = df.iloc[:, :-2] # recommended to iloc to produce a slice # :-1 means all except the last one (galeery of all features)
df_input = df_input_primary.iloc[:, :36102] # recommended to iloc to produce a slice # :-1 means all except the last one (gallery of 3 datsets of common)
X = df_input.values
# output
df_ouput = df.iloc[:,-2] # -1 means select the last one only and it is the cohort (not a value analysed)
y = df_ouput.values
# get the tag_of_cohort to mark the cohort used :
df_cohort_col = df.iloc[:,-1]
sorted_list_of_cohorts = sorted(df_cohort_col.unique())
tag_cohort = "JoinNewDesign1CommonFtsof6"
# Group membership vector
# dict_ntasks_nfeatures = {0 : 12034, 1 : 12034, 2 : 12034, 3 : 12034, 4 : 12034, 5 : 12034} # all common features of 6 datasets
dict_ntasks_nfeatures = {0 : 12034, 1 : 12034, 2 : 12034} # all common features of 3 datasets
# n_tasks = len(list(dict_ntasks_nfeatures.keys()))
groups_in_data = np.array([(1+x) for a_taskt in list(dict_ntasks_nfeatures.keys()) for x in np.arange(dict_ntasks_nfeatures[a_taskt])], dtype=np.int32)

#>>>>>>>>>>> Introduce a custom estimator based on Chloé work and based on scikit-learn estimators
# Help from https://scikit-learn.org/stable/developers/develop.html and https://sklearn-template.readthedocs.io/en/latest/user_guide.html
from sklearn import base
from sklearn.utils import validation, multiclass

# a class implemented to have sklearn capabilites
class CustomSPAMSestimatorLossIsSQUARERegulIsSPARSEGROUPLASSOL2V1(base.BaseEstimator, base.ClassifierMixin):
    """
    This class implements a sparse group logistic regression that is fitted using SPAMS.
    """
    def __init__(self, lambda1=1., lambda2=0., groups=None):
        self.lambda1 = lambda1
        self.lambda2 = lambda2
        self.groups = groups

    def fit(self, X, y):
        # Check that X and y have correct shape
        X, y = validation.check_X_y(X, y)
        # Store the classes seen during fit
        self.classes_ = multiclass.unique_labels(y)
        self.X_ = X
        self.y_ = y
        # Fitting
        X_sparse = sparse.csc_matrix(self.X_)  # np.asfortranarray(self.X_) #
        y_asfa = np.asfortranarray(self.y_.reshape((self.y_.shape[0], 1)))
        w_init = np.zeros((X_sparse.shape[1], 1), order="F")
        w = spams.fistaFlat(y_asfa, X_sparse, W0=w_init, loss='square', regul='sparse-group-lasso-l2', groups=self.groups, lambda1=self.lambda1, lambda2=self.lambda2)
        self.coef_ = w.reshape((w.shape[0],))
        # Return the classifier
        return self

    def predict_proba(self, X):
        # Check that fit has been called
        validation.check_is_fitted(self)
        # Input validation
        X = validation.check_array(X)
        # Prediction
        return (1. / (1 + np.exp(-np.dot(X, self.coef_))))

    def predict(self, X):
        return np.where(self.predict_proba(X) > 0.5, 1, 0)

#<<<<<<<<<<<<<<<<<<<< lets use the implemented class
# - the variation parmas of the alg
regularization_used = "SPAMSSGLL2lossIsSquare"
# list_seeds=[0,1,2,3,4,5,6,7,8,9]
list_seeds=[0,1] # for tests
reg_strength_space = np.geomspace(0.0001, 100.0, num=200) # 0.0001 to 1 (200 lambda values)
if 1.0 not in reg_strength_space :
    reg_strength_spaceplus1value = np.append(reg_strength_space, 1.0)
    reg_strength_spaceplus1value_sorted = np.sort(reg_strength_spaceplus1value) # 0.0001 to 1 (200 lambda values, including default value 1)
else:
    reg_strength_spaceplus1value_sorted = reg_strength_space
reg_strength_space1value_sorted_inverts = 1/reg_strength_spaceplus1value_sorted # 10000 to 0.01 (200 C values including the default value)
# - the results collectors
single_task_lasso_coefs = pd.DataFrame()
single_task_lasso_coefs["Features"] = df_input.columns
single_task_lasso_val_scores = []
single_task_lasso_test_scores = []
single_task_lasso_val_bestval_hp_of_interest = []
# go through the seeds and get :
# 1- define the data splits in train and test to use
# 2- get the coef of the fts for the best model in validation, the best model in validation hp of intesrest value, the best model in val test score
# 3- for each of those, keep it in one of the collectors
for a_seed in list_seeds:  # test aseed = 0
    # - fixate the actual seed
    np.random.seed(a_seed)
    # - get the different train and test part of our data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=a_seed)
    # - define the grid of params to explore
    param_grid = {'lambda1': reg_strength_space1value_sorted_inverts,'lambda2': reg_strength_space1value_sorted_inverts}  # define the grid of params and params values to explore
    # - the scoring metrics
    mcc_as_scorer = make_scorer(matthews_corrcoef) # mcc scoring line beta 2
    # - put the model in gridsearchcv (model is CustomSPAMSestimatorLossIsSQUARERegulIsSPARSEGROUPLASSOL2V1(groups=groups_in_data))
    model_gs = model_selection.GridSearchCV(CustomSPAMSestimatorLossIsSQUARERegulIsSPARSEGROUPLASSOL2V1(groups=groups_in_data), param_grid, scoring=mcc_as_scorer, cv=10, n_jobs=-1) # same as before but without stating the refit (beta 2)
    # - fit lasso
    model_gs.fit(X_train, y_train)
    # - keep coefficients
    colname_coefs_values = "Coefficient Estimate Seed " + str(a_seed)
    # best_estimator_.coef_ is here the a 1D array of same numbers of values (coefs) as the number of fts. so need to flatten to make it usable as a column
    A = model_gs.best_estimator_.coef_
    B = A.flatten()
    single_task_lasso_coefs[colname_coefs_values] = pd.Series(B)
    # - keep val scores
    single_task_lasso_val_scores.append(model_gs.best_score_)
    # - keep hp of interest
    single_task_lasso_val_bestval_hp_of_interest.append(list(model_gs.best_params_.values())[0])
    # - keep test scores with hp of interest value
    model_retained_asbest = model_gs.best_estimator_
    model_retained_asbest_testscore = matthews_corrcoef(y_test, model_retained_asbest.predict(X_test))
    single_task_lasso_test_scores.append(model_retained_asbest_testscore)

print("Summary of model selection analysis : ")
num_seeds = len(list_seeds)
if (len(single_task_lasso_val_scores) ==num_seeds) & (len(single_task_lasso_val_bestval_hp_of_interest) ==num_seeds) & (len(single_task_lasso_test_scores) ==num_seeds) & (single_task_lasso_coefs.shape[1] ==(num_seeds+1)) :
    print("- All results are accounted for!")
else :
    print("- Attention! At least one collector have missing values !")
for a_seed in list_seeds :
    index_present_seed = list_seeds.index(a_seed)
    seed_best_model_val_params = single_task_lasso_val_bestval_hp_of_interest[index_present_seed]
    seed_best_model_val_params_translated = 1/seed_best_model_val_params # obtain a lambda value instead of C
    seed_best_model_val_score = single_task_lasso_val_scores[index_present_seed]
    seed_best_model_test_score = single_task_lasso_test_scores[index_present_seed]
    print("- Seed %d best model in validation had best params as %s (ie lambda of %s ) with validation score as %s and test score as %s." % (a_seed,seed_best_model_val_params,seed_best_model_val_params_translated,seed_best_model_val_score,seed_best_model_test_score))

# get the averages :
# - for the perf across seeds
average_test_scores_as_median = np.nanmedian(single_task_lasso_test_scores)
average_test_scores_as_mean = np.nanmean(single_task_lasso_test_scores)
print("- The average test score from the 10 seeds is median %s and mean %s" % (average_test_scores_as_median,average_test_scores_as_mean))
# - for the hp of interest across seeds
average_hp_of_interest = np.nanmean(single_task_lasso_val_bestval_hp_of_interest)
average_hp_of_interest_translated = 1/average_hp_of_interest
print("- The average value of the hp of interest from the 10 seeds is : %s (ie lambda of %s )" % (average_hp_of_interest,average_hp_of_interest_translated))
# - for the coef :
list_of_cols_coefs = ['Coefficient Estimate Seed 0','Coefficient Estimate Seed 1','Coefficient Estimate Seed 2',
                      'Coefficient Estimate Seed 3','Coefficient Estimate Seed 4','Coefficient Estimate Seed 5',
                      'Coefficient Estimate Seed 6','Coefficient Estimate Seed 7','Coefficient Estimate Seed 8','Coefficient Estimate Seed 9']
single_task_lasso_coefs_abs = single_task_lasso_coefs
single_task_lasso_coefs_abs[list_of_cols_coefs] = single_task_lasso_coefs[list_of_cols_coefs].abs()
# make a col of mean coefs across the 10 seeds cols of coefs
single_task_lasso_coefs_abs["Mean Coefficient Estimate 10 Seeds"] = single_task_lasso_coefs_abs[list_of_cols_coefs].mean(axis=1, skipna=True) # axis = 0 means along the column and axis = 1 means working along the row
single_task_lasso_coefs_abs_mean_only = single_task_lasso_coefs_abs[["Features","Mean Coefficient Estimate 10 Seeds"]]
single_task_lasso_coefs_abs_mean_only_nonnull_fts = single_task_lasso_coefs_abs_mean_only[single_task_lasso_coefs_abs_mean_only["Mean Coefficient Estimate 10 Seeds"] != 0]
number_of_nuls_coefs_fts = single_task_lasso_coefs_abs_mean_only.shape[0] - single_task_lasso_coefs_abs_mean_only_nonnull_fts.shape[0]
print("- Out of %s , number of features with null coefs is %s and number of non null is %s " %(single_task_lasso_coefs_abs_mean_only.shape[0],number_of_nuls_coefs_fts,single_task_lasso_coefs_abs_mean_only_nonnull_fts.shape[0]))
# lets sort by mean coef value the remaining fts (they have non null coefs)
single_task_lasso_coefs_abs_mean_only_nonnull_fts_sorted = single_task_lasso_coefs_abs_mean_only_nonnull_fts.sort_values("Mean Coefficient Estimate 10 Seeds", axis=0, ascending=False, kind='mergesort') # axis=0 ie sort the rows


# - saving the list of non null coefs features
name_coefs_report = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_singletask_sklearn/non_null_coefs_sklearn_"+ regularization_used +"_10seeds_"+ tag_cohort +"_"+ tag_num_trial+".csv"
single_task_lasso_coefs_abs_mean_only_nonnull_fts_sorted.to_csv(name_coefs_report, index=None, header=True)
print("- File with non nul coefs saved into following path file : ")
print(name_coefs_report)
# all the analysis is done : get the runtime
runtime_analysis = duration_from(globalstart)
print(bcolors.OKGREEN + " Analysis (" + tag_num_trial + ") done : Time taken is : ", runtime_analysis, bcolors.ENDC)
# end concatenated with "," instead of "+" to avoid TypeError: unsupported operand type(s) for +: 'datetime.timedelta' and 'str'

# # end