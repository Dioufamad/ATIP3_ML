# this script source is : https://www.youtube.com/watch?v=SJT4ZyLxIE0&list=PLMpDEwpxDXcYl4fBsFpom95SBaymcNGpm&index=2

# Objective
# - the basic pipeline of logistic regression (used when you have classes as the response)
# - how to call for a confusion matrix from sklearn (instead of making one manually) as it is cleaner

# >>>>>>> ECPLORATORY ANALYSIS
# how to create a pandas series
import pandas as pd
x = pd.Series([6,3,6,4])
x # x has a default index and is one dimensional

# how to create a pandas dataframe
import pandas as pd
import numpy as np # needed to just create the 4x3 matrix of random numbers we will fill the dataframe with
df = pd.DataFrame(np.random.randn(4,3))
df # df has a default index and is two dimensional (rows and cols) and default cols names are integers from 0

# Exploratory analysis using pandas
# - import the necessary libs and read the dataset using the read_csv() function
import pandas as pd
import numpy as np
import matplotlib as plt
# %matplotlib inline # use to display the figure inside the notebook

local_link_to_csv_dataset = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/JoinNewDesign1CommonFtsof7_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_7cohortname.csv"
df = pd.read_csv(local_link_to_csv_dataset) # read the dataset in a df and an option is "sep_in_file = ","" to precise what was the separator in the file
# when the first column was kept because it was the previous index, we can put it back as index with this
df.rename(columns={"Unnamed: 0" : "samples_names"}, inplace=True)
df = df.set_index(list(df.columns)[0])
# display the top few rows and see the quirks of data and eventually the aspects that can be scheduled for changes while data cleaning
df.head()
# get a summary of stats for each column and that way understand them a bit more
df_mini_30x10first = df.iloc[:30,0:10]
df_mini_30x10first.describe()

# univariate analysis (looking at the values of one variable
# - numrical values distribution
df_mini_30x10first["A1CF_in_GSE41998"].hist(bins=50) # this shows you pretty quick if there are some extreme values and so decide if we need to do steps of data preparation like normalastion before doing ml stuff
# -  categorical values distribution
# some correction to this part
temp1 = df_mini_30x10first["A1CF_in_GSE41998"].value_counts(ascending=True)
temp2 = df_mini_30x10first[["A1CF_in_GSE41998","Y_pCR"]].pivot_table(values="Y_pCR", index=["A1CF_in_GSE41998"],aggfunc=lambda x: x.map({"Y":1,"N":0}).mean())
print("Frequency table for the feature A1CF_in_GSE41998")
print(temp1)
print("\nProbability of being pCR for each class of the feature A1CF_in_GSE41998")
print(temp2)
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,4))
ax1 = fig.add_subplot(121)
ax1.set_xlabel("credit_history")
ax1.set_ylabel("count of applicants")
ax1.set_title("Applicants by credit history")
# temp1 = df.iloc[:,-2]
temp1.plot(kind="bar") # not shown but we just get x barx with x the numbers of classes ans x is as big as the numbers ofsmaples having the numbers of samples in a class hence we can automatically the desparity and numbers of our resp classes

# - some other visualisation 1 : look at frequency distribution to se if they make sense or not
df_mini_30x10first["A1CF_in_GSE41998"].value_counts()
#  - some other visualisation 2 : to understand the distribution
df_mini_30x10first[["A1CF_in_GSE41998","Y_pCR"]].boxplot(column="A1CF_in_GSE41998", by="Y_pCR")



# Data wrangling
# - deal with missing values, with nul values and set the dataset in the particular form it needs to be before using algorithmson it

# dealing with nul values
# - step 1 : see if the data has missing values
df_mini_30x10first.apply(lambda x:sum(x.isnull()),axis=0) # axis=1 means "do the task by going through the rows" ie"for each row, find the number of missing values". for the columns, axis=0 is used
# strategy 1 : if the total number of samples with missing values is minimal compared to the size of the dataset, you can exclude the samples with missing values
# strategy 2 : if not the case of strategy 1, we can use mean of existing values in a col to fill up null values
df_mini_30x10first["A1CF_in_GSE41998"].fillna(df_mini_30x10first["A1CF_in_GSE41998"].mean(),inplace=True)
df_mini_30x10first.apply(lambda x:sum(x.isnull()),axis=0) # done to check again tat the number of missing values are zero now
# check the datatypes of the cols throughout the df
df_mini_30x10first.dtypes
# perform basic maths operations
df_mini_30x10first.mean() # mean of all the numerical columns # df.median is another fucntion that can be used here
# combining dfs
one = pd.DataFrame(np.random.randn(5,4))
two = pd.DataFrame(np.random.randn(5,4))
# - combine 2 dfs across the rows if the structure is the same (same cols list)
pd.concat([one,two])
# - combine dfs when the structure is not identical
left = pd.DataFrame({"key": ["foo",'bar',],'lval':[1,2]})
left
right = pd.DataFrame({"key": ["foo",'bar','bar'],'rval':[3,4,5]})
right
# the last col is different so structure of left and right dfs here are different. they will be combined this way
pd.merge(left,right,on="key")

# >>>>> MODEL BUILDING
# - a bunch of API exists for model building (e.g. scikit learn module)
# - to use scikit learn you"ll need to imports first modules and submodules if necessary
# typical imports lines are :
from sklearn.linear_model import LogisticRegression # (has also a LogisticRegressionCV version)
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier,export_graphviz
from sklearn import metrics

# Extracting the variables frames (independent ie features and the dependent ie response) and splitting the data into training and testing set
# - extracting only the independent variables
X = df_mini_30x10first.iloc[:,[5,8]].values
# - extracting only the dependent variables (one only exist here)
y = df_mini_30x10first.iloc[:,9].values
# splitting the dataset into Training set and test set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25, random_state=0)

# Feature scaling (to care of relatively scattered values in data also as extreme values)
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)

# how to implement logistic regression
# - logistic regression is for classification and is usually used when the dependent variable is binary
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)
# Predicting the test set results
y_pred = classifier.predict(X_test)
y_pred
# describe the performance of the model using a confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
cm
# on sklearn confusion matrices, the diagonal numbers (upper left number is TN, lower right number is TP) go up with the accuracy
# (upper right number is FP, lower left number is FN)

# compute accuracy
from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)



