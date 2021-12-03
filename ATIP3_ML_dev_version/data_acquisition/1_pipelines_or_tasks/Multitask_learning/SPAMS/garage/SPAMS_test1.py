
### lets try the test1 from the doc of spams to isolate where the memory error is coming from
### we think of a memory limit being in play here : if so, we'll try to locate that limit for the used computing material at end
### link to the kaggle notebook that is equivalent to this script is : https://www.kaggle.com/khamasiga/spams-error139-11-reproduction1

# - add spams before importing it if you are using this script in a notebook like in Kaggle
# !pip install spams
# print("spams installed")
### --------------------
import spams
import numpy as np
from scipy import sparse # to convert arrays
print('imports done!')
### ---------------
param = {'numThreads' : -1,'verbose' : True, 'lambda1' : 0.05, 'it0' : 10, 'max_it' : 200, 'L0' : 0.1, 'tol' : 1e-3, 'intercept' : False, 'pos' : False}
np.random.seed(0)
print("params and seed set")
### ---------------
# - setting m samples and n features
m = 206
n = 46340
# error 139-11 memory related is obtained for m = 206 & n=72204/n=100000
# max value is 206 x 46625 ie 9 200 000 cells...adding features set off the error 139-11 memory related)
# 4000 x 22000 ie 88 000 000 cells works and this means it is not a limit of number of cells but of number of features
# testing the limit of fts number when num samples is 206, we have as limit (on our DELL Precision 5540 unit) 46340 fts
# dochotomy search from 46625 fts : 46k is ok # 46.6k not # 46.3 ok # 46.45k not # 46375 not # 46337 ok # 46356 not # 46346 not # 46340 ok # 46343 not # 46342 not # 46341 not # final test of confirmation : 46340
# - version with the version of X using a sparse matrix instead of a fortran array
# the csc_matrix version is X = sparse.csc_matrix(X_train,dtype='float64') and does not solve the memory issue
# X = sparse.csc_matrix(np.random.normal(size = (m,n)),dtype='float64')
# X = sparse.csc_matrix(np.random.normal(size = (m,n)),dtype='float')
# - version using a fortran array as spams docs recommend it as also used in the tests of spams by authors
X = np.asfortranarray(np.random.normal(size = (m,n)))
X = np.asfortranarray(X - np.tile(np.mean(X,0),(X.shape[0],1)),dtype='float')
# np.tile(np.mean(X,0),(X.shape[0],1) is a repetition of the row containing the mean of each col. repeated the number of rows times and not repeated once at the right
X = spams.normalize(X)
Y = np.asfortranarray(np.random.normal(size = (m,1)))
Y = np.asfortranarray(Y - np.tile(np.mean(Y,0),(Y.shape[0],1)),dtype='float')
Y = spams.normalize(Y)
W0 = np.zeros((X.shape[1],Y.shape[1]),dtype='float',order="F")
print("data set")
### ---------------
# Regression experiments
# 100 regression problems with the same design matrix X.
print('\nVarious regression experiments')
param['compute_gram'] = True
print('\nFISTA + Regression l1')
param['loss'] = 'square'
param['regul'] = 'l1'
# param.regul=’group-lasso-l2’
# param.size_group=10
print("analysis introduction set")
### ---------------
print('guard before is seen')
(W, optim_info) = spams.fistaFlat(Y,X,W0,True,**param)
print('guard after is seen')
### ---------------
print("Shape of the coefficents array : ")
W.shape
### ---------------


####---------to be cleaned up ?!
# #<<<< trying with my data
# X = np.asfortranarray(X_train,dtype='float')
# Y = np.asfortranarray(y_train.reshape((y_train.shape[0], 1)),dtype='float')
# # Y = np.asfortranarray(y_train)
# W0 = np.zeros((X.shape[1],Y.shape[1]),dtype='float',order="F")
# param = {'numThreads' : -1,'verbose' : True, 'lambda1' : 0.05, 'it0' : 10, 'max_it' : 200, 'L0' : 0.1, 'tol' : 1e-3, 'intercept' : False, 'pos' : False}
# np.random.seed(0)
# # Regression experiments
# # 100 regression problems with the same design matrix X.
# print('\nVarious regression experiments')
# param['compute_gram'] = True
# print('\nFISTA + Regression l1')
# param['loss'] = 'square'
# param['regul'] = 'l1'
# (W, optim_info) = spams.fistaFlat(Y,X,W0,True,**param)

# ### lets try something from the doc of spams
# import spams
# import numpy as np
# param = {'numThreads' : -1,'verbose' : True, 'lambda1' : 0.05, 'it0' : 10, 'max_it' : 200, 'L0' : 0.1, 'tol' : 1e-3, 'intercept' : False, 'pos' : False}
# np.random.seed(0)
# m = 100
# n = 200
# X = np.asfortranarray(np.random.normal(size = (m,n)))
# X = np.asfortranarray(X - np.tile(np.mean(X,0),(X.shape[0],1)),dtype=myfloat)
# X = spams.normalize(X)
# Y = np.asfortranarray(np.random.normal(size = (m,1)))
# Y = np.asfortranarray(Y - np.tile(np.mean(Y,0),(Y.shape[0],1)),dtype=myfloat)
# Y = spams.normalize(Y) W0 = np.zeros((X.shape[1],Y.shape[1]),dtype=myfloat,order="F")
# # Regression experiments
# # 100 regression problems with the same design matrix X.
# print(’\nVarious regression experiments’)
# param[’compute_gram’] = True
# print(’\nFISTA + Regression l1’)
# param[’loss’] = ’square’
# param[’regul’] = ’l1’
# # param.regul=’group-lasso-l2’
# # param.size_group=10
# (W, optim_info) = spams.fistaFlat(Y,X,W0,True,**param)