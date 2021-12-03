# ----- This is a script for all the pieces of code not needed but that might come in handy another day


# the tests code for the pipe when summing together multiples dataframes
my_matrix2 = my_matrix
rownames(my_matrix2) <- my_matrix2[,1]
my_matrix2[,1] <- NULL

df1 = my_matrix2[1:10,]
df2 = my_matrix2[1:5,]
df3 = my_matrix2[1,]

# add rownames as a column in each data.frame and bind rows
my_matrix3of3 <- bind_rows(df1 %>% add_rownames(), 
                           df2 %>% add_rownames(), 
                           df3 %>% add_rownames()) %>% 
  # evaluate following calls for each value in the rowname column
  group_by(rowname) %>% 
  # add all non-grouping variables
  summarise_all(sum)

# add rownames as a column in each data.frame and bind rows
bind_rows(df1 %>% add_rownames(), 
          df2 %>% add_rownames()) %>% 
  # evaluate following calls for each value in the rowname column
  group_by(rowname) %>% 
  # add all non-grouping variables
  summarise_all(sum)

# code snippets for launching non all 7 FSs
# -- unifying 3 FSs
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs <- bind_rows(list_fs_tables_retrieved_RAW_marks_only_and_pruned[[1]] %>% add_rownames(), 
                                                                 list_fs_tables_retrieved_RAW_marks_only_and_pruned[[2]] %>% add_rownames(),
                                                                 list_fs_tables_retrieved_RAW_marks_only_and_pruned[[3]] %>% add_rownames()) %>% 
  # evaluate following calls for each value in the rowname column
  group_by(rowname) %>% 
  # add all non-grouping variables
  summarise_all(sum)



# # à utiliser un jour pour isoler les gènes par multiplicité
# a= c()
# b=c()
# for (a_correct_ft_name in list_fts_unik_in_fs_table) {
#   if(length(which(list_fts_all_in_fs_table_as_correct_names == a_correct_ft_name)) ==6){
#     a <-c(a,a_correct_ft_name)
#   }else{
#     b<-c(b,a_correct_ft_name)
#   }
# }


# ---------data cleaning checks in gse41998 (to be redone in a clean way)
# myFtDesired
# [1] "Gene Symbol"    "ENTREZ_GENE_ID"
# >   # 2) changing the names
#   >   dictionary = gset@featureData@data[, c('ID', myFtDesired)]  #This is a lookup table for probe ID and ORF 
# > View(dictionary)
# > dictT = dictionary2[which(grepl("T", dictionary$"Gene Symbol", fixed=TRUE)),] 
# > View(dictT)
# > dictT1 = dictT[which(dictT$"Gene Symbol" = "T"),]
# Error: unexpected '=' in "dictT1 = dictT[which(dictT$"Gene Symbol" ="
# > dictT1 = dictT[which(dictT$"Gene Symbol" == "T"),]
# > View(dictT1)
# >   # - getting the best probes
#   >   # - - make sure that correct entrez_gene_id entries only stays in table
#   >   dictionary1 = dictionary
# >   list_egi_uniks_in_dict1 = unique(as.character(dictionary1$ENTREZ_GENE_ID))
# >   list_egi_uniks_in_dict1_no_nan <- na.omit(list_egi_uniks_in_dict1) #remove nan
# >   list_egi_uniks_no_nanNunknown = list_egi_uniks_in_dict1_no_nan[list_egi_uniks_in_dict1_no_nan != ""] # remove "" (unknown feature data for probe)
# >   # dictionary1_done = dictionary1[match(list_egi_uniks_no_nanNunknown, dictionary1$ENTREZ_GENE_ID), ] #xxx bad due to eliminating duplicates too early on
#   >   dictionary1_done = dictionary1[which(dictionary1$ENTREZ_GENE_ID %in% list_egi_uniks_no_nanNunknown),]
# > a = dictionary1$"Gene Symbol"
# > b = dictionary1_done$"Gene Symbol"
# > c = a - b
# Error in a - b : non-numeric argument to binary operator
# > c = setdiff(a, b)
# > c
# > dictionary1_done_absent = dictionary1[which(dictionary1$`Gene Symbol` %in% c),]
# > View(dictionary1_done_absent)
# >   # test presence of ATIP3 probes : c_dict1 = dictionary1_done_bis[which(dictionary1_done_bis$"ID" %in% c("212093_s_at","212095_s_at","212096_s_at","239576_at")),]
#   >   # - - make sure that correct gene_symbol entries only stays in table
#   >   dictionary2 = dictionary1_done
# >   list_gs_uniks_in_dict2 = unique(as.character(dictionary2$"Gene Symbol"))
# >   list_gs_uniks_in_dict2_no_nan <- na.omit(list_gs_uniks_in_dict2) #remove nan
# >   list_gs_uniks_no_nanNunknown = list_gs_uniks_in_dict2_no_nan[list_gs_uniks_in_dict2_no_nan != ""] # remove "" (unknown feature data for probe)
# >   # dictionary2_done = dictionary2[match(list_gs_uniks_no_nanNunknown, dictionary2$"Gene Symbol"), ] #xxx bad due to eliminating duplicates too early on
#   >   dictionary2_done = dictionary2[which(dictionary2$"Gene Symbol" %in% list_gs_uniks_no_nanNunknown),]


# 
# for (i in list_fts_unik_in_fs_table_raw_nnc_only_marks_only){
#   if ()
# }

# 
# 
# # -- version 2 (include booleans to mark the signs of the majority coefs counted) and does not depend on the counts of type of FS found (the same marks are used always)
# # ---  these are to mark the quality of the majority sign among the counted coefs
# for_type_alg_1_value_bool_yes = 1
# for_type_alg_1_value_bool_no = 0
# for_type_alg_2_value_bool_yes = 0.1 
# for_type_alg_2_value_bool_no = 0
# # ---  these are to keep what was the majority sign among the counted coefs
# for_type_alg_1_value_bool_yes_for_maj_with_sign_neg = 10
# for_type_alg_1_value_bool_no_for_maj_with_sign_neg = 0
# for_type_alg_1_value_bool_yes_for_maj_with_sign_pos = 1
# for_type_alg_1_value_bool_no_for_maj_with_sign_pos = 0
# 
# for_type_alg_2_value_bool_yes_for_maj_with_sign_neg = 0.1
# for_type_alg_2_value_bool_no_for_maj_with_sign_neg = 0
# for_type_alg_2_value_bool_yes_for_maj_with_sign_pos = 0.01
# for_type_alg_2_value_bool_no_for_maj_with_sign_pos = 0
# 
# # old 
# #...add to the version of the table to modify the columns that will be supplied with values
# fs_table_raw_nnc_only$space_init_Min = NA
# fs_table_raw_nnc_only$space_init_Max = NA
# fs_table_raw_nnc_only$space_init_LB = NA
# fs_table_raw_nnc_only$space_init_HB = NA
# fs_table_raw_nnc_only$space_init_Num_outliers = NA
# fs_table_raw_nnc_only$space_fin_Size = NA
# fs_table_raw_nnc_only$space_fin_Num_zeros = NA
# fs_table_raw_nnc_only$space_fin_Num_signs = NA
# fs_table_raw_nnc_only$space_fin_Num_pos = NA
# fs_table_raw_nnc_only$space_fin_Num_neg = NA
# fs_table_raw_nnc_only$crit_A1 = NA
# fs_table_raw_nnc_only$crit_Q1 = NA
# fs_table_raw_nnc_only$crit_M1 = NA
# fs_table_raw_nnc_only$crit_F1 = NA
# fs_table_raw_nnc_only$crit_S1 = NA
# fs_table_raw_nnc_only$crit_A2 = NA
# fs_table_raw_nnc_only$crit_Q2 = NA
# fs_table_raw_nnc_only$crit_M2 = NA
# fs_table_raw_nnc_only$crit_F2 = NA
# fs_table_raw_nnc_only$crit_S2 = NA
# # new
# 
# 
# #################### old ending
# 
# # (decision 1) : the table with only the genes where we have the count wether the final space has zeros or not 
# # ... we just have to focus on the cols A to T of the table fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2
# paste("- For Decision 1, # remaining fts is ",dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2)[1],sep='')
# 
# # - (choice 1): the table with only the genes whose count of sign in majority is more than the median of range 0-# signs (ie lowest level of stringency on final space of coefs)
# fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_c1 <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_M > 0.0),] 
# paste("- For choice 1, # remaining fts is ",dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_c1)[1],sep='')
# 
# # - (choice 2): the table with only the genes whose count of sign in majority is more or equal to the 3rd quartile (Q3) of range 0-# signs (ie mid level of stringency on final space of coefs)
# fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_c2 <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_Q > 0.0),] 
# paste("- For choice 2, # remaining fts is ",dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_c2)[1],sep='')
# 
# # - (choice 3): the table with only the genes whose count of sign in majority equal to the # of signs (ie highest level of stringency on final space of coefs)
# fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_c3 <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_A > 0.0),] 
# paste("- For choice 3, # remaining fts is ",dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_c3)[1],sep='')
# 
# # - (Tables SameSignAlways and NotSameSignAlways) : the table with the genes that always have the same sign for the coefs (and the table holding the rest)
# list_fts_SameSignAlways_in_table_V2 = c()
# list_fts_NotSameSignAlways_in_table_V2 = c()
# list_fts_in_table_V2 = unique(as.character(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$Features))
# for (a_ft_in_table_V2 in list_fts_in_table_V2){ # for test use a_ft_in_table_V2 = list_fts_in_table_V2[3]
#   # for the ft, lets get S (value crit_S) and its components as letters in S = AB,CD
#   val_S = fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_S[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$Features == a_ft_in_table_V2)]
#   val_A = floor(val_S/10) # got one
#   val_AB = floor(val_S)
#   val_B = val_AB - (val_A*10) # got one
#   val_ABC = floor(val_S*10)
#   val_C = val_ABC - (val_AB*10) # got one
#   val_ABCD = floor(val_S*100)
#   val_D = val_ABCD - (val_ABC*10) # got one
#   # paste("- in succession, here are S,A,B,C,D : ",val_S,val_A,val_B,val_C,val_D,sep=' - ') # to test
#   # for the ft, lets get the value of the total negatives in the form of (crit_T - crit_F)
#   val_all_neg_in_form_TminusF = val_A + (val_C/10)
#   va__all_pos_in_form_TminusF = val_B + (val_D/10)
#   # for the ft, lets get the value of TminusF = (crit_T - crit_F)
#   val_T = fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_T[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$Features == a_ft_in_table_V2)]
#   val_F = fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$crit_F[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$Features == a_ft_in_table_V2)]
#   val_TminusF = val_T - val_F
#   # for the ft, lets see if all the signs of its used Nmaj are the same and if so lets add it to a list 
#   if ((val_TminusF==val_all_neg_in_form_TminusF)|(val_TminusF==va__all_pos_in_form_TminusF)){
#     list_fts_SameSignAlways_in_table_V2 = c(list_fts_SameSignAlways_in_table_V2,a_ft_in_table_V2)
#   }else{
#     list_fts_NotSameSignAlways_in_table_V2 = c(list_fts_NotSameSignAlways_in_table_V2,a_ft_in_table_V2)
#   }
# }
# # the table SameSignAlways_in_table_V2
# fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$Features %in% list_fts_SameSignAlways_in_table_V2), ]
# paste("- For table SameSignAlways , # remaining fts is ",dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways)[1],sep='')
# # the table NotSameSignAlways_in_table_V2
# fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_NotSameSignAlways <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2$Features %in% list_fts_NotSameSignAlways_in_table_V2), ]
# paste("- For table NotSameSignAlways , # remaining fts is ",dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_NotSameSignAlways)[1],sep='')
# 
# ##! review the following    
# 
# # - (Tables SameSignAlways_allTminusFareA, SameSignAlways_allTminusFareQ, SameSignAlways_allTminusFareM)
# list_fts_SameSignAlways_allTminusFareA_in_table_V2 = c()
# list_fts_SameSignAlways_allTminusFareQ_in_table_V2 = c()
# list_fts_SameSignAlways_allTminusFareM_in_table_V2 = c()
# list_fts_in_table_V2_SameSignAlways = unique(as.character(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways$Features))
# for (a_ft_in_table_V2_SameSignAlways in list_fts_in_table_V2_SameSignAlways){ # for test use a_ft_in_table_V2 = list_fts_in_table_V2[3]
#   # for the ft, lets get the value of TminusF = (crit_T - crit_F)
#   val_T_V2_SameSignAlways = fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways$crit_T[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways$Features == a_ft_in_table_V2_SameSignAlways)]
#   val_F_V2_SameSignAlways = fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways$crit_F[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways$Features == a_ft_in_table_V2_SameSignAlways)]
#   val_TminusF_V2_SameSignAlways = val_T_V2_SameSignAlways - val_F_V2_SameSignAlways
#   # for the ft, lets see if its value TminusF is equal to crit_A, critQ or crit_M
#   val_A_V2_SameSignAlways = fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways$crit_A[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways$Features == a_ft_in_table_V2_SameSignAlways)]
#   val_Q_V2_SameSignAlways = fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways$crit_Q[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways$Features == a_ft_in_table_V2_SameSignAlways)]
#   val_M_V2_SameSignAlways = fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways$crit_M[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways$Features == a_ft_in_table_V2_SameSignAlways)]
#   if (val_TminusF_V2_SameSignAlways ==  val_A_V2_SameSignAlways){
#     list_fts_SameSignAlways_allTminusFareA_in_table_V2 = c(list_fts_SameSignAlways_allTminusFareA_in_table_V2,a_ft_in_table_V2_SameSignAlways)
#   }
#   if (val_TminusF_V2_SameSignAlways == val_Q_V2_SameSignAlways){
#     list_fts_SameSignAlways_allTminusFareQ_in_table_V2 = c(list_fts_SameSignAlways_allTminusFareQ_in_table_V2,a_ft_in_table_V2_SameSignAlways)
#   }
#   if (val_TminusF_V2_SameSignAlways == val_M_V2_SameSignAlway){
#     list_fts_SameSignAlways_allTminusFareM_in_table_V2 = c(list_fts_SameSignAlways_allTminusFareM_in_table_V2,a_ft_in_table_V2_SameSignAlways)
#   }
# }
# 
# # the table SameSignAlways_allTminusFareA
# fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways_allTminusFareA <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways$Features %in% list_fts_SameSignAlways_allTminusFareA_in_table_V2), ]
# paste("- For table SameSignAlways_allTminusFareA , # remaining fts is ",dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways_allTminusFareA)[1],sep='')
# # the table SameSignAlways_allTminusFareQ
# fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways_allTminusFareQ <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways$Features %in% list_fts_SameSignAlways_allTminusFareQ_in_table_V2), ]
# paste("- For table SameSignAlways_allTminusFareQ , # remaining fts is ",dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways_allTminusFareQ)[1],sep='')
# # the table SameSignAlways_allTminusFareM
# fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways_allTminusFareM <- fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways[which(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways$Features %in% list_fts_SameSignAlways_allTminusFareM_in_table_V2), ]
# paste("- For table SameSignAlways_allTminusFareM , # remaining fts is ",dim(fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V2_SameSignAlways_allTminusFareM)[1],sep='')
# 


fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Same_Sign_Always_Yes_Pos <- "_NOT_CHANGED_YET"
fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs_V3$Same_Sign_Always_Yes_Neg <- "_NOT_CHANGED_YET"

list_fts_Same_Sign_Always_Yes_Pos = c()
list_fts_Same_Sign_Always_Yes_Neg = c()


for (index_of_an_alg in c(1:length(list_tag_alg))) { # for test use index_of_an_alg = 1
  writeLines(paste("- FS ",index_of_an_alg,"...", sep=''))
}


# >>>>>>>>>> supply the colname where the selected features will be in each file
official_colname_of_selected_features_col = "Features"

# >>>>>>>>>>>> the ideas of scores
# we have a table with these cols to inform : 
# + m_0_st_seen, m_pos_st_seen, m_neg_st_seen, st_fs_where_seen,mt_cp_found, s_st_fs_ x i fs, s_mt_cp_ x i cp, s_all (initialized with 0)
# we loop on the FSs : 
# for each FSs, we loop on the genes : 
# - for each gene, 
# + we get m_0_st_fs, m_pos_st_fs, m_neg_st_fs
# + we compute s_st_dt with the 3 fs values
# + we update these cols with them : m_0_st_seen, m_pos_st_seen, m_neg_st_seen
# + we update this cols : s_st_fs_ x i fs with i corresp to the fs being analysed if st fs (or s_mt_cp_ x i cp with i corresp to the cp being analysed if mt fs)
# + we update fs_seen with + 1
# all the FSs have been gone through and all the table cols are supplied with values
# we make each time a paragraph to compute one of the final rules : the result is a table from the inital table that has only the genes answering to the restriction 



"GSE41998_x_GSE26639_x_GSE32646_x_GSE25055_x_GSE20194_x_GSE63471"

list_tag_numcohort
list_tag_alg <- c(list_tag_alg,tag_alg7)

list_tag_alg <- c(list_tag_alg,tag_alg1)

list_fts_all_in_fs_table_as_correct_names <- c()
for (index_a_MT_ft_name in c(1:length(list_fts_unik_in_fs_table_raw_nnc_only_marks_only))){
  a_MT_ft_name = list_fts_unik_in_fs_table_raw_nnc_only_marks_only[index_a_MT_ft_name]
  pieces_of_ftname_as_MT_name <- strsplit(a_MT_ft_name, "_in_")[[1]] # NB : if the sep is not found, a vector of only the entire word is kept so getting the 1st elt gives it also
  ftname_as_correct_initial_name <-pieces_of_ftname_as_MT_name[1]
  list_fts_all_in_fs_table_as_correct_names <- c(list_fts_all_in_fs_table_as_correct_names,ftname_as_correct_initial_name)
}
list_fts_all_in_fs_table_as_correct_names_uniks = unique(list_fts_all_in_fs_table_as_correct_names)


# Create a function to print squares of numbers in sequence.
new.function <- function(a) {
  for(i in 1:a) {
    b <- i^2
    print(b)
  }
}

# Call the function new.function supplying 6 as an argument.
new.function(6)


# Create a function with arguments.
new.function <- function(a,b,c) {
  result <- a * b + c
  #print(result)
}

# Call the function by position of arguments.
new.function(5,3,11)
a = new.function(5,3,11)
a
# Call the function by names of the arguments.
new.function(a = 11, b = 5, c = 3)

# Create a function to define score s.
score_s <- function(m_0,m_pos,m_neg) { 
  m = m_0 + m_pos + m_neg
  if ((m_0 >= (m-1)) | (m_pos == m_neg)) {
    result = 0
  }else{
    if (m_pos > m_neg) {
      result = 1*(m_pos/(m_pos+m_neg))
    }else if (m_neg > m_pos) {
      result = -1*(m_neg/(m_pos+m_neg))
    }
  }
  # result
  return(result)
}
# for tests   
score_s(1,7,2)
score_s(1,2,7)
score_s(9,0,1)
score_s(2,4,4)
score_s(10,0,0)


tag_numcohort_corresp_2_fs_retrieved

suffixes_of_multiples_scores_mt_to_append = strsplit(tag_numcohort_corresp, "_x_")[[1]]
for (suffix_i in suffixes_of_multiples_scores_mt_to_append){
  name_of_a_score_mt_to_append = paste("s_mt_cp_",suffix_i, sep='')
  # writeLines(name_of_a_score_mt_to_append) # for verifications 
  list_cols_to_create2 <- c(list_cols_to_create2,name_of_a_score_mt_to_append)
}

  
pieces_of_ftname_as_MT_name <- strsplit(a_MT_ft_name, "_in_")[[1]] # NB : if the sep is not found, a vector of only the entire word is kept so getting the 1st elt gives it also
ftname_as_correct_initial_name <-pieces_of_ftname_as_MT_name[1]



# output is fs_table_raw_nnc_only_marks_only_and_pruned_ALL_FSs (a table with all unique genes, each one with its marks for storytelling)   


# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ # not needed chunk 1
# # >>>>>>>> * lets get the different types of alg analysed here and their counts
# # (with it, we can better characterize our analysis...for e.g. to know how many columns to create for FS specific scores)
# count_type_alg_1_ie_ST = 0
# count_type_alg_2_ie_MT = 0
# for (index_a_tag_algi in c(1:length(list_tag_alg))) {
#   a_tag_algi = list_tag_alg[index_a_tag_algi]
#   if (grepl("_ST_", a_tag_algi, fixed=TRUE)){
#     count_type_alg_1_ie_ST = count_type_alg_1_ie_ST + 1
#   } else if (grepl("_MT_", a_tag_algi, fixed=TRUE)){
#     count_type_alg_2_ie_MT = count_type_alg_2_ie_MT + 1
#   }
# }
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ # not needed 1.5
# # lets created the boolean following the number of types of alg we have to analyse
# # score is as "the number at pos x is the score for the xth type of models ran"
# # # -- version 1 with change 1 (deprecated)
# # if ((count_type_alg_1_ie_ST>=1)&(count_type_alg_2_ie_MT>=1)){
# #   for_type_alg_1_value_bool_yes = 1 # was 10 before change1
# #   for_type_alg_1_value_bool_no = 0
# #   for_type_alg_2_value_bool_yes = 0.1 # was 1 before change1
# #   for_type_alg_2_value_bool_no = 0
# # } else if((count_type_alg_1_ie_ST==0)|(count_type_alg_2_ie_MT==0)){
# #   for_type_alg_1_value_bool_yes = 1
# #   for_type_alg_1_value_bool_no = 0
# #   for_type_alg_2_value_bool_yes = 1
# #   for_type_alg_2_value_bool_no = 0
# # }
# # before change1 for_type_alg_1_value_bool_yes was 10 and for_type_alg_2_value_bool_yes was 1 using unit number as for alg 2 score and ten's number as alg 1 score 
# # but separating with a comma can bring a clearer separation, while giving more of the feeling of "parts" as the individual fts are in the MT as well as giving us a lot of insights 
# #when the code has some exceptions that   it does not take into account
# # -- version 2 (include booleans to mark the signs of the majority coefs counted) and does not depend on the counts of type of FS found (the same marks are used always)
# # ---  these are to mark the quality of the majority sign among the counted coefs
# for_type_alg_1_value_bool_yes = 1
# for_type_alg_1_value_bool_no = 0
# for_type_alg_2_value_bool_yes = 0.1 
# for_type_alg_2_value_bool_no = 0
# # ---  these are to keep what was the majority sign among the counted coefs
# for_type_alg_1_value_bool_yes_for_maj_with_sign_neg = 10
# for_type_alg_1_value_bool_no_for_maj_with_sign_neg = 0
# for_type_alg_1_value_bool_yes_for_maj_with_sign_pos = 1
# for_type_alg_1_value_bool_no_for_maj_with_sign_pos = 0
# for_type_alg_2_value_bool_yes_for_maj_with_sign_neg = 0.1
# for_type_alg_2_value_bool_no_for_maj_with_sign_neg = 0
# for_type_alg_2_value_bool_yes_for_maj_with_sign_pos = 0.01
# for_type_alg_2_value_bool_no_for_maj_with_sign_pos = 0
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~é

# #~~~~~~~~~~~~~~~ # not needed chunk 2
# fs_table_raw_nnc_only$space_init_Min = NA
# fs_table_raw_nnc_only$space_init_Max = NA
# fs_table_raw_nnc_only$space_init_LB = NA
# fs_table_raw_nnc_only$space_init_HB = NA
# fs_table_raw_nnc_only$space_init_Num_outliers = NA
# fs_table_raw_nnc_only$space_fin_Size = NA
# fs_table_raw_nnc_only$space_fin_Num_zeros = NA
# fs_table_raw_nnc_only$space_fin_Num_signs = NA
# fs_table_raw_nnc_only$space_fin_Num_pos = NA
# fs_table_raw_nnc_only$space_fin_Num_neg = NA
# fs_table_raw_nnc_only$crit_A1 = NA
# fs_table_raw_nnc_only$crit_Q1 = NA
# fs_table_raw_nnc_only$crit_M1 = NA
# fs_table_raw_nnc_only$crit_S1 = NA
# fs_table_raw_nnc_only$crit_F1 = NA
# fs_table_raw_nnc_only$crit_T1 = NA
# fs_table_raw_nnc_only$crit_A2 = NA
# fs_table_raw_nnc_only$crit_Q2 = NA
# fs_table_raw_nnc_only$crit_M2 = NA
# fs_table_raw_nnc_only$crit_S2 = NA
# fs_table_raw_nnc_only$crit_F2 = NA
# fs_table_raw_nnc_only$crit_T2 = NA
# #~~~~~~~~~~~~~~~~~~~~~~~~~

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ # not needed chunk 3
# Nsigns = Npos + Nneg
# Nmaj = 0 # initialized at zeros because cant be zero (would be zero if all coefs are zeros and such case have been removed because only nnc are kept)
# if (Npos > Nneg) {
#   Nmaj = Npos
# } else if (Nneg > Npos){
#   Nmaj = Nneg
# } else { # Npos = Nneg
#   Nmaj = (Nsigns / 2)
# }
# # for each gene, get the median and the q3 if values can be counted from 1 until Nsigns (they will be used as arbitrary limit of a space 1-Nsigns instead of 1-10seeds)
# Nsigns_counts_med = median(c(0:Nsigns)) # ie 5 for a Nsigns=10 (case of all coefs used)
# Nsigns_counts_q3 = quantile(c(0:Nsigns),0.75)[[1]] # ie 7.5 for a Nsigns=10 (case of all coefs used)
# # for each gene, we defined previously the following booleans : A1, Q1, M1 , F1, S1 and A2, Q2, M2 , F2, S2 
# # but we need to define what type of alg we are currently analysing in this step of the loop and decide the proper boolean values to use
# if (grepl("_ST_", tag_alg_corresp_2_fs_retrieved, fixed=TRUE)){
#   type_alg_specific_value_bool_yes = for_type_alg_1_value_bool_yes
#   type_alg_specific_value_bool_no = for_type_alg_1_value_bool_no
#   type_alg_specific_value_bool_yes_for_maj_with_sign_neg = for_type_alg_1_value_bool_yes_for_maj_with_sign_neg 
#   type_alg_specific_value_bool_no_for_maj_with_sign_neg = for_type_alg_1_value_bool_no_for_maj_with_sign_neg 
#   type_alg_specific_value_bool_yes_for_maj_with_sign_pos = for_type_alg_1_value_bool_yes_for_maj_with_sign_pos
#   type_alg_specific_value_bool_no_for_maj_with_sign_pos = for_type_alg_1_value_bool_no_for_maj_with_sign_pos
# } else if (grepl("_MT_", tag_alg_corresp_2_fs_retrieved, fixed=TRUE)){
#   type_alg_specific_value_bool_yes = for_type_alg_2_value_bool_yes
#   type_alg_specific_value_bool_no = for_type_alg_2_value_bool_no
#   type_alg_specific_value_bool_yes_for_maj_with_sign_neg = for_type_alg_2_value_bool_yes_for_maj_with_sign_neg 
#   type_alg_specific_value_bool_no_for_maj_with_sign_neg = for_type_alg_2_value_bool_no_for_maj_with_sign_neg 
#   type_alg_specific_value_bool_yes_for_maj_with_sign_pos = for_type_alg_2_value_bool_yes_for_maj_with_sign_pos
#   type_alg_specific_value_bool_no_for_maj_with_sign_pos = for_type_alg_2_value_bool_no_for_maj_with_sign_pos
# }
# 
# # for each gene, we give the value of the booleans following the gene's final space of coefs values
# # T1 is always defined with "T1 = type_alg_specific_value_bool_yes" because it is a counter (it is not added up if the gene if not gone through while analysing a FS because it is absent there)
# if (Nzeros!=0){ # the final space of coefs values has at least one zero so the gallery of bools to change is A2, Q2, M2 , F2, S2
#   A1 = 0
#   Q1 = 0
#   M1 = 0
#   S1 = 0
#   F1 = 0
#   T1 = 0 
#   T2 = type_alg_specific_value_bool_yes # the gene is analysed so T for the gallery to change is added up with bool yes
#   if((Npos == Nneg)|(Nsigns==0)|(Nsigns==1)){ # the values when Nsigns gallery is not admissible for use 
#     F2=type_alg_specific_value_bool_yes
#     A2=0
#     Q2=0
#     M2=0
#     S2=0
#   }else{ # the values when Nsigns gallery is admissible for use 
#     F2=type_alg_specific_value_bool_no
#     if(Nmaj==Nsigns){
#       A2=type_alg_specific_value_bool_yes
#     }else{
#       A2=type_alg_specific_value_bool_no
#     }
#     if(Nmaj>=Nsigns_counts_q3){
#       Q2=type_alg_specific_value_bool_yes
#     }else{
#       Q2=type_alg_specific_value_bool_no
#     }
#     if(Nmaj>Nsigns_counts_med){
#       M2=type_alg_specific_value_bool_yes
#     }else{
#       M2=type_alg_specific_value_bool_no
#     }
#     if(Nneg > Npos){
#       S2=type_alg_specific_value_bool_yes_for_maj_with_sign_neg + type_alg_specific_value_bool_no_for_maj_with_sign_pos
#     }else if (Npos > Nneg){
#       S2=type_alg_specific_value_bool_no_for_maj_with_sign_neg + type_alg_specific_value_bool_yes_for_maj_with_sign_pos
#     } else { # Npos = Nneg
#       S2 = 0
#     }
#   }
# }else{ # Nzeros==0 ie # the final space of coefs does not have zeros so the gallery of bools to change is A1, Q1, M1 , F1, S1
#   A2 = 0
#   Q2 = 0
#   M2 = 0
#   S2 = 0
#   F2 = 0
#   T2 = 0
#   T1 = type_alg_specific_value_bool_yes # the gene is analysed so T for the gallery to change is added up with bool yes
#   if((Npos == Nneg)|(Nsigns==0)|(Nsigns==1)){ # the values when Nsigns gallery is not admissible for use 
#     F1=type_alg_specific_value_bool_yes
#     A1=0
#     Q1=0
#     M1=0
#     S1=0
#   }else{ # the values when Nsigns gallery is admissible for use 
#     F1=type_alg_specific_value_bool_no
#     if(Nmaj==Nsigns){
#       A1=type_alg_specific_value_bool_yes
#     }else{
#       A1=type_alg_specific_value_bool_no
#     }
#     if(Nmaj>=Nsigns_counts_q3){
#       Q1=type_alg_specific_value_bool_yes
#     }else{
#       Q1=type_alg_specific_value_bool_no
#     }
#     if(Nmaj>Nsigns_counts_med){
#       M1=type_alg_specific_value_bool_yes
#     }else{
#       M1=type_alg_specific_value_bool_no
#     }
#     if(Nneg > Npos){
#       S1=type_alg_specific_value_bool_yes_for_maj_with_sign_neg + type_alg_specific_value_bool_no_for_maj_with_sign_pos
#     }else if (Npos > Nneg){
#       S1=type_alg_specific_value_bool_no_for_maj_with_sign_neg + type_alg_specific_value_bool_yes_for_maj_with_sign_pos
#     } else { # Npos = Nneg
#       S1 = 0
#     }
#   }
# }
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ # not needed chunk 4
# # for each gene, update the values of the 8 new cols that are crit_A1 through crit_S2 
# # ie storing in its row inside the raw table the values related to its coefs space and booleans of storytelling ability
# fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"space_init_Min"] = space_initial_min
# fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"space_init_Max"] = space_initial_max
# fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"space_init_LB"] = space_initial_lower_bracket
# fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"space_init_HB"] = space_initial_higher_bracket
# fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"space_init_Num_outliers"] = space_initial_outliers_size
# fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"space_fin_Size"] = space_final_size
# fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"space_fin_Num_zeros"] = Nzeros
# fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"space_fin_Num_signs"] = Nsigns
# fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"space_fin_Num_pos"] = Npos
# fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"space_fin_Num_neg"] = Nneg
# fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_A1"] = A1
# fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_Q1"] = Q1
# fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_M1"] = M1
# fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_S1"] = S1
# fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_F1"] = F1
# fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_T1"] = T1
# fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_A2"] = A2
# fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_Q2"] = Q2
# fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_M2"] = M2
# fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_S2"] = S2
# fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_F2"] = F2
# fs_table_raw_nnc_only[which(fs_table_raw_nnc_only$Features %in% present_gene),"crit_T2"] = T2
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


high_string_status
lenient_string_status
s_all

final_table_V1$high_string_status <- "_NOT_CHANGED_YET"
final_table_V1$lenient_string_status <- "_NOT_CHANGED_YET"
final_table_V1$s_all <- 0

table_grp1 = final_table_V3_grp1[,(index_one_fs_ascolname-1+3)]
table_grp1 = final_table_V3_grp1[which(final_table_V3_grp1$high_string_status == "Y"),]
table_grp1 <- subset(final_table_V3_grp1, one_fs_ascolname == 1,select = colnames(final_table_V3_grp1))
for (index_a_correct_gene_name in c(1:length(colnames(final_table_V3)))){}
a_correct_gene_name = list_fts_all_in_fs_table_as_correct_names_uniks[index_a_correct_gene_name]

##########plots 
library(forcats)
library(dplyr)
library(ggplot2)

#------------------------
# Load ggplot2
library(ggplot2)

# Create data
data <- data.frame(
  name=c("A","B","C","D","E") ,  
  value=c(3,12,5,18,45)
)
# Barplot
ggplot(data, aes(x=name, y=value)) + 
  geom_bar(stat = "identity")

#----------------------------


a<-starwars %>% 
  filter(!is.na(species)) %>%
  count(species, sort = TRUE)
  
  
b = mtcars  
#---------------------------------
# Libraries
library(ggplot2)

# 1: uniform color. Color is for the border, fill is for the inside
ggplot(mtcars, aes(x=as.factor(cyl) )) +
  geom_bar(color="blue", fill=rgb(0.1,0.4,0.5,0.7) )

# 2: Using Hue
ggplot(mtcars, aes(x=as.factor(cyl), fill=as.factor(cyl) )) + 
  geom_bar( ) +
  scale_fill_hue(c = 40) +
  theme(legend.position="none")

# 3: Using RColorBrewer
ggplot(mtcars, aes(x=as.factor(cyl), fill=as.factor(cyl) )) + 
  geom_bar( ) +
  scale_fill_brewer(palette = "Set1") +
  theme(legend.position="none")


# 4: Using greyscale:
ggplot(mtcars, aes(x=as.factor(cyl), fill=as.factor(cyl) )) + 
  geom_bar( ) +
  scale_fill_grey(start = 0.25, end = 0.75) +
  theme(legend.position="none")


# 5: Set manualy
ggplot(mtcars, aes(x=as.factor(cyl), fill=as.factor(cyl) )) +  
  geom_bar( ) +
  scale_fill_manual(values = c("red", "green", "blue") ) +
  theme(legend.position="none")



# -  a bar plot for the props
# Make the frequencies numbers (rather than factors)
df_genes_grps_props <- as.numeric(as.character(df_genes_grps_props))
## Find a range of y's that'll leave sufficient space above the tallest bar
ylim <- c(0, 1.1*max(df_genes_grps_props))
## Plot, and store x-coordinates of bars in xx
xx <- barplot(df_genes_grps_props, xaxt = 'n', width = 0.85, ylim = ylim,
              main = "Proportions of SIGs following the stringency criteria",
              xlab = "Feature selections (FS) from highest to lowest performance using F1",
              ylab = "% genes (over the initial cohort genes)",col = c("red","orange", "blue"),beside=TRUE)
## Add text at top of bars
text(x = xx, y = df_genes_grps_props, label = df_genes_grps_props, pos = 3, cex = 0.8, col = "red")
## Add x-axis labels 
axis(1, at=xx, labels=dat$fac, tick=FALSE, las=2, line=-0.5, cex.axis=0.5)

barplot((as.matrix(df_genes_grps_props)),
        main = "Proportions of SIGs following the stringency criteria",
        xlab = "Feature selections (FS) from highest to lowest performance using F1",
        col = c("red","orange", "blue"),
        beside=TRUE)
legend("topleft",
       c("high strigency (grp1)","added by lenient stringency (grp2)","lenient stringency (grp3=grp1+grp2)"),
       fill = c("red","orange", "blue"))


## Make the frequencies numbers (rather than factors)
dat$freqs <- as.numeric(as.character(dat$freqs))
## Find a range of y's that'll leave sufficient space above the tallest bar
ylim <- c(0, 1.1*max(dat$freqs))
## Plot, and store x-coordinates of bars in xx
xx <- barplot(dat$freqs, xaxt = 'n', xlab = '', width = 0.85, ylim = ylim,
              main = "Sample Sizes of Various Fitness Traits", 
              ylab = "Frequency")
## Add text at top of bars
text(x = xx, y = dat$freqs, label = dat$freqs, pos = 3, cex = 0.8, col = "red")
## Add x-axis labels 
axis(1, at=xx, labels=dat$fac, tick=FALSE, las=2, line=-0.5, cex.axis=0.5)


df_genes_grps[,"Groups"] = c("high strigency (grp1)","added by lenient stringency (grp2)","lenient stringency (grp3=grp1+grp2)", 
                             "Smax",
                             "Between SstrongV1 et Smax","Between SweakV1 et SstrongV1",
                             "Between SstrongV2 et Smax","Between SweakV2 et SstrongV2")
# - limit values for s_all_bs
Smax = 1
SstrongV1 = 0.9
SweakV1 = 0.7
# lets get the limits V2
list_values_s_abs_for_lenient <- final_table_V3_grp3[['s_all_abs']]
# using a 1st time the bimodal finding of a limit, we have limitV21 
limitV2_1 = 0.3639074 # computed with another script
# this being a limit too low compared to lowest limit given, we consider it as SweakV2 and we try to find now SstrongV2
list_values_s_abs_for_lenient_bis <- list_values_s_abs_for_lenient[list_values_s_abs_for_lenient>limitV2_1]
limitV2_2 = 0.813884 # compu

k = list_fs_tables_retrieved_RAW_marks_only_and_pruned[[1]]
a = k[which(k$Features %in% c("CXCL14","MIPEP","PKP1","SORD")),]
a_1 = list_fs_tables_retrieved_RAW_marks_only_and_pruned[[1]][which(rownames(list_fs_tables_retrieved_RAW_marks_only_and_pruned[[1]]) %in% c("CXCL14","MIPEP","PKP1","SORD")),]
a_2 = list_fs_tables_retrieved_RAW_marks_only_and_pruned[[2]][which(rownames(list_fs_tables_retrieved_RAW_marks_only_and_pruned[[2]]) %in% c("CXCL14","MIPEP","PKP1","SORD")),]
a_3 = list_fs_tables_retrieved_RAW_marks_only_and_pruned[[3]][which(rownames(list_fs_tables_retrieved_RAW_marks_only_and_pruned[[3]]) %in% c("CXCL14","MIPEP","PKP1","SORD")),]
a_4 = list_fs_tables_retrieved_RAW_marks_only_and_pruned[[4]][which(rownames(list_fs_tables_retrieved_RAW_marks_only_and_pruned[[4]]) %in% c("CXCL14","MIPEP","PKP1","SORD")),]
a_5 = list_fs_tables_retrieved_RAW_marks_only_and_pruned[[5]][which(rownames(list_fs_tables_retrieved_RAW_marks_only_and_pruned[[5]]) %in% c("CXCL14","MIPEP","PKP1","SORD")),]
a_6 = list_fs_tables_retrieved_RAW_marks_only_and_pruned[[6]][which(rownames(list_fs_tables_retrieved_RAW_marks_only_and_pruned[[6]]) %in% c("CXCL14","MIPEP","PKP1","SORD")),]
a_7 = list_fs_tables_retrieved_RAW_marks_only_and_pruned[[7]][which(rownames(list_fs_tables_retrieved_RAW_marks_only_and_pruned[[7]]) %in% c("CXCL14","MIPEP","PKP1","SORD")),]


a_2 = list_fs_tables_retrieved_RAW_marks_only_and_pruned[[2]][which(list_fs_tables_retrieved_RAW_marks_only_and_pruned[[2]]$Features %in% c("CXCL14","MIPEP","PKP1","SORD")),]


final_table_V1$SIG_status <- 0
final_table_V1$Class_of_SIG <- 0


# 
# # these are the new base folder paths for datasets : 
# # type 1
# /home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_warehouse/outputs/atip3_ml_dataset_type1/
# # type 1 unified
# /home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_warehouse/outputs/atip3_unified_datasets/
# 
# 
# 
# 

# test1 : 
l_fs_all = unique(as.character(table_pres_abs$Features_bis))
l_ds_all = unique(as.character(table_pres_abs_7_DSs$Features_bis))
# test2 : 
l_fs_all = l5
l_ds_all = l6



l7_test_DLEU_l_fs_all = c()
l7_test_DLEU_l_ds_all = c()

for (i in l_fs_all){
  if (grepl("DLEU", i, fixed=TRUE)){
    # keep the previous table
    l7_test_DLEU_l_fs_all = c(l7_test_DLEU_l_fs_all,i)
  }
}

for (j in l_ds_all){
  if (grepl("DLEU", j, fixed=TRUE)){
    # keep the previous table
    l7_test_DLEU_l_ds_all = c(l7_test_DLEU_l_ds_all,j)
  }
}


ds_diff_writing = c()
for (ds in l2){
  if (grepl("ACTB", ds, fixed=TRUE)){
    # keep the previous table
    ds_diff_writing = c(ds_diff_writing,ds)
  }
}





k_odd = c()
for (odd in k1){
  if (!(odd %in% k_fs)){
    # keep the previous table
    k_odd = c(k_odd,odd)
  }
}

k_abs = c()
for (abs in k1){
  if (!(abs %in% k_fs)){
    # keep the previous table
    k_abs = c(k_abs,abs)
  }
}



d1 = unique(as.character(df_left$Features))
d2 = unique(as.character(df_right$Features_bis))
d_1_not_in_2 = setdiff(d1,d2)






table_mcr_FS1 = list_fs_tables_retrieved_MCR[[1]] # lets get the table of coef per gene in each fs
table_mcr_FS2 = list_fs_tables_retrieved_MCR[[2]]
table_mcr_FS3 = list_fs_tables_retrieved_MCR[[3]]
table_mcr_FS4 = list_fs_tables_retrieved_MCR[[4]]




list_paths2files_MCR <- c(list_paths2files_MCR,path2file6_MCR)





# lets supply the cols
for (a_ft_in_final_table_V5 in list_fts_final_table_V5){ # for test a_ft_in_final_table_V5 = list_fts_final_table_V5[1]
  # + lets supply the val of the rank for the present gene in all 3 single-tasks FSs (step 1 : we get the vale, step 2 : we put the val in place)
  if(a_ft_in_final_table_V5 %in% list_fts_table_mcr_FS1){ # for FS1
    mean_coefs_rank_for_R04 = table_mcr_FS1[which(table_mcr_FS1$Features %in% a_ft_in_final_table_V5),"Mean_of_rank_across_10_seeds"]
    final_table_V5[which(final_table_V5$Features %in% a_ft_in_final_table_V5),"Mean_coefs_rank_for_R04"] = mean_coefs_rank_for_R04
  }
  if(a_ft_in_final_table_V5 %in% list_fts_table_mcr_FS2){ # for FS2
    mean_coefs_rank_for_MDA = table_mcr_FS2[which(table_mcr_FS2$Features %in% a_ft_in_final_table_V5),"Mean_of_rank_across_10_seeds"]
    final_table_V5[which(final_table_V5$Features %in% a_ft_in_final_table_V5),"Mean_coefs_rank_for_MDA"] = mean_coefs_rank_for_MDA
  }
  if(a_ft_in_final_table_V5 %in% list_fts_table_mcr_FS3){ # for FS3
    mean_coefs_rank_for_BMS = table_mcr_FS3[which(table_mcr_FS3$Features %in% a_ft_in_final_table_V5),"Mean_of_rank_across_10_seeds"]
    final_table_V5[which(final_table_V5$Features %in% a_ft_in_final_table_V5),"Mean_coefs_rank_for_BMS"] = mean_coefs_rank_for_BMS
  }
}  
  # + lets supply the val of the rank for the present gene in 4 ways : 1-as a mean of all 3 ranks given for 3 copies of the gene, 2-as a rank for each copy of the gene (3 copies)
  MT_name_start = paste(a_ft_in_final_table_V5,"_in_",sep='') # we get the name of all the copies of the genes in the multi-task
  list_MT_names_corresponding = c()
  for (a_MT_name_known in list_fts_table_mcr_FS4){
    if(startsWith(a_MT_name_known, MT_name_start)){
      list_MT_names_corresponding = c(list_MT_names_corresponding,a_MT_name_known)
    }
  }
  # focusing on the copies of a gene if it has copies in the multitask
  table_mcr_FS4_rows_w_MT_name_start = table_mcr_FS4[which(table_mcr_FS4$Features %in% list_MT_names_corresponding),] # we get a short table with only the 3 copies of the present gene (to get mean and the copies of the presentgene)
  numrows_table_mcr_FS4_rows_w_MT_name_start = nrow(table_mcr_FS4_rows_w_MT_name_start)
  if(numrows_table_mcr_FS4_rows_w_MT_name_start > 0){
    mean_coefs_rank_for_MT_all_3_copies=mean(table_mcr_FS4_rows_w_MT_name_start$Mean_of_rank_across_10_seeds, na.rm = TRUE) # get val of the mean of the copies
    final_table_V5[which(final_table_V5$Features %in% a_ft_in_final_table_V5),"Mean_coefs_rank_for_MT_all_3_copies"] = mean_coefs_rank_for_MT_all_3_copies # val of mean of the copies added
    for (one_of_list_MT_names_corresponding in list_MT_names_corresponding){
      # get the val of the rank of the copy, whatever copy it is...
      mean_coefs_rank_for_MT_copy_of_the_gene = table_mcr_FS4[which(table_mcr_FS4$Features %in% one_of_list_MT_names_corresponding),"Mean_of_rank_across_10_seeds"] 
      # ...report that value for the proper col of the copy 
      if(grepl("_in_GSE63471", one_of_list_MT_names_corresponding, fixed=TRUE)){
        final_table_V5[which(final_table_V5$Features %in% a_ft_in_final_table_V5),"Mean_coefs_rank_for_MT_copy_of_the_gene_from_R04"] = mean_coefs_rank_for_MT_copy_of_the_gene
      }else if (grepl("_in_GSE25055", one_of_list_MT_names_corresponding, fixed=TRUE)){
        final_table_V5[which(final_table_V5$Features %in% a_ft_in_final_table_V5),"Mean_coefs_rank_for_MT_copy_of_the_gene_from_MDA"] = mean_coefs_rank_for_MT_copy_of_the_gene
      }else if(grepl("_in_GSE41998", one_of_list_MT_names_corresponding, fixed=TRUE)){
        final_table_V5[which(final_table_V5$Features %in% a_ft_in_final_table_V5),"Mean_coefs_rank_for_MT_copy_of_the_gene_from_BMS"] = mean_coefs_rank_for_MT_copy_of_the_gene
      }
    } # all copies of the present gene have their value added
  } # cond of having at least one copy of the present gene in the multi-task is close
} # all present genes in the final table have been supplied with proper values of ranks





# Version : Vranksasentallftsselectedornot





















