#=================================test of mclust 1 but for one gene only
# source : https://www.youtube.com/watch?v=6OtFwdcRp7k&list=WL&index=2

# load necessary librairies
library(lattice) # for plots
library(mclust) # to extract the 6 parameters of a mixture of 2 models
library(AdaptGauss)


# set the seed so that the random action can be fixated for repetability issues
set.seed(12345)

#--1--Setting the dataset to manipulate (some options throughout the script change depending on chosen dataset)
# - uncomment one of these 4 following lines to choose a dataset
# cohort <- "Remagus02"
# cohort <- "Remagus04"
cohort <- "MDAnderson"
# cohort <-  "another_dataset_you_want_to_use"


#--3--Setting the dataset of entry  
# entry_data <- ex1 # a dataset with best probesets
entry_data <- ex1_bis_with_GS # the same dataset but with the gene symbol used instead 
the_samples_list = "MTUS1"
x<-entry_data[the_samples_list,]

# #--Test Data
# # example of data to use for test
# x=c(rnorm(100,0,0.5), rnorm(200,3,1))
# # plotting the two distributions of the test data
# y = c(rep(0,100), rep(1,200))
# densityplot(~x|as.factor(y), layout=c(1,2), n=200, width=1.5)
# # show a binomdal plot 
# densityplot(x, 200, width = 1.5) # xlab, lim, ylim options see hist in others scripts 

#--verifications
# NB : check if MTUS1 is present "MTUS1" %in% dimnames(x)[[1]] # should display TRUE



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

# for MDA use the following function in order to make sure we keep the intersection between the two means
# ##################Notes
# ####Another way to compute the threshold#######################
# # source : https://stackoverflow.com/questions/16982146/point-of-intersection-2-normal-curves
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



# draw the histogram
h <- hist(x, 100, col = "cornsilk1", freq = FALSE, 
          main = paste("Histogram of the intensities (", "Cohort : ", cohort, ", gene : ",the_samples_list,")", sep=""), 
          border = "antiquewhite4",
          xlab = paste("Intensities of the best probeset for the gene (", "threshold (red line) : ~",as.character(round(intersec_coord_x, digits = 3)),")", sep=""),
          xlim = c(min(x),max(x)))
lines(density(x),lwd=1.5,col="blue")
xs = seq(min(x), max(x), by=.01) # add the bimodal curve
lines(xs, Weight1*dnorm(xs, Mean1,SD1), lty=2,col = "darkgreen") # add the curve of mode 1
lines(xs, Weight2*dnorm(xs, Mean2,SD2), lty=2,col = "coral4") # add the curve of mode 2
# mach_threshold <- intersec_coord_x
abline(v = intersec_coord_x, col = "red", lwd = 2) # add the threshold line
###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# getting a report on the sample in common with Sylvie (rownames as samples names in accession, , MTUS1, Threshold, ATIP3_class_predicted)
# - make a short matrix of the restriction on MTUS1
x_thres_collector<-as.data.frame(t(entry_data)) # transpose x to put a new col later as the threshold of each rows ie each samples 
# NB: as transposing outputs a matrices that col cant be added to it easily, we coerce it into a df to be able to add a col to it later
x_thres_collector = x_thres_collector[c("MTUS1")]
x_thres_collector$Threshold_low_high <- intersec_coord_x # new threshold col with a placeholder to know if changed or not
x_thres_collector$ATIP3_class_predicted <- "NOT_CHANGED_YET" # predictions with gene threshold
x_thres_collector$ATIP3_class_predicted[which(x_thres_collector$MTUS1 < intersec_coord_x)]<-"low"
x_thres_collector$ATIP3_class_predicted[which(x_thres_collector$MTUS1 > intersec_coord_x)]<-"high"
count_class_low = sum(x_thres_collector$ATIP3_class_predicted == "low") # counts of the classes with gene threshold
count_class_high = sum(x_thres_collector$ATIP3_class_predicted == "high")
# reporting on results
paste(cohort," cohort gene threshold : ", intersec_coord_x, sep="")
paste(cohort," cohort MTUS1 classes count : ATIP3 low (", count_class_low, "), ATIP3 high (",count_class_high,")", sep="")
paste(cohort," cohort range MTUS1 is : ",range(x_thres_collector$MTUS1)[1] ," to ",range(x_thres_collector$MTUS1)[2], sep="")
# part for saving on file and reread anytime
outfilename = paste(cohort, "_threshold_of_MTUS1_gene_atip3_classes.csv", sep='')
write.csv(x_thres_collector, outfilename, row.names=T)
        
    

####>>>>>>>>>>> SCRIPT TO MAKE SAMPLES CORRESPONDS IN EACH COHORT <<<<<<<<### 
library(readxl) # for ability to read xlsx and xls files  

#--1-- load a table with classes predicted from thresholds
# path2file1 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/Remagus02_threshold_of_MTUS1_gene_atip3_classes.csv" # R02
# path2file1 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/Remagus04_threshold_of_MTUS1_gene_atip3_classes.csv" # R04
path2file1 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/MDAnderson_threshold_of_MTUS1_gene_atip3_classes.csv" # MDA
table1 <- read.csv(file = path2file1, header = TRUE)

#--2-- load a table with two types of samples names
# path2file2 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/atip3_material/Sample_Names_correspondance/R02 pour Amad.xlsx" # R02
path2file2 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/atip3_material/Sample_Names_correspondance/MDA_pour_moi.csv" # R02
# table2 <- read_excel(path2file2, sheet = 1) # R02
table2 <- read.csv(file = path2file2, header = TRUE) # MDA

# restrict the table to only needed cols
names(table2) # to see the cols to keep
# table2 = table2[c("!Sample_geo_accession","cletri")] # R02
table2 = table2[c("Accession","Title")] # MDA

#--3-- add old names table contents in the classes predicted table
# rename columns that are not in good name
names(table1)[1] <- "Sample_GEO_accession"
# table1_2_joined<-merge(x = table1, y = table2, by.x = "Sample_GEO_accession",by.y = "!Sample_geo_accession", all = TRUE) # R02
table1_2_joined<-merge(x = table1, y = table2, by.x = "Sample_GEO_accession",by.y = "Accession", all = TRUE) # MDA

#--4--add old classes to joined table of new names and old names
path2file3 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/3_results/res_clustering/Clustering pour Amad 180520.xls"
# table3 <- read_excel(path2file3, sheet = 1)  # R02
# table3 <- read_excel(path2file3, sheet = 2)  # R04
table3 <- read_excel(path2file3, sheet = 3)  # MDA
# resrict the table cols
names(table3) # to see the cols to keep
# names(table3) <- c("CLETRI_classes_by_Sylvie","letgo1","letgo1","letgo2","letgo3","letgo4","ATIP3_classes_by_Sylvie") # R02
names(table3) <- c("CLETRI_classes_by_Sylvie","letgo1","letgo1","letgo2","ATIP3_classes_by_Sylvie") # MDA
table3 = table3[c("CLETRI_classes_by_Sylvie","ATIP3_classes_by_Sylvie")]

#--5-- add olc classes in table with the classes predicted table
# table1_2_3_joined<-merge(x = table1_2_joined, y = table3, by.x = "cletri",by.y = "CLETRI_classes_by_Sylvie", all = TRUE) # R02
table1_2_3_joined<-merge(x = table1_2_joined, y = table3, by.x = "Title",by.y = "CLETRI_classes_by_Sylvie", all = TRUE) # MDA

#--6-- add columns to compare with sylvie ATIP3 low
# - add a col to compare with the median thres classes
table1_2_3_joined$Same_ATIP3_low_than_Sylvie <- "different_from_Sylvie_work"
table1_2_3_joined$Same_ATIP3_low_than_Sylvie[which((table1_2_3_joined$ATIP3_class_predicted == "low")&(table1_2_3_joined$ATIP3_classes_by_Sylvie == 1))]<-"low_as_in_Sylvie_work"
# make the count of the overlap
count_class_low_same_as_sylvie_work = sum(table1_2_3_joined$Same_ATIP3_low_than_Sylvie == "low_as_in_Sylvie_work") # counts of the classes with gene threshold
# reporting on results
paste(cohort," cohort MTUS1 classes count that are same as in sylvie's work : ", count_class_low_same_as_sylvie_work, sep="")
# sort the final table on the order of classes by sylvie and see what we have for the ATIP3 low samples in sylvie's work
table1_2_3_joined_sorted_on_sylvie_classes<-table1_2_3_joined[order(table1_2_3_joined$ATIP3_classes_by_Sylvie),]







# # a table of the the same ATIP3 samples using the median thres in comparison with Sylvie work
# table_coordance_med_thres_w_sylvie <- table1_2_3_joined[which(table1_2_3_joined$Same_ATIP3_low_than_Sylvie_w_med_thres == "low_as_in_Sylvie_work"),]
# # a table of the the same ATIP3 samples using the sample specific thres in comparison with Sylvie work
# table_coordance_sample_thres_w_sylvie <- table1_2_3_joined[which(table1_2_3_joined$Same_ATIP3_low_than_Sylvie_w_sample_thres == "low_as_in_Sylvie_work"),]


# Results summarized : 
# - using the median of the sample specific threshold : 0 out of 25 ATIP3 low of Sylvie's work captured
# - using the sample specific thresholds : 0 out of 25 ATIP3 low of Sylvie's work captured


####>>>>>>>>>>>>>>>>>>>>>>>>Notes
# # use these lines to check for the presence of a sample
# "11004" %in% table1_2_joined$cletri
# "11004" %in% table3$CLETRI_classes_by_Sylvie
# table3_low_only <-table3[which(table3$ATIP3_classes_by_Sylvie == 1),]
# table1_2_3_joined_low_only <-table1_2_3_joined[which(table1_2_3_joined$ATIP3_classes_by_Sylvie == 1),]












