
# install the package cutoff if not done yet

# load the library
library(cutoff)
# This package contains two main functions: 
# * that fit a finite mixture model to bimodal data with the Expectation-Maximization algorithm 
# * that calculate a cutoff value from a fitted finite mixture model, given a type-1 error 
# NB : There are additional functions, mainly to visualize the results 

# the dataset analysed is : ex1_bis_with_GS

measles = ex1_bis_with_GS

# step 1 : Bimodal data
length(measles)
range(measles)
# A histogram of the data:
hist(measles,100,F,xlab="concentration",ylab="density",ylim=c(0,.55), main=NULL,col="grey")
# A kernel density estimation of the distribution:
lines(density(measles),lwd=1.5,col="blue")
# This figure shows the histogram of the data together with a non-parametric estimation of the distribution. 
# The two peaks suggest a bimodal distribution of the data

# step 2 : Finite mixture models
## summarize here the paragraph on the distribution


# Estimating the parameters of the finite mixture model:
(measles_out <- em(measles,"normal","normal"))


