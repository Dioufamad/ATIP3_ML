# source for hp of the alg : https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

# >>>>>>>>>>>>>>>>   Choices made for the tests of the scikit-learn LogisticRegression :
# - The solver used : The ‘newton-cg’, ‘sag’, and ‘lbfgs’ solvers support only L2 regularization with primal formulation, or no regularization.
# The ‘liblinear’ solver supports both L1 and L2 regularization, with a dual formulation only for the L2 penalty.
# => the liblinear is used for L1 and L2.
# => "saga" is the only solver that supports elasticnet. it also supports L1 and L2 => the saga solver is used for the elasticnet, L1 and L2 for comparison

# - dual,bool, default=False
# Dual or primal formulation. Dual formulation is only implemented for l2 penalty with liblinear solver. Prefer dual=False when n_samples > n_features.
# => dual=False (use default)
# - tol,float, default=1e-4
# Tolerance for stopping criteria.
# - Cfloat, default=1.0
# Inverse of regularization strength; must be a positive float. Like in support vector machines, smaller values specify stronger regularization.
# => use lambda space of 0.0001 to 100.O (200 lambda values) + 1.0 => C space of 1000 to 0.001 + 1.0
# - fit_intercept, bool, default=True
# Specifies if a constant (a.k.a. bias or intercept) should be added to the decision function.
# - intercept_scaling,float, default=1
# Useful only when the solver ‘liblinear’ is used and self.fit_intercept is set to True. In this case, x becomes [x, self.intercept_scaling], i.e. a “synthetic” feature with constant value equal to intercept_scaling is appended to the instance vector.
# The intercept becomes intercept_scaling * synthetic_feature_weight. # Note! the synthetic feature weight is subject to l1/l2 regularization as all other features.
# To lessen the effect of regularization on synthetic feature weight (and therefore on the intercept) intercept_scaling has to be increased.

# - New in version 0.17: class_weight=’balanced’
# The “balanced” mode uses the values of y to automatically adjust weights inversely proportional to class frequencies in the input data as n_samples / (n_classes * np.bincount(y))
# - random_state,int, RandomState instance, default=None
# from the sklearn page of RandomizedLogisticRegression, we pull "If None, the random number generator is the RandomState instance used by np.random."

# - NB : error when computing MCC as a scoring in GridSearchCV :
# error is  :  /home/amad/anaconda3/envs/atip3_1_from_old_slate_env5/lib/python3.7/site-packages/sklearn/metrics/_classification.py:846: RuntimeWarning: invalid value encountered in double_scalars
#   mcc = cov_ytyp / np.sqrt(cov_ytyt * cov_ypyp)
# Explanation here : https://github.com/ThilinaRajapakse/simpletransformers/issues/4 ie the rule in the sklearn API for whats returned as mcc value is : if not defined value (nan as mcc) return 0
# Means that at some point, some of the 4 values of the confusion matrix were zero and made the MCC undefined. so sometimes, mcc is nan and we have an error showed and mcc value is 0 (0 is the worst value of mcc)

# Used when solver == ‘sag’, ‘saga’ or ‘liblinear’ to shuffle the data.

### Combinaison for ridge : penalty = "l2", solver = "saga",C=space of 1000 to 0.001 + 1.0, class_weight=’balanced’, random_state=int, l1_ratio= 0.5 or space [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95], optionally fit_intercept =False
# defaults : [dual = False, tol = 1e-4,fit_intercept =True,intercept_scaling=1,max_iter=100,multi_class="auto",verbose=0,warm_start=False,n_jobs=-1,]

### Combinaison for lasso : penalty = "l1", solver = "saga",C=space of 1000 to 0.001 + 1.0, class_weight=’balanced’, random_state=int, l1_ratio= 0.5 or space [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95] or leave dflt as None,
# defaults : [dual = False, tol = 1e-4,fit_intercept =True,intercept_scaling=1,max_iter=100,multi_class="auto",verbose=0,warm_start=False,n_jobs=-1,]

### Combinaison for elastic-net : penalty = "elasticnet", solver = "saga",C=space of 1000 to 0.001 + 1.0, class_weight=’balanced’, random_state=int, l1_ratio= 0.5 or space [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95] or leave dflt as None,
# defaults : [dual = False, tol = 1e-4,fit_intercept =True,intercept_scaling=1,max_iter=100,multi_class="auto",verbose=0,warm_start=False,n_jobs=-1,]
### Combinaison for sparse group lasso :

#### the metrics [A=(abs(mcc) + abs(cohen_kappa) + f1score + balanced accuracy+auc)/5]
# source of the idea : https://stackoverflow.com/questions/31615190/sklearn-gridsearchcv-scoring-function-error
# source for f1score : https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html
# source for prec, recall, f1score support : https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html
# source for bal acc : https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html
# source for auc : see later
# NB : all our already chosen 4 metrics have made a choice on the limit probability for the calling of a class, hence they are a step further than a compuation of ROC auc
# Hence, for simplicity and to be able to base all on our contigency matrix, we do not include a computation of auc or roc_auc_score.
# Later, we can complexify our mixedmetricof4 by adding a form of auc value in it
# source : https://stackoverflow.com/questions/31159157/different-result-with-roc-auc-score-and-auc

# source for cohen_kappa and mcc : see others docs made on them

# >>>>>>> tests results :
# - on L2, with tol=10-4, max_iter is not enough for convergence (~ 30 min, one seed could not finish and we have to do 10 for each dataset)
# + works on max_iter=100,tol=0.01 and takes 10min by seed,
# + use fit intercept as False and max iter = 200, and tol=0.001 : reaches the max iter without coverging (ran 10 min)
# + use fit intercept as False and max iter = 200, and tol=0.01 : works in 2min. keep it!

#>>>>>>>>>>>>>>>>>>>   the choice of the lambda space to search for this first exploratory predictive abilities of the model
# - decision 1 : use the the function geomspace, which takes the values of the endpoints rather than their logarithms
# import numpy as np
# - decision 2 : the tested space for lambda in sklearn (uses C values with C = 1/lambda ie the bigger is C the smaller is lambda)
# A_space1 = np.logspace(-3, 2, num=100) # a space of values from 0,001 to 100 (100 C values) ie 100 lambda values from 1000 to 0.01
# Lambda values are for the regularization strength. If lambda = 0, that specific regularization is not happening. Also in sklearn, default lambda is 1.
# so we want to test a large space of very low lambda values and a from 10 to 0.0001.
# - why 0,0001 as lowest value of lambda : well the LogisticRegression model in sklearn has a default tolerance value of 0,0001 (ie lowest difference acceptable between minimized function and the objective value)
# we take that this is a trace weak enough to be kept as a factor for the whole of our weights regularization. we start with that and we see where we go from there to one with 100 values
# - why do we go only as high as 100 for lambda values : well, the default value in sklearn for LogisticRegression is 1. We think of going past it but we dont know until where. So we just make a 100 values past 1
# so 0.0001 to 1 (100 values) and 1 to 100 (100 values).
# A_space1_2 = np.geomspace(0.0001, 100.0, num=200) # 0.0001 to 1 (200 lambda values)
# if 1.0 not in A_space1_2 :
#     A_space1_2plus1value = np.append(A_space1_2, 1.0)
#     A_space1_2plus1value_sorted = np.sort(A_space1_2plus1value) # 0.0001 to 100 (200 lambda values, including default value 1)
# A_space1_2plus1value_sorted_inverts = 1/A_space1_2plus1value_sorted # 10000 to 0.01 (200 C values including the default value)
# - decision 2 :
# use A_space1_2plus1value_sorted_inverts for all C values exploratory search
# use A_space1_2plus1value_sorted for all lambda values exploratory search

# - the array of values for C explained
# the array of value to test for C : is returned here a list of values evenly spaced, log10(start value is -3 ie start val is 0,001) and log10(end value is 2 ie start val is 100)
# # this is to be able to have non nul values evenly spaced that goes from 0,OO1 to 100 (from the lowest without being zero to the very high like 100)
#-------------



#### TO BE ADDED AT THE END OF THE script "C1_gridsearchcv_sklearn_corr1_MCC"
############### drawing of learning curves to know at which point we dont need to add more samples to better our best model selected at validation
#--------imports
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve

# - one figure
# N, train_score, val_score = learning_curve(model_retained_asbest, X_train, y_train,train_sizes=np.linspace(0.1, 1, 10), cv=10)
# print(N)
# plt.plot(N, train_score.mean(axis=1), label='train')
# plt.plot(N, val_score.mean(axis=1), label='validation')
# plt.xlabel('train_sizes')
# plt.ylabel('score')
# plt.legend()

# # - the following is 10 figures :
# # source : https://stackoverflow.com/questions/37424530/how-to-make-more-than-10-subplots-in-a-figure/37444059
# # plt.figure(0)
# # from sklearn.utils import shuffle
# # X_shuffle, y_shuffle = shuffle(X, y)
# plt.figure(figsize=(12, 10))
# plots = []
# for i in range(5):
#     for j in range(2):
#         ax = plt.subplot2grid((5,2), (i,j))
#         # - give the seeds to use
#         if j==0:
#             a_see_used = i
#         else:
#             a_see_used = 5 + i
#         # print("i is %d, j is %d and seed is %d" % (i,j,a_see_used)) # use this for testing
#         # - get the different train and test part of our data
#         X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=a_see_used)
#         N, train_score, val_score = learning_curve(model_retained_asbest, X_train, y_train, train_sizes=np.linspace(0.1, 1, 10), cv=10,random_state=a_see_used)
#         print(N)
#         plt.plot(N, train_score.mean(axis=1), label='train')
#         plt.plot(N, val_score.mean(axis=1), label='validation')
#         plt.xlabel('train_sizes')
#         plt.ylabel('score')
#         plt.legend()
#         print("- done curve seed %d"%(a_see_used))
# plt.show()
# # - saving the plot of the learning curves of best validation model across 10 seeds
# name_learning_curve_best_val_model_plot = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_singletask_sklearn/non_null_coefs_sklearn_"+ regularization_used +"_10seeds_"+ tag_cohort +".png"
# plt.savefig(name_learning_curve_best_val_model_plot, bbox_inches='tight')
#
# print("- File with plot of the learning curves of best validation model across 10 seeds : ")
# print(name_learning_curve_best_val_model_plot)
#
# # end