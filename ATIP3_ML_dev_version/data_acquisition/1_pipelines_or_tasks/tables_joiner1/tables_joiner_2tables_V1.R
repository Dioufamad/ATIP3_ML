# this script is designed to join 2 tables in this fashion : 
# - table 1 has a col C1 to supply with info contained in a specific col in multiples others files

# the idea is : 
# step 1 : get a formatted and good version of table 1 ready to accpt the info
# step 2 : loop on the filepaths from one folder and for each file path, get a table,limit the table to index col at right and the col info to add, and make a join, make new table 1 as the result
# NB 1 : necessary checks
# - check 1 : after obtaining table 1, say if table 1 col used as index for join has duplicates and if their is a duplicate, display its values in the col to supply with info
# - check 2 : after obtaining each table 2, add it to a vertical join of all tables 2 and then go through the final table 2 to make the same check as previous 
# (the final table 2 has to have a col origin file with the name of origin file that is also to be displayed in case of duplicates in the right index col



# this script is designed to join 
# - the FSs overlaps table (df_ol)
# - the genes classes from cohort data table (df_gc_c)
# - the genes classes from a library table (df_gc_l)
# - the SIGs status table (df_sig)
# NB : df_gc_c and df_gc_l can be joined into a consensus table when data is in accordance (result_table is df_gc)

# ---Case 1 : all the unique features observed across the the 6 single-task models and 1 multi-task model (7 models)
# - join the presence/absence cols and the SIGs tables on all 7 models
df_ol<-upsetplot_building_matrix
colref_ol <- "Unique features across all initial sets"
df_sig <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3_Same_Sign_Always_Yes_allafscascritA
colref_sig <- "Features"
df3 <- merge(x = df1, y = df2, by.x = colref1, by.y = colref2)
# a new figure for intersection...  