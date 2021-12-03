#=================================get a list of the probes that HKPs by dataset

# load necessary librairies

#--1--Setting the dataset to manipulate (some options throughout the script change depending on chosen dataset)
# - uncomment one of these 4 following lines to choose a dataset
cohort <- "Remagus02"
# cohort <- "Remagus04"
# cohort <- "MDAnderson"
# cohort <-  "another_dataset_you_want_to_use"

#--3--Setting the dataset of entry  
# entry_data <- ex1 # a dataset with best probesets
x <- ex1_bis_with_GS # the same dataset but with the gene symbol used instead 

#====> criteria of HKGs
# 1-the intensity of the gene must be greater than 
# the median intensity of all the genes for the sample, 
# and that must be the case in each of the samples

# 2- the coefficient of variance (CV, standard deviation/average) of the gene 
# across samples must be less than 0.35.

# make a collector of results
x_res_collector<-as.data.frame(x)
# add a new col for criteria of high enough for housekeeping
x_res_collector$HK_status_criteria1 <- "NOT_CHANGED_YET"
# reduce it to only the results cols
x_res_collector <- x_res_collector[c("HK_status_criteria1")]

# make a df with median intensifies of the all the genes sample by sample
x_median_intensities_all_genes_by_sample<-as.data.frame(t(x))
x_median_intensities_all_genes_by_sample$Median_all_genes_for_sample = apply(x_median_intensities_all_genes_by_sample, 1, FUN=function(x){median(x, na.rm=T)})
x_median_intensities_all_genes_by_sample <- x_median_intensities_all_genes_by_sample[c("Median_all_genes_for_sample")]


# get the list of genes to loop on
the_genes_list <-dimnames(x)[[1]]
# get the list of samples to check if first part of criteria 1 is true for them
the_samples_list <-dimnames(x)[[2]]
# the number of samples equals to the number of times first part of criteria 1 has to be true
len_cohort_samples = length(the_samples_list)
# len_variables = length(the_genes_list) # not needed # just for checking in
# loop on the genes and compute if criteria 1 is YES or NO
for (a_gene_as_rowname in the_genes_list) {   # to test a_gene_as_rowname = the_genes_list[1] and a_sample_as_colname = the_samples_list[1]
  # count of the gene, the number of samples that have a value higher than the median of all genes
  counter_of_samples_w_val_of_gene_sup_median_genes = 0
  for (a_sample_as_colname in the_samples_list) {
    if (x[a_gene_as_rowname,a_sample_as_colname] > x_median_intensities_all_genes_by_sample[a_sample_as_colname,"Median_all_genes_for_sample"]){
      counter_of_samples_w_val_of_gene_sup_median_genes = counter_of_samples_w_val_of_gene_sup_median_genes + 1
    }
  }
  # set the criteria 1 value if YES for all samples are superior to the median of all genes
  if (counter_of_samples_w_val_of_gene_sup_median_genes == len_cohort_samples) {
    x_res_collector$HK_status_criteria1[which(row.names(x_res_collector) == a_gene_as_rowname)]<-"YES"
    # x_res_collector[a_gene_as_rowname,"HK_status_criteria1"] = "YES"
  }else {
    x_res_collector$HK_status_criteria1[which(row.names(x_res_collector) == a_gene_as_rowname)]<-"NO"
    # x_res_collector[a_gene_as_rowname,"HK_status_criteria1"] = "NO"
  }
}

