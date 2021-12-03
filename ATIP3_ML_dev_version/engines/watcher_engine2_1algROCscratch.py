# this is a scratch that contains the successions of lines that where needed in a old main script to make the roc curves
# this is to help make the new roc curve that only are 1 alg instead of 2 alg

# ----------- main scrip part of the roc curves
from engines.watcher_engine2 import roc_curve_updater_after_one_iteration_of_the_mdl,roc_curve_finisher_after_all_iterations_of_the_mdl,average_roc_curve_init,average_roc_curve_finisher
import matplotlib.pyplot as plt # used to make plots # for roc curves
import numpy as np
# collectors for the auc and the roc curve computations for each seed (for the omc mdl)
tprs_col_by_seed_omc_mdl = []  # intialise a list to stock the arrays of tpr values for each iteration
aucs_col_by_seed_omc_mdl = []  # intialise a list to stock the arrays of auc values for each iteration
mean_fpr_by_seed_omc_mdl = np.linspace(0, 1, 100)  # a gallery of values to base the interpolating on ##!! change the 100 to number of samples that is equals to num of fpr and tpr that will be at each iteration computed
figure_omc_mdl, ax1 = plt.subplots()

# # collectors for the auc and the roc curve computations for each seed (for the allfts mdl)
# tprs_col_by_seed_allfts_mdl = []  # intialise a list to stock the arrays of tpr values for each iteration
# aucs_col_by_seed_allfts_mdl = []  # intialise a list to stock the arrays of auc values for each iteration
# mean_fpr_by_seed_allfts_mdl = np.linspace(0, 1, 100)  # a gallery of values to base the interpolating on ##!! change the 100 to number of samples that is equals to num of fpr and tpr that will be at each iteration computed
# figure_allfts_mdl, ax2 = plt.subplots()

# collectors for a figure reuniting both models averages roc curves
figure_mdl_vs_mdl, ax3 = plt.subplots()
average_roc_curve_init(ax3)

# 3---#a dataframe by model, to keep track of predictions probs of classes in folds with only the header  : fold, pdxindex, res, sen (the two class in the same order they are given to the classwt)
# print_pred = pd.DataFrame(pd.np.empty((0,4))*pd.np.nan) ##!!! maybe not needed
# print_pred.columns = ["Fold", "PDXindex","Res","Sen"] # (for the OMC) ##!!! maybe not needed
print_pred_col = []  # collect here the df resulting before concatenating them into print_pred df of content

# # print_pred_all = pd.DataFrame(pd.np.empty((0, 4)) * pd.np.nan) ##!!! maybe not needed
# # print_pred_all.columns = ["Fold", "PDXindex", "Res", "Sen"] # (for the all version) ##!!! maybe not needed
# print_pred_all_col = [] # collect here the df resulting before concatenating them into print_pred_all df of content

# ~~~adding to keep tracker of predictions in folds of outer loop 2 but for the omc model ##isolated
# ---adding raw predictions to a keep tracker of predictions in folds
print_pred_col = raw_predictions_pusher(ol2_pred_2probs_w_omc, one_ol2_fold_tools[0], one_ol2_fold_tools[2], encoded_classes, print_pred_col,ol2_pred_call_w_omc,aseed)

# ~~~~~(finishing touches for outer loop 1 collectors)-C-omc model
# lets report the predictions with each seed in a file from the temp dataframe ## no need to write, juste make df of it # used for the auc computations and roc curve plot
df_from_print_pred_col = pd.concat(print_pred_col)
all_seeds_col_of_df_from_print_pred_col.append(df_from_print_pred_col)  # stock it from all seeds version creation
# on the full dataset LOO folds, to calculate the AUC and make the roc curve, make 2 arrays of the mdl corresponding probs of preds and the responses...
array_of_omc_mdl_predictions_2probs_on_all_data = np.array(df_from_print_pred_col.loc[:,[df_from_print_pred_col.columns[4]]]) # df_from_print_pred_col.columns[4] is the name of the col containing the probabilities of the pos class. its colname is derived from RespClasses[1] but has been modified so we can't catch it with it
array_of_omc_mdl_implicated_samples_observations_considering_predictions_2probs_on_all_data = np.array(dataBin.loc[df_from_print_pred_col[df_from_print_pred_col.columns[2]].tolist(), :]) # df_from_print_pred_col.columns[2] is the same as the older "Test_sample_index"
#~~~~~~~~uncomment this for indivudal computation of the mcc

# 4 : make the calculations and plots needed for auc and roc curves (the AUC value for the OMC mdl for this seed is catched at the same time)
roc_auc_w_omc = roc_curve_updater_after_one_iteration_of_the_mdl(array_of_omc_mdl_implicated_samples_observations_considering_predictions_2probs_on_all_data, array_of_omc_mdl_predictions_2probs_on_all_data, encoded_classes, mean_fpr_by_seed_omc_mdl, tprs_col_by_seed_omc_mdl, aucs_col_by_seed_omc_mdl, aseed, ax1)
#...add this value later in the report after remoling the columns

# # ~~~~~(finishing touches for outer loop 1 collectors)-C-allfts models
# # lets report the predictions with each seed in a file from the temp dataframe ## no need to write, juste make df of it # used for the auc computations and roc curve plot
# df_from_print_pred_all_col = pd.concat(print_pred_all_col)
# all_seeds_col_of_df_from_print_pred_all_col.append(df_from_print_pred_all_col) # stock it from all seeds version creation
# # on the full dataset LOO folds, to calculate the AUC and make the roc curve, make 2 arrays of the mdl corresponding probs of preds and the responses...
# array_of_allfts_mdl_predictions_2probs_on_all_data = np.array(df_from_print_pred_all_col.loc[:, [df_from_print_pred_all_col.columns[4]]])
# array_of_allfts_mdl_implicated_samples_observations_considering_predictions_2probs_on_all_data = np.array(dataBin.loc[df_from_print_pred_all_col[df_from_print_pred_all_col.columns[2]].tolist(), :])
# # 2 : ...calculate the 8 metrics...
#
# # 4 : make the calculations and plots needed for auc and roc curves (the AUC value for the Allfts mdl for this seed is catched at the same time)
# roc_auc_w_allfts = roc_curve_updater_after_one_iteration_of_the_mdl(array_of_allfts_mdl_implicated_samples_observations_considering_predictions_2probs_on_all_data, array_of_allfts_mdl_predictions_2probs_on_all_data, encoded_classes, mean_fpr_by_seed_allfts_mdl, tprs_col_by_seed_allfts_mdl, aucs_col_by_seed_allfts_mdl, aseed, ax2)
# # ...add this value later in the report after remoling the columns

#...and finish the roc curve and while doing that computations done will give us the mean auc (catched at the same time)
mean_auc_from_cols_of_omc_mdl, std_auc_from_aucs_col_of_omc_mdl = roc_curve_finisher_after_all_iterations_of_the_mdl(figure_omc_mdl, ax1, ax3, tprs_col_by_seed_omc_mdl, mean_fpr_by_seed_omc_mdl, aucs_col_by_seed_omc_mdl, basedir, tag_task_type, tag_alg, models_compared[0], tag_ctype, tag_drugname, tag_profilename, tag_num_trial)
Mean_ROC_AUC_omc_for_allseeds = ufloat(mean_auc_from_cols_of_omc_mdl, std_auc_from_aucs_col_of_omc_mdl)
# ...add this value (and it s std) later in the report after remoling the columns

# # ...and finish the roc curve and while doing that computations done will give us the mean auc (catched at the same time)
# mean_auc_from_cols_of_allfts_mdl, std_auc_from_aucs_col_of_allfts_mdl = roc_curve_finisher_after_all_iterations_of_the_mdl(figure_allfts_mdl, ax2, ax3, tprs_col_by_seed_allfts_mdl, mean_fpr_by_seed_allfts_mdl, aucs_col_by_seed_allfts_mdl, basedir, tag_task_type, tag_alg, models_compared[1], tag_ctype, tag_drugname, tag_profilename, tag_num_trial)
# Mean_ROC_AUC_allfts_for_allseeds = ufloat(mean_auc_from_cols_of_allfts_mdl, std_auc_from_aucs_col_of_allfts_mdl)
# # ...add this value (and it s std) later in the report after remoling the columns

# for both models, after the last average roc curve is plotted, we can finish the separate plot to compare only the average roc curve of both models
average_roc_curve_finisher(ax3,figure_mdl_vs_mdl,models_compared,tag_task_type,tag_alg,tag_ctype,tag_drugname,tag_profilename,tag_num_trial,basedir)

