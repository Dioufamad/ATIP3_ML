# first tests of cyanure

# installing cyanure
# - install the mkl lib
# - installl cyanure mkl with pip install cyanure-mkl


#===================================start of basic tests of cyanure
# test cyanure
# - the first example of multiclass classification with a said multitask
import cyanure as cyan
import numpy as np
#load ckn_mnist dataset 10 classes, n=60000, p=2304
data=np.load('/data_acquisition/1_pipelines_or_tasks/Multitask_learning/Cyanure/ckn_mnist.npz'); y=data['y']; X=data['X']
#center and normalize the rows of X in-place, without performing any copy
# keep a version of the fts values to compare and see effect of normalisation
X_before_norm = X
cyan.preprocess(X,centering=True,normalize=True,columns=False)
#declare a multinomial logistic classifier with group Lasso regularization
classifier=cyan.MultiClassifier(loss='multiclass-logistic',penalty='l1l2')
# uses the auto solver by default, performs at most 500 epochs
classifier.fit(X,y,lambd=0.0001,max_epochs=500,tol=1e-3,it0=5)

# - Learning the multiclass classifier took about 3mn.
# To conclude, we provide a last more classical example of :
# learning l2-logistic regression classifiers on the same dataset, in a one-vs-all fashion.

import cyanure as cyan
import numpy as np
#load ckn_mnist dataset 10 classes, n=60000, p=2304
data=np.load('/data_acquisition/1_pipelines_or_tasks/Multitask_learning/Cyanure/ckn_mnist.npz'); y=data['y']; X=data['X']
#center and normalize the rows of X in-place, without performing any copy
cyan.preprocess(X,centering=True,normalize=True,columns=False) # X is a np array as input matrix
#declare a multinomial logistic classifier with group Lasso regularization
classifier=cyan.MultiClassifier(loss='logistic',penalty='l2')
# uses the auto solver by default, performs at most 500 epochs
classifier.fit(X,y,lambd=0.01/X.shape[0],max_epochs=500,tol=1e-3)

# trial : also can do this cv method to score the model
classifier=cyan.MultiClassifier(loss='logistic',penalty='l2')
from sklearn.model_selection import cross_val_score
print(cross_val_score(classifier, X, y, cv=3,verbose=1,fit_params={'lambd':0.01/X.shape[0],'max_epochs':500,'tol':1e-3}))
# result : does not work because model is not a scikit-learn estimator

#===================================================end of basic tests of cyanure

#===================================start of the tests to carry out on our data
# 1) l2 penalty (ridge)
# - the first example of multiclass classification with a said multitask
import cyanure as cyan
import numpy as np
from sklearn.preprocessing import binarize
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
#load ckn_mnist dataset 10 classes, n=60000, p=2304
data=np.load('/data_acquisition/1_pipelines_or_tasks/Multitask_learning/Cyanure/ckn_mnist.npz'); y=data['y']; X=data['X']
#center and normalize the rows of X in-place, without performing any copy
# binarize the response
y = binarize(y, threshold=5.0, copy=True)
# splitting dataset in train test
train_x,test_x,train_y,test_y = train_test_split(X,y,test_size=0.2,random_state=0)
# standardise
train_x_b4norm = train_x
test_x_b4norm = test_x
scaler=StandardScaler()
train_x=scaler.fit_transform(train_x)
test_x = scaler.transform(test_x)
# # keep a version of the fts values to compare and see effect of normalisation
# X_before_norm = X
# cyan.preprocess(X,centering=True,normalize=True,columns=False)
#declare a multinomial logistic classifier with group Lasso regularization
# classifier=cyan.MultiClassifier(loss='logistic',penalty='l1')
classifier=cyan.BinaryClassifier(loss='logistic',penalty='l1')
# uses the auto solver by default, performs at most 500 epochs
classifier.fit(train_x,train_y,lambd=0.0001,max_epochs=500,tol=1e-3,it0=5)
# a prediction
y_pred1 = classifier.predict(test_x)
y_pred1_t = y_pred1.reshape(-1,1)    # reshape into a column array the precction
# a score
classifier.score(test_x,test_y)
# the coefs
coefs1 = classifier.get_weights()
# 2) l1 penalty (lasso)

# 3)

#===================================end of the tests to carry out on our data


#===================================== start of tests using sklearn api to get perfs
# TEST : trial gridsearchcv
# - TEST : does the gridsearchcv works with cyanure ?
# - the basic multiclassifier classifier with l1l2 for multitask group lasso
import cyanure as cyan
import numpy as np
#load ckn_mnist dataset 10 classes, n=60000, p=2304
data=np.load('/data_acquisition/1_pipelines_or_tasks/Multitask_learning/Cyanure/ckn_mnist.npz'); y=data['y']; X=data['X']
#center and normalize the rows of X in-place, without performing any copy
cyan.preprocess(X,centering=True,normalize=True,columns=False)
#declare a multinomial logistic classifier with group Lasso regularization
# classifier=cyan.MultiClassifier(loss='multiclass-logistic',penalty='l1l2')
# uses the auto solver by default, performs at most 500 epochs
# classifier.fit(X,y,lambd=0.0001,max_epochs=500,tol=1e-3,it0=5)
# - the gridsearchcv to compare a multitask group lasso and a multitask sparse group lasso
from sklearn.model_selection import GridSearchCV
clf = GridSearchCV(cyan.MultiClassifier(loss='multiclass-logistic'), {
    'penalty': ['l1l2','l1l2+l1']
}, cv=5, return_train_score=False)
clf.fit(X,y,lambd=0.0001,max_epochs=500,tol=1e-3,it0=5)
clf.cv_results_
# results : an error
# TypeError: Cannot clone object '<cyanure.MultiClassifier object at 0x7fad9dc458d0>' (type <class 'cyanure.MultiClassifier'>):
# it does not seem to be a scikit-learn estimator as it does not implement a 'get_params' method.

# - TEST : try the manual implementation for a gridsearch using embedded for loops (to compare a multitask group lasso and a multitask sparse group lasso)
import cyanure as cyan
import numpy as np
#load ckn_mnist dataset 10 classes, n=60000, p=2304
data=np.load('/data_acquisition/1_pipelines_or_tasks/Multitask_learning/Cyanure/ckn_mnist.npz'); y=data['y']; X=data['X']
#center and normalize the rows of X in-place, without performing any copy
cyan.preprocess(X,centering=True,normalize=True,columns=False)
# the for loops
from sklearn.model_selection import cross_val_score
penalty_types = ['l1l2','l1l2+l1']
lambd_values = [0.1,0.01,0.001,0.0001]
avg_scores = {}
for pval in penalty_types:
    for lval in lambd_values:
        model = classifier=cyan.MultiClassifier(loss='multiclass-logistic',penalty=pval)
        cv_scores = cross_val_score(model, X, y, cv=5)
        avg_scores[pval + '_' + str(lval)] = np.average(cv_scores)

avg_scores
# result :
# TypeError: Cannot clone object '<cyanure.MultiClassifier object at 0x7f89ce7dc750>' (type <class 'cyanure.MultiClassifier'>):
# it does not seem to be a scikit-learn estimator as it does not implement a 'get_params' method.
#>>>>>>>>>>>>>>>model used for code
# kernels = ['rbf', 'linear']
# C = [1,10,20]
# avg_scores = {}
# for kval in kernels:
#     for cval in C:
#         cv_scores = cross_val_score(svm.SVC(kernel=kval,C=cval,gamma='auto'),iris.data, iris.target, cv=5)
#         avg_scores[kval + '_' + str(cval)] = np.average(cv_scores)
#
# avg_scores
#>>>>>>>>>>

# - TEST : try the manual implementation of a gridsearch but without using the fast processing tools from scikit-learn
import cyanure as cyan
import numpy as np
#load ckn_mnist dataset 10 classes, n=60000, p=2304
data=np.load('/data_acquisition/1_pipelines_or_tasks/Multitask_learning/Cyanure/ckn_mnist.npz'); y=data['y']; X=data['X']
#center and normalize the rows of X in-place, without performing any copy
cyan.preprocess(X,centering=True,normalize=True,columns=False)
# the for loops
penalty_types = ['l1l2','l1l2+l1']
lambd_values = [0.1,0.01,0.001,0.0001]
avg_scores = {}
for pval in penalty_types:
    for lval in lambd_values:
        # declare a multinomial logistic classifier with group Lasso regularization
        classifier = cyan.MultiClassifier(loss='multiclass-logistic', penalty=pval)
        # uses the auto solver by default, performs at most 500 epochs
        classifier.fit(X, y, lambd=lval, max_epochs=500, tol=1e-3, it0=5)

        cv_scores = cross_val_score(model, X, y, cv=5)
        avg_scores[pval + '_' + str(lval)] = np.average(cv_scores)

avg_scores
# result : run be run and finished

#======================================end of tests using sklearn api to get perfs