###--------------------- This is the location of some functions to report on the results (used primarily during regression work of single-task vs multitask) -----------------------

###---------------------IMPORTS
import numpy as np
import locale
from engines.watcher_engine import duration_from,bcolors # for duration of operations and display colors
#====================================================================
# added to test new functions
# (ie remove anything not necessary in the end and update older versions of these functions)
from datetime import datetime # for time functions (2)
#---for drawing roc curves
# import numpy as np
# from scipy import interp  # used to interpolate data points between data instances # for roc curve # fucntion name has changed so we use the identical tolder fucntion np.interp
from sklearn.metrics import roc_curve, auc # to compute fpr,tpr based by looping on a gallery of thresholds # compute auc of roc curve # for roc curve
from textwrap import wrap # to wrap plot titles
import matplotlib.pyplot as plt # used to make plots # for roc curves

# ---------------------Variables to initialise------------------------------------------
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') #for setting the characters format
#====================================================================

# >>>>>>>>>>>> a group of function that draws the roc curve for a best model search
# this is inspired by the old roc curves functions that were comparing omc vs all_fts_mdl in subplts


#-----------drawing ROC curves functions version 2
# (this is only for the GSCV of one alg ie 1 fig is obtained with the each seed roc curve and the average roc curve)
def roc_curve_updater_after_one_iteration_of_the_mdl2(array_of_the_mdl_implicated_samples_observations_considering_predictions_2probs_on_all_data,
                                                      array_of_the_mdl_predictions_2probs_on_all_data,
                                                      RespClasses,
                                                      mean_fpr_of_mdl,
                                                      tprs_col_of_mdl,
                                                      aucs_col_of_mdl,
                                                      id_iter,
                                                      fig_subplot_as_axi):
	# fpr and tpr using a set of thresholds
	fpr_mdl_one_iter, tpr_mdl_one_iter, thresholds_mdl_one_iter = roc_curve(array_of_the_mdl_implicated_samples_observations_considering_predictions_2probs_on_all_data, array_of_the_mdl_predictions_2probs_on_all_data, pos_label=RespClasses[1])
	# first arg is col truth classes, 2nd arg is col of class pos in classic array of probabilities, 3rd arg indicate the classes to take as pos among the two seen if the classes are not {0,1} or {-1,1}
	# a galerie of thresholds is made and each value of it is used to make calls of predictions and calculate with truth classes col, the fpr and tpr
	# Nb : one value in thresholds will seems out of the classic range 0-1 of probabilites in the positives (eg: 1,888). it is to ancher the extreme value of (0,0) and by calling alls samples as neg
	# to make a situation of TP = 0 ie tpr = 0 ie all curves of each iteration have a starting point
	# that pose the question of why not and when to fixated also the extreme point of (1,1) : it not needed for each iteration curve, we let them end wherever. though, that extreme point will be
	# defined at the time of building the mean curve ie the real roc curve
	tprs_col_of_mdl.append(np.interp(mean_fpr_of_mdl, fpr_mdl_one_iter, tpr_mdl_one_iter))  # stock the array of values of tpr that will be in y axis
	tprs_col_of_mdl[-1][0] = 0.0  # force the first value of the first array in the content of tpr collector to be 0.0 (see previous explanation)
	roc_auc_of_mdl_one_iter = auc(fpr_mdl_one_iter, tpr_mdl_one_iter)  # compute the auc value for this iteration
	aucs_col_of_mdl.append(roc_auc_of_mdl_one_iter)  # ...and add it to the auc collector
	fig_subplot_as_axi.plot(fpr_mdl_one_iter, tpr_mdl_one_iter, lw=1, alpha=0.3, label='ROC curve seed %d (AUC = %0.2f)' % (id_iter, roc_auc_of_mdl_one_iter))  # plot this iteration roc curve and what will be in the legend marked for it (roc interation id and auc value)
	return
# return nothing but old version used to return roc_auc_of_mdl_one_iter in order to put it in a table (no need for that here)

def roc_curve_finisher_after_all_iterations_of_the_mdl2(fig,
                                                        fig_subplot_as_axi,
                                                        tprs_col_of_mdl,
                                                        mean_fpr_of_mdl,
                                                        aucs_col_of_mdl,
                                                        basedir,
                                                        task_type,
                                                        scheme_used,
                                                        the_model_compared,
                                                        tag_ctype,
                                                        tag_drugname,
                                                        tag_profilename,
                                                        tag_num_trial):
	# NB : this is the succession of the arguments in the older model that was used when a 3rd axi in the plot is dedicated to showing the average roc curves only
    # the part to add the average roc curve to that 3rd plot is uncommented so the 3rd axi is removed from the arguments (it was the 3rd arg)
    # old succesio of args was : fig,fig_subplot_as_axi,mdls_comp_fig_subplot_as_axi,tprs_col_of_mdl,mean_fpr_of_mdl,aucs_col_of_mdl,basedir,task_type,scheme_used,the_model_compared,tag_ctype,tag_drugname,tag_profilename,tag_num_trial
	##--for the ROC curve of omc mdl
	# add to the plot the line for the random prediction
	fig_subplot_as_axi.plot([0, 1], [0, 1], linestyle='--', lw=2, color='r', label='Random predictor', alpha=.8)
	# compute mean of tpr collector of tpr array : gives an array of tpr use for mean roc curve
	mean_tpr_from_tprs_col_of_mdl = np.mean(tprs_col_of_mdl, axis=0)
	# fixate the etrame values of tpr for the mean curve to 1
	mean_tpr_from_tprs_col_of_mdl[-1] = 1.0
	# use mean fpr and mean tpr to get mean auc (same as using auc function for one fpr,one tpr and get one auc value)
	mean_auc_from_cols_of_mdl = auc(mean_fpr_of_mdl, mean_tpr_from_tprs_col_of_mdl)
	# compute standard deviation on the flattened array given
	std_auc_from_aucs_col_of_mdl = np.std(aucs_col_of_mdl)
	# plot the mean roc curve and what will be in the legend marked for it (mean roc and auc value)
	fig_subplot_as_axi.plot(mean_fpr_of_mdl, mean_tpr_from_tprs_col_of_mdl, color='b', label=r'Mean ROC curve (AUC = %0.2f $\pm$ %0.2f)' % (mean_auc_from_cols_of_mdl, std_auc_from_aucs_col_of_mdl), lw=2, alpha=.8)

	# #>>> uncomment when the average roc curve has to be added to a figure where only the average curve of multiples models are put in order to be compared visualy
	# #----*added : this mean roc curve to the average plot
	# if the_model_compared.startswith("OMC"):
	# 	color_of_line = 'c' # 'c' for cyan for OMC
	# else :
	# 	color_of_line = 'm'  # 'm' for magenta for Allfts
	# # plot the mean roc curve and what will be in the legend marked for it (mean roc and auc value)
	# mdls_comp_fig_subplot_as_axi.plot(mean_fpr_of_mdl, mean_tpr_from_tprs_col_of_mdl, color=color_of_line, label=r'Mean ROC %s model (AUC = %0.2f $\pm$ %0.2f)' % (the_model_compared,mean_auc_from_cols_of_mdl, std_auc_from_aucs_col_of_mdl), lw=2, alpha=.8)
	# #----*
    # #<<<

	# # -----*substracted : this to color between the highest and lowest of a mean TPR+-std dev at a fixated FPR value
	# # compute standard deviation on the arrays given, give a list of values, one for each column
	# std_tpr_from_tprs_col_of_mdl = np.std(tprs_col_of_mdl, axis=0)
	#
	# # to fill up with grayed-out color the area between the highest and lowest tpr values, we get the highest tpr value without going past 1
	# tprs_upper_from_tprs_col_of_mdl = np.minimum(mean_tpr_from_tprs_col_of_mdl + std_tpr_from_tprs_col_of_mdl, 1)
	# # ...same but wo going under 0
	# tprs_lower_from_tprs_col_of_mdl = np.maximum(mean_tpr_from_tprs_col_of_mdl - std_tpr_from_tprs_col_of_mdl, 0)
	# # make the grayed-out indicate area
	# fig_subplot_as_axi.fill_between(mean_fpr_of_mdl, tprs_lower_from_tprs_col_of_mdl, tprs_upper_from_tprs_col_of_mdl, color='grey', alpha=.2, label=r'$\pm$ std. dev. of mean TPR at fixated FPR ') # old version had 1 std. dev.
	# # -----*
	# limits of the x axis and y axis
	fig_subplot_as_axi.set_xlim([-0.05, 1.05])
	fig_subplot_as_axi.set_ylim([-0.05, 1.05])
	# labels of the x axis and y axis
	fig_subplot_as_axi.set_xlabel('False Positive Rate')
	fig_subplot_as_axi.set_ylabel('True Positive Rate')
	# title of the plot ##!! to modify using tags
	fig_subplot_as_axi.set_title("\n".join(wrap('ROC curve of %(Task)s using %(Alg)s-%(Model)s model, on case %(Ctype)s-%(Drug)s, %(Profile)s profile,  %(Trial)s' %
								 {"Task": task_type, "Alg": scheme_used, "Model": the_model_compared, "Ctype": tag_ctype, "Drug": tag_drugname, "Profile": tag_profilename, "Trial": tag_num_trial})))
	# position of legend
	fig_subplot_as_axi.legend(loc="lower right")
	## display the plot ##!! replace it with a plot saving ##!! check it our way of creating files creates also folders
	fig.savefig(basedir + 'Output_' + task_type + "_" + scheme_used + "_" + the_model_compared + "_" + tag_ctype + "_" + tag_drugname + "_" + tag_profilename + "_" + tag_num_trial + '_ROCcurve.png', bbox_inches='tight')
	return
# return nothing but old version used to return mean_auc_from_cols_of_mdl, std_auc_from_aucs_col_of_mdl in order to put it in a table (no need for that here)



#>>> uncomment because not needed for one alg GSCV
# the following existed for the old version of roc curves drawing that created an isolated fig for only the averages roc curves
##! not reviewed also (copied and pasted directly from old drawing functions without updating... review before use)
# def average_roc_curve_init(mdls_comp_fig_subplot_as_axi):
# 	mdls_comp_fig_subplot_as_axi.plot([0, 1], [0, 1], linestyle='--', lw=2, color='r', label='Random', alpha=.8)
#
#
# def average_roc_curve_finisher(mdls_comp_fig_subplot_as_axi, mdls_comp_fig, models_compared, task_type, tag_alg, tag_ctype, tag_drugname, tag_profilename, tag_num_trial, basedir):
# 	# limits of the x axis and y axis
# 	mdls_comp_fig_subplot_as_axi.set_xlim([-0.05, 1.05])
# 	mdls_comp_fig_subplot_as_axi.set_ylim([-0.05, 1.05])
# 	# labels of the x axis and y axis
# 	mdls_comp_fig_subplot_as_axi.set_xlabel('False Positive Rate')
# 	mdls_comp_fig_subplot_as_axi.set_ylabel('True Positive Rate')
# 	# title of the plot ##!! to modify using tags
# 	mdls_comp_fig_subplot_as_axi.set_title("\n".join(wrap('ROC curve comparing %(Model1)s and %(Model2)s models for %(Task)s using %(Alg)s, on case %(Ctype)s-%(Drug)s, %(Profile)s profile,  %(Trial)s' %
# 														  {"Model1": models_compared[0], "Model2": models_compared[1], "Task": task_type, "Alg": tag_alg, "Ctype": tag_ctype, "Drug": tag_drugname, "Profile": tag_profilename, "Trial": tag_num_trial})))
# 	# position of legend
# 	mdls_comp_fig_subplot_as_axi.legend(loc="lower right")
# 	## display the plot ##!! replace it with a plot saving ##!! check it our way of creating files creates also folders
# 	mdls_comp_fig.savefig(basedir + 'Output_' + task_type + "_" + tag_alg + "-" + models_compared[0] + "vs" + models_compared[1] + "_" + tag_ctype + "-" + tag_drugname + "-" + tag_profilename + "_" + tag_num_trial + '_ROCcurve.png', bbox_inches='tight')

# <<<

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>> a function that makes a full report after a GridSearchCV during regression tasks
# the arguments of this function usually appears along the script in this following order, so best to give them like this to the function to not forget one of them :
# globalstart, 0
# tag_cohort, 1
# num_seeds, 2
# scheme_used, 3
# name_of_the_estimator_used, 3
# tag_scorer, 4
# tag_num_trial,5
# size_list_all_fts_df_input, 6
# PdCol_coefs, 7
# list_of_cols_coefs, 8
# ListCol_val_scores, 9
# DictCol_test_scores,10
# DictCol_bestval_HPsExplored,11
# list_seeds,12

def report_maker1(tag_cohort, num_seeds, resp_values_type, add_intercept,tag_scorer,list_tags_metrics,
                  tag_ctype,tag_drugname,tag_profilename,
                  task_type,scheme_used, name_of_the_estimator_used, the_model_compared, tag_num_trial,
                  list_seeds,
                  PdCol_coefs,ListCol_val_scores, DictCol_test_scores, DictCol_bestval_HPsExplored,
                  size_list_all_fts_df_input,list_of_cols_coefs,
                  basedir,
                  globalstart):
    print(" >>>> Summary of model selection analysis : ")
    # ------------- state the choices made that will influence the run
    print("- These choices have been made and influence the run : ")
    print("+ Dataset analysed is known as : ", tag_cohort)
    print("+ Number of random states explored and averaged : ", num_seeds)
    print("+ Formatting of response values : ", resp_values_type)
    print("+ Adding an intercept : ", add_intercept)
    print("+ Scorer used in the best model selection (gridsearchcv) : ", tag_scorer)
    print("+ List of metrics computed for best models : ", list_tags_metrics, "and ROC curves.")

    # ------------ describe the specicity of the run using some tags entered
    print("- The run is described by the following : ")
    print("+ Illness studied :", tag_ctype)
    print("+ Drug studied :", tag_drugname)
    print("+ Profile of data used :", tag_profilename)
    print("+ Type of Supervised Learning task used :", task_type)
    print("+ Scheme/Alg used :", scheme_used)
    print("+ Estimator used :", name_of_the_estimator_used)
    print("+ The type of model produced :", the_model_compared)
    print("+ trial : ", tag_num_trial)

    # ------------ report the integrity of the results
    print(" >>>> Checking for integrity of the results collected...")
    # a counter of the verifications passed : if it is in the right number at the end, we mark all is okay
    num_global_verifs_passed = 0
    # check the coefs of best model : one col by seed + 1 col for the first col that has the names of the fts
    if PdCol_coefs.shape[1] == (num_seeds + 1):
        num_global_verifs_passed += 1
    else:
        print("+ Warning : the df used as best model coefs collector has wrong numbers of columns !")
    # check the list of val score saved : one val score for each seed
    if len(ListCol_val_scores) == num_seeds:
        num_global_verifs_passed += 1
    else:
        print("+ Warning : the list used as best model validation score collector has wrong numbers of elements !")
    # check for each HP, the size of the list of best values : one best value by seed
    num_verifications_passed_in_best_val_HP_dict = 0
    for a_HP_that_has_list_of_best_values in list(DictCol_bestval_HPsExplored.keys()):
        if len(DictCol_bestval_HPsExplored[a_HP_that_has_list_of_best_values]) == num_seeds:
            num_verifications_passed_in_best_val_HP_dict += 1
        else:
            print("+ Warning : the HP", a_HP_that_has_list_of_best_values, " has a list of best values that has wrong numbers of elements !")
    if num_verifications_passed_in_best_val_HP_dict == len(list(DictCol_bestval_HPsExplored.keys())):
        num_global_verifs_passed += 1
    # check for each metric of test score, the size of the list of best values : one best value by seed
    num_verifications_passed_in_best_val_testscoremetric_dict = 0
    for a_testscoremetric_that_has_list_of_best_values in list(DictCol_test_scores.keys()):
        if len(DictCol_test_scores[a_testscoremetric_that_has_list_of_best_values]) == num_seeds:
            num_verifications_passed_in_best_val_testscoremetric_dict += 1
        else:
            print("+ Warning : the test score metric", a_testscoremetric_that_has_list_of_best_values, " has a list of best values that has wrong numbers of elements !")
    if num_verifications_passed_in_best_val_testscoremetric_dict == len(list(DictCol_test_scores.keys())):
        num_global_verifs_passed += 1

    ##! add the verif part for the roc curves related collectors

    # give an answer to the full verification
    if num_global_verifs_passed == 4:
        print("+ All results are accounted for!")
    else:
        print("+ Please, check the faulty collectors or the process.")

    # ------------ for each seed, report the results obtained :
    print(" >>>> Report, for each seed, the results (best value for HPs explored, validation score, test score) for the best model found : ")
    for a_certain_seed in list_seeds:
        # an index of the seed, used each time to get the best value corresponding to the seed in a collector
        index_present_seed = list_seeds.index(a_certain_seed)
        # get the val_score
        seed_best_model_val_score = ListCol_val_scores[index_present_seed]
        # a dict with each key being an HP and its value being the best value for the seed
        seed_best_model_val_params = {}
        for one_of_the_HP_explored in list(DictCol_bestval_HPsExplored.keys()):
            seed_best_model_val_params[one_of_the_HP_explored] = DictCol_bestval_HPsExplored[one_of_the_HP_explored][index_present_seed]
        if "C" in list(DictCol_bestval_HPsExplored.keys()):
            seed_best_model_val_params_Ctranslated = 1 / (seed_best_model_val_params["C"])  # obtain a lambda value instead of a C value
        else:
            seed_best_model_val_params_Ctranslated = "not_in_this_context"
        # a dict with each key being a test score metric and its value being the value of the metric for the seed
        seed_best_model_test_score = {}
        for one_of_the_testscoremetric_computed in list(DictCol_test_scores.keys()):
            seed_best_model_test_score[one_of_the_testscoremetric_computed] = DictCol_test_scores[one_of_the_testscoremetric_computed][index_present_seed]
        # print the results depending if C is in the HPs explored or not (use % knowing %d is for the int and %s change everything into a string so no need to change dictionnaries of params into str first
        if "C" in list(DictCol_bestval_HPsExplored.keys()):
            print("+ Seed %d best model had : best params as %s (ie lambda from C of %s ) , validation score of %s and test score as %s." % (a_certain_seed, seed_best_model_val_params, seed_best_model_val_params_Ctranslated, seed_best_model_val_score, seed_best_model_test_score))
        else:
            print("+ Seed %d best model had : best params as %s , validation score of %s and test score as %s." % (a_certain_seed, seed_best_model_val_params, seed_best_model_val_score, seed_best_model_test_score))

    # ------------ get the perfs and best HPs values averages across the seeds :
    print(" >>>> Report, the averages across the seeds, for the results (test score, best value for HPs explored) for the best model  : ")
    # + for the perf across seeds
    dict_testscoremetrics_averaged_as_mean = {}  # for the mean values
    dict_testscoremetrics_averaged_as_median = {}  # for the median values
    dict_testscoremetrics_averaged_as_std = {}  # for the std values
    for a_testscoremetric_known in list(DictCol_test_scores.keys()):
        dict_testscoremetrics_averaged_as_mean[a_testscoremetric_known] = np.nanmean(DictCol_test_scores[a_testscoremetric_known])
        dict_testscoremetrics_averaged_as_median[a_testscoremetric_known] = np.nanmedian(DictCol_test_scores[a_testscoremetric_known])
        dict_testscoremetrics_averaged_as_std[a_testscoremetric_known] = np.nanstd(DictCol_test_scores[a_testscoremetric_known])
    print("+ The average test score, across the seeds : Mean %s" % dict_testscoremetrics_averaged_as_mean)
    print("+ The average test score, across the seeds : Median %s " % dict_testscoremetrics_averaged_as_median)
    print("+ The average test score, across the seeds : Std %s " % dict_testscoremetrics_averaged_as_std)

    # + for the hp of interest across seeds
    dict_HPexploredBestValues_averaged_as_mean = {}  # for the mean values
    dict_HPexploredBestValues_averaged_as_median = {}  # for the median values
    dict_HPexploredBestValues_averaged_as_std = {}  # for the std values
    for a_HPexplored_known in list(DictCol_bestval_HPsExplored.keys()):
        dict_HPexploredBestValues_averaged_as_mean[a_HPexplored_known] = np.nanmean(DictCol_bestval_HPsExplored[a_HPexplored_known])
        dict_HPexploredBestValues_averaged_as_median[a_HPexplored_known] = np.nanmedian(DictCol_bestval_HPsExplored[a_HPexplored_known])
        dict_HPexploredBestValues_averaged_as_std[a_HPexplored_known] = np.nanstd(DictCol_bestval_HPsExplored[a_HPexplored_known])
    if "C" in list(DictCol_bestval_HPsExplored.keys()):
        average_as_mean_of_Ctranslated = 1 / (dict_HPexploredBestValues_averaged_as_mean["C"])  # obtain a lambda value instead of a C value
        average_as_median_of_Ctranslated = 1 / (dict_HPexploredBestValues_averaged_as_median["C"])  # obtain a lambda value instead of a C value
        average_as_std_of_Ctranslated = 1 / (dict_HPexploredBestValues_averaged_as_std["C"])  # obtain a lambda value instead of a C value
    else:
        average_as_mean_of_Ctranslated = "not_in_this_context"
        average_as_median_of_Ctranslated = "not_in_this_context"
        average_as_std_of_Ctranslated = "not_in_this_context"
    # print the results depending if C is in the HPs explored or not
    if "C" in list(DictCol_bestval_HPsExplored.keys()):
        print("+ The average best value for the HPs explored, across the seeds : Mean %s (ie lambda from C of %s ) " % (dict_HPexploredBestValues_averaged_as_mean, average_as_mean_of_Ctranslated))
        print("+ The average best value for the HPs explored, across the seeds : Median %s (ie lambda from C of %s ) " % (dict_HPexploredBestValues_averaged_as_median, average_as_median_of_Ctranslated))
        print("+ The average best value for the HPs explored, across the seeds : Std %s (ie lambda from C of %s ) " % (dict_HPexploredBestValues_averaged_as_std, average_as_std_of_Ctranslated))
    else:
        print("+ The average best value for the HPs explored, across the seeds : Mean %s " % dict_HPexploredBestValues_averaged_as_mean)
        print("+ The average best value for the HPs explored, across the seeds : Median %s " % dict_HPexploredBestValues_averaged_as_median)
        print("+ The average best value for the HPs explored, across the seeds : Std %s " % dict_HPexploredBestValues_averaged_as_std)

    # ------------ for each seed, report the counts on the coefs obtained : # collectors are also created here to use them later for the Mean, Median and Std computations during the overall coefs statistics
    print(" >>>> Report, for each seed, the counts of the coefs, for each best model : ")
    # make collectors needed
    ListCol_number_of_NON_nuls_coefs_fts_in_seed = []
    ListCol_number_of_nuls_coefs_fts_in_seed = []
    ListCol_percentage_of_NON_nuls_coefs_fts_in_seed = []
    ListCol_percentage_of_nuls_coefs_fts_in_seed = []
    # loop on the col respective to the seed (the cols of the seeds coefs are in the same order than the seeds)
    for a_certain_seed_bis in list_seeds:
        a_colname_col_coefs = "Coefficient Estimate Seed " + str(a_certain_seed_bis) # remaking what must be the name of the column that must have accepted the values
        PdCol_coefs_present_seed = PdCol_coefs[[a_colname_col_coefs]] # make the df of the col of the seed only
        PdCol_coefs_present_seed_nonnull_fts = PdCol_coefs_present_seed[PdCol_coefs_present_seed[a_colname_col_coefs] != 0] # a df with the rows (fts) containing non null coefs only
        number_of_NON_nuls_coefs_fts_in_seed = PdCol_coefs_present_seed_nonnull_fts.shape[0]
        number_of_nuls_coefs_fts_in_seed = size_list_all_fts_df_input - number_of_NON_nuls_coefs_fts_in_seed # we know number_of_total_fts = size_list_all_fts_df_input
        percentage_of_NON_nuls_coefs_fts_in_seed = (number_of_NON_nuls_coefs_fts_in_seed / size_list_all_fts_df_input) * 100
        percentage_of_nuls_coefs_fts_in_seed = (number_of_nuls_coefs_fts_in_seed / size_list_all_fts_df_input) * 100
        # lets supply the collectors used for later Mean, Median and Std computations
        ListCol_number_of_NON_nuls_coefs_fts_in_seed.append(number_of_NON_nuls_coefs_fts_in_seed)
        ListCol_number_of_nuls_coefs_fts_in_seed.append(number_of_nuls_coefs_fts_in_seed)
        ListCol_percentage_of_NON_nuls_coefs_fts_in_seed.append(percentage_of_NON_nuls_coefs_fts_in_seed)
        ListCol_percentage_of_nuls_coefs_fts_in_seed.append(percentage_of_nuls_coefs_fts_in_seed)
        # print the seed results
        print("+ Seed %d : Total features (fts) is %s , number NON null coefs fts is %s (ie %s %% of total ) , number null coefs fts is %s (ie %s %% of total ) " % (a_certain_seed_bis,
                                                                                                                                                                     size_list_all_fts_df_input,
                                                                                                                                                                     number_of_NON_nuls_coefs_fts_in_seed,
                                                                                                                                                                     percentage_of_NON_nuls_coefs_fts_in_seed,
                                                                                                                                                                     number_of_nuls_coefs_fts_in_seed,
                                                                                                                                                                     percentage_of_nuls_coefs_fts_in_seed))  # %% is % escaped in python strings

    # ------------ a report for the coefs (averages and consensus) :
    print(" >>>> Report, across the seeds, the averages and the consensus of the regression coefs : ")
    # - the overall statistics report
    # for the ListCol_number_of_NON_nuls_coefs_fts_in_seed
    ListCol_number_of_NON_nuls_coefs_fts_in_seed_averaged_as_mean = np.nanmean(ListCol_number_of_NON_nuls_coefs_fts_in_seed)
    ListCol_number_of_NON_nuls_coefs_fts_in_seed_averaged_as_median = np.nanmedian(ListCol_number_of_NON_nuls_coefs_fts_in_seed)
    ListCol_number_of_NON_nuls_coefs_fts_in_seed_averaged_as_std = np.nanstd(ListCol_number_of_NON_nuls_coefs_fts_in_seed)
    # for the ListCol_number_of_nuls_coefs_fts_in_seed
    ListCol_number_of_nuls_coefs_fts_in_seed_averaged_as_mean = np.nanmean(ListCol_number_of_nuls_coefs_fts_in_seed)
    ListCol_number_of_nuls_coefs_fts_in_seed_averaged_as_median = np.nanmedian(ListCol_number_of_nuls_coefs_fts_in_seed)
    ListCol_number_of_nuls_coefs_fts_in_seed_averaged_as_std = np.nanstd(ListCol_number_of_nuls_coefs_fts_in_seed)
    # for the ListCol_percentage_of_NON_nuls_coefs_fts_in_seed
    ListCol_percentage_of_NON_nuls_coefs_fts_in_seed_averaged_as_mean = np.nanmean(ListCol_percentage_of_NON_nuls_coefs_fts_in_seed)
    ListCol_percentage_of_NON_nuls_coefs_fts_in_seed_averaged_as_median = np.nanmedian(ListCol_percentage_of_NON_nuls_coefs_fts_in_seed)
    ListCol_percentage_of_NON_nuls_coefs_fts_in_seed_averaged_as_std = np.nanstd(ListCol_percentage_of_NON_nuls_coefs_fts_in_seed)
    # for the ListCol_percentage_of_nuls_coefs_fts_in_seed
    ListCol_percentage_of_nuls_coefs_fts_in_seed_averaged_as_mean = np.nanmean(ListCol_percentage_of_nuls_coefs_fts_in_seed)
    ListCol_percentage_of_nuls_coefs_fts_in_seed_averaged_as_median = np.nanmedian(ListCol_percentage_of_nuls_coefs_fts_in_seed)
    ListCol_percentage_of_nuls_coefs_fts_in_seed_averaged_as_std = np.nanstd(ListCol_percentage_of_nuls_coefs_fts_in_seed)
    # print
    print("+ The averages of the counts of the coefs (Mean values part) : number NON null coefs fts is %s (ie %s %% of total ) , number null coefs fts is %s (ie %s %% of total ) " % (ListCol_number_of_NON_nuls_coefs_fts_in_seed_averaged_as_mean,
                                                                                                                                                                        ListCol_percentage_of_NON_nuls_coefs_fts_in_seed_averaged_as_mean,
                                                                                                                                                                        ListCol_number_of_nuls_coefs_fts_in_seed_averaged_as_mean,
                                                                                                                                                                        ListCol_percentage_of_nuls_coefs_fts_in_seed_averaged_as_mean))
    print("+ The averages of the counts of the coefs (Median values part) : number NON null coefs fts is %s (ie %s %% of total ) , number null coefs fts is %s (ie %s %% of total ) " % (ListCol_number_of_NON_nuls_coefs_fts_in_seed_averaged_as_median,
                                                                                                                                                                          ListCol_percentage_of_NON_nuls_coefs_fts_in_seed_averaged_as_median,
                                                                                                                                                                          ListCol_number_of_nuls_coefs_fts_in_seed_averaged_as_median,
                                                                                                                                                                          ListCol_percentage_of_nuls_coefs_fts_in_seed_averaged_as_median))
    print("+ The averages of the counts of the coefs (Std values part) : number NON null coefs fts is %s (ie %s %% of total ) , number null coefs fts is %s (ie %s %% of total ) " % (ListCol_number_of_NON_nuls_coefs_fts_in_seed_averaged_as_std,
                                                                                                                                                                       ListCol_percentage_of_NON_nuls_coefs_fts_in_seed_averaged_as_std,
                                                                                                                                                                       ListCol_number_of_nuls_coefs_fts_in_seed_averaged_as_std,
                                                                                                                                                                       ListCol_percentage_of_nuls_coefs_fts_in_seed_averaged_as_std))
    # - the consensus report
    # list_of_cols_coefs = ['Coefficient Estimate Seed 0','Coefficient Estimate Seed 1','Coefficient Estimate Seed 2',....,'Coefficient Estimate Seed 8','Coefficient Estimate Seed 9'] created and updated already
    PdCol_coefs_abs = PdCol_coefs.copy()  # make a copy of the df of coefs to keep the old one as result and be able tosee again if needed the coefs values with their signs
    PdCol_coefs_abs[list_of_cols_coefs] = PdCol_coefs_abs[list_of_cols_coefs].abs()  # to only make as absolute the cols with values and not touch the 1st col containing the names of the fts
    # make a col of mean coefs across the 10 seeds cols of coefs
    PdCol_coefs_abs["Mean Coefficient Estimate 10 Seeds"] = PdCol_coefs_abs[list_of_cols_coefs].mean(axis=1, skipna=True)  # axis = 0 means along the column and axis = 1 means working along the row
    PdCol_coefs_abs_mean_only = PdCol_coefs_abs[["Features", "Mean Coefficient Estimate 10 Seeds"]]
    PdCol_coefs_abs_mean_only_nonnull_fts = PdCol_coefs_abs_mean_only[PdCol_coefs_abs_mean_only["Mean Coefficient Estimate 10 Seeds"] != 0]
    number_of_NON_nuls_coefs_fts = PdCol_coefs_abs_mean_only_nonnull_fts.shape[0]
    number_of_nuls_coefs_fts = size_list_all_fts_df_input - number_of_NON_nuls_coefs_fts # we know number_of_total_fts = size_list_all_fts_df_input
    percentage_of_NON_nuls_coefs_fts = (number_of_NON_nuls_coefs_fts / size_list_all_fts_df_input) * 100
    percentage_of_nuls_coefs_fts = (number_of_nuls_coefs_fts / size_list_all_fts_df_input) * 100
    # print the seeds consensus results
    print("+ The consensus on the counts of the coefs : Total features (fts) is %s , number NON null coefs fts is %s (ie %s %% of total ) , number null coefs fts is %s (ie %s %% of total ) " % (size_list_all_fts_df_input,
                                                                                                                                                                           number_of_NON_nuls_coefs_fts,
                                                                                                                                                                           percentage_of_NON_nuls_coefs_fts,
                                                                                                                                                                           number_of_nuls_coefs_fts,
                                                                                                                                                                           percentage_of_nuls_coefs_fts))  # %% is % escaped in python strings

    # lets sort by mean coef value the remaining fts (they have non null coefs)
    PdCol_coefs_abs_mean_only_nonnull_fts_sorted = PdCol_coefs_abs_mean_only_nonnull_fts.sort_values("Mean Coefficient Estimate 10 Seeds", axis=0, ascending=False, kind='mergesort')  # axis=0 ie sort the rows
    # here is a list of the tables to keep for the coefs :
    # - PdCol_coefs (the original list of values)
    # - PdCol_coefs_abs_mean_only_nonnull_fts_sorted (the sorted list of selected fts, sorted by descending mean of absolute values of coefs)

    # fig.savefig(basedir + 'Output_' + task_type + "_" + scheme_used + "-" + the_model_compared + "_" + tag_ctype + "-" + tag_drugname + "-" + tag_profilename + "_" + tag_num_trial + '_ROCcurve.png'
    #
    # - saving the list of non null coefs features
    print(" >>>> Savings the tables containing views of the regression coefs")
    path_table_sorted_non_null_coefs = basedir + 'Output_' + task_type + "_" + scheme_used + "_" + the_model_compared + "_" + tag_ctype + "_" + tag_drugname + "_" + tag_profilename + "_" + tag_num_trial + "_NonNullCoefs.csv"
    path_table_original_list_of_coefs = basedir + 'Output_' + task_type + "_" + scheme_used + "_" + the_model_compared + "_" + tag_ctype + "_" + tag_drugname + "_" + tag_profilename + "_" + tag_num_trial + "_RawListOfCoefs.csv"
    PdCol_coefs_abs_mean_only_nonnull_fts_sorted.to_csv(path_table_sorted_non_null_coefs, index=None, header=True)
    PdCol_coefs.to_csv(path_table_original_list_of_coefs, index=None, header=True)
    print("+ A table with the only NON null coefs sorted in descending order is saved in this path : ")
    print(path_table_sorted_non_null_coefs)
    print("+ A table with the raw coefs, sorted in the features order is saved in this path : ")
    print(path_table_original_list_of_coefs)

    # - all the analysis is done : get the runtime
    runtime_analysis = duration_from(globalstart)
    print(bcolors.OKGREEN + " >>>> Analysis done. Time taken is : ", runtime_analysis, bcolors.ENDC)
    # end concatenated with "," instead of "+" to avoid TypeError: unsupported operand type(s) for +: 'datetime.timedelta' and 'str'
    # end of summary
    return