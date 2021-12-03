# # origin_of_top20_HKGs = "the_cohort_only"
# # origin_of_top20_HKGs = "common_to_cohorts"
# #
# # # ----for the origin of the top 20 HKGs to use to compute Std
# # origin_of_top20_HKGs = "the_cohort_only"
# #
#
# if cohort_used == "REMAGUS02":
#     list_mtus1_probe_2_focus_on = ["GSasMTUS1wGBANasAI695017wPSIas212093_s_at", "GSasMTUS1wGBANasBE552421wPSIas212095_s_at", "GSasMTUS1wGBANasAL096842wPSIas212096_s_at", "GSasMTUS1wGBANasAI028661wPSIas239576_at"]
# else:
#     list_mtus1_probe_2_focus_on = ["GSasMTUS1wGBANasAI695017wPSIas212093_s_at", "GSasMTUS1wGBANasBE552421wPSIas212095_s_at", "GSasMTUS1wGBANasAL096842wPSIas212096_s_at"]
#
#
#
#
#
#
#
#
#
#
#
# # list1 = ["HUWE1"]
# # list2 = ["RPL39","RPL2","RPL5","RPL28"]
# # list3 = ["RPL37A","RPL3","RPL6","RPL2"]
# # list4 = ["RPS27","RPS5","RPS9"]
# # list5 = ["RPS16","RPS8"]
# # list6 = ["RPL41","RPL10","RPL7","RPL1"]
# # list7 = ["RP5-882O7.1", "RP11","RP10","RP5"]
# # list8 = ["RPS18","RPS15","RPS23","RPS31"]
#
# # list2 = ["RPL39","RPL2","RPL5","RPL28"] + ["RPL37A","RPL3","RPL6","RPL2"] + ["RPL41","RPL10","RPL7","RPL1"]
# # list3 = ["RPS27","RPS5","RPS9","RPS50"] + ["RPS16","RPS8","RPS54","RPS8"] + ["RPS18","RPS15","RPS23","RPS31"]
# # list4 = ["RP5-882O7.1", "RP11","RP10","RP5"]
# #
# #
# # RPS16,8,54,8
# # RPL41,10,7,1
# # RP5-882O7.1,11,10,5
# # RPS18,15,23,31
#
#
# # if i.startswith(g):
#
# if ath_origin == "Aexp_R02":
# 	if ath_top20_aspect_origin == "the_cohort_only":
# 		ath_mtus1_probe1 = 0.321904360625095
# 		ath_mtus1_probe2 = 0.350056987276414
# 		ath_mtus1_probe3 = 0.653212849897016
# 		ath_mtus1_probe4 = 0.50194726128412
# 	else: # ath_top20_aspect_origin == "common_to_cohorts"
# 		ath_mtus1_probe1 = 0.313928929360514
# 		ath_mtus1_probe2 = 0.340353034010916
# 		ath_mtus1_probe3 = 0.635712177457833
# 		ath_mtus1_probe4 = 0.488092284240476
# elif ath_origin == "Aexp_R04":
# 	if ath_top20_aspect_origin == "the_cohort_only":
# 		ath_mtus1_probe1 = 0.439682035430134
# 		ath_mtus1_probe2 = 0.241507440470879
# 		ath_mtus1_probe3 = 0.715313199384631
# 	else:  # ath_top20_aspect_origin == "common_to_cohorts"
# 		ath_mtus1_probe1 = 0.419447546923098
# 		ath_mtus1_probe2 = 0.230393091612411
# 		ath_mtus1_probe3 = 0.682393963333242
# else: # ath_origin == "Aexp_MDA"
# 	if ath_top20_aspect_origin == "the_cohort_only":
# 		ath_mtus1_probe1 = 0.600719188222076
# 		ath_mtus1_probe2 = 0.613977067098925
# 		ath_mtus1_probe3 = 0.613038636134454
# 	else:  # ath_top20_aspect_origin == "common_to_cohorts"
# 		ath_mtus1_probe1 = 0.603200908099517
# 		ath_mtus1_probe2 = 0.620596077841658
# 		ath_mtus1_probe3 = 0.613071962822774
#
#
#
# # list0_probes_to_compare_with = ["MTUS1"]
# # list1 = ["HUWE1","HUWE11"]
# # list2 = ["RPL39","RPL2","RPL5","RPL28"] + ["RPL37A","RPL3","RPL6","RPL2"] + ["RPL41","RPL10","RPL7","RPL1"]
# # list3 = ["RPS27","RPS5","RPS9","RPS50"] + ["RPS16","RPS8","RPS54","RPS8"] + ["RPS18","RPS15","RPS23","RPS31"]
# # list4 = ["RP5-882O7.1", "RP11","RP10","RP5"]
# #
# # # - the list can contains duplicates have happens to be columns added again because include multiples of our GS of the query
# # list_of_R02_cols_with_GS_2keep = list(set(list_of_R02_cols_with_GS_2keep))
# # list_of_R04_cols_with_GS_2keep = list(set(list_of_R04_cols_with_GS_2keep))
# # list_of_MDA_cols_with_GS_2keep = list(set(list_of_MDA_cols_with_GS_2keep))
# #
# # # - create the list that cols to keep
# # list_of_R02_cols_with_GS_2keep = []
# # list_of_R04_cols_with_GS_2keep = []
# # list_of_MDA_cols_with_GS_2keep = []
# # # - supply the lists of cols to keep
# # for g in list_of_genes_2_search:
# #     for i in sorted(list(df_file_R02_restricted.columns)):
# #         if g in i:
# #             list_of_R02_cols_with_GS_2keep.append(i)
# # for g in list_of_genes_2_search:
# #     for i in sorted(list(df_file_R04_restricted.columns)):
# #         if g in i:
# #             list_of_R04_cols_with_GS_2keep.append(i)
# # for g in list_of_genes_2_search:
# #     for i in sorted(list(df_file_MDA_restricted.columns)):
# #         if g in i:
# #             list_of_MDA_cols_with_GS_2keep.append(i)
# #
# # list_of_R02_cols_with_GS_2keep = []
# # list_of_R04_cols_with_GS_2keep = []
# # list_of_MDA_cols_with_GS_2keep = []
# # # - supply the lists of cols to keep
# # for g in list_of_genes_2_search:
# # 	for i in sorted(list(df_file_R02_restricted.columns)):
# # 		if g in i:
# # 			if i not in list_of_R02_cols_with_GS_2keep:
# # 				list_of_R02_cols_with_GS_2keep.append(i)
# #
# #
# #
# #
#
#
#
#
#
#
#
#
#
# # for g in list_of_genes_2_search:
# #   ...:     for i in df_file_R02_restricted.columns:
# #   ...:         if g in i:
# #   ...:             list0_probes_to_compare_with.append(i)
# #
# #   for a_inquired_GS in list_of_genes_2_search:
# #       list_of_R02_GS_where_it_is_found = []
# #       list_of_R04_GS_where_it_is_found = []
# #       list_of_MDA_GS_where_it_is_found = []
# #       for a_R02_GS in list(df_file_R02_restricted.columns):
# #           if a_inquired_GS in a_R02_GS:
# #               list_of_R02_GS_where_it_is_found.append(a_R02_GS)
# #       for a_R04_GS in list(df_file_R04_restricted.columns):
# #           if a_inquired_GS in a_R04_GS:
# #               list_of_R04_GS_where_it_is_found.append(a_R04_GS)
# #       for a_MDA_GS in list(df_file_MDA_restricted.columns):
# #           if a_inquired_GS in a_MDA_GS:
# #               list_of_MDA_GS_where_it_is_found.append(a_MDA_GS)
# #       # stash the results
# #       list_of_lists_for_col2.append(list_of_R02_GS_where_it_is_found)
# #       list_of_lists_for_col3.append(list_of_R04_GS_where_it_is_found)
# #       list_of_lists_for_col4.append(list_of_MDA_GS_where_it_is_found)
# #
# #
# # #########
#
# # #########>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# # # - get the df of checking genes presence results
# # sep_in_file = ","
# # file_path_results_checking_genes_inquired_presence = "/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/output/GS_inquiry1/inquired_GS_search_results1.csv"
# # df_results_checking_presence = pd.read_csv(file_path_results_checking_genes_inquired_presence, sep_in_file)
# # # - extract a list of fts to keep for each cohort
# # #>>>>>>>for R02
# # list_cols_2keep_R02 = df_results_checking_presence['R02_GS_where_it_is_found'].tolist()
# # list_cols_2keep_R02_repaired = [literal_eval(x) for x in list_cols_2keep_R02]
# # list_cols_2keep_R02_extracted = [ft for inner_list in list_cols_2keep_R02_repaired for ft in inner_list]
# # # - add to it the GS for the probes of ATIP3 (MTSU1 gene)
# # list_cols_2keep_R02_extracted_wATIP3 = list_cols_2keep_R02_extracted + ["MTUS1"]
# # #>>>>>>>for R04
# # list_cols_2keep_R04 = df_results_checking_presence['R04_GS_where_it_is_found'].tolist()
# # list_cols_2keep_R04_repaired = [literal_eval(x) for x in list_cols_2keep_R04]
# # list_cols_2keep_R04_extracted = [ft for inner_list in list_cols_2keep_R04_repaired for ft in inner_list]
# # # - add to it the GS for the probes of ATIP3 (MTSU1 gene)
# # list_cols_2keep_R04_extracted_wATIP3 = list_cols_2keep_R04_extracted + ["MTUS1"]
# # #>>>>>>>for MDA
# # list_cols_2keep_MDA = df_results_checking_presence['MDA_GS_where_it_is_found'].tolist()
# # list_cols_2keep_MDA_repaired = [literal_eval(x) for x in list_cols_2keep_MDA]
# # list_cols_2keep_MDA_extracted = [ft for inner_list in list_cols_2keep_MDA_repaired for ft in inner_list]
# # # - add to it the GS for the probes of ATIP3 (MTSU1 gene)
# # list_cols_2keep_MDA_extracted_wATIP3 = list_cols_2keep_MDA_extracted + ["MTUS1"]
# #
# # # select the columns name to keep for each cohort
# # # - for R02
# # list_of_all_cols_R02 = list(df_file_R02_restricted.columns)
# # list_of_R02_cols_with_GS_2keep = [a_col for a_col in list_of_all_cols_R02 if any(a_GS_2_keep in a_col for a_GS_2_keep in list_cols_2keep_R02_extracted_wATIP3)]
# # # - for R04
# # list_of_all_cols_R04 = list(df_file_R04_restricted.columns)
# # list_of_R04_cols_with_GS_2keep = [a_col for a_col in list_of_all_cols_R04 if any(a_GS_2_keep in a_col for a_GS_2_keep in list_cols_2keep_R04_extracted_wATIP3)]
# # # - for MDA
# # list_of_all_cols_MDA = list(df_file_MDA_restricted.columns)
# # list_of_MDA_cols_with_GS_2keep = [a_col for a_col in list_of_all_cols_MDA if any(a_GS_2_keep in a_col for a_GS_2_keep in list_cols_2keep_MDA_extracted_wATIP3)]
# # #########>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>