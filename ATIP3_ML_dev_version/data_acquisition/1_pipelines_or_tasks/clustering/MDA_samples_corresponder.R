####>>>>>>>>>>> SCRIPT TO MAKE SAMPLES CORRESPONDS IN EACH COHORT <<<<<<<<### 
library(readxl) # for ability to read xlsx and xls files

#--1-- load a table with classes predicted from thresholds
path2file1 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/MDAnderson_threshold_atip3_classes.csv"
table1 <- read.csv(file = path2file1, header = TRUE)


# source ofcorresponding names : https://www.ncbi.nlm.nih.gov/geo/browse/?view=samples&series=25066



#--2-- load a table with two types of samples names
path2file2 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/heatmaps_correction/MDA_pour_moi.csv"

table2 <- read.csv(file = path2file2, header = TRUE, stringsAsFactors = FALSE)
# restrict the table to only needed cols
names(table2) # to see the cols to keep
table2 = table2[c("Accession","Title")]

#--3-- add old names table contents in the classes predicted table
# rename columns that are not in good name
names(table1)[1] <- "Sample_GEO_accession"
table1_2_joined<-merge(x = table1, y = table2, by.x = "Sample_GEO_accession",by.y = "Accession", all = TRUE)
# sort the joined table on the Title column to find easily locate the PERU sample and deal with the changes due to update mix up infiles given at start of the project ATIP3
table1_2_joined<-table1_2_joined[order(table1_2_joined$Title),]
# NB : the case of the PERU samples 
# They are six : two that are confusing PERU12_14 and PERU14_16 (from the GEO title) are named PERU14 and PERU16 in Sylvie_work
# so we modifiy them before going forward
table1_2_joined$Title[which(table1_2_joined$Title == "PERU12_14")]<-"PERU14" # same as in table1_2_joined["309",7]<-"PERU14" but without having to check for the line number
table1_2_joined$Title[which(table1_2_joined$Title == "PERU14_16")]<-"PERU16"

  
  
#--4--add old classes to joined table of new names and old names
path2file3 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/heatmaps_correction/Clustering\ pour\ Amad\ 180520.xls"
table3 <- read_excel(path2file3, sheet = 3) 
# resrict the table cols
names(table3) # to see the cols to keep
names(table3) <- c("CLETRI_classes_by_Sylvie","letgo1","letgo2","letgo3","ATIP3_classes_by_Sylvie")
table3 = table3[c("CLETRI_classes_by_Sylvie","ATIP3_classes_by_Sylvie")]

#--5-- add olc classes in table with the classes predicted table
table1_2_3_joined<-merge(x = table1_2_joined, y = table3, by.x = "Title",by.y = "CLETRI_classes_by_Sylvie", all = TRUE)

#--6-- add columns to compare with sylvie ATIP3 low
# - add a col to compare with the median thres classes
table1_2_3_joined$Same_ATIP3_low_than_Sylvie_w_med_thres <- "different_from_Sylvie_work"
table1_2_3_joined$Same_ATIP3_low_than_Sylvie_w_med_thres[which((table1_2_3_joined$ATIP3_class_predicted_w_med_thres == "low")&(table1_2_3_joined$ATIP3_classes_by_Sylvie == 1))]<-"low_as_in_Sylvie_work"
# table1_2_3_joined$Same_ATIP3_low_than_Sylvie_w_med_thres[which(!((table1_2_3_joined$ATIP3_class_predicted_w_med_thres == "low")&(table1_2_3_joined$ATIP3_classes_by_Sylvie == 1)))]<-"different_from_Sylvie_work" # not needed
# -add a col to compare with the sample specific thres classes
table1_2_3_joined$Same_ATIP3_low_than_Sylvie_w_sample_thres <- "different_from_Sylvie_work"
table1_2_3_joined$Same_ATIP3_low_than_Sylvie_w_sample_thres[which((table1_2_3_joined$ATIP3_class_predicted_w_sample_thres == "low")&(table1_2_3_joined$ATIP3_classes_by_Sylvie == 1))]<-"low_as_in_Sylvie_work"
# table1_2_3_joined$Same_ATIP3_low_than_Sylvie_w_sample_thres[which(!((table1_2_3_joined$ATIP3_class_predicted_w_sample_thres == "low")&(table1_2_3_joined$ATIP3_classes_by_Sylvie == 1)))]<-"different_from_Sylvie_work" # not needed
# sort the final table on the order of classes by sylvie and see what we have for the ATIP3 low samples in sylvie's work
table1_2_3_joined_sorted_on_sylvie_classes<-table1_2_3_joined[order(table1_2_3_joined$ATIP3_classes_by_Sylvie),]


# a table of the the same ATIP3 samples using the median thres in comparison with Sylvie work
table_coordance_med_thres_w_sylvie <- table1_2_3_joined[which(table1_2_3_joined$Same_ATIP3_low_than_Sylvie_w_med_thres == "low_as_in_Sylvie_work"),]
# a table of the the same ATIP3 samples using the sample specific thres in comparison with Sylvie work
table_coordance_sample_thres_w_sylvie <- table1_2_3_joined[which(table1_2_3_joined$Same_ATIP3_low_than_Sylvie_w_sample_thres == "low_as_in_Sylvie_work"),]

# Results summarized : 
# - using the median of the sample specific threshold : 10 out of 40 ATIP3 low of Sylvie's work 
# - using the sample specific thresholds :12 out of 40 ATIP3 low of Sylvie's work captured



####>>>>>>>>>>>>>>>>>>>>>>>>Notes
# # use these lines to check for the presence of a sample
# "11004" %in% table1_2_joined$cletri
# "11004" %in% table3$CLETRI_classes_by_Sylvie
# table3_low_only <-table3[which(table3$ATIP3_classes_by_Sylvie == 1),]
# table1_2_3_joined_low_only <-table1_2_3_joined[which(table1_2_3_joined$ATIP3_classes_by_Sylvie == 1),]
