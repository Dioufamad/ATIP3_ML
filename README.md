###### Welcome to the ATIP3_ML project repository!

###### Prologue : 
Previously to 2020, at the Clara Nahmias Lab of the Gustave Roussy Institute in France, the Microtubule 
Associated Protein (MAP) ATIP3 has been at the center of a important observation (in Rodrigues-Ferreira et al., 2019) 
: among breast cancer patients treated with taxanes (mitotic poisons type of breast cancer treatment) in a neoadjuvant 
chemotherapy 
(NAC) fashion, lower levels of the 
ATIP3 protein have been significantly more frequent among the pCR (pathological complete response) subgroup. This 
relation between ATIP3 and the response can be qualified of biomarker behaviour from ATIP3. 

NB : pCR patient (responding patient); NCR patient (non responding patient); relative to a treatment applied. 

A deeper dive into the question poses this hypothesis : when focusing on patients treated with taxanes with 
previously to treatment a state of low levels of ATIP3, does it exist a list of elements that differenciate the pCR 
and the NpR subgroups ?

These two scientific questions around the ATIP3 protein and its biomarker behaviour were a basis for this project : 

- Q1 : What are the molecular workings of the ATIP3 protein in the setting of those severe cases of breast cancer 
  including triple-negative subtype : more precisely, what are the elements in a list of elements that differenciate 
  the pCR and the NpR patients with low levels of ATIP3 ?
- Q2 : What compounds could be candidates for treatments for severe cases of breast cancer including triple-negative subtype  ?

During the period of February 2020 and July 2021, Q1 has been studied.


This repository contains the codes, data, results and observations for the Q1. 

###### Objectives and developments : 
- focusing on Machine Learning interpretable methods, finding the best predictive models in performance of 
  differenciating pCR and NpR response (among low levels of ATIP3 patients) and precise the lists of elements used 
  by those models.
- the Machine Learning algorithms approached here the of Supervised Learning class. Among this class, we focus first 
  on Regression algorithms.
- among Regression algorithms, single-task algorithms have been used. Also Multi-tasks algorithms have been 
  explored (due to the low amount of patients data adequate for the project and the 
  informative advantage to pull together the data from multiples datasets)
- codes and work uses mainly Python and R languages

##### Contents 
This repository main sections are : 
- the "ATIP3_ML" folder : all codes, tools developped, and results 
- the "Documentation" folder : all documents that relate the evolution of the project and the results
  - The "Full_guide" doc is a progressively edited file that contains all the information about the project
  - The "Quick_start_guide" doc is a summary of the most needed information when exploring the repo. 

NB : in order of reading, it is advised to the start with the "Quick_start_guide" then the "Full_guide"

##### FAQ : 
(see Quick_start_guide doc)

