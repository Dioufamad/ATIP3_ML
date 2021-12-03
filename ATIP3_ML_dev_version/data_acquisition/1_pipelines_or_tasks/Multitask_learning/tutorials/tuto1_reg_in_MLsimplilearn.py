# the source of this tuto is : https://www.youtube.com/watch?v=rPBFvvw2OM4&list=PLMpDEwpxDXcYl4fBsFpom95SBaymcNGpm&index=6

# Objective : this script shows
# - how to go from a df to the coeffcients in a table and even how to visualize them
# - a visual of how from linear, ridge to lasso, we reduce the coeff

# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# loading predefined Boston dataset
boston_dataset = datasets.load_boston()
# Load the dataset
boston_pd = pd.DataFrame(boston_dataset.data) # load the data ie numbers into a df
boston_pd.columns = boston_dataset.feature_names # get the features names and put them as colnames of the df of numbers
boston_pd_target = np.asarray(boston_dataset.target) # load the response values as an numpy array
boston_pd['House Price'] = pd.Series(boston_pd_target) # put that np array as df type and put that df type as a new col added at the end of the df created for the data

# input
X = boston_pd.iloc[:, :-1] # recommended to iloc to produce a slice # :-1 means all except the last one

# output
Y = boston_pd.iloc[:,-1] # -1 means select the last one only

# shows all the cols but only the first 5 rows by default " with pycharm it cannot display all cols they they are numerous but gives at least a "n rows x m cols" as what is intendedto be displayed
print(boston_pd.head())

# lets go ahead and split our data then print the shapes of the split made to verify that everything matches as it should # (379,) as a shape means 379 rows and 1 col
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.25)
print("Train data shape of X = % s and Y = % s : "%(x_train.shape,y_train.shape))
print("Test data shape of X = % s and Y = % s : "%(x_test.shape,y_test.shape))

# Apply multiple Linear Rgression Model
lreg = LinearRegression()
lreg.fit(x_train,y_train)
# Generate prediction on test set
lreg_y_pred = lreg.predict(x_test)
# Calculating Mean Squared Error (MSE)
mean_squared_error = np.mean((lreg_y_pred - y_test)**2)
print("Mean Squared Error on test set : ",mean_squared_error)
# Putting together the coefficients and their corresponding variables names
lreg_coefficient = pd.DataFrame()
lreg_coefficient["Columns"] = x_train.columns
lreg_coefficient["Coefficient Estimate"] = pd.Series(lreg.coef_)
print(lreg_coefficient )

# plotting the coefficient scores to see whats going on
fig, ax = plt.subplots(figsize = (20,10))
color = ["tab:grey","tab:blue","tab:orange",
         "tab:green","tab:red","tab:purple","tab:brown",
         "tab:pink","tab:gray","tab:olive","tab:cyan",
         "tab:orange","tab:green","tab:blue","tab:olive"]
ax.bar(lreg_coefficient["Columns"],
       lreg_coefficient["Coefficient Estimate"],
       color = color)
ax.spines["bottom"].set_position("zero")
plt.style.use("ggplot")
plt.show()
# this gives a bar plot with the features on the horizontal axis and each bar for a feature is as big as the feature coef is high in the negative or postive
# the interpretation of these coef requires knowledge of the domain
# for now the objective would be to reduce the coef as much as we can through another regularization (we were doing linear regression)

# Now our motive is to reduce the coefficient scores

# Lets start with Ridge regression
# import ridge regression frim sklearn library
from sklearn.linear_model import Ridge
# Train the model
ridgeR = Ridge(alpha = 1) # alpha = 0 means it become a standard linear regression model meaning there is not constraint applied and we default back to only the square of errors of a defalut linear reg
ridgeR.fit(x_train,y_train)
y_pred = ridgeR.predict(x_test)
# calculate mean square error
mean_squared_error_ridge = np.mean((y_pred - y_test)**2)
print("Mean Squared Error on test set : ",mean_squared_error_ridge)
# get ridge coefficient and print them
ridge_coefficient = pd.DataFrame()
ridge_coefficient["Columns"] = x_train.columns
ridge_coefficient["Coefficient Estimate"] = pd.Series(ridgeR.coef_)
print(ridge_coefficient)
# plotting the coefficient scores to see whats going on (for the ridge regression model)
fig, ax = plt.subplots(figsize = (20,10))
color = ["tab:grey","tab:blue","tab:orange",
         "tab:green","tab:red","tab:purple","tab:brown",
         "tab:pink","tab:gray","tab:olive","tab:cyan",
         "tab:orange","tab:green","tab:blue","tab:olive"]
ax.bar(ridge_coefficient["Columns"],
       ridge_coefficient["Coefficient Estimate"],
       color = color)
ax.spines["bottom"].set_position("zero")
plt.style.use("ggplot")
plt.show()
# the shows already how the ridge has reduced the biggest coefficient by almost half and this reduction is what was the objective of the shift from linear to ridge

# lets shift to Lasso regression with the objective of a stronger reduction in coefficients
# import lasso regression frim sklearn library
from sklearn.linear_model import Lasso
# Train the model
lasso = Lasso(alpha = 1)
lasso.fit(x_train,y_train)
y_pred_lasso = lasso.predict(x_test)
# calculate mean squared error
mean_squared_error_lasso = np.mean((y_pred_lasso - y_test)**2)
print("Mean Squared Error on test set : ",mean_squared_error_lasso)
# get ridge coefficient and print them
lasso_coefficient = pd.DataFrame()
lasso_coefficient["Columns"] = x_train.columns
lasso_coefficient["Coefficient Estimate"] = pd.Series(lasso.coef_)
print(lasso_coefficient)
# plotting the coefficient scores to see whats going on (for the lasso regression model)
fig, ax = plt.subplots(figsize = (20,10))
color = ["tab:grey","tab:blue","tab:orange",
         "tab:green","tab:red","tab:purple","tab:brown",
         "tab:pink","tab:gray","tab:olive","tab:cyan",
         "tab:orange","tab:green","tab:blue","tab:olive"]
ax.bar(lasso_coefficient["Columns"],
       lasso_coefficient["Coefficient Estimate"],
       color = color)
ax.spines["bottom"].set_position("zero")
plt.style.use("ggplot")
plt.show()
# we can see that our error continues to go up as we try to reduce the coef through applying models that have more and more strict regularization
# - if we had to choose a model based only on performance the first model (linear regression) would be chosen for a project
# - domain wise, if we try to pick out the variables with most importances to our response, we can go down until lasso and select it because it has reduced strongly the coef and hence shows the var to keep
