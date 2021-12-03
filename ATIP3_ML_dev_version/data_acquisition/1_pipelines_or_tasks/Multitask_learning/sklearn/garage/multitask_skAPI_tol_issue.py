# All the initials codes for multitask on scikit learn API
# >>>> has helped to determine the issue of the tol limit that allow convergence (ie that say a lot about the quality of the alg)
#>>>>>>> the source for all the multitask
# https://scikit-learn.org/stable/modules/classes.html#module-sklearn.linear_model
#>>>>>>> the source for the multitask lasso
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso
#>>>>>>> the source for the multitask lasso cv
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV
#>>>>>>> the source for the multitask elasticnet

#>>>>>>> the source for the multitask elasticnet cv

# imports
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import  train_test_split
from sklearn.model_selection import  GridSearchCV
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
from sklearn import metrics
from sklearn.linear_model import MultiTaskLassoCV
from sklearn.linear_model import MultiTaskLasso
from sklearn.linear_model import MultiTaskElasticNetCV
from sklearn.linear_model import MultiTaskElasticNet
from sklearn.datasets import make_regression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error


#>>>>>>>>> load the dataset to analyse
filepath_of_ml_dataset1 = "/data_acquisition/1_pipelines_or_tasks/Joinof7_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_7cohortname.csv"
sep_in_file = ","
df_file1 = pd.read_csv(filepath_of_ml_dataset1, sep_in_file)
# df_file1.rename(columns={"Unnamed: 0" : "samples_names"}, inplace=True)
df_file1 = df_file1.set_index(list(df_file1.columns)[0])
# segregate the dataset
real_x_df = df_file1.iloc[:,0:12034]
real_y_df = df_file1.iloc[:,12034:]
real_x = df_file1.iloc[:,0:12034].values
real_y = df_file1.iloc[:,12034:].values


####### the multitask lass cv example
X, y = make_regression(n_targets=2, noise=4, random_state=0)
reg = MultiTaskLassoCV(cv=5, random_state=0).fit(X, y)
r2_score(y, reg.predict(X))
reg.alpha_
reg.predict(X[:1,])
# my data1
reg = MultiTaskLassoCV(cv=10, random_state=0, tol=0.001).fit(real_x, real_y)
mean_squared_error(real_y,reg.predict(real_x))
r2_score(real_y, reg.predict(real_x))
reg.alpha_
# reg.predict(X[:1,])
#>>>>>>>>>>>>>>>>>>>>>> res1 cv=5 tol : 0,1
# mean_squared_error(real_y,reg.predict(real_x))
# Out[6]: 0.028029997512460013
# r2_score(real_y, reg.predict(real_x))
# Out[7]: 0.7578568781083869
# reg.alpha_
# Out[8]: 0.06031737348060826
#>>>>>>>>>>>>>>>>>> res1 cv=10 tol : 0,1
# mean_squared_error(real_y,reg.predict(real_x))
# Out[10]: 0.030903847458394123
# r2_score(real_y, reg.predict(real_x))
# Out[11]: 0.7338822615680415
# reg.alpha_
# Out[12]: 0.06935032210334721
#>>>>>>>>>>>>>>>>>> res1 cv=10 tol : 0,01
# Out[15]: 0.031128483111121465
# r2_score(real_y, reg.predict(real_x))
# Out[16]: 0.7311516910914161
# reg.alpha_
# Out[17]: 0.06935032210334721
#>>>>>>>>>>>>>>>>>> res1 cv=10 tol : 0,001 # Convergence problem starting here
# #>>>>>>>>>>>>>>>>>> GridSearchCV
# mtl = MultiTaskLasso
# parameters = {"alpha" : [1,5,10, 20, 30, 35,40, 45,50,55,100]}
# ridge_regressor=GridSearchCV(mtl,parameters,scoring="neg_mean_squared_error",cv=10)
# ridge_regressor.fit(real_x,real_y)
# print(ridge_regressor.best_params_)
# print(ridge_regressor.best_score_)
# # np.arange(1, 100, 0.5).tolist()

####### the multitask elasticnet cv example
# my data1
reg = MultiTaskElasticNetCV(cv=10, random_state=0, tol=0.0001).fit(real_x, real_y)
mean_squared_error(real_y,reg.predict(real_x))
r2_score(real_y, reg.predict(real_x))
reg.alpha_

#>>>> cv=5 tol = 0.1
# mean_squared_error(real_y,reg.predict(real_x))
# Out[7]: 0.026788399060218637
# r2_score(real_y, reg.predict(real_x))
# Out[8]: 0.7684391556900685
# reg.alpha_
# Out[9]: 0.11250436876644078
#>>>>>>>>>>>>>>>>>> res1 cv=10 tol : 0,1
# mean_squared_error(real_y,reg.predict(real_x))
# Out[11]: 0.03104225551586347
# r2_score(real_y, reg.predict(real_x))
# Out[12]: 0.7329013941148781
# reg.alpha_
# Out[13]: 0.1387006442066943
#>>>>>>>>>>>>>>>>>> res1 cv=10 tol : 0,01
# mean_squared_error(real_y,reg.predict(real_x))
# Out[15]: 0.03275207173618415
# r2_score(real_y, reg.predict(real_x))
# Out[16]: 0.7191988046666323
# reg.alpha_
# Out[17]: 0.14872415445455434
#>>>>>>>>>>>>>>>>>> res1 cv=10 tol : 0,001
# mean_squared_error(real_y,reg.predict(real_x))
# Out[19]: 0.0327469870789006
# r2_score(real_y, reg.predict(real_x))
# Out[20]: 0.7194408659448843
# reg.alpha_
# Out[21]: 0.14872415445455434
#>>>>>>>>>>>>>>>>>> res1 cv=10 tol : 0,0001 # Convergence problem starting here