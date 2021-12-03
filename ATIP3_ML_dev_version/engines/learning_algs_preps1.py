###--------------------- This is the location of some functions to prepare because needed by some learnings algorithms to run like intended -----------------------

###---------------------IMPORTS
import pandas as pd
import numpy as np
import locale
#====================================================================

# ---------------------Variables to initialise------------------------------------------
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') #for setting the characters format
#====================================================================

# >>>>>>>>>>> create the list of the seeds of the different random states to estimate the model selection on
def list_seeds_maker(num_seeds=10):
    list_seeds = list(range(num_seeds))
    # use num_seeds=10 for trial runs
    # use num_seeds=2 for test runs
    return list_seeds

# >>>>>>>>>>>>> SPAMS group membership vector maker when input dataset has features in format "TrueNameOfTheFeature_in_CohortOfOriginOfTheFeature"

def SPAMS_grp_membership_vector_maker1(list_all_fts_df_input):
    # - a list of the unique names of features in the order they are met when going through the original list of features
    list_all_fts_no_tag_cohort = []
    for ft in list_all_fts_df_input:
        ft_no_tag_cohort = ft.split("_in_")[0]
        if ft_no_tag_cohort not in list_all_fts_no_tag_cohort:
            list_all_fts_no_tag_cohort.append(ft_no_tag_cohort)
    # length_list_fts_no_tag_cohort = len(list_all_fts_no_tag_cohort)  # not needed # use it to get the number of unique fts
    # - dict : ft_no_tag --- numero for ft_no_tag (1 to length list fts no tag (included))
    dict_ftnottag_indexplus1 = {}
    for ftnotag in list_all_fts_no_tag_cohort:
        dict_ftnottag_indexplus1[ftnotag] = list_all_fts_no_tag_cohort.index(ftnotag) + 1
    # - dict : ft_w_tag --- numero for ft_no_tag (1 to length list fts no tag (included))
    dict_ftwtag_index_ftnotag = {}
    A = list(dict_ftnottag_indexplus1.keys())
    for ftwtag in list_all_fts_df_input:
        for it_might_the_corresponding_ftnotag in A:
            if ftwtag.startswith(it_might_the_corresponding_ftnotag):
                dict_ftwtag_index_ftnotag[ftwtag] = dict_ftnottag_indexplus1[it_might_the_corresponding_ftnotag]
    # a list of the numbers that communicates with the full list of fts_w_tag
    list_of_group_membership_ftswtag = list(dict_ftwtag_index_ftnotag.values())
    # making the membership array to use
    groups_in_data = np.array(list_of_group_membership_ftswtag, dtype=np.int32)

    return groups_in_data


# >>>>>>>>>>>>> an creator of the collectors for the results of a regression alg best model search using gridsearcv
def creator_of_collectors_for_reg_gdscv(list_all_fts_df_input,list_tags_metrics,param_grid):
    # - Collector1 -  introduce a df that later will have : with col 1 = the list of fts, col seed 1 to col last_seed have each the coefs of the best model of the seed
    PdCol_coefs = pd.DataFrame()
    PdCol_coefs["Features"] = list_all_fts_df_input  # make the col of the fts # was previously df_input.columns and its has been already got through ""
    # - Collector1bis -  a list of the colnames containing coefs at each seed (useful later to access directly the cols with coefs and change them into absolute values)
    list_of_cols_coefs = []
    # - Collector2 -  the list where to stash the validation (gridscorer) score obtained at each seed by the best model
    ListCol_val_scores = []
    # - Collector3 -  the dict key as tag of a metric and value as a list of values that are the test scores of the best models (one at each seed)
    DictCol_test_scores = {}
    list_tags_metrics_computed_for_testscore = list_tags_metrics  # a list of the names of the keys to use for the previous dict of test scores
    # - Collector4 -  the dict key as a name of hp and value as a list of values that have been the best value of the hp at a seed
    DictCol_bestval_HPsExplored = {}
    list_names_HPs_explored = list(param_grid.keys())  # a list of the names of the hp explored (used to update the previous dict "HP" as key and "best values of HP" as values
    # - Collector5 - the collectors related to building the ROC curves for the alg at each seed and make an average ROC curve
    tprs_col_by_seed_one_alg = []  # intialise a list to stock the arrays of tpr values for each iteration
    aucs_col_by_seed_one_alg = []  # intialise a list to stock the arrays of auc values for each iteration
    mean_fpr_by_seed_one_alg = np.linspace(0, 1, 100)  # a gallery of values to base the interpolating on ##!! change the 100 to number of samples that is equals to num of fpr and tpr that will be at each iteration computed

    return PdCol_coefs, list_of_cols_coefs, ListCol_val_scores, DictCol_test_scores, list_tags_metrics_computed_for_testscore, DictCol_bestval_HPsExplored, list_names_HPs_explored, tprs_col_by_seed_one_alg,aucs_col_by_seed_one_alg,mean_fpr_by_seed_one_alg