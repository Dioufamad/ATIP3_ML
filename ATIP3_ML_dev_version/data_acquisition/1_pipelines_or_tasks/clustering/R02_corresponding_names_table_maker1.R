
####>>>>>>>>>>> SCRIPT TO MAKE SAMPLES CORRESPONDS IN EACH COHORT <<<<<<<<### 
library(readxl) # for ability to read xlsx and xls files  

#--1-- load a table with classes predicted from thresholds
# path2file1 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/Remagus02_threshold_of_MTUS1_gene_atip3_classes.csv" # R02
# path2file1 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/Remagus04_threshold_of_MTUS1_gene_atip3_classes.csv" # R04
path2file1 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/MDAnderson_threshold_of_MTUS1_gene_atip3_classes.csv" # MDA
table1 <- read.csv(file = path2file1, header = TRUE)

#--2-- load a table with two types of samples names
path2file2 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/atip3_material/Sample_Names_correspondance/R02 pour Amad.xlsx" # R02
# path2file2 = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/atip3_material/Sample_Names_correspondance/MDA_pour_moi.csv" # R02
# table2 <- read_excel(path2file2, sheet = 1) # R02
table2 <- read.csv(file = path2file2, header = TRUE) # MDA

# restrict the table to only needed cols
names(table2) # to see the cols to keep
# table2 = table2[c("!Sample_geo_accession","cletri")] # R02
table2 = table2[c("Accession","Title")] # MDA
# NB : the case of the PERU samples 
# They are six : two that are confusing PERU12_14 and PERU14_16 (from the GEO title) are named PERU14 and PERU16 in Sylvie_work
# so we modifiy them before going forward
table2$Title[which(table2$Title == "PERU12_14")]<-"PERU14" # same as in table1_2_joined["309",7]<-"PERU14" but without having to check for the line number
table2$Title[which(table2$Title == "PERU14_16")]<-"PERU16"

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#--3-- add old names table contents in the classes predicted table
# rename columns that are not in good name
names(table1)[1] <- "Sample_GEO_accession"
# table1_2_joined<-merge(x = table1, y = table2, by.x = "Sample_GEO_accession",by.y = "!Sample_geo_accession", all = TRUE) # R02
table1_2_joined<-merge(x = table1, y = table2, by.x = "Sample_GEO_accession",by.y = "Accession", all = TRUE) # MDA
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


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
# table2_3_joined<-merge(x = table2, y = table3, by.x = "cletri",by.y = "CLETRI_classes_by_Sylvie", all = TRUE) # R02
table2_3_joined<-merge(x = table2, y = table3, by.x = "Title",by.y = "CLETRI_classes_by_Sylvie", all = TRUE) # MDA
# sort the final table on the order of classes by sylvie and see what we have for the ATIP3 low samples in sylvie's work
table2_3_joined_sorted_on_sylvie_classes<-table2_3_joined[order(table2_3_joined$ATIP3_classes_by_Sylvie),]
count_class_low_for_sylvie_work = sum(table3$ATIP3_classes_by_Sylvie == 1)
