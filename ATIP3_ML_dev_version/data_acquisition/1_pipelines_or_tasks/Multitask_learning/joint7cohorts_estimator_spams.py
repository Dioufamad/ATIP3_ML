# making an estimator that will use the 7 cohorts joint dataset (common fts)

#>>>>>>>>>>>imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#>>>>>>>>>>bring in the data
# - link for the common fts dataset
local_link_to_csv_dataset = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/JoinNewDesign1CommonFtsof6_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"
df = pd.read_csv(local_link_to_csv_dataset) # read the dataset in a df and an option is "sep_in_file = ","" to precise what was the separator in the file
# when the first column was kept because it was the previous index, we can put it back as index with this
df.rename(columns={"Unnamed: 0" : "samples_names"}, inplace=True)
df = df.set_index(list(df.columns)[0])

# lets find the n_samples_per_task list
dict_cht_nsamples_in_order = {}
col_cohort_list = list(df["cohort"])
for a_cohort in col_cohort_list:
    if a_cohort not in list(dict_cht_nsamples_in_order.keys()) :
        count_samples_from_cohort = df.loc[df['cohort'] == a_cohort].shape[0]
        dict_cht_nsamples_in_order[a_cohort] = count_samples_from_cohort
n_samples_per_task = list(dict_cht_nsamples_in_order.values())

# lets separate our data
# input
df_input = df.iloc[:, :-2] # recommended to iloc to produce a slice # :-1 means all except the last one
X = df_input.values
# output
df_ouput = df.iloc[:,-2] # -1 means select the last one only and it is the cohort (not a value analysed)
y = df_ouput.values

# >>>>>>>>>>>> Separate single - task l1 - regularized logistic regressions on each task with sklearn
#     Let 's consider our 7 tasks separately and run an l1-regularized logistic regression
n_tasks = len(list(dict_cht_nsamples_in_order.keys()))
n_features = X.shape[1]
from sklearn import linear_model
from sklearn import model_selection
param_grid = {'C': np.logspace(-3, 2, num=100)} # define the grid of params and params values to explore
# the array of value to test for C : is returned here a list of values evenly spaced, log10(start value is -3 ie start val is 0,001) and log10(end value is 2 ie start val is 100)
# this is to be able to have non nul values evenly spaced that goes from 0,OO1 to 100 (from the lowest without being zero to the very high like 100)
from sklearn.metrics import matthews_corrcoef # define the scoring to use
from sklearn.metrics import make_scorer
my_scoring1 = {'mcc': make_scorer(matthews_corrcoef)} # 'roc_auc_score':make_scorer(roc_auc_score)
lasso_gs = model_selection.GridSearchCV(linear_model.LogisticRegression(penalty='l1', solver='liblinear'), param_grid, scoring=my_scoring1,cv=10, n_jobs=-1) # old scoring="f1"
single_task_lasso_coefs = np.zeros(shape=(n_tasks, n_features)) # initialize a empty grid for the coefs
start_idx = 0
end_idx = 0
# go through the tasks and get :
# 1- the coef od the fts for the best model
# 2-the best params for that best model
for r in range(n_tasks):  # test r = 0
    end_idx += n_samples_per_task[r]
    # fit lasso
    # X_train1 = X[start_idx:end_idx, :]
    # y_train1 = y[start_idx:end_idx]
    lasso_gs.fit(X[start_idx:end_idx, :], y[start_idx:end_idx])
    # obtain coefficients
    single_task_lasso_coefs[r, :] = lasso_gs.best_estimator_.coef_ # best_estimator_.coef_ is here the a 1D array of same numbers of values (coefs) as the number of fts. ## to test, do a=lasso_gs.best_estimator_.coef_
    # obtain lambda
    print("Best lambda for task %d: %s with score %s" % (r, lasso_gs.best_params_,lasso_gs.best_score_)) # best params give me a dict of key as a param and value as best value for the param
    start_idx += n_samples_per_task[r]
