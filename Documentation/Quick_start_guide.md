# ** ATIP3_ML project quick start guide !**

This file is destined to readers that are familiar with the project are looking briefly for an information, related 
to the data collected or used, the codes developped and the results obtained.

This file will be structured in the form of a FAQ.

Below are various immediate questions about the repo and the related answer. 

# ** Where are the microarray datasets files ? : **

We worked on 6 cohorts for which microrray data was fully available. We analysed them as standalone and as joined-in_one.

- single-task datasets : 

Each dataset corresponding to only one cohort (single-task dataset) is stored in the path below : 
"ATIP3_ML/ATIP3_ML_dev_version/data_warehouse/outputs/atip3_ml_dataset_type1/"

In his folder, each cohort will have multiples files corresponding each either to a variation of how the dataset is formatted 
(columns are gene names or probes names, etc) or to a specific info stored (treatment applied to the patients).
All versions will be described in the Full_guide doc later on.

Each cohort will have its variations files identified by their filename  starting with the cohort GSE identifier.

For each cohort, the variation from the folder to use when launching an ML model has its filename ending with 
"_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname"
E.g. : GSE41998_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_cohortname.csv for the cohort "GSE41998"

- Multi-task datasets : 

Each dataset corresponding to multiple cohorts joined (Multi-task dataset) is stored in the path below :
"ATIP3_ML/ATIP3_ML_dev_version/data_warehouse/outputs/atip3_unified_datasets/"

In this folder, multiples variations of cohorts reunited exists following the cohorts reunited and how they have been reunited.
At this moment, the versions used for our multitask analysis are : 

-- a reunion of the 6 cohorts initially analysed : "JoinNewDesign2CommonFtsof6_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"

-- a reunion of the 3 inndividual cohorts among the top 4 cohorts in performance: "JoinNewDesign2CommonFtsof3oftop4FSsL1_ml_dataset_taxanesonly_ATIP3lowonly_GEX_pCR_6cohortname.csv"

NB : to simplify the call on the files during models launching, the following script contains all the paths to the datasets
and a tag attached to each dataset path to call it easily and specifically from a script.

"ATIP3_ML/ATIP3_ML_dev_version/engines/data_engine3_bay.py"

# ** Which RNAseq cohorts have been identified as adequate for our project ?**
At this present time, we have found : 
- total number of samples across complete cohorts (clinical data available) : 252.
This is for 2 cohorts (GSE123845 and GSE145151) with respectively (227,25) samples treated with taxanes.
- total number of samples across UNcomplete cohorts (clinical data NOT available) : 566.
This is for 6 cohorts (GSE116335,GSE122630,GSE75367,GSE142767,GSE131099,GSE131983) with respectively (265,95,74,66,62,4) samples
(not 100% sure that they are all treated with taxanes as clinical data is still to be obtained). 
NB : the following file explicits all about the research of these cohorts :

"ATIP3_ML/ATIP3_ML_dev_version/data_warehouse/inputs/atip3_material/RNAseq_cohorts/Point_sur_cohortes_RNAseq_V2.pdf"

# ** Where are the files to launch a regression model ?**
This repo's codes operates around these main subfolders : 
- ATIP3_ML/ATIP3_ML_dev_version/data_acquisition : where the codes developped are located
- ATIP3_ML/ATIP3_ML_dev_version/data_warehouse : where all entry files and datasets are stored
- ATIP3_ML/ATIP3_ML_dev_version/engines : where are located the complementary modules for the code to work properly
- ATIP3_ML/ATIP3_ML_dev_version/envs_archives : contains virtual environments archives, used to recreate an environment 
with all libraries used at some point

Two types of regression models can be launched using the codes in this repo : 
- single-task regression models : they use a dataset of one cohort and the code uses Scikit-learn as the main library. 
The script used as template for such an analysis is : 

ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/sklearn/GSCV_Sklearn_L1vsSPAMS.py

- Multi-task regression models : they use a dataset joining multiples cohorts and the code uses SPAMS as the main library. 
The script used as template for such an analysis is :

ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/SPAMS/GSCV_SpamsSparseGroupL1LogReg_Es0.py

NB : More precisions about the code will be added in the Full_guide doc later on.
# ** Where are the latest results ?**

The results are mainly in 2 categories : 
- the performances of the tested predictive models : 
  - 6 single-task models : 
  ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/scikit_learn
  - 1 multi-task model by joining 6 cohorts in 1 : 
  ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/spams_sparse_group_lasso_l2__l1onlyused_6cohortes
  - 1 multi-task model by joining the 3 cohorts present in the top 4 ranking in 1 : 
  ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/spams_sparse_group_lasso_l2_l1onlyused_3oftop4FSsL1
- the lists of genes that have been curated the latest : 
ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/All_sorted_on_perc_of_representation_among_top4_FSs_V4.xlsx
- ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/Mean_on_coefs_SIGs_among_top4_FSs_V4.xlsx
- ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/Previous_41_SIGs_situation_after_SIGs_comp_with_Top4FSs.xlsx
- ATIP3_ML/ATIP3_ML_dev_version/data_acquisition/1_pipelines_or_tasks/Multitask_learning/res_learning_tasks/outputs/runs/Share_on_coefs_SIGs_among_top4_FSs_V4.xlsx

NB : additional changes have to be made for these four lists :
- a correction on how the mean of th coefficients from multitask regression have been computed
- added the correlation matrices info in order to further restrict the lists in size

These changes will be made by Amad and added at the same time than a more complete documentation (the Full_guide doc)
