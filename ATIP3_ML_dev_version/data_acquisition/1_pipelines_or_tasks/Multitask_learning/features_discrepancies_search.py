# This script is to go from two datasets and finding if there are some the discrepancies they have in features (some fts exist in this dt and not the others)

# In our initial search, 7 datasets have been found for the multitask
# - 5 of them have 12153 (12151 fts+ 1 col resp+ 1 col cohort) (group A)
# - 1 of them have 19421 (12419 fts+ 1 col resp+ 1 col cohort) (group B1)
# - 5 of them have 12419 (12417 fts+ 1 col resp+ 1 col cohort) (group B2)

# The platform for froup 1 is Affy U133 PLus 2.0 (GPL 570)
# The platform for group B1 and B2 is Affy U133 A (GPL571 for the U133A 2.0 and GPL96 for the U133A)

# the same platforms should not be used and finish with a difference in gene symbols observed
# so we at least try to understand what are the genes that miss from one dataset and are in the other dataset, although both dataset are formed using the same platform
# df_file2 is the dataset with gene symbols of the best probeset that comes from GSE26639
# df_file3 is the dataset with gene symbols of the best probeset that comes from GSE32646

gse266_list_col = list(df_file2.columns) # a list of 19421 elts
gse326_list_col = list(df_file3.columns) # a list of 19419 elts
inter266_326 = list(set(gse266_list_col) & set(gse326_list_col)) # a list of 19419 elts
add_values_in_326 = (set(gse326_list_col).difference(gse266_list_col)) # a set of 0 elts
add_values_in_266 = (set(gse266_list_col).difference(gse326_list_col)) # a set of 2 elts : "GAPDH", "ACTB"