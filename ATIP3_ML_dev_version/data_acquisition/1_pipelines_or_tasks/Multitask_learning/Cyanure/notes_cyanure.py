# summary of the doc for cyanure


# what is group lasso : see here (https://en.wikipedia.org/wiki/Lasso_(statistics) and summary diagram in notes
#  - why group lasso and not lasso : the groups, despite being finer than
#  the extreme scenario here (https://stats.stackexchange.com/questions/214325/why-use-group-lasso-instead-of-lasso), will still help us:
#  the choice would still be made between a group of true covariates and a group of untrue covariates. We're still borrowing strength.
#  another source from the upper source states :
#  an upper bound on the prediction error of the group lasso is lower than
#  a lower bound on the prediction error of the plain lasso.
#  That is, they proved that the grouping makes our estimation do better


# - For documentation of Cyanure, see here  : http://thoth.inrialpes.fr/people/mairal/cyanure/python.html
# we have 4 part in the doc :
#   + The BinaryClassifier Class :
        # classcyanure.BinaryClassifier(loss='square', penalty='l2', fit_intercept=False)
        #  derives from ERM (empirical risk minimization problems)
        # goal is to minimize a classification the sum of a classification loss and a regularization function (or constraint)
        # regulariation fuction is function of w ie a p-dimensional vactor representing model params
        # also b is an optional unregularized intercept
        # Params :
        # - loss (loss func to be used) : string, default=’square’, best choice for work : "logistic"
        # - penalty (Regularization function called psi in source code) : string, default=’l2’, best choice for work : "l2" for std lasso, "elastic-net" for elastic-net
        # - fit_intercept (learns an unregularized intercept b) : boolean, default=’False’, best choice for work : default
        # Methods (only the ones we might need) :
        # - eval(self, X, y[, lambd, lambd2, lambd3]) : get the value of the objective function and computes a relative duality gap, see function fit for the format of parameters.
        # - fit(self, X, y[, lambd, lambd2, lambd3, …]) : The fitting function (the one that does the job)
        # - get_weights(self) : get the model parameters (either w or the tuple (w,b))
        # - predict(self, X) : predict the labels given an input matrix X (same format as fit)
        # - score(self, X, y) : Compute classification accuracy of the model for new test data (X,y)
        # fit methods's params :
        # - X : n x p np array (samples on rows)
        # - y : labels : np array, vector of size n with {-1,+1} labels for binary classification, which will be automatically converted if labels in {0,1} are provided
        # - lambd: float, default=0,  first regularization parameter λ used in l2 or in l1 (best choice of any lambda is from CV or f(num_samples))
        # - lambd2: float, default=0, second regularization parameter λ2, used in elastic-net after a lambd
        # - lambd3: float, default=0, third regularization parameter λ3, used in a fused-lasso after lambd and lambd2
        # - solver: string, default=’auto’, Optimization solver, best choice = see result of the benchmark to select it
        # - tol : float, default=’1e-3’, tolerance on the duality gap, best choice : default (0.001)
            # NB : duality gap : In optimization problems in applied mathematics, the duality gap is the difference
            # between the primal and dual solutions. If d* is the optimal dual value and p* is the optimal primal value
            # then the duality gap is equal to p* - d*.
            # This value is always greater than or equal to 0 (for minimization problems).
            # The duality gap is zero if and only if strong duality holds (p* = d* primal value is not the only best).
            # Otherwise the gap is strictly positive and weak duality holds (p* < d* ie p* is the only best and others good values d* are from optimization)
            # [source : https://en.wikipedia.org/wiki/Duality_gap#:~:text=In%20computational%20optimization%2C%20another%20%22duality,iterate%20for%20the%20primal%20problem.]
            # tolerance : This is a convergence parameter, representing the tolerance for the relative duality gap.
            # When the difference between the primal and dual objective function values falls below this tolerance,
            # the Optimizer determines that the optimal solution has been found
        # - max_epochs: int, default=500, Maximum number of iteration of the algorithm in terms of passes over the data, best choice : default
        # - it0: int, default=10, Frequency of duality-gap computation (in epochs i presume), best choice : 10 (or max_epochs/50)
        # - verbose: boolean, default=True, Display information or not, best choice : default
        # - nthreads: int, default=-1, maximum number of cores the method may use (-1 = all cores), best choice : default (ie all cores)
        # - seed: int, default=0, random seed, best choice : default
        # - restart: boolean, default=False, use a restart strategy (useful for computing regularization path), best choice : default (false)
        # - univariate: boolean, default=True, univariate or multivariate problems, best choice : default (True for uni ##! change again in multitaks)
        # - l_qning: int, default=20 : memory parameter for the qning method, best choice : default
        # - f_restart: int, default=50, restart strategy for fista, best choice : default
        #>>>> - returns a np array
        # NB : fit and predict function has the same format
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#   + The Regression Class:
        # cyanure.Regression(loss='square', penalty='l2', fit_intercept=False)
        # The objective is the same as for the BinaryClassifier class, but we use a regression loss only (see below), and the targets will be real values.
        # Params :
        # loss: string, default=’square’, Only the square loss is implemented at this point
        # penalty: same as for the class BinaryClassifier
        # fit_intercept: same as for the class BinaryClassifier
        # Methods :
        # - eval : same as for the class BinaryClassifier
        # - fit : same as for the class BinaryClassifier (except we do not except binary values)
        # - get_weights : same as for the class BinaryClassifier
        # - predict : same as for the class BinaryClassifier (except we do not except binary values) (same format as fit)
#   + The MultiClassifier Class :
        # classcyanure.MultiClassifier(loss='square', penalty='l2', fit_intercept=False)
        # derived from the BinaryClassifier to handle multiple learning task simultaneously
        # the binary classfier was :
        # goal is to minimize a classification the sum of a classification loss and a regularization function (or constraint)
        # regulariation fuction is function of w ie a p-dimensional vactor representing model params
        # also b is an optional unregularized intercept
        # the changes are :
        # (1/2) w is now W=[w1,…,wk], a (p x k) matrix that carries the k predictors,
        # where k is the number of classes (design is one vs all so num class = num tasks),
        # and yi is a label in {1,…,k}
        # (2/2) b is a now a k-dimensional vector representing one unregularized intercept for each task (which is optional)
        # Params :
        # - loss: any loss function compatible with the class BinaryClassifier
        # NB : in such a case, the loss function encodes a one vs. all strategy based on the chosen binary-classification loss.
        # or ‘multiclass-logistic’, which is also called multinomial or softmax logistic,
        # best choice : ‘multiclass-logistic’
        # - penalty : any penalty function compatible with the class BinaryClassifier.
        # in such a case, the penalty is applied on each predictor wj (inside W) individually
        # or ‘l1l2’, which is the multi-task group Lasso regularization
        # or ‘l1linf’ (a group lasso but with infinite predictors ie we assume its all predictors that can be built)
        # or ‘l1l2+l1’, which is the multi-task group Lasso regularization + l1 (group lasso + lasso on the group for sparse group lasso)
        # best choice : ‘l1l2’ for group lasso, and ‘l1l2+l1 for sparse group lasso
        # fit_intercept: boolean, default=’False’, learns an unregularized intercept b, which is a k-dimensional vector, best choice : default
        # Methods :
        # - eval : same as for the class BinaryClassifier
        # - fit : same as for the class BinaryClassifier, but y should be a vector of n-dimensional vector of integers
        # - get_weights : same as for the class BinaryClassifier
        # - predict : same as for the class BinaryClassifier (same format as fit)
        # - score : same as for the class BinaryClassifier
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#   + The MultiVariateRegression Class :
        # classcyanure.MultiVariateRegression(loss='square', penalty='l2', fit_intercept=False)
        # # The objective is the same as for the Regression class but the targets yi are k-dimensional vectors.
        # Params :
        # loss: string, default=’square’, Only the square loss is implemented at this point
        # penalty: same as for the class MultiClassifier
        # fit_intercept: same as for the class MultiClassifier
        # Methods :
        # - eval : same as for the class BinaryClassifier
        # - fit : Same as ERM.fit, but y should be n x k, where k is size of the target for each data point
        # - get_weights : same as for the class BinaryClassifier
        # - predict : same as for the class BinaryClassifier (same format as fit)
        ##! find the scoring function for the regression functions
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#   + Scikit-learn compatible classes :
        # classcyanure.LinearSVC(loss='sqhinge', penalty='l2', fit_intercept=False, C=1, max_iter=500)
        # classcyanure.LogisticRegression(penalty='l2', fit_intercept=False, C=1, max_iter=500)
        # These 2 will be more explored later


#
# - my choices in the future :
#   + for multitask lasso : basic preproc, loss='logistic'


# Parameters
#         ----------
#         loss : string, default='square'
#             Loss function to be used. Possible choices are
#             - 'square' =>  L(y,z) = 0.5 ( y-z)^2
#             - 'logistic' => L(y,z) = log(1 + e^{-y z} )
#             - 'sqhinge' or 'squared_hinge' => L(y,z) = 0.5 max( 0, 1- y z)^2
#             - 'safe-logistic' => L(y,z) = e^{ yz - 1 } - y z  if yz <= 1
#                                  and 0 otherwise
#             - 'multiclass-logistic' => multinomial logistic (see Latex
#                                        documentation).
#             Note that for binary classification, we assume the labels to be of
#             the form {-1,+1}

# penalty: string, default='none'
#             Regularization function psi. Possible choices are
#
#             For univariate problems
#             - 'none' => psi(w) = 0
#             - 'l2' =>  psi{w) = (lambd/2) ||w||_2^2
#             - 'l1' =>  psi{w) = lambd ||w||_1
#             - 'elastic-net' =>  psi{w) = lambd ||w||_1 + (lambd2/2)||w||_2^2
#             - 'fused-lasso' => psi(w) = lambd sum_{i=2}^p |w[i]-w[i-1]|
#                                       + lambd2||w||_1 + (lambd3/2)||w||_2^2
#             - 'l1-ball'     => encodes the constraint ||w||_1 <= lambd
#             - 'l2-ball'     => encodes the constraint ||w||_2 <= lambd
#
#             For multivariate problems, the previous penalties operate on each
#             individual (e.g., class) predictor.
#             In addition, multitask-group Lasso penalties are provided for
#             multivariate problems (w is then a matrix)
#             - 'l1l2' or 'l1linf', see Latex documentation
#
#         fit_intercept: boolean, default='False'
#             learns an unregularized intercept b  (or several intercepts for
#             multivariate problems)



# Update : SPAMS and Cyanure installed
# - cyanure is pretty straightforward and the way of doing multitask is a one-vs-all learning on each response, in a simultaneous way.
# I just have to recode my responses values into one multiclass response
# - SPAMS is 3 toolbox into one type of tool :
# + one box is for dictionnary learning and non negative based operation slike the NnMatrix factorisation
# + another box is for the sparse decomposition toolbox having as landmarks methods being the OMP (Orthogonal Matching Pursuit), the LARS algorithm and the coordinate descent implanted.
# others highlights are that a greedy solver exists and is use by the OMP and a solver for simultaneous signal approximation (similar to
# + and finally the last box is for implemented proximal methods (ISTA and FISTA) for approximation problems combined with different loss and regularizations.
# we also have tree-structure based methods in here.


# NB : test files location
# Cyanure tests can be done using 2 datsets supplied. They are the two file "ckn_mnist.npz"
# and "rcv1.npz".
# they are stored in data_warehouse/outputs folder