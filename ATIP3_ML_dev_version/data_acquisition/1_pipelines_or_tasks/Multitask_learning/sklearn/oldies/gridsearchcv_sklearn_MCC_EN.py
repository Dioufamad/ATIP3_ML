# making an estimator that will use the 7 cohorts joined dataset (common fts)
# source of the train, validation and then test method : https://github.com/MachineLearnia/Python-Machine-Learning/blob/master/21%20-%20Sklearn%20:%20Model%20Selection.ipynb


#>>>>>>>>>>>imports (used)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn import model_selection
from sklearn.metrics import make_scorer,matthews_corrcoef,cohen_kappa_score,f1_score,balanced_accuracy_score # define the scoring to use
from engines.watcher_engine import timer_started,duration_from,bcolors # for duration of operations and display colors

globalstart = timer_started() # start a clock to get the time after all the analysis

#>>>>>>>>>>bring in the data
# - links for the datasets
# tag_cohort = "GSE41998" # dt1
# filepath_of_ml_dataset= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE41998_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
# tag_cohort = "GSE26639" # dt2
# filepath_of_ml_dataset= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE26639_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
# tag_cohort = "GSE32646" # dt3
# filepath_of_ml_dataset= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE32646_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
# tag_cohort = "GSE25055" # dt4
# filepath_of_ml_dataset= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE25055_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
# tag_cohort = "GSE20194" # dt5
# filepath_of_ml_dataset= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE20194_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
# tag_cohort = "GSE23988" # to not use (cohort with 4 samples)-----------------<<<<<<<<<< ##!
# filepath_of_ml_dataset= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE23988_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
# tag_cohort = "GSE63471" # dt6
# filepath_of_ml_dataset= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE63471_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv"
tag_cohort = "CommonFtsof6_FSidea1thinking1or3"
filepath_of_ml_dataset= "/data_acquisition/1_pipelines_or_tasks/JoinNewDesign1CommonFtsof6_FSidea1thinking1or3_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"
# tag_cohort = "CommonFtsof6_FSidea1thinking2ptfU133A2"
# filepath_of_ml_dataset= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/JoinNewDesign1CommonFtsof6_FSidea1thinking2ptfU133A2_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"
# tag_cohort = "CommonFtsof6_FSidea1thinking2ptfU133plus2"
# filepath_of_ml_dataset= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/JoinNewDesign1CommonFtsof6_FSidea1thinking2ptfU133plus2_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"
# tag_cohort = "CommonFtsof6_FSidea1thinking2ptfU133A"
# filepath_of_ml_dataset= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/JoinNewDesign1CommonFtsof6_FSidea1thinking2ptfU133A_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"
# tag_cohort = "CommonFtsof6_FSidea2thinking1UTttest"
# filepath_of_ml_dataset= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/JoinNewDesign1CommonFtsof6_FSidea2thinking1UTttest_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"
# tag_cohort = "" # not created yet
# filepath_of_ml_dataset= ""
local_link_to_csv_dataset = filepath_of_ml_dataset
# Name of the trial that will be run for this exact analysis
tag_num_trial = "trial1" # = "Trial_test" for testing
df = pd.read_csv(local_link_to_csv_dataset) # read the dataset in a df and an option is "sep_in_file = ","" to precise what was the separator in the file
# when the first column was kept because it was the previous index, we can put it back as index with this
df.rename(columns={"Unnamed: 0" : "samples_names"}, inplace=True)
df = df.set_index(list(df.columns)[0])

# - lets separate our data
# input
df_input = df.iloc[:, :-2] # recommended to iloc to produce a slice # :-1 means all except the last one
X = df_input.values
# output
df_ouput = df.iloc[:,-2] # -1 means select the last one only and it is the cohort (not a value analysed)
y = df_ouput.values
# get the tag_of_cohort to mark the cohort used :
df_cohort_col = df.iloc[:,-1]
# old tag cohort
# sorted_list_of_cohorts = sorted(df_cohort_col.unique())
# tag_cohort = sorted_list_of_cohorts[0]



# define our scorer MM4 = "MixedMetricof4"
tag_scorer = "MM4"
def overall_average_score(actual,prediction):
    mcc_abs_val = abs(matthews_corrcoef(actual, prediction))
    ck_abs_val = abs(cohen_kappa_score(actual, prediction))
    f1_sc = f1_score(actual, prediction, average='binary')
    bal_acc = balanced_accuracy_score(actual, prediction)
    total_score = mcc_abs_val + ck_abs_val + f1_sc + bal_acc
    total_score_average = total_score / 5
    return total_score_average
grid_scorer = make_scorer(overall_average_score, greater_is_better=True)
# how to use (see : https://stackoverflow.com/questions/31615190/sklearn-gridsearchcv-scoring-function-error)
#1) print("Overall average score: ", overall_average_score(y_test, y_pred))
#2) scoring=grid_scorer in GridSearchCV()

# >>>>>>>>>>>> Let 's run a Separate single - task l1 - regularized logistic regressions on each dataset with sklearn on 10 seeds
regularization_used = "EN"
# - the variating params of the alg
list_seeds=[0,1,2,3,4,5,6,7,8,9] # list_seeds=[0,1] # for tests
reg_strength_space = np.geomspace(0.0001, 100.0, num=200) # 0.0001 to 100.O (200 lambda values)
# update the list of lambda values with the known default lambda value within some APIs to explore with that value also
# we cite 1.0 for sklearn, 0.1 for SPAMS but for now we only try to include the dafault value of lambda in the present API only (lambda of sklearn)
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
# 2- the best model in validation, get : a) the coef of the fts, the hp of interest value, its test score
# 3- for each of those, keep it in one of the collectors
for a_seed in list_seeds:  # test a_seed = 0, # a_seed = 1
    print("- Started working with seed", a_seed)
    # - fixate the actual seed
    np.random.seed(a_seed)
    # - get the different train and test part of our data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=a_seed)
    # - define the grid of params to explore
    param_grid = {'C': reg_strength_space1value_sorted_inverts}  # define the grid of params and params values to explore
    # - define the gridsearchcv
    # lasso_gs = model_selection.GridSearchCV(linear_model.LogisticRegression(penalty='l1', solver='liblinear'), param_grid, scoring="f1",cv=10, n_jobs=-1) # old scoring="f1" line (alpha)
    # my_scoring1 = {'mcc': make_scorer(matthews_corrcoef)}  # 'roc_auc_score':make_scorer(roc_auc_score) # mcc scoring line beta 1
    # lasso_gs = model_selection.GridSearchCV(linear_model.LogisticRegression(penalty='l1', solver='liblinear'), param_grid, scoring=my_scoring1, refit="mcc", cv=10, n_jobs=-1)  # new scoring="mcc" with a "refit declared as using the mcc" line beta 1
    # mcc_as_scorer = make_scorer(matthews_corrcoef) # mcc scoring line beta 2 (last used)
    # lasso_gs = model_selection.GridSearchCV(linear_model.LogisticRegression(penalty='l2', solver='saga',random_state=a_seed,class_weight="balanced",max_iter=100), param_grid, scoring=mcc_as_scorer, cv=10, n_jobs=-1) # same as before but without stating the refit (beta 2) (last used)
    lasso_gs = model_selection.GridSearchCV(linear_model.LogisticRegression(penalty='elasticnet', solver='saga', random_state=a_seed, class_weight="balanced", fit_intercept=False,max_iter=200,tol=0.01,l1_ratio= 0.5), param_grid, scoring=grid_scorer, cv=10, n_jobs=-1)  # same as before but without stating the refit
    # - fit lasso
    lasso_gs.fit(X_train, y_train)
    # - keep coefficients
    colname_coefs_values = "Coefficient Estimate Seed " + str(a_seed)
    # best_estimator_.coef_ is here the a 1D array of same numbers of values (coefs) as the number of fts. so need to flatten to make it usable as a column
    A = lasso_gs.best_estimator_.coef_
    B = A.flatten()
    single_task_lasso_coefs[colname_coefs_values] = pd.Series(B)
    # - keep val scores
    single_task_lasso_val_scores.append(lasso_gs.best_score_)
    # - keep hp of interest
    single_task_lasso_val_bestval_hp_of_interest.append(list(lasso_gs.best_params_.values())[0])
    # - keep test scores with hp of interest value
    model_retained_asbest = lasso_gs.best_estimator_
    # model_retained_asbest_testscore = matthews_corrcoef(y_test, model_retained_asbest.predict(X_test)) # last used
    model_retained_asbest_testscore = overall_average_score(y_test, model_retained_asbest.predict(X_test))
    single_task_lasso_test_scores.append(model_retained_asbest_testscore)
    print("- Finished working with seed", a_seed)

print("Summary of model selection analysis : ")
num_seeds = len(list_seeds)
if (len(single_task_lasso_val_scores) ==num_seeds) & (len(single_task_lasso_val_bestval_hp_of_interest) ==num_seeds) & (len(single_task_lasso_test_scores) ==num_seeds) & (single_task_lasso_coefs.shape[1] ==(num_seeds+1)) :
    print("- All results are accounted for!")
else :
    print("- Attention! At least one collector have missing values !")
for a_seed in list_seeds :
    index_present_seed = list_seeds.index(a_seed)
    seed_best_model_val_params = single_task_lasso_val_bestval_hp_of_interest[index_present_seed]
    seed_best_model_val_params_translated = 1/seed_best_model_val_params # obtain a lambda value instead of a C value
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
single_task_lasso_coefs_abs = single_task_lasso_coefs.copy()
# single_task_lasso_coefs_abs[list_of_cols_coefs] = single_task_lasso_coefs[list_of_cols_coefs].abs() # to only make as absolute the cols with values and not touch the 1st col containing the names of the fts (old way)
single_task_lasso_coefs_abs[list_of_cols_coefs] = single_task_lasso_coefs_abs[list_of_cols_coefs].abs() # to only make as absolute the cols with values and not touch the 1st col containing the names of the fts
# make a col of mean coefs across the 10 seeds cols of coefs
single_task_lasso_coefs_abs["Mean Coefficient Estimate 10 Seeds"] = single_task_lasso_coefs_abs[list_of_cols_coefs].mean(axis=1, skipna=True) # axis = 0 means along the column and axis = 1 means working along the row
single_task_lasso_coefs_abs_mean_only = single_task_lasso_coefs_abs[["Features","Mean Coefficient Estimate 10 Seeds"]]
single_task_lasso_coefs_abs_mean_only_nonnull_fts = single_task_lasso_coefs_abs_mean_only[single_task_lasso_coefs_abs_mean_only["Mean Coefficient Estimate 10 Seeds"] != 0]
number_of_nuls_coefs_fts = single_task_lasso_coefs_abs_mean_only.shape[0] - single_task_lasso_coefs_abs_mean_only_nonnull_fts.shape[0]
print("- Out of %s , number of features with null coefs is %s and number of non null is %s " %(single_task_lasso_coefs_abs_mean_only.shape[0],number_of_nuls_coefs_fts,single_task_lasso_coefs_abs_mean_only_nonnull_fts.shape[0]))
# lets sort by mean coef value the remaining fts (they have non null coefs)
single_task_lasso_coefs_abs_mean_only_nonnull_fts_sorted = single_task_lasso_coefs_abs_mean_only_nonnull_fts.sort_values("Mean Coefficient Estimate 10 Seeds", axis=0, ascending=False, kind='mergesort') # axis=0 ie sort the rows

print(">>>Info of Analysis for file saving : ")
print("- Regularisation: ",regularization_used,", Cohort : ",tag_cohort,", Scorer : ",tag_scorer,", Num_trial : ",tag_num_trial)

# - saving the list of non null coefs features
name_coefs_report = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_singletask_sklearn/non_null_coefs_sklearn_"+ regularization_used +"_10seeds_"+ tag_cohort +"_"+ tag_scorer+"_"+ tag_num_trial+".csv"
single_task_lasso_coefs_abs_mean_only_nonnull_fts_sorted.to_csv(name_coefs_report, index=None, header=True)
print("- File with non nul coefs saved into following path file : ")
print(name_coefs_report)
# all the analysis is done : get the runtime
runtime_analysis = duration_from(globalstart)
print(bcolors.OKGREEN + " Analysis (" + tag_num_trial + ") done : Time taken is : ", runtime_analysis, bcolors.ENDC)
# end concatenated with "," instead of "+" to avoid TypeError: unsupported operand type(s) for +: 'datetime.timedelta' and 'str'





