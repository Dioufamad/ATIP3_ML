###--------------------- This is the location of some functions to compute for metrics : this a new gen of metrics where we start to compose them ourselves -----------------------

###---------------------IMPORTS
import pandas as pd
import locale
from sklearn.metrics import make_scorer, matthews_corrcoef,cohen_kappa_score,f1_score,balanced_accuracy_score,accuracy_score,precision_score,recall_score,roc_auc_score # define the scoring to use
from engines.data_engine2_allocation import add_entry_in_dict # a function updater of dict with values a list (needed to create the list for the first elements and add to it if the list exists already)
#====================================================================
from engines.watcher_engine2 import roc_curve_updater_after_one_iteration_of_the_mdl2,roc_curve_finisher_after_all_iterations_of_the_mdl2
import matplotlib.pyplot as plt # used to make plots # for roc curves

# ---------------------Variables to initialise------------------------------------------
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') #for setting the characters format
#====================================================================

# >>>>>>>>>>>>> define the function of differents scorers (e.g. f1, MM4 = "MixedMetricof4", etc.)
# - f1 for binary classification
def f1bin_score(actual,prediction): # f1 = "f1_score" ie F1 = 2 * (precision * recall) / (precision + recall)
    f1bin = f1_score(actual, prediction, average='binary')
    return f1bin

# - MM4 = "MixedMetricof4"
def MM4_bespoke_score(actual,prediction): # old name was making_scorer_as_MM4
    mcc_abs_val = abs(matthews_corrcoef(actual, prediction))
    ck_abs_val = abs(cohen_kappa_score(actual, prediction))
    f1_sc = f1bin_score(actual, prediction)
    bal_acc = balanced_accuracy_score(actual, prediction)
    scorer_function = (mcc_abs_val + ck_abs_val + f1_sc + bal_acc) / 4
    return scorer_function
# how to use MM4 (see : https://stackoverflow.com/questions/31615190/sklearn-gridsearchcv-scoring-function-error)
# use : print("Overall average score: ", overall_average_score(y_test, y_pred))

# - precision for binary classification
def precbin_score(actual,prediction): # tp / (tp + fp)
    precbin = precision_score(actual, prediction, average='binary')
    return precbin

# - recall for binary classification
def recbin_score(actual,prediction): # tp / (tp + fn)
    recbin = recall_score(actual, prediction, average='binary')
    return recbin

# NB : accuracy of classification is diff from prec and diff from rec : accuracy is "the number of correct predictions made divided by the total number of predictions made"
# accuracy estimates the "correctness of the model all classes considered"
# precision estimates the "correctness of the model when looking at everything it called as the positive class" ie how precise it strike when it strikes
# recall estimates the " correctness of the model when looking at everything that was really the positive class" ie how much of members of the group of interest it can get back when they are thrown out there
# our choice here is to implement, in addition to precision and recall, the balanced accuracy but also the accuracy (to see the impact of classes imbalance)

# - accuracy for binary classification (balanced accuracy is simple so its called directly when needed)
def acc_norm_score(actual,prediction):
    acc_norm = accuracy_score(actual, prediction, normalize=True)
    return acc_norm

# >>>>>>>>>>>>> making a function that supplies the collectors for the results of a regression gdscv
def collectors_supplier_after_reg_gdscv(PdCol_coefs,
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
                                        fig_subplot_as_axi,
                                        modelselector_by_GSCV,
                                        y_test,X_test):
    # - keep coefficients
    # best_estimator_.coef_ is here is a 1D array of same numbers of values (coefs) as the number of fts. so we need to flatten to make it usable as a column
    A = modelselector_by_GSCV.best_estimator_.coef_
    B = A.flatten()
    colname_coefs_values = "Coefficient Estimate Seed " + str(a_seed)  # making the name of the column that will accept the values
    list_of_cols_coefs.append(colname_coefs_values)
    PdCol_coefs[colname_coefs_values] = pd.Series(B)
    # - keep val scores
    ListCol_val_scores.append(modelselector_by_GSCV.best_score_)
    # - keep hp of interest
    for a_hp_explored in list_names_HPs_explored:
        a_hp_explored_best_val = modelselector_by_GSCV.best_params_[a_hp_explored]
        add_entry_in_dict(DictCol_bestval_HPsExplored, a_hp_explored, a_hp_explored_best_val)
    # DictCol_bestval_HPsExplored.append(list(modelselector_by_GSCV.best_params_.values())[0]) # deprecated (only captured the val of the 1st hp)
    # - keep the test score for the model retained as best model during the gridsearchcv
    # Part 1 : compute the testscore for each metric that is optional
    model_retained_asbest = modelselector_by_GSCV.best_estimator_ # step 1 : we capture the best model...
    X_test_preds = model_retained_asbest.predict(X_test) # ...and we get the predictions for X_test
    X_test_probs_all_classes = model_retained_asbest.predict_proba(X_test) # ...also we get the probabilites of class 1 for X_test
    if X_test_probs_all_classes.ndim == 1:
        X_test_probs_of_class1_when_classes_are_bin = X_test_probs_all_classes
    elif X_test_probs_all_classes.ndim == 2:
        X_test_probs_of_class1_when_classes_are_bin = X_test_probs_all_classes[:, 1]
    else : # (if X_test_probs_all_classes.ndim > 2 :)
        index_last_col_table_of_probs = X_test_probs_all_classes.shape[1] - 1 # get index last col because it where the postive class is always (wether both classes probs are computed or not)
        X_test_probs_of_class1_when_classes_are_bin = X_test_probs_all_classes[:,index_last_col_table_of_probs]
    # NB : # AUC and ROC curves drawings needs a different thing as predictions related argument : instead of X_test_predicted_classes, it uses X_test_probabilities_of_class1_when_classes_are_binary
    # normal code snippet is model_retained_asbest.predict_proba(X_test)[:, 1] but predict_proba of spams custom estimator gives the prob of class1 (instead of 2 cols of probs for class0 and class1 resp)
    for a_metric_of_testscore_to_compute in list_tags_metrics_computed_for_testscore: # step 2 : we get the test score of the best model for each metric that we had in our list of metrics to compute
        if a_metric_of_testscore_to_compute == "MM4":
            model_retained_asbest_testscore = MM4_bespoke_score(y_test, X_test_preds)  # MM4
        elif a_metric_of_testscore_to_compute == "MCC":
            model_retained_asbest_testscore = matthews_corrcoef(y_test, X_test_preds)  # MCC
        elif a_metric_of_testscore_to_compute == "CK":
            model_retained_asbest_testscore = cohen_kappa_score(y_test, X_test_preds)  # cohen_kappa
        elif a_metric_of_testscore_to_compute == "F1":
            model_retained_asbest_testscore = f1bin_score(y_test, X_test_preds)  # f1_score
        elif a_metric_of_testscore_to_compute == "BalAcc":
            model_retained_asbest_testscore = balanced_accuracy_score(y_test, X_test_preds)  # bal acc
        elif a_metric_of_testscore_to_compute == "Acc":
            model_retained_asbest_testscore = acc_norm_score(y_test, X_test_preds)  # acc
        elif a_metric_of_testscore_to_compute == "Prec":
            model_retained_asbest_testscore = precbin_score(y_test, X_test_preds) # prec
        elif a_metric_of_testscore_to_compute == "Rec":
            model_retained_asbest_testscore = recbin_score(y_test, X_test_preds)  # rec
        elif a_metric_of_testscore_to_compute == "AUC":
            model_retained_asbest_testscore = roc_auc_score(y_test, X_test_probs_of_class1_when_classes_are_bin)  # auc
        else : # tag of a metric for which a computation has not been implemented
            model_retained_asbest_testscore = 0.0
            print("Warning! the tag",a_metric_of_testscore_to_compute,"does not correspond to an implemented metric computation. Test score of 0.0 to it by default")
        # stash the testscore computed in the proper place if the testscores dict metric as key and list of testscores as value
        add_entry_in_dict(DictCol_test_scores, a_metric_of_testscore_to_compute, model_retained_asbest_testscore)
    # Part 2 : make the computation for the mandatory part (the ROC curve drawing for this seed)
    RespClassesList = sorted(list(set(y_test)))
    roc_curve_updater_after_one_iteration_of_the_mdl2(y_test,
                                                      X_test_probs_of_class1_when_classes_are_bin,
                                                      RespClassesList,
                                                      mean_fpr_by_seed_one_alg,
                                                      tprs_col_by_seed_one_alg,
                                                      aucs_col_by_seed_one_alg,
                                                      a_seed,
                                                      fig_subplot_as_axi)
    return

# >>>>>>> the difference between auc() and roc_auc_score() in sklearn :
# source : https://stackoverflow.com/questions/31159157/different-result-with-roc-auc-score-and-auc
# - the AUC is for 'before' taking a decision on the threshold to use to call for the predictions : its better so we will use it
# as in here :
"""
y_probs = clf.predict_proba(xtest)[:,1]
fp_rate, tp_rate, thresholds = roc_curve(y_true, y_probs)
auc(fp_rate, tp_rate)
# this first gets a roc curve, and then calls auc() to get the area
"""

# - roc_auc_score uses the predictions (not the probabilities)
# as in here :
"""
y_pred = clf.predict(xtest)
roc_auc_score(y_true, y_pred)
"""
###! go through the old roc curve implentation and inspect it

# # use this to test auc (the one that have roc_curve computation before) # used to test our roc curve implementation
# import numpy as np
# from sklearn import metrics
# y = np.array([1, 1, 2, 2])
# pred = np.array([0.1, 0.4, 0.35, 0.8])
# fpr, tpr, thresholds = metrics.roc_curve(y, pred, pos_label=2)
# metrics.auc(fpr, tpr)

# auc from the predictions is computed
# now get the roc curve with its auc on it

