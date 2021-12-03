# This is the V2.0 of the script "gridsearchcv_sklearn_MCC_L1.py"
# Objective : run sklearn L1 log reg on differents datasets (priority is the 1 cohort datasets)
# New possibilities :
# - an MM4 corrected by dividing by 4 and not 5 for 4 metrics average
# - manipulations before and after the GSCV are done now by functions from modules imported
# - test score show now values for 5 metrics : MM4, MCC, CK, F1, BalAcc
# source of the train, validation and then test method : https://github.com/MachineLearnia/Python-Machine-Learning/blob/master/21%20-%20Sklearn%20:%20Model%20Selection.ipynb



#>>>>>>>>>>> imports (mandatory)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.metrics import make_scorer,matthews_corrcoef,cohen_kappa_score,f1_score,balanced_accuracy_score # define the scoring to use and computetest metrics
from engines.watcher_engine import timer_started # for duration of operations
from engines.data_engine3_bay import local_link_to_csv_dataset_getter,dataset_summoner
from engines.learning_algs_preps1 import list_seeds_maker
from engines.metrics_engine2 import overall_average_score_MM4
from engines.learning_algs_param_grids import param_grid_sklearn_206C_maker1
from engines.data_engine2_allocation import add_entry_in_dict # a function updater of dict with values a list (needed to create the list for the first elements and add to it if the list exists already)
from engines.watcher_engine2 import report_maker1
# >>>>>> imports (choose one)
# from engines.learning_algs_engine_spams import SPAMSCustomEstimator0
from sklearn import linear_model # for sklearn regressions

globalstart = timer_started() # start a clock to get the time after all the analysis

# >>>> Analysis_stickers
# - these have functional roles...
# a specific string to choose a dataset to analyse
tag_cohort = "GSE63471"
# a number of seeds, each one for a random state where we have to estimate the model selection
num_seeds = 10 # use 2 for tests
# response val type for the response values
# resp_values_type = "resp_val_type_as_float"
resp_values_type = "resp_val_type_as_int"

# - these are here to mark our final files and summary of what we have done exactly
scheme_used = "SklearnLogRegL1"
name_of_the_estimator_used = "SklearnEstimator"
# the scorer used in the best model selection in gridsearchcv
tag_scorer = "MM4" # MM4 = "MixedMetricof4"
# Name of the trial that will be run for this exact analysis
tag_num_trial = "trial1" # = "Trial_test" for testing

# >>>>>>>>> bring in the data
local_link_to_csv_dataset = local_link_to_csv_dataset_getter(tag_cohort)

# >>>>> dataset summoning
list_data_summoned = dataset_summoner(local_link_to_csv_dataset,resp_values_type)
df_input = list_data_summoned[0]
df_output = list_data_summoned[1]
X = list_data_summoned[2]
y = list_data_summoned[3]
list_all_fts_df_input = list_data_summoned[4]
size_list_all_fts_df_input = len(list_all_fts_df_input)

#>>>>>>>>>>>> define our scorer
grid_scorer = make_scorer(overall_average_score_MM4, greater_is_better=True)
# use :  scoring=grid_scorer in GridSearchCV()

# >>>>>>>>> lets build the gallery of our hyperparameters (the variating params of the alg) values here
param_grid = param_grid_sklearn_206C_maker1()

# >>>>>>>>>>> Introduce an estimator to use as learning alg
# done in imports


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  the results collectors
# - Collector1 -  introduce a df that later will have : with col 1 = the list of fts, col seed 1 to col last_seed have each the coefs of the best model of the seed
PdCol_coefs = pd.DataFrame()
PdCol_coefs["Features"] = df_input.columns # make the col of the fts
# - Collector1bis -  a list of the colnames containing coefs at each seed (useful later to access directly the cols with coefs and change them into absolute values)
list_of_cols_coefs = []
# - Collector2 -  the list where to stash the validation (gridscorer) score obtained at each seed by the best model
ListCol_val_scores = []
# - Collector3 -  the dict key as tag of a metric and value as a list of values that are the test scores of the best models (one at each seed)
DictCol_test_scores = {}
list_tags_metrics_computed_for_testscore = ["MM4","MCC","CK","F1","BalAcc"] # a list of the names of the keys to use for the previous dict of test scores
# - Collector4 -  the dict key as a name of hp and value as a list of values that have been the best value of the hp at a seed
DictCol_bestval_HPsExplored = {}
list_names_HPs_explored = list(param_grid.keys()) # a list of the names of the hp explored (used to update the previous dict "HP" as key and "best values of HP" as values


# >>>>>>>>>>>>>> The GridSearchCV for best model selection repeated on multiple seeds
# - the idea is to go through the seeds and do these steps :
# 1- define the data splits in train+validation and test to use respectively for best model search and for best model estimation
# 2- for the best model in validation, we keep in the respective collectors : a) the coef of the fts, b) the validation score, c) the HPs explored values, d) the test score

# - make a list of seeds, each one for a random state where we have to estimate the model selection
list_seeds=list_seeds_maker(num_seeds)
# - loop on the seeds and carry out the idea
for a_seed in list_seeds:  # test a_seed = 0, # a_seed = 1
    print("- Started working with seed", a_seed)
    # - fixate the actual seed
    np.random.seed(a_seed)
    # - get the different train and test part of our data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=a_seed)
    # - define the gridsearchcv
    modelselector_by_GSCV = model_selection.GridSearchCV(linear_model.LogisticRegression(penalty='l1', solver='saga', random_state=a_seed, class_weight="balanced", fit_intercept=False,max_iter=200,tol=0.01), param_grid, scoring=grid_scorer, cv=10, n_jobs=-1) # same as before but without stating the refit
    # - fit lasso
    modelselector_by_GSCV.fit(X_train, y_train)
    # - keep coefficients
    # best_estimator_.coef_ is here is a 1D array of same numbers of values (coefs) as the number of fts. so we need to flatten to make it usable as a column
    A = modelselector_by_GSCV.best_estimator_.coef_
    B = A.flatten()
    colname_coefs_values = "Coefficient Estimate Seed " + str(a_seed) # making the name of the column that will accept the values
    list_of_cols_coefs.append(colname_coefs_values)
    PdCol_coefs[colname_coefs_values] = pd.Series(B)
    # - keep val scores
    ListCol_val_scores.append(modelselector_by_GSCV.best_score_)
    # - keep hp of interest
    for a_hp_explored in list_names_HPs_explored:
        a_hp_explored_best_val = modelselector_by_GSCV.best_params_[a_hp_explored]
        add_entry_in_dict(DictCol_bestval_HPsExplored, a_hp_explored, a_hp_explored_best_val)
    # DictCol_bestval_HPsExplored.append(list(modelselector_by_GSCV.best_params_.values())[0]) # deprecated (only captured the val of the 1st hp)
    # - keep test scores with hp of interest value
    model_retained_asbest = modelselector_by_GSCV.best_estimator_
    # - keep the test score for the model retained as best model during the gridsearchcv
    for a_metric_of_testscore_to_compute in list_tags_metrics_computed_for_testscore:
        # compute the testscore for a metric
        if a_metric_of_testscore_to_compute == "MM4" :
            model_retained_asbest_testscore = overall_average_score_MM4(y_test, model_retained_asbest.predict(X_test))  # MM4
        elif a_metric_of_testscore_to_compute == "MCC" :
            model_retained_asbest_testscore = matthews_corrcoef(y_test, model_retained_asbest.predict(X_test))  # MCC
        elif a_metric_of_testscore_to_compute == "CK" :
            model_retained_asbest_testscore = cohen_kappa_score(y_test, model_retained_asbest.predict(X_test))  # cohen_kappa
        elif a_metric_of_testscore_to_compute == "F1" :
            model_retained_asbest_testscore = f1_score(y_test, model_retained_asbest.predict(X_test), average='binary')  # f1_score
        else : # a_metric_of_testscore_to_compute == "BalAcc"
            model_retained_asbest_testscore = balanced_accuracy_score(y_test, model_retained_asbest.predict(X_test))  # bal acc
        # stash the testscore computed in the proper place if the testscores dict metric as key and list of testscores as value
        add_entry_in_dict(DictCol_test_scores, a_metric_of_testscore_to_compute, model_retained_asbest_testscore)
    # - announce the end of the work for a seed
    print("- Finished working with seed", a_seed)

# >>>>>>>>>>>>> Produce a report of the analysis using variables and collectors updated
report_maker1(globalstart,
              tag_cohort,
              num_seeds,
              scheme_used,
              name_of_the_estimator_used,
              tag_scorer,
              tag_num_trial,
              size_list_all_fts_df_input,
              PdCol_coefs,
              list_of_cols_coefs,
              ListCol_val_scores,
              DictCol_test_scores,
              DictCol_bestval_HPsExplored,
              list_seeds)


# end of analysis