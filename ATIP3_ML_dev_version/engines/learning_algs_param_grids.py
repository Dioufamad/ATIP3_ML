###--------------------- This is the location of some functions that deliver directly available param_grids ready for use -----------------------

###---------------------IMPORTS
import numpy as np
import locale
#====================================================================

# ---------------------Variables to initialise------------------------------------------
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') #for setting the characters format
#====================================================================

# # -------- NB 1 : geomspace vs logspace
# numpy.geomspace(start, stop, num=50, endpoint=True, dtype=None, axis=0)[source]¶
# Return numbers spaced evenly on a log scale (a geometric progression).
# This is similar to logspace, but with endpoints specified directly.
# source : https://numpy.org/doc/stable/reference/generated/numpy.geomspace.html

# # >>>>>>>>>>>>> a regularization strength values space version 1     ##! not needed
# # call by using lambda_lowest=0.0001,lambda_highest=100.0,num_initial_values=200 and get 206 lambdas values
# def reg_strength_space_maker1(lambda_lowest=0.0001,lambda_highest=100.0,num_initial_values=200):
#     # the different regularization strength values
#     reg_strength_space = np.geomspace(lambda_lowest, lambda_highest, num=num_initial_values)  # 0.0001 to 100.O (200 lambda values)
#     # update the list of lambda values by adding to it some values that across either used as default lambdas values in different APIs or are some values of lambdas we would for sure just include in the list
#     # we cite : or sklearn [1.0, ], for SPAMS  [1.0,0, 0.1, 0.05, 10, 0.001,0.01,0.0001, ]
#     # this correspond to this list of lambdas : [0.0001, 0.001, 0.05,0.01, 0.1, 1.0, 10.0, 100.0]
#     # the 0.0 value is omitted because it nullify the regularization intended and can result in errors due to some parameters that are not making sense anymore
#     list_of_lambda_values_2_add = [0.0001, 0.001, 0.05,0.01, 0.1, 1.0, 10.0, 100.0]
#     for a_lambda_value_2_add in list_of_lambda_values_2_add:
#         if a_lambda_value_2_add not in reg_strength_space:
#             reg_strength_space = np.append(reg_strength_space, a_lambda_value_2_add)
#     reg_strength_space_sorted = np.sort(reg_strength_space)  # from min to max (~200 lambda values, including default value 1)
#     reg_strength_space_sorted_inverts = 1 / reg_strength_space_sorted  # 1/previous_max to 1/previous_min (~200 C values including the default value 1=1/previousLambdaIs1)
#     size_final_lambda_values_space = len(reg_strength_space_sorted)
#     return reg_strength_space_sorted, reg_strength_space_sorted_inverts, size_final_lambda_values_space


# # >>>>>>>>>>> the different regularization strength spaces that might be used in the following param_grids definition    ##! not needed
# # - regularization strength values space 1
# reg_strength_space1_gallery = reg_strength_space_maker1(0.0001,100.0,200) # 0.0001 to 100.O (206 lambda values) as a gallery of 3 : the sorted array, its array of inversed, and the lenghth
# reg_strength_space1_sorted = reg_strength_space1_gallery[0] # 0 for algs using lambdas (smallest to highest lambda value)
# reg_strength_space1_sorted_inverts = reg_strength_space1_gallery[1] # 1 for algs using C = 1/lambda (highest to smallest C value)
# reg_strength_space1_length = reg_strength_space1_gallery[2]

# >>>>>>>>>>>>> a regularization strength values space using geomspace or logspace, a min val, a max val, a option to invert values, and an option to add remarkable values

def reg_strength_space_maker2(space_type_lambda, minlambda, maxlambda, numlambda,beef_up_lambda, list_lambda_val_to_add, lambdaCing):
    # - possible values of arguments
    # space_type_lambda : "log" or "geom"
    # minlambda : to make the minimal reg strength, a value to use directly as a reg value from geomspace() or used by a log function to make a reg value from logspace()
    # maxlambda : to make the maximal reg strength, a value to use directly as a reg value from geomspace() or used by a log function to make a reg value from logspace()
    # numlambda : int, the number of values in the space produced
    # beef_up_lambda : "yes" or "no", used to choose if we want or not to add values from a list to the reg strength space
    # list_lambda_val_2_add : None will use the list [0.0001, 0.001, 0.05,0.01, 0.1, 1.0, 10.0, 100.0] by default, a list of floats to add to the created reg strength space
    # lambdaCing : "yes" or "no", used to choose if we want or not to invert the values of strength to go from lambda values to C values (C=1/lambda, the reg strength param in sklearn)
    # NB : the old defaults values are : space_type_lambda="log",minlambda=-4,maxlambda=1,numlambda=5,beef_up_lambda="yes",list_lambda_val_to_add = None,lambdaCing="no"
    # - the different regularization strength values
    if space_type_lambda=="log": # the min and max values given for each lambda will be used in a logspace() as starting points of the space (you make a log with them to get the lambda values)
        reg_strength_space = np.logspace(minlambda, maxlambda, num=numlambda) # log(minlambda) to log(maxlambda) (numlambda lambda values)
    else: # space_type_lambda=="geom" # the min and max values given for each lambda will be used in a geomspace() as end points of the space (they are directly lambdas values)
        reg_strength_space = np.geomspace(minlambda, maxlambda, num=numlambda)  # minlambda to maxlambda (numlambda lambda values)
    # - the part where we add remarkable values that we would want to test in the reg strength space
    if beef_up_lambda=="yes":
        # the idea...
        # is to update the list of lambda values by adding to it some values that are either
        # used as default lambdas values in different APIs (eg :
        # or are some values of lambdas we would for sure just include in the list
        # we cite : or sklearn [1.0, ], for SPAMS  [1.0,0, 0.1, 0.05, 10, 0.001,0.01,0.0001, ]
        # this correspond to this list of lambdas : [0.0001, 0.001, 0.05,0.01, 0.1, 1.0, 10.0, 100.0]
        # NB : the 0.0 value is omitted because it nullify the regularization intended and can result in errors due to some parameters that are not making sense anymore
        if list_lambda_val_to_add is None:
            list_lambda_val_to_add = [0.0001, 0.001, 0.05,0.01, 0.1, 1.0, 10.0, 100.0]
        # adding the values...
        for a_lambda_value_to_add in list_lambda_val_to_add:
            if a_lambda_value_to_add not in reg_strength_space:
                reg_strength_space = np.append(reg_strength_space, a_lambda_value_to_add)
        # - the full reg strength space is sorted
        reg_strength_space = np.sort(reg_strength_space)  # from min to max (~numlambda lambda values, numlambda+ some those that were added that werent here, eg : default value 1)
    # - Cing is the process where we invert the reg strength values to get the C param of sklearn (C=1/lambda)
    if lambdaCing=="yes":
        reg_strength_space = 1 / reg_strength_space  # 1/previous_max to 1/previous_min (~numlambda C values including the default value 1=1/previousLambdaIs1)
    # - get a precise size of the space created
    size_final_reg_strength_space = len(reg_strength_space)
    return reg_strength_space, size_final_reg_strength_space

# - exemples of calls :
# call by using lambda_lowest=0.0001,lambda_highest=100.0,num_initial_values=200 and get 206 lambdas values




# >>>>>>>>>>> SPAMS param_grids : lets build the gallery of our hyperparamerters (the variating params of the alg) values here
def param_grid_lambdas123_space_maker1(space_type_lambda1="log",minlambda1=-4,maxlambda1=1,numlambda1=5,beef_up_lambda1="yes",list_lambda1_val_to_add = None,lambda1Cing="no",
                                          space_type_lambda2="log",minlambda2=-4,maxlambda2=1,numlambda2=0,beef_up_lambda2="yes",list_lambda2_val_to_add = None,lambda2Cing="no",
                                          space_type_lambda3="log",minlambda3=-4,maxlambda3=1,numlambda3=0,beef_up_lambda3="yes",list_lambda3_val_to_add = None,lambda3Cing="no"):
    # to test param grid with a desired num of lambda1 and/or lambda2 and/or lambda3, use this
    # NB : the default run of the funct gives 5 lambda1 values from -4 to 1 in logspace, with a beef up with the default gallery of values to add, no Cing
    # - make an empty dict as a collector of what to put in (make also a collector of the size of each lambda space)
    param_grid_lambdas123 = {}
    param_grid_lambdas123_counts = {}
    # - the lambda1, lambda2 and lambda3 values added in this order in the dict (their count also):
    if numlambda1 > 0 :
        # get a gallery of 2 : the sorted array and its length in that order
        lambda1_reg_strength_gallery = reg_strength_space_maker2(space_type_lambda1,minlambda1,maxlambda1,numlambda1,beef_up_lambda1,list_lambda1_val_to_add,lambda1Cing)
        if lambda1Cing == "no":
            param_grid_lambdas123['lambda1'] = lambda1_reg_strength_gallery[0]
            param_grid_lambdas123_counts['lambda1'] = lambda1_reg_strength_gallery[1]
        else:
            param_grid_lambdas123['C'] = lambda1_reg_strength_gallery[0]
            param_grid_lambdas123_counts['C'] = lambda1_reg_strength_gallery[1]
    if numlambda2 > 0:
        # get a gallery of 2 : the sorted array and its length in that order
        lambda2_reg_strength_gallery = reg_strength_space_maker2(space_type_lambda2, minlambda2, maxlambda2, numlambda2, beef_up_lambda2, list_lambda2_val_to_add, lambda2Cing)
        param_grid_lambdas123['lambda2'] = lambda2_reg_strength_gallery[0]
        param_grid_lambdas123_counts['lambda2'] = lambda2_reg_strength_gallery[1]
    if numlambda3 > 0:
        # get a gallery of 2 : the sorted array and its length in that order
        lambda3_reg_strength_gallery = reg_strength_space_maker2(space_type_lambda3, minlambda3, maxlambda3, numlambda3, beef_up_lambda3, list_lambda3_val_to_add, lambda3Cing)
        param_grid_lambdas123['lambda3'] = lambda3_reg_strength_gallery[0]
        param_grid_lambdas123_counts['lambda3'] = lambda3_reg_strength_gallery[1]

    return param_grid_lambdas123,param_grid_lambdas123_counts

# # >>>>>>>>>>> sklearn param_grids : lets build the gallery of our hyperparamerters (the variating params of the alg) values here   ##! not needed
# def param_grid_sklearn_206C_maker1():
#     # to test param grid use this for an even shorter test
#     param_grid_sklearn_206C = {'C': reg_strength_space1_sorted_inverts}
#     return param_grid_sklearn_206C

# ------------- reserve of ideas to add

# # - the params_list that we should print, copy the print and paste it in the code part were we want all these values
# params_list = {'numThreads': -1, 'verbose': True, 'it0': 10, 'max_it': 200, 'L0': 0.1, 'intercept': False, 'pos': False}
# params_list['compute_gram'] = True
# params_list['loss'] = 'square'
# params_list['regul'] = 'l1'
# params_list['tol'] = 0.01
# params_list["lambda1"] = 0.05
# # params_list["lambda2"] = 0.05
# # params_list["lambda3"] = 0.05
# print(params_list)

# - the param_grid is the gallery of values to be given to the gridsearchcv function for the search
# to explore one of the lambdas, uncomment of these
# param_grid = {"lambda1": reg_strength_space}
# param_grid = {"lambda2": reg_strength_space}
# param_grid = {"lambda3": reg_strength_space}

# -----------------------------------------------------------------------------------------------------------------------------------