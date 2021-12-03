# making an estimator that will use one single task dataset (all fts)
# source of the train, validation and then test method : https://github.com/MachineLearnia/Python-Machine-Learning/blob/master/21%20-%20Sklearn%20:%20Model%20Selection.ipynb


#>>>>>>>>>>> imports (mandatory)
import numpy as np
import sys # to make all stdout display go to a log file (our .o in the results batch of files)
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.metrics import make_scorer,matthews_corrcoef,cohen_kappa_score,f1_score,balanced_accuracy_score # define the scoring to use and computetest metrics
from engines.watcher_engine import timer_started # for duration of operations
from engines.data_engine3_bay import local_link_to_csv_dataset_getter,dataset_summoner
from engines.learning_algs_preps1 import SPAMS_grp_membership_vector_maker1,list_seeds_maker,creator_of_collectors_for_reg_gdscv
from engines.metrics_engine2 import f1bin_score, MM4_bespoke_score,collectors_supplier_after_reg_gdscv
from engines.learning_algs_param_grids import param_grid_lambdas123_space_maker1
from engines.watcher_engine2 import report_maker1,roc_curve_finisher_after_all_iterations_of_the_mdl2
import matplotlib.pyplot as plt # used to make plots # for roc curves
# >>>>>> imports (choose one)
from engines.learning_algs_engine_spams import SPAMSCustomEstimator0
from sklearn import linear_model # for sklearn regressions


globalstart = timer_started() # start a clock to get the time after all the analysis

# >>>> Analysis_stickers
# - these have functional roles...
# + a specific string to choose a dataset to analyse
# tag_cohort = "GSE41998"
# tag_cohort = "GSE26639"
# tag_cohort = "GSE32646"
# tag_cohort = "GSE25055"
# tag_cohort = "GSE20194"
tag_cohort = "GSE63471"
# + a number of seeds, each one for a random state where we have to estimate the model selection
num_seeds = 10 # use 2 for tests
# + response val type for the response values
# resp_values_type = "resp_val_type_as_float"
resp_values_type = "resp_val_type_as_int"
# + use intercept or not
add_intercept = "yes"
# add_intercept = "no"
# + the scorer used in the best model selection in gridsearchcv
# tag_scorer = "MM4" # MM4 = "MixedMetricof4"
tag_scorer = "f1" # f1 = "f1_score"
# + the list of tags for the metrics to compute and report for each best model
# list_tags_metrics = ["MM4", "MCC", "CK", "F1", "BalAcc"]
list_tags_metrics = ["MM4", "MCC", "CK", "F1", "BalAcc", "Acc","Prec", "Rec","AUC"]
# a tag saying if to make a log or not # tag caught
tag_decision_make_log = "yes"
# tag_decision_make_log = "no"


# - these are here to mark our final files and summary of what we have done exactly
# the illness studied
tag_ctype = "BRCA"
# the drug studied
tag_drugname = "NACTaxanesBR"
# the profile of data studied
tag_profilename = "GEX_MA"
# type of SL task
task_type = "Regr" ##! add later the classif tag
# a tag for the name of the alg ran
scheme_used = "SklearnL1LogReg"
# a tag for the precise version of the estimator used as the alg
name_of_the_estimator_used = "FromSklearnlinearModelLbrary"
# the type of model produced (omc, allfts, mutlitask, etc.)
the_model_compared = "Allfts_Singletask"
# Name of the trial that will be run for this exact analysis
tag_num_trial = "Trial0066" # = "Trial_test" for testing
# name of the base dir where to put our results files
basedir = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks"

#>>>>>>>>>>>>>>>>>>>>>>>>>>>REDIRECTION OF STDOUT TO .o FILE OR NOT 1/2<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# A log file name Output_following_trialNameGivenByUser.0 is created
if tag_decision_make_log == "yes":
	original_out = sys.stdout
	sys.stdout = open(basedir + '/outputs/Output_' + task_type + "_" + scheme_used + "_" + the_model_compared + "_" + tag_ctype + "_" + tag_drugname + "_" + tag_profilename + "_" + tag_num_trial + ".o", 'w')
	print('This is the log file following the course of the analysis:')
else :
	print("A log file is not to be created. Analysis is to be followed on this standard output :")
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



# >>>>>>>>> bring in the data
local_link_to_csv_dataset = local_link_to_csv_dataset_getter(tag_cohort)

# >>>>> dataset summoning
list_data_summoned = dataset_summoner(local_link_to_csv_dataset,resp_values_type,add_intercept)
df_input = list_data_summoned[0]
df_output = list_data_summoned[1]
X = list_data_summoned[2]
y = list_data_summoned[3]
list_all_fts_df_input = list_data_summoned[4]
size_list_all_fts_df_input = len(list_all_fts_df_input)

# # >>>>>> lets make the groupe membership vector : its np.array(list_of_1st_index_where_a_ft_occurs)
# groups_in_data = SPAMS_grp_membership_vector_maker1(list_all_fts_df_input)

#>>>>>>>>>>>> define our scorer
if tag_scorer == "MM4" : # tag_scorer = "MM4" # MM4 = "MixedMetricof4"
	grid_scorer = make_scorer(MM4_bespoke_score, greater_is_better=True)
elif tag_scorer == "f1" : # f1 = "f1_score" as the default for the gridscorer
	grid_scorer = make_scorer(f1bin_score, greater_is_better=True)
else:
	grid_scorer = "undefined_scorer"
	print("Warning : Non recognized tag for a scorer to use for model selection in gridsearch. Please supply a tag pointing to a scorer implemented !")

# use :  scoring=grid_scorer in GridSearchCV()


# >>>>>>>>> lets build the gallery of our hyperparameters (the variating params of the alg) values here
# param_grid_gallery = param_grid_lambdas123_space_maker1() # for a test ie 5 lambda1 values + beefing up
# param_grid_gallery = param_grid_lambdas123_space_maker1("geom",0.0001,100.0,200,"yes",None,"no") # for a run with 200 lambda1 values from 0.0001 to 100.0, with added values, no Cing (205 values of lambda1)
# param_grid_gallery = param_grid_lambdas123_space_maker1("geom",0.0001,100.0,0,"yes",None,"no","geom",0.0001,100.0,200,"yes",None,"no") # 200 values of lambda2 only
# param_grid_gallery = param_grid_lambdas123_space_maker1("geom",0.0001,100.0,200,"yes",None,"no","geom",0.0001,100.0,200,"yes",None,"no") # 200 values of lambda1 and 200 values of lambda2
param_grid_gallery = param_grid_lambdas123_space_maker1("geom",0.0001,100.0,200,"yes",None,"yes") # 5 values of lambda1 in sklearn (C) # for test
# param_grid_gallery = param_grid_lambdas123_space_maker1("geom",0.0001,100.0,200,"yes",None,"yes") # 200 values of lambda1 in sklearn (C)
param_grid = param_grid_gallery[0]
param_grid_sizes = param_grid_gallery[1]
# >>>>>>>>>>> Introduce an estimator to use as learning alg
# done in imports


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  the results collectors
list_collectors_created = creator_of_collectors_for_reg_gdscv(list_all_fts_df_input,list_tags_metrics,param_grid)
# - Collector1 -  introduce a df that later will have : with col 1 = the list of fts, col seed 1 to col last_seed have each the coefs of the best model of the seed
PdCol_coefs = list_collectors_created[0]
# - Collector1bis -  a list of the colnames containing coefs at each seed (useful later to access directly the cols with coefs and change them into absolute values)
list_of_cols_coefs = list_collectors_created[1]
# - Collector2 -  the list where to stash the validation (gridscorer) score obtained at each seed by the best model
ListCol_val_scores = list_collectors_created[2]
# - Collector3 -  the dict key as tag of a metric and value as a list of values that are the test scores of the best models (one at each seed)
DictCol_test_scores = list_collectors_created[3]
list_tags_metrics_computed_for_testscore = list_collectors_created[4] # a list of the names of the keys to use for the previous dict of test scores
# - Collector4 -  the dict key as a name of hp and value as a list of values that have been the best value of the hp at a seed
DictCol_bestval_HPsExplored = list_collectors_created[5]
list_names_HPs_explored = list_collectors_created[6] # a list of the names of the hp explored (used to update the previous dict "HP" as key and "best values of HP" as values
# Collector5 - the collectors related to building the ROC curves for the alg at each seed and make an average ROC curve
tprs_col_by_seed_one_alg = list_collectors_created[7]
aucs_col_by_seed_one_alg = list_collectors_created[8]
mean_fpr_by_seed_one_alg = list_collectors_created[9]
# Collector6 - the figure for the plot that receives the roc curves
figure_one_alg, ax1 = plt.subplots()

# >>>>>>>>>>>>>> The GridSearchCV for best model selection repeated on multiple seeds
# - the idea is to go through the seeds and do these steps :
# 1- define the data splits :
# one part is for train+validation (for best model search) (a 2nd internal separation of the training and validation set is made by the gridsearchcv
# another part is for test to use (for best model estimation)
# 2- for the best model obtained from validation, we keep in the respective collectors these values : a) the coef of all the fts, b) the validation score, c) the HPs explored values, d) the test score

# - make a list of seeds, each one for a random state where we have to estimate the model selection
list_seeds=list_seeds_maker(num_seeds)
# - loop on the seeds and carry out the idea
for a_seed in list_seeds:  # test a_seed = 0, # a_seed = 1
	print("- Started working with seed", a_seed)
	# - fixate the actual seed
	np.random.seed(a_seed)
	# - get the different train and test part of our data
	X_train, X_test, y_train, y_test = train_test_split(X, y,stratify=y, test_size=0.1, random_state=a_seed)
	# - define the gridsearchcv
	modelselector_by_GSCV = model_selection.GridSearchCV(linear_model.LogisticRegression(penalty='l1', solver='saga', random_state=a_seed, class_weight="balanced", fit_intercept=False,max_iter=200,tol=0.01), param_grid, scoring=grid_scorer, cv=10, n_jobs=-1) # same as before but without stating the refit
	# - fit lasso
	modelselector_by_GSCV.fit(X_train, y_train)
	# - collecting metrics values for the model selected from the best model search
	collectors_supplier_after_reg_gdscv(PdCol_coefs,
										list_of_cols_coefs,
										ListCol_val_scores,
										DictCol_test_scores,
										list_tags_metrics_computed_for_testscore,
										DictCol_bestval_HPsExplored,
										list_names_HPs_explored,
										mean_fpr_by_seed_one_alg,
										tprs_col_by_seed_one_alg,
										aucs_col_by_seed_one_alg,
										a_seed,
										ax1,
										modelselector_by_GSCV,
										y_test,X_test)
	# - announce the end of the work for a seed
	print("- Finished working with seed", a_seed)

# - making the operations for the average roc curve
roc_curve_finisher_after_all_iterations_of_the_mdl2(figure_one_alg,
													ax1,
													tprs_col_by_seed_one_alg,
													mean_fpr_by_seed_one_alg,
													aucs_col_by_seed_one_alg,
													basedir,
													task_type,scheme_used,the_model_compared,
													tag_ctype,tag_drugname,tag_profilename,tag_num_trial)


# >>>>>>>>>>>>> Produce a report of the analysis using variables and collectors updated
report_maker1(tag_cohort,num_seeds,resp_values_type,add_intercept,tag_scorer,list_tags_metrics,
			  tag_ctype,tag_drugname,tag_profilename,
			  task_type,scheme_used,name_of_the_estimator_used,the_model_compared,tag_num_trial,
			  list_seeds,
			  PdCol_coefs,ListCol_val_scores,DictCol_test_scores,DictCol_bestval_HPsExplored,
			  size_list_all_fts_df_input,list_of_cols_coefs,
			  basedir,
			  globalstart)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>REDIRECTION OF STDOUT TO .o FILE OR NOT 2/2<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# stop redirection of stdout if it was being done
if tag_decision_make_log == "yes":
	sys.stdout = original_out
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# end of analysis



