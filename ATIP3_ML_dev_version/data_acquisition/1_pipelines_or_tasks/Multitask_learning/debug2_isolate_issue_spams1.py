###################################################################################################################################################
#########################################################TESTING NOW ##########################################################################
###################################################################################################################################################

# #>>>>>>>>>>>imports (full list)
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn import linear_model
# from sklearn import model_selection
# from sklearn.metrics import cohen_kappa_score,make_scorer # define the scoring to use
# from sklearn.model_selection import learning_curve
# from engines.watcher_engine import timer_started,duration_from,bcolors # for duration of operations and display colors
# import spams # for SPAMS API workings
# from scipy import sparse # to convert arrays

# >>>> strictly used imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import spams # for SPAMS API workings
# from scipy import sparse # to convert arrays


# globalstart = timer_started() # start a clock to get the time after all the analysis
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
df_input = df.iloc[:, :-2] # recommended to iloc to produce a slice # :-1 means all except the last one
# df_input = df.iloc[:, :200] # testing with just 200 cols like in the examples
# df_input = df.iloc[:, :36102] # testing with half of the columns
# df_input = df.iloc[:, :48136] # testing with the columns of 4 dfs fts
# df_input = df.iloc[:, :60170] # testing with the columns of 4 dfs fts (48k N, 40k Y, 44 Y, 46 Y, -2 N,)
X = df_input.values
# output
df_ouput = df.iloc[:,-2] # -1 means select the last one only and it is the cohort (not a value analysed)
y = df_ouput.values
# get the tag_of_cohort to mark the cohort used :
df_cohort_col = df.iloc[:,-1]
sorted_list_of_cohorts = sorted(df_cohort_col.unique())
tag_cohort = "JoinNewDesign1CommonFtsof6"
tag_scorer = "CKS"
# Group membership vector
dict_ntasks_nfeatures = {0 : 12034, 1 : 12034, 2 : 12034, 3 : 12034, 4 : 12034, 5 : 12034}
# n_tasks = len(list(dict_ntasks_nfeatures.keys()))
groups_in_data = np.array([(1+x) for a_taskt in list(dict_ntasks_nfeatures.keys()) for x in np.arange(dict_ntasks_nfeatures[a_taskt])], dtype=np.int32)

#<<<<<<<<<<<<<<<<<<<< lets use the implemented class
# - the variation parmas of the alg
regularization_used = "SPAMSSGLL2lossIsSquare"
# list_seeds=[0,1,2,3,4,5,6,7,8,9]
list_seeds=[0,1] # for tests
reg_strength_space = np.geomspace(0.0001, 100.0, num=200) # 0.0001 to 1 (200 lambda values)
if 0.1 not in reg_strength_space :
    reg_strength_spaceplus1value = np.append(reg_strength_space, 0.1)
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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #! check ,random_state=a_seed is to be added
# - fixate the actual seed
a_seed = 0
print("- Starting working with seed", a_seed)
np.random.seed(a_seed)
# - get the different train and test part of our data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=a_seed)

#<<<< trying with my data
X = np.asfortranarray(X_train,dtype='float') # working version  # the csc_matrix version is X = sparse.csc_matrix(X_train,dtype='float64') and does not solve the memory issue
Y = np.asfortranarray(y_train.reshape((y_train.shape[0], 1)),dtype='float')
# Y = np.asfortranarray(y_train)
W0 = np.zeros((X.shape[1],Y.shape[1]),dtype='float',order="F")
# param = {'numThreads' : -1,'verbose' : True, 'lambda1' : 0.05, 'it0' : 10, 'max_it' : 200, 'L0' : 0.1, 'tol' : 1e-3, 'intercept' : False, 'pos' : False} # ori
# param = {'numThreads' : -1,'verbose' : True, 'lambda1' : 0.05} # test1 for the 200 cols used in the original test
param = {'numThreads' : -1,'verbose' : True, 'lambda1' : 0.05, 'it0' : 10, 'max_it' : 50, 'L0' : 0.1, 'tol' : 1e-3, 'intercept' : False, 'pos' : False} # test for the limit num of fts that shows the process error
# np.random.seed(0)
# Regression experiments
# 100 regression problems with the same design matrix X.
print('\nVarious regression experiments')
param['compute_gram'] = True
print('\nFISTA + Regression l1')
param['loss'] = 'square'
param['regul'] = 'l1'
(W, optim_info) = spams.fistaFlat(Y,X,W0,True,**param)


# end