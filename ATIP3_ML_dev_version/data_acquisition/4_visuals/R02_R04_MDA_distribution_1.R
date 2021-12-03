####>>>>>>>>>>> SCRIPT TO SEE THE DISTRIBUTION OF PROBESETS ON INITIALS COHORTS FILES <<<<<<<<### 
# source : https://jcoliver.github.io/learn-r/008-ggplot-dendrograms-and-heatmaps.html

# #--1--Clean up the environment (optional)
# rm(list = ls()) # 

# #--2--Creating two folders we’ll use to organize our efforts
# # in order to control where these folders will be created, set the working directory first (cmd line or in Rstudio options do "Session > Set working directory")
# dir.create("data")
# dir.create("output")
# 
# #--2--Load needed librairies
# library("ggplot2")
# library("ggdendro")
# library("reshape2")
# library("grid")
# library("ape")

#--3--Setting the dataset to manipulate (some options throughout the script change depending on chosen dataset)
# - uncomment one of these 4 following lines to choose a dataset
cohort <- "Remagus02"
# cohort <- "Remagus04"
# cohort <- "MDAnderson"
# cohort <-  "another_dataset_you_want_to_use"
# - store the path of the dataset
if (cohort=="Remagus02") {
  path2file = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/atip3_material/datasets_to_process_folder/R02/BRCA_Treatment11_REMAGUS02xNACx226Sx54675Fx4RasRCH3HSall_GEX.csv" # for R02
} else if (cohort=="Remagus04") {
  path2file = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/atip3_material/datasets_to_process_folder/R04/BRCA_Treatment12_REMAGUS04xNACx142Sx22277Fx4RasRCH3HSall_GEX.csv" # for R04
} else if (cohort=="MDAnderson") {
  path2file = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/atip3_material/datasets_to_process_folder/MDA/BRCA_Treatment13_MDAndersonxNACx133Sx22283Fx4RasRCH3HSall_GEX.csv" # for MDA
} else
  print("Replace this statement with a command to store the path of another_dataset_you_want_to_use")

#--4--Data preparation
# - make a dataframe from dataset# 
otter <- read.csv(file = path2file, header = TRUE)


otter1 = otter[1,5:22281]
x=t(otter1)

h <- hist(x, 100, col = "cornsilk1", freq = FALSE, 
          main = paste("Histogram of the intensities of the cohort : ", cohort, sep=""), 
          border = "antiquewhite4",
          xlab = paste("Intensities of the probesets", sep=""),
          xlim = c(min(x),max(x)))

