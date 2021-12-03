#!/usr/bin/env python
# coding: utf-8

# ## Exploring hierarchical clustering of REMAGUS02 cohort
# imports
import numpy as np
# from numpy import seterr,isneginf # used to manage the change into log2 o values in a np array
import matplotlib.pyplot as plt
from textwrap import wrap # to wrap plot titles
import pandas as pd
from statannot import add_stat_annotation

# setting up the stage
sep_in_file = ","
dict_idcohort_filepathcohort = {"GSE41998":"/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE41998_ATIP3probesetsonly_probesnames_279x7_ph.csv",
"GSE26639":"/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE26639_ATIP3probesetsonly_probesnames_226x5_ph.csv",
"GSE32646":"/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE32646_ATIP3probesetsonly_probesnames_115x6_ph.csv",
"GSE25055":"/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE25055_ATIP3probesetsonly_probesnames_310x6_ph.csv",
"GSE20194":"/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE20194_ATIP3probesetsonly_probesnames_278x7_ph.csv",
"GSE20271":"/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE20271_ATIP3probesetsonly_probesnames_178x7_ph.csv",
"GSE23988":"/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE23988_ATIP3probesetsonly_probesnames_61x3_ph.csv",
"GSE63471":"/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE63471_ATIP3probesetsonly_probesnames_142x5_ph.csv",
"GSE25066":"/home/amad/PALADIN_1/3CEREBRO/garage/projects/ATIP3/ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/GSE25066_ATIP3probesetsonly_probesnames_508x6_ph.csv"}
dict_idcohort_numtotalsamples = {}
dict_idcohort_listofuniksamplesnames = {}
dict_idcohort_idofotherscohortssearchedinto = {}
dict_idcohort_listofsamplesfoundinotherscohortssearchedinto = {}
dict_idcohort_listofnumoccurencesinotherscohortssearchedinto = {}
def add_entry_in_dict(dict_to_supply,key,value):
	try:
		dict_to_supply[key].append(value)
	except KeyError:  # if the key does not exit (case of the first append for a key) # except means "in case of this following event, do this :
		dict_to_supply[key] = [value]
	return
# load the datasets samples info
list_of_the_idcohorts = list(dict_idcohort_filepathcohort.keys())
for an_idcohort in list_of_the_idcohorts: # for test, an_idcohort = list_of_the_idcohorts[0] # # for test level 2 , an_idcohort = list_of_the_idcohorts[1]
	# idcohort = an_idcohort # known
	index_manipulated_cohort = list_of_the_idcohorts.index(an_idcohort)
	filepath_cohort = dict_idcohort_filepathcohort[an_idcohort]
	sep_in_file = ","
	df_file_ph = pd.read_csv(filepath_cohort, sep_in_file)
	# put the rownames (genes) as index
	df_file_ph = df_file_ph.set_index(list(df_file_ph.columns)[0]) # because a csv from R has the rownames becoming the first col
	samplesnamesbin = df_file_ph.loc[:,["geo_accession"]] # get the 1st column of data ... # anciently it was dframe[Resp_col_name] but gives a series instead of a df
	# ...and get the unique sample names
	list_of_unik_samplesnames_in_cohort = sorted(samplesnamesbin.iloc[:, 0].unique())
	numtotalsamples = len(list_of_unik_samplesnames_in_cohort)
	# add info in dict that are collectors of info
	dict_idcohort_listofuniksamplesnames[an_idcohort] = list_of_unik_samplesnames_in_cohort
	dict_idcohort_numtotalsamples[an_idcohort] = numtotalsamples
print("we finished loading cohorts info")

# go through each cohort samples names and search the others cohorts if one include all of them
number_cohort_searched_into = 0
for an_idcohort1 in list_of_the_idcohorts: # for test, an_idcohort1 = list_of_the_idcohorts[0]
	# idcohort = an_idcohort # known
	list_of_samples_searched = dict_idcohort_listofuniksamplesnames[an_idcohort1]
	list_of_cohorts_to_search_into = list_of_the_idcohorts
	for an_id_of_cohort_tosearch_into in list_of_cohorts_to_search_into: # for test, an_id_of_cohort_tosearch_into = list_of_cohorts_to_search_into[0]
		if an_id_of_cohort_tosearch_into == an_idcohort1:
			pass
		else: # an_id_of_cohort_tosearch_into different from an_idcohort1
			# keep the name of the cohort gone through
			add_entry_in_dict(dict_idcohort_idofotherscohortssearchedinto, an_idcohort1, an_id_of_cohort_tosearch_into)
			# count the numbers of samples found in the cohort searched into
			list_of_samples_searched_into = dict_idcohort_listofuniksamplesnames[an_id_of_cohort_tosearch_into]
			list_of_samples_found_after_search = list(set(list_of_samples_searched) & set(list_of_samples_searched_into))
			num_of_samples_occurences_found_after_search = len(list_of_samples_found_after_search)
			# keep the list of samples found
			add_entry_in_dict(dict_idcohort_listofsamplesfoundinotherscohortssearchedinto, an_idcohort1, list_of_samples_found_after_search)
			# keep the number of occurences
			add_entry_in_dict(dict_idcohort_listofnumoccurencesinotherscohortssearchedinto, an_idcohort1, num_of_samples_occurences_found_after_search)
	number_cohort_searched_into += 1
	print("Cohort", number_cohort_searched_into, "all searched out of",len(list_of_cohorts_to_search_into))

# make a report of the results :
print("A FULL REPORT :")
for an_idcohort2 in list_of_the_idcohorts:
	print("For the cohort",an_idcohort2,":")
	print("- total number of samples is",dict_idcohort_numtotalsamples[an_idcohort2])
	list_of_cohorts_to_search_into = dict_idcohort_idofotherscohortssearchedinto[an_idcohort2]
	for an_id_of_cohort_tosearch_into1 in list_of_cohorts_to_search_into:
		index_of_cohort_searched_into_where_itis_kept = list_of_cohorts_to_search_into.index(an_id_of_cohort_tosearch_into1)
		print("- number of occurences in",an_id_of_cohort_tosearch_into1,"is",dict_idcohort_listofnumoccurencesinotherscohortssearchedinto[an_idcohort2][index_of_cohort_searched_into_where_itis_kept])
print("ALL REPORTS DONE.")
# end

# lastest reports in 9 microarray cohorts :
# For the cohort GSE25055 :
# - total number of samples is 310
# - number of occurences in GSE25066 is 310
# For the cohort GSE25066 :
# - total number of samples is 508
# - number of occurences in GSE25055 is 310




