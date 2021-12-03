# OBJ1 : we want to better understand the scikit learn AIP for multitask learning
# OBJ2 : get a table of the coef of regression and a represent them
# the blog used as a source is  : https://medium.com/@venali/conventional-guide-to-supervised-learning-with-scikit-learn-multi-task-elastic-net-generalized-63dba8009183
# the support code for this is here  : https://gist.github.com/venali/ffb3c74eadc40daf1baf779f55bf1945#file-supervised_6-ipynb

#>>>> DO THE IMPORTS
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import MultiTaskLasso,MultiTaskElasticNet, Lasso

#>>>>> INTRODUCE A RANDOM RANGE
rng = np.random.RandomState(42)

#>>>> MAKE UP A DATASET THAT HOLD THE RERESSION TYPE DATASETS DOWN TO THE COFFICIENTS
n_samples, n_features, n_tasks = 100, 30, 40 # VALUES OF DIMENSIONS INTHE DATASET
n_relevant_features = 5
coef = np.zeros((n_tasks, n_features)) # a n taks X p fts array with zeros as values
times = np.linspace(0, 2 * np.pi, n_tasks) # an array of 1 column from 0 to 2.pi with n tasks values

#>>>> fill the first x relevant fts cols with values following a sin pattern
for k in range(n_relevant_features):
    coef[:, k] = np.sin((1. + rng.randn(1)) * times + 3 * rng.randn(1))

#>>> make the fts gallery and the response gallery
X = rng.randn(n_samples, n_features) # a n samples X p fts gallery
Y = np.dot(X, coef.T) + rng.randn(n_samples, n_tasks) # a n samples X r responses of random values

#>>> previews of first 5 lines of each gallery
X5 = X[:5]
Y5 = Y[:5]

#>>>> fit a MultiTaskElasticNet to the dataset of wave features among others fts
coef_multi_task_lasso_ = MultiTaskElasticNet(alpha=1.0).fit(X, Y).coef_
# we obtain from this an array of r responses x p fts :
# each value is the cof of the fts (the col) in the task (the row)

# plot the found coef
# - make the canvas of the figure
fig = plt.figure(figsize=(8, 5))

plt.spy(coef_multi_task_lasso_) # plot the sparse matrix (ie figure a table as a figure with dots as values (see refs below)
plt.xlabel('Feature')
plt.ylabel('Time (or Task)')
plt.text(10, 5, 'MultiTaskLasso')
fig.suptitle('Coefficient non-zero location')

feature_to_plot = 0 # plot a ground truth curve (it looks like a perfect sinus curve)
plt.figure()
lw = 2
plt.plot(coef[:, feature_to_plot], color='seagreen', linewidth=lw,
         label='Ground truth')

# plot a curve representing the values of the first feature for all tasks
# (its a gold line
plt.plot(coef_multi_task_lasso_[:, feature_to_plot], color='gold', linewidth=lw,
         label='MultiTaskLasso')
plt.legend(loc='upper center')
plt.axis('tight')
plt.ylim([-1.1, 1.1])
plt.show()


# sparsity matrices for tables sources
# - https://cmdlinetips.com/2019/02/how-to-visualize-sparse-matrix-in-python/


