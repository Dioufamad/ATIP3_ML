#=================================test of mclust 1
# source : https://www.youtube.com/watch?v=6OtFwdcRp7k&list=WL&index=2

# load necessary librairies
library(lattice) # for plots
library(mclust) # to extract the 6 parameters of a mixture of 2 models
library(AdaptGauss)


# set the seed so that the random action can be fixated for repetability issues
set.seed(12345)

#--1--Setting the dataset to manipulate (some options throughout the script change depending on chosen dataset)
# - uncomment one of these 4 following lines to choose a dataset
cohort <- "Remagus02"
# cohort <- "Remagus04"
# cohort <- "MDAnderson"
# cohort <-  "another_dataset_you_want_to_use"

#--2--Setting the part of dataset to usemanipulate (some options throughout the script change depending on chosen part of dataset)
part_of_dataset <- "sample_col1"
# part_of_dataset <- "sample_col2"
# part_of_dataset <- "sample_col3"
# part_of_dataset <- "all_samples"

#--3--Setting the dataset of entry  
# entry_data <- ex1 # a dataset with best probesets
entry_data <- ex1_bis_with_GS # the same dataset but with the gene symbol used instead 

# #--Test Data
# # example of data to use for test
# x=c(rnorm(100,0,0.5), rnorm(200,3,1))
# # plotting the two distributions of the test data
# y = c(rep(0,100), rep(1,200))
# densityplot(~x|as.factor(y), layout=c(1,2), n=200, width=1.5)
# # show a binomdal plot 
# densityplot(x, 200, width = 1.5) # xlab, lim, ylim options see hist in others scripts 


# select cohort data
if (part_of_dataset=="sample_col1") {
  x<-entry_data[,1]
  the_samples_list <-colnames(entry_data)[1] # the dimnames(x)[[1]] is list of rownames, dimnames(x)[[2]] is list of cols
} else if (part_of_dataset=="sample_col2") {
  x<-entry_data[,2]
  the_samples_list <-colnames(entry_data)[2] 
} else if (part_of_dataset=="sample_col3") {
  x<-entry_data[,3]
  the_samples_list <-colnames(entry_data)[3] 
} else if (part_of_dataset=="all_samples") {
  x<-entry_data
  # the_samples_list <-dimnames(x)[[2]] # no need because no hist drawn
} else
  print("Replace this statement with a command to store the specific part of another_dataset_you_want_to_use")

#--verifications
# NB : check if MTUS1 is present "MTUS1" %in% dimnames(x)[[1]] # should display TRUE


if (part_of_dataset %in% c("sample_col1","sample_col2","sample_col3")) {
  ###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ONE SAMPLE THRESOLD (MOSTLY FOR AN HISTOGRAM) >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  #--1--Mclust : 1 for the one-dimensional model
  # make a model called fit 
  fit = Mclust(x,G=2)
  # plot(fit)
  # recover the parameters
  
  # fit$parameter$pro # - the mixing proportions for the components of the mixture
  Weight1 = fit$parameter$pro[1] # the proportions of the 1st component values
  Weight2 = fit$parameter$pro[2] # the proportions of the 2nd component values
  
  # fit$parameter$mean # - The mean for each component
  # NB : If there is more than one component, this is a matrix whose kth column is the mean of the kth component of the mixture model.
  Mean1 = fit$parameter$mean[[1]] # the mean of the 1st component values
  Mean2 = fit$parameter$mean[[2]] # the mean of the 2nd component values
  
  # fit$parameter$variance$sigmasq # - the variances : a vector whose kth component is the variance for the kth component in the mixture model
  # fit$parameter$variance$sigmasq[1] # the variance of the 1st component values
  # fit$parameter$variance$sigmasq[2] # the variance of the 2nd component values
  if (length(fit$parameter$variance$sigmasq) != 1) {
    SD1 = sqrt(fit$parameter$variance$sigmasq[1]) # the std dev of the 1st component values
    SD2 = sqrt(fit$parameter$variance$sigmasq[2]) # the std dev of the 2nd component values
  }else { # if fit$parameter$variance$sigmasq does not have two values it means one common values to both components
    SD1 = sqrt(fit$parameter$variance$sigmasq[1]) # the std dev of the 1st component values
    SD2 = sqrt(fit$parameter$variance$sigmasq[1]) # the std dev of the 2nd component values
  }
  
  # -------------- Notes on Mclust    : 
  # sigmasq or scale : what is the proper value for the variances? 
  # its sigmasq (see why here https://rdrr.io/cran/mclust/man/mclustVariance.html
  
  # NB : with k-means, we observe a bias where the small cluster mean is pushed out to absorb more values (see source 17:22)
  
  # another good full courses on Mclust library : 
  # http://rug.mnhn.fr/semin-r/PDF/semin-R_mclust_APerrard_240513.pdf
  # https://cran.r-project.org/web/packages/mclust/vignettes/mclust.html
  # implement the EM algorithm : 
  # https://tinyheero.github.io/2016/01/03/gmm-em.html
  
  #--2--Finds the intersect of two gaussians or log gaussians from package AdaptGauss
  intersec_coord = Intersect2Mixtures(Mean1,SD1,Weight1,Mean2,SD2,Weight2) 
  # options are : Mean1,SD1,Weight1,Mean2,SD2,Weight2,IsLogDistribution,MinData,MaxData
  # see doc here : https://rdrr.io/cran/AdaptGauss/man/Intersect2Mixtures.html
  
  # let's keep the threshold
  # intersec_coord_y <- intersec_coord$CutY # the y of the intersection
  intersec_coord_x <- intersec_coord$CutX # the x of the intersection
  
  # draw the histogram
  h <- hist(x, 100, col = "cornsilk1", freq = FALSE, 
            main = paste("Histogram of the intensities (", "Cohort : ", cohort, ", sample : ",the_samples_list,")", sep=""), 
            border = "antiquewhite4",
            xlab = paste("Intensities of the best probesets (", "threshold (red line) : ~",as.character(round(intersec_coord_x, digits = 3)),")", sep=""),
            xlim = c(min(x),max(x)))
  lines(density(x),lwd=1.5,col="blue")
  xs = seq(min(x), max(x), by=.01) # add the bimodal curve
  lines(xs, Weight1*dnorm(xs, Mean1,SD1), lty=2,col = "darkgreen") # add the curve of mode 1
  lines(xs, Weight2*dnorm(xs, Mean2,SD2), lty=2,col = "coral4") # add the curve of mode 2
  # mach_threshold <- intersec_coord_x
  abline(v = intersec_coord_x, col = "red", lwd = 2) # add the threshold line
  ###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  
} else if (part_of_dataset=="all_samples") {
  x_thres_collector<-as.data.frame(t(x)) # transpose x to put a new col later as the threshold of each rows ie each samples 
  # NB: as transposing outputs a matrices that col cant be added to it easily, we coerce it into a df to be able to add a col to it later
  x_thres_collector = x_thres_collector[c("MTUS1")]
  x_thres_collector$Threshold_low_high <- "NOT_CHANGED_YET" # new threshold col with a placeholder to know if changed or not
  for (a_sample_as_colname in the_samples_list) {
    x_1col = x[,a_sample_as_colname] # we captured our x values
    ###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>ALL SAMPLES THRESOLDs (TO CALL THE CLASSES FOR A GENE)>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #--1--Mclust : 1 for the one-dimensional model
    # make a model called fit 
    fit = Mclust(x_1col,G=2)
    # plot(fit)
    # recover the parameters
    
    # fit$parameter$pro # - the mixing proportions for the components of the mixture
    Weight1 = fit$parameter$pro[1] # the proportions of the 1st component values
    Weight2 = fit$parameter$pro[2] # the proportions of the 2nd component values
    
    # fit$parameter$mean # - The mean for each component
    # NB : If there is more than one component, this is a matrix whose kth column is the mean of the kth component of the mixture model.
    Mean1 = fit$parameter$mean[[1]] # the mean of the 1st component values
    Mean2 = fit$parameter$mean[[2]] # the mean of the 2nd component values
    
    # fit$parameter$variance$sigmasq # - the variances : a vector whose kth component is the variance for the kth component in the mixture model or one common value
    # fit$parameter$variance$sigmasq[1] # the variance of the 1st component values
    # fit$parameter$variance$sigmasq[2] # the variance of the 2nd component values
    if (length(fit$parameter$variance$sigmasq) != 1) {
      SD1 = sqrt(fit$parameter$variance$sigmasq[1]) # the std dev of the 1st component values
      SD2 = sqrt(fit$parameter$variance$sigmasq[2]) # the std dev of the 2nd component values
    }else { # if fit$parameter$variance$sigmasq does not have two values it means one common values to both components
      SD1 = sqrt(fit$parameter$variance$sigmasq[1]) # the std dev of the 1st component values
      SD2 = sqrt(fit$parameter$variance$sigmasq[1]) # the std dev of the 2nd component values
    }
    
    # -------------- Notes on Mclust    : 
    # sigmasq or scale : what is the proper value for the variances? 
    # its sigmasq (see why here https://rdrr.io/cran/mclust/man/mclustVariance.html
    
    # NB : with k-means, we observe a bias where the small cluster mean is pushed out to absorb more values (see source 17:22)
    
    # another good full courses on Mclust library : 
    # http://rug.mnhn.fr/semin-r/PDF/semin-R_mclust_APerrard_240513.pdf
    # https://cran.r-project.org/web/packages/mclust/vignettes/mclust.html
    # implement the EM algorithm : 
    # https://tinyheero.github.io/2016/01/03/gmm-em.html
    
    #--2--Finds the intersect of two gaussians or log gaussians from package AdaptGauss
    intersec_coord = Intersect2Mixtures(Mean1,SD1,Weight1,Mean2,SD2,Weight2) 
    # options are : Mean1,SD1,Weight1,Mean2,SD2,Weight2,IsLogDistribution,MinData,MaxData
    # see doc here : https://rdrr.io/cran/AdaptGauss/man/Intersect2Mixtures.html
    
    # let's keep the threshold
    # intersec_coord_y <- intersec_coord$CutY # the y of the intersection
    intersec_coord_x <- intersec_coord$CutX # the x of the intersection
    ###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # lets store the intersection value in the collector
    x_thres_collector[a_sample_as_colname,"Threshold_low_high"] = intersec_coord_x # store the best found probe for the long egi
  }
  # show an error if not all values are computed
  if ("NOT_CHANGED_YET" %in% unique(as.character(x_thres_collector$Threshold_low_high))) {
    print("Beware : At least one threshold have not been computed !!!")
  }
  # change the thresholds column into numeric values instead of character 
  x_thres_collector<-transform(x_thres_collector, Threshold_low_high = as.numeric(Threshold_low_high))
  # complete the table of results of thresholds with classes following the gene of interest
  median_threshold = median(x_thres_collector$Threshold_low_high) # as.numeric() can be used around the column if the values kept are not detected as numbers but instead as characters
  x_thres_collector$Median_Threshold_cohort <- median_threshold
  x_thres_collector$ATIP3_class_predicted_w_med_thres <- "NOT_CHANGED_YET" # predictions with median threshold
  x_thres_collector$ATIP3_class_predicted_w_med_thres[which(x_thres_collector$MTUS1 < median_threshold)]<-"low"
  x_thres_collector$ATIP3_class_predicted_w_med_thres[which(x_thres_collector$MTUS1 > median_threshold)]<-"high"
  x_thres_collector$ATIP3_class_predicted_w_sample_thres <- "NOT_CHANGED_YET" # predictions with sample specific threshold
  x_thres_collector$ATIP3_class_predicted_w_sample_thres[which(x_thres_collector$MTUS1 < x_thres_collector$Threshold_low_high)]<-"low"
  x_thres_collector$ATIP3_class_predicted_w_sample_thres[which(x_thres_collector$MTUS1 > x_thres_collector$Threshold_low_high)]<-"high"
  count_class_low_gene_of_interest = sum(x_thres_collector$ATIP3_class_predicted_w_med_thres == "low") # counts of the classes with median threshold
  count_class_high_gene_of_interest = sum(x_thres_collector$ATIP3_class_predicted_w_med_thres == "high")
  count_class_low_thres_sample_specific = sum(x_thres_collector$ATIP3_class_predicted_w_sample_thres == "low") # counts of the classes with sample specific threshold
  count_class_high_thres_sample_specific = sum(x_thres_collector$ATIP3_class_predicted_w_sample_thres == "high")
  # reporting on results
  paste(cohort," cohort Median threshold : ", median_threshold, sep="")
  paste(cohort," cohort MTUS1 classes count : ATIP3 low (", count_class_low_gene_of_interest, "), ATIP3 high (",count_class_high_gene_of_interest,")", sep="")
  paste(cohort," cohort MTUS1 classes if using sample threshold : ATIP3 low (", count_class_low_thres_sample_specific, "), ATIP3 high (",count_class_high_thres_sample_specific,")", sep="")
  paste(cohort," cohort thresholds range is : ",range(x_thres_collector$Threshold_low_high)[1] ," to ",range(x_thres_collector$Threshold_low_high)[2], sep="")
  paste(cohort," cohort range MTUS1 is : ",range(x_thres_collector$MTUS1)[1] ," to ",range(x_thres_collector$MTUS1)[2], sep="")
  # part for saving on file and reread anytime
  outfilename = paste(cohort, "_threshold_atip3_classes.csv", sep='')
  write.csv(x_thres_collector, outfilename, row.names=T)
} else
  print("Replace this statement with a command to store the threshold of the specific part of another_dataset_you_want_to_use")
  
  

# check the columns type before going forward
summary(x_thres_collector)
# # get the min and max of the sample specific thresholds 
# min(x_thres_collector[,"Threshold_low_high"], na.rm = TRUE)
# max(x_thres_collector[,"Threshold_low_high"], na.rm = TRUE)
# # or use this if col not in numeric
# # min(as.numeric(x_thres_collector$Threshold_low_high), na.rm = TRUE)
# # max(as.numeric(x_thres_collector$Threshold_low_high), na.rm = TRUE)


# R02 : when median threshold is 4, we have 0 and 0
# not needed to test this for the others datasets because they lower end of the range of atip3 values is higher than 4. 

###################Notes 
# ####Another way to compute the threshold#######################
# source : https://stackoverflow.com/questions/16982146/point-of-intersection-2-normal-curves
# # the 6 parameters of the model
# m1=Mean1; sd1=SD1; m2=Mean2; sd2=SD2; p1=Weight1; p2=Weight2 # test with mydata
# # a fonction to find the intersection points x values
# intersect <- function(m1, sd1, m2, sd2, p1, p2){
#   B <- (m1/sd1^2 - m2/sd2^2)
#   A <- 0.5*(1/sd2^2 - 1/sd1^2)
#   C <- 0.5*(m2^2/sd2^2 - m1^2/sd1^2) - log((sd1/sd2)*(p2/p1))
#   if (A!=0){
#     (-B + c(1,-1)*sqrt(B^2 - 4*A*C))/(2*A)
#   } else {-C/B}
# } 
# intersec_coord_list<-intersect(m1,sd1,m2,sd2,p1,p2)
# # keep only values that are between the two means
# intersec_coord_list <- intersec_coord_list[intersec_coord_list < m2]
# intersec_coord_list <- intersec_coord_list[intersec_coord_list > m1]
# intersec_coord_x<-intersec_coord_list[length(intersec_coord_list)]
# ###############################################################