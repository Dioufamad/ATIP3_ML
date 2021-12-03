###--------------------- This is the location of some classes to impememnt SPAMS custom estimators to for GridSearchCV model selection -----------------------

###---------------------IMPORTS
import numpy as np
import locale
import spams # for SPAMS API workings
from scipy import sparse # to convert arrays
#====================================================================


# ---------------------Variables to initialise------------------------------------------
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') #for setting the characters format
#====================================================================


# >>>>>>>>>>> Introduce a custom estimator based on Chloé work and based on scikit-learn estimators
# Help from https://scikit-learn.org/stable/developers/develop.html and https://sklearn-template.readthedocs.io/en/latest/user_guide.html
from sklearn import base
from sklearn.utils import validation, multiclass

# a class implemented to have sklearn capabilites
class SPAMSCustomEstimator0(base.BaseEstimator, base.ClassifierMixin): # rest of name LossIsSQUARERegulIsSPARSEGROUPLASSOL2V1
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
        w = spams.fistaFlat(y_asfa, X_sparse, W0=w_init, loss='logistic', regul='sparse-group-lasso-l2', groups=self.groups, lambda1=self.lambda1, lambda2=self.lambda2)
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

# ===================================