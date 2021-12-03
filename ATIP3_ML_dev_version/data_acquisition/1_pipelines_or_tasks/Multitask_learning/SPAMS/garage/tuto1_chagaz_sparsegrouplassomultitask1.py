# source : https://github.com/chagaz/ml-notebooks/blob/master/Multitask%20Lasso.ipynb
# or also see the email following :
###
# Hello Asma et Amad,
#
# Pour être sûre qu'on soit bien sur la même page en ce qui concerne
# l'utilisation d'un sparse group lasso pour résoudre un multitask lasso,
# j'ai fait un notebook jupyter pour tester ça avec spams :
# https://github.com/chagaz/ml-notebooks/blob/master/Multitask%20Lasso.ipynb
#
# Vous pouvez sauter directement à la section "Classification" pour les
# problèmes de classification.
#
# Mon branchement entre spans et sklearn est assez naïf (j'ai créé vite
# fait une classe qui hérite de BaseEstimator, et en particulier je
# reconvertis à chaque fois les données depuis un array numpy vers un
# array scipy sparse, à vrai dire si ça se trouve ce n'est pas nécessaire
# et scikit-learn accepte aussi un sparse scipy array plutôt qu'un numpy
# array pour X) et du coup lent, mais Amad, ça devrait peut-être convenir
# pour tes données.
# @Asma : tu vois, on peut utiliser une matrice de design sparse avec
# spams, du coup l'histoire du sparse group lasso n'est peut-être pas si
# horrible !
#
# Je vais essayer de rajouter bientôt d'autres implémentations que spams
# -- je pense à
# - celer https://github.com/mathurinm/celer
# - gap safe rules https://github.com/EugeneNdiaye/Gap_Safe_Rules
# - copt https://github.com/FedericoV/copt
# pour voir un peu comment elles se comportent.
#
# N'hésitez pas si vous avez des remarques ou des questions !
#
# Chloé.
#
# --
# Chloe-Agathe Azencott
# CBIO Mines ParisTech - Institut Curie - INSERM U900
# http://cazencott.info
###

#>>>>>>>>>>>imports
import numpy as np
import matplotlib.pyplot as plt

#>>>>>>>>>>>> 2. Classification
# Same as above but with a logistic penalty.

# 2.1 Simulation data
# We have here a very simple simulation design (more samples than features, rather high signal-to-noise ration) to test possibilities.
n_tasks = 3
n_features = 20
n_samples_per_task = [30, 30, 40]
n_samples = np.sum(n_samples_per_task)
n_causal_features = 5 # first n_causal_features have non-zero weights
epsilon = 0.05 # noise level

causal_weights_per_task = np.zeros(shape=(n_tasks, n_features)) # create an array of zeros with r rows (r num of tasks) and n cols (n is fts num)
for r in range(n_tasks):
    causal_weights_per_task[r, :n_causal_features] = np.random.random(size=(n_causal_features,)) # for each task in array weights for task as row, set the first 5 fts as a random value) ie 5 fts have non nul weights now

# folowing scatter plot shows how, for each of the tasks, the weights are non nul for the first 5 fts and are flat out zeros for the rest of the fts ##!
for r in range(n_tasks):
    plt.scatter(np.arange(n_features), causal_weights_per_task[r, :], label=('task %s' % r))
plt.legend()

# populate a full X fts gallery and y gallery with mock values that follow a trend of fts that are important and other not important with also noise involved
X = np.zeros((n_samples, n_features))
y = np.zeros((n_samples, ))
start_idx = 0
end_idx = 0
for r in range(n_tasks):
    end_idx += n_samples_per_task[r] # choose betwenn 30, 30 and 40 what is the non selectable index pointing at the last sample of the present task (each loop push it further)
    X[start_idx:end_idx, :] = np.random.random(size=(n_samples_per_task[r], n_features)) # populate with random values all the rows and cols of the task samples
    y_tmp = np.dot(X[start_idx:end_idx, :], causal_weights_per_task[r]) + epsilon * np.random.random(size=(n_samples_per_task[r], )) # create a intermediary of the X gallery of fts and deduce from it the mock response values below
    y[start_idx:end_idx] = np.where(y_tmp > np.mean(y_tmp), 1, 0)
    start_idx += n_samples_per_task[r] # choose betwenn 30, 30 and 40 what is the non selectable index pointing at the last sample of the previous task to use as selectable index of the present task  (each loop push it further)
# plotting the intermediary gallery of fts values that gave the response (without the noise part) and do it against the response values (we can see fts values with 1 and other with 0)
fig = plt.figure(figsize=(11, 3))
start_idx = 0
end_idx = 0
for r in range(n_tasks):
    ax = plt.subplot(1, 3, (r+1))
    end_idx += n_samples_per_task[r]
    ax.scatter((np.dot(X[start_idx:end_idx, :], causal_weights_per_task[r])), y[start_idx:end_idx], label=('task %d' % r))
    start_idx += n_samples_per_task[r]
    t = plt.title("Task %d" % r)
    t = plt.xlabel(r"Without noise ($\langle w, x\rangle$)")
    t = plt.ylabel(r"Label")

# 2.2 Separate single - task l1 - regularized logistic regressions on each task with sklearn
#     Let 's consider our 3 tasks separately and run an l1-regularized logistic regression

from sklearn import linear_model
single_task_lasso_coefs = np.zeros(shape=(n_tasks, n_features))
from sklearn import model_selection
param_grid = {'C': np.logspace(-3, 2, num=100)} # define the grid of params and params values to explore
# the array of value to test for C : is returned here a list of values evenly spaced, log10(start value is -3 ie start val is 0,001) and log10(end value is 2 ie start val is 100)
# this is to be able to have non nul values evenly spaced that goes from 0,OO1 to 100 (from the lowest without being zero to the very high like 100)
lasso_gs = model_selection.GridSearchCV(linear_model.LogisticRegression(penalty='l1', solver='liblinear'), param_grid, scoring='f1')
single_task_lasso_coefs = np.zeros(shape=(n_tasks, n_features)) #already done so why do it again # leave it like that anyway
start_idx = 0
end_idx = 0
# go through the tasks and get : 1- the coef od the fts for the best model 2-the best params for that best model
for r in range(n_tasks):
    end_idx += n_samples_per_task[r]
    # fit lasso
    lasso_gs.fit(X[start_idx:end_idx, :], y[start_idx:end_idx])
    # obtain coefficients
    single_task_lasso_coefs[r, :] = lasso_gs.best_estimator_.coef_ # best_estimator_.coef_ is here the a 1D array of same numbers of values (coefs) as the number of fts. ## to test, do a=lasso_gs.best_estimator_.coef_
    # obtain lambda
    print("Best lambda for task %d: %s" % (r, lasso_gs.best_params_)) # best params give me a dict of key as a param and value as best value for the param
    start_idx += n_samples_per_task[r]
# plot the results
fig = plt.figure(figsize=(11, 3))
for r in range(n_tasks):
    # create a subplot in the (r+1) position of a 1x3 grid
    ax = fig.add_subplot(1, 3, (r + 1)) # a fig of 1 line, 3 cols, put a subplot at pos 1 (and then 2 and then 3) # count subplot start at 1
    plt.scatter(np.arange(n_features), causal_weights_per_task[r, :], marker='+', label='true weights')
    plt.scatter(np.arange(n_features), single_task_lasso_coefs[r, :], marker='x', label='predicted weights')
    plt.legend()
    ax.set_title(('task %s' % r))
fig.tight_layout(pad=1.0)

# Remark: Note this does not work so well, the selected model doesn't have enough regularization...(this can be seen by the some weights not being predicted as zeros while they were zeros in the true weights gallery)

# 2.3 Turning the problem into a sparse group lasso problem
# Now we're ready to move to solving the 3 tasks together in a mulittask formulation.
#
# New design matrix
X_mt = np.zeros((n_samples, n_features * n_tasks))
start_idx = 0
end_idx = 0
# populate each part of the fts gallery (Xk) with it old fts values (ie each Xk will have upper or below a large nan part)
for r in range(n_tasks):
    end_idx += n_samples_per_task[r]
    X_mt[start_idx:end_idx, r * n_features:(r + 1) * n_features] = X[start_idx:end_idx, :]
    start_idx += n_samples_per_task[r]
# Let's look at this new design matrix and check it's block diagonal, with each data set forming one block. ##! use this later on my datasets
plt.imshow(X_mt, cmap='viridis', aspect='equal')
plt.colorbar()

# Group membership vector
groups = np.array([(1+x) for r in range(n_tasks) for x in np.arange(n_features)], dtype=np.int32)

# 2.4 Using spams
# Testing spams directly

import spams
from scipy import sparse
# change the fts array into a scipy sparse array (used by spams)
X_sparse = sparse.csc_matrix(X_mt)
# change the response array as a fortran array
y_FA = np.asfortranarray(y.reshape(y.shape[0], 1))
# bring it a vector of initialization full of zeros with # vector_rows is # fts and # vector_cols is # of cols response (tasks)
w_initialization = np.zeros((X_sparse.shape[1], y_FA.shape[1]), order="F")
# lets see what we have now in our arrays to use
print(X_sparse.shape, y_FA.shape, w_initialization.shape, groups.shape)
# (100, 60)(100, 1)(60, 1)(60, )
# create our spams alg and fit it
w = spams.fistaFlat(y_FA, X_sparse, W0=w_initialization, loss='logistic', regul='sparse-group-lasso-l2', groups=groups, lambda1=.005, lambda2=0.001)
# plot the features weights (true vs predicted)
fig = plt.figure(figsize=(11, 3))
for r in range(n_tasks):
    # create a subplot in the (r+1) position of a 1x3 grid
    ax = fig.add_subplot(1, 3, (r + 1))
    plt.scatter(np.arange(n_features), causal_weights_per_task[r, :], marker='+', label='true features')
    plt.scatter(np.arange(n_features), w[r * n_features:(r + 1) * n_features], marker='x', label='predicted features')
    plt.legend()
    ax.set_title(('task %s' % r))
fig.tight_layout(pad=1.0)

# the regularization is better here because true and predicted weights have closer profiles

# Turn it into a scikit-learn estimator¶
# In order to use sklearn.model_selection we need to turn this into an estimator.
# Help from https://scikit-learn.org/stable/developers/develop.html and https://sklearn-template.readthedocs.io/en/latest/user_guide.html
from sklearn import base
from sklearn.utils import validation, multiclass

# a class implemented to have sklearn capabilites
class MySpamsSparseGroupL1LogReg(base.BaseEstimator, base.ClassifierMixin):
    """
    This class implements a sparse group logistic regression that is fitted using SPAMS.
    """
    def __init__(self, lambda1=1., lambda2=0., groups=None):
        self.lambda1 = lambda1
        self.lambda2 = lambda2
        self.groups = groups

    def fit(self, X, y):
        # Check that X and y have correct shape
        X, y = validation.check_X_y(X, y)
        # Store the classes seen during fit
        self.classes_ = multiclass.unique_labels(y)
        self.X_ = X
        self.y_ = y
        # Fitting
        X_sparse = sparse.csc_matrix(self.X_)  # np.asfortranarray(self.X_) #
        y_asfa = np.asfortranarray(self.y_.reshape((self.y_.shape[0], 1)))
        w_init = np.zeros((X_sparse.shape[1], 1), order="F")
        w = spams.fistaFlat(y_asfa, X_sparse, W0=w_init, loss='square', regul='sparse-group-lasso-l2', groups=self.groups, lambda1=self.lambda1, lambda2=self.lambda2)
        self.coef_ = w.reshape((w.shape[0],))
        # Return the classifier
        return self

    def predict_proba(self, X):
        # Check that fit has been called
        validation.check_is_fitted(self)
        # Input validation
        X = validation.check_array(X)
        # Prediction
        return (1. / (1 + np.exp(-np.dot(X, self.coef_))))

    def predict(self, X):
        return np.where(self.predict_proba(X) > 0.5, 1, 0)

# use the implemented class
my_model = MySpamsSparseGroupL1LogReg(groups=groups, lambda1=0.001, lambda2=0.01)
my_model.fit(X_mt, y)
w = my_model.coef_

# plotting the results of using the implemented class to have sklearn capabilities
fig = plt.figure(figsize=(11, 3))
for r in range(n_tasks):
    # create a subplot in the (r+1) position of a 1x3 grid
    ax = fig.add_subplot(1, 3, (r + 1))
    plt.scatter(np.arange(n_features), causal_weights_per_task[r, :], marker='+', label='true features')
    plt.scatter(np.arange(n_features), w[r * n_features:(r + 1) * n_features], marker='x', label='predicted features')
    plt.legend()
    ax.set_title(('task %s' % r))
fig.tight_layout(pad=1.0)

# gives a two files that are similar on the dispersion seen on the non null weights but is different still on the nul true weights

# how to add grid selection to that..
# the param grid
param_grid = {'lambda1': np.logspace(-4, 1, num=30), 'lambda2': np.logspace(-4, 1, num=30)}
# make the model selection line
sglasso_gs = model_selection.GridSearchCV(MySpamsSparseGroupL1LogReg(groups=groups), param_grid, scoring='f1')
# fit it with training data
sglasso_gs.fit(X_mt, y)
# obtain coefficients
multi_task_lasso_coefs = sglasso_gs.best_estimator_.coef_
# obtain lambda (and all other best values for each param...)
print("Best lambdas: %s" % sglasso_gs.best_params_)

# plot the results of the gridsearchcv based on the class implemented
fig = plt.figure(figsize=(11, 3))
for r in range(n_tasks):
    # create a subplot in the (r+1) position of a 1x3 grid
    ax = fig.add_subplot(1, 3, (r + 1))
    plt.scatter(np.arange(n_features), causal_weights_per_task[r, :], marker='+', label='true features')
    plt.scatter(np.arange(n_features), multi_task_lasso_coefs[r * n_features:(r + 1) * n_features], marker='x', label='predicted features')
    plt.legend()
    ax.set_title(('task %s' % r))
fig.tight_layout(pad=1.0)
