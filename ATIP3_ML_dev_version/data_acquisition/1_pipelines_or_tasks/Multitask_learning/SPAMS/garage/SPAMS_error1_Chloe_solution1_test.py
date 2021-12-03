# this script is to test the solution proposed by Chloe to the error 1 :


'''
Hello Amad,

SPAMS attend un vecteur de float pour y et non pas de int...

J'ai utilisé le code suivant pour charger tes données et chez moi ça marche, en tout cas pour des valeurs fixes de lambda1 et lambda2 (cf capture d'écran ci-dessous).

Chloé


import pandas as pd

atip3_df = pd.read_csv("data/JoinNewDesign1CommonFtsof6_FSidea1thinking1or3_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv", sep=",")

atip3_X = np.array(atip3_df.drop(['samples_names', 'Y_pCR', 'cohort'], axis=1))

atip3_y = np.array(atip3_df['Y_pCR'], dtype='float')

atip3_n_features = int((atip3_df.shape[1]-3)/3)
atip3_task_names = list(atip3_df['cohort'].unique())
atip3_n_tasks = len(atip3_task_names)
atip3_groups = np.array([(1+x) for r in range(atip3_n_tasks) for x in np.arange(atip3_n_features)], dtype=np.int32)

'''

import pandas as pd
import numpy as np
import spams # for SPAMS API workings
from scipy import sparse # to convert arrays
import matplotlib.pyplot as plt


local_link_to_csv_dataset= "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/JoinNewDesign1CommonFtsof6_FSidea1thinking1or3_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"

atip3_df = pd.read_csv(local_link_to_csv_dataset, sep=",")

atip3_X = np.array(atip3_df.drop(['samples_names', 'Y_pCR', 'cohort'], axis=1))

atip3_y = np.array(atip3_df['Y_pCR'], dtype='float')

atip3_n_features = int((atip3_df.shape[1]-3)/3)
atip3_task_names = list(atip3_df['cohort'].unique())
atip3_n_tasks = len(atip3_task_names)
atip3_groups = np.array([(1+x) for r in range(atip3_n_tasks) for x in np.arange(atip3_n_features)], dtype=np.int32)

# >>>>>>>>>> the following is imported from Chloe's initial script of customestimator example for SPAMS "tuto1_chagaz_sparsegrouplassomultitask1"
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
my_model = MySpamsSparseGroupL1LogReg(groups=atip3_groups, lambda1=10., lambda2=1.)
my_model.fit(atip3_X, atip3_y)
w = my_model.coef_

# a count of non nulls and nulls values :
total_num_non_null_coefs = (w!=0).sum()
total_num_null_coefs = (w == 0).sum()
print("- non null coefs : ",total_num_non_null_coefs)
print("- null coefs : ",total_num_null_coefs)
# - non null coefs :  210
# - null coefs :  35892

# plotting the results of using the implemented class to have sklearn capabilities
fig = plt.figure(figsize=(11, 3))
for r in range(atip3_n_tasks):
    # create a subplot in the (r+1) position of a 1x3 grid
    ax = fig.add_subplot(1, 3, (r + 1))

    # plt.scatter(np.arange(n_features), causal_weights_per_task[r, :], marker='+', label='true features')

    plt.scatter(np.arange(atip3_n_features), w[r * atip3_n_features:(r + 1) * atip3_n_features], marker='x', label='predicted features')
    plt.legend()
    # ax.set_title(('task %s' % r))
    # the title of each fig shows "a non nulls, b nulls" coefs
    task_num_non_null_coefs = (w[r * atip3_n_features:(r + 1) * atip3_n_features]!=0).sum()
    task_num_null_coefs = (w[r * atip3_n_features:(r + 1) * atip3_n_features] == 0).sum()
    ax.set_title(('task %s : %s non nulls, %s nulls (coefs)' % (r,task_num_non_null_coefs,task_num_null_coefs)))
fig.tight_layout(pad=1.0)

# ========================
# => no lets go add the changes in my script for SPAMS and see if it runs