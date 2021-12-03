# All the initials codes for multitask

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

#>>>> condittions

#>>>>>>>>> load the dataset to analyse
filepath_of_ml_dataset1 = "/data_acquisition/1_pipelines_or_tasks/Joinof7_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_7cohortname.csv"
sep_in_file = ","
df_file1 = pd.read_csv(filepath_of_ml_dataset1, sep_in_file)
# df_file1.rename(columns={"Unnamed: 0" : "samples_names"}, inplace=True)
df_file1 = df_file1.set_index(list(df_file1.columns)[0])
# segregate the dataset
real_x = df_file1.iloc[:,0:12034].values
real_y = df_file1.iloc[:,12034].values
# splitting dataset in train test
train_x,test_x,train_y,test_y = train_test_split(real_x,real_y,test_size=0.2,random_state=0)
# standardise
scaler=StandardScaler()
train_x=scaler.fit_transform(train_x)
test_x = scaler.fit_transform(test_x)
# imports libs needed for regressors
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet

# running Linear models
lm=LinearRegression()
lm
lasso=Lasso()
lasso
ridge=Ridge()
ridge
elastic=ElasticNet()
elastic

# fitting the models
lm.fit(train_x,train_y)
lasso.fit(train_x,train_y)
ridge.fit(train_x,train_y)
elastic.fit(train_x,train_y)

# the coefficients of importance
important_coeff_lm = pd.Series(lm.coef_,index=list(df_file1.columns)[:12034])
important_coeff_lasso = pd.Series(lasso.coef_,index=list(df_file1.columns)[:12034])
important_coeff_ridge = pd.Series(ridge.coef_,index=list(df_file1.columns)[:12034])
important_coeff_elastic = pd.Series(elastic.coef_,index=list(df_file1.columns)[:12034])

# predictions
pred_test_lm = lm.predict(test_x)
pred_test_lasso = lasso.predict(test_x)
pred_test_ridge = ridge.predict(test_x)
pred_test_elaslic = elastic.predict(test_x)

# estimate predictions
print("MSE, For the lm : ",np.round(metrics.mean_squared_error(test_y,pred_test_lm),2))
print("MSE, For the lasso : ",np.round(metrics.mean_squared_error(test_y,pred_test_lasso),2))
print("MSE, For the ridge : ",np.round(metrics.mean_squared_error(test_y,pred_test_ridge),2))
print("MSE, For the elastic : ",np.round(metrics.mean_squared_error(test_y,pred_test_elaslic),2))
print("R2, For the lm : ",np.round(metrics.r2_score(test_y,pred_test_lm),2))
print("R2, For the lasso : ",np.round(metrics.r2_score(test_y,pred_test_lasso),2))
print("R2, For the ridge : ",np.round(metrics.r2_score(test_y,pred_test_ridge),2))
print("R2, For the elastic : ",np.round(metrics.r2_score(test_y,pred_test_elaslic),2))

# finding best alpha value
# - ridge regression
parameters = {"alpha" : [1,5,10, 20, 30, 35,40, 45,50,55,100]}
ridge_regressor=GridSearchCV(ridge,parameters,scoring="neg_mean_squared_error",cv=5)
ridge_regressor.fit(train_x,train_y)
print(ridge_regressor.best_params_)
print(ridge_regressor.best_score_)



#>>>>>>> the source for all the multitask
# https://scikit-learn.org/stable/modules/classes.html#module-sklearn.linear_model

#>>>>>>> the source for the multitask lasso
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso
#>>>>>>> the source for the multitask lasso cv
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV
#>>>>>>> the source for the multitask elasticnet
#>>>>>>> the source for the multitask elasticnet cv

####### the multitask lass cv
from sklearn.linear_model import MultiTaskLassoCV
from sklearn.datasets import make_regression
from sklearn.metrics import r2_score
X, y = make_regression(n_targets=2, noise=4, random_state=0)
reg = MultiTaskLassoCV(cv=5, random_state=0).fit(X, y)
r2_score(y, reg.predict(X))
reg.alpha_
reg.predict(X[:1,])

# my data1
X, y = make_regression(n_targets=2, noise=4, random_state=0)
reg = MultiTaskLassoCV(cv=5, random_state=0).fit(X, y)
r2_score(y, reg.predict(X))
reg.alpha_
reg.predict(X[:1,])