###### Welcome to the ATIP3_ML project repository!

A start on ATIP 3 and around it a bit...

Scientific questions : 

- Q1 : What are the molecular workings of the ATIP3 protein in the setting of those severe cases of breast cancer ?
- Q2 : What compounds could be candidates for a treatment ?



###### Progress on Q1

The idea : lets start small and build a code that can give us genes that are candidates for a role in the variation of a response

Steps for Q1 : 
- 0 : make a code for each class of methods (univariate, multivariate and learning based) as ready to run code ()
- 1 : just choose a dataset for gex and compare away! 
- 2 : a synthetic benchmark is needed. NB : the email of the synthetic dataset from Chloé use it for the synthetic benchmark after the code is ready 
- 3 : we need to push further on the networks and compare them to the supervised learning approch methods 
- 4 : at this point, generating list of features is a hot launch, we need to focus on the treatments side and also mak it a hot launch 
- 5 : what we know about each of the two wings of the projects has to be crossed...to be thought about.

###### Present developpements : 
- the wiki has the entries for the scientific reasoning until here
- 3 cohorts datasets (REMAGUS02, REMAGUS02 or MDAnderson) are available with gene expression data ()
- A Python 3.7 code has been started
- the code for univariate and multivariate analysis is ready. Tests will be done on each subsets of candidates selected by ML methods
- the code for ML methods is at 70%.

- 

###### Ongoing : 
- finishing the code for ML to select subsets of genes (multivariate and univariates methods to relaunch for subset of those subsets) 

###### Progress on Q2

None

#### Last caution
- the folder atip3_material/3_cohorts... has to be replaced by its newest edition in the drive
- get alias symbols for genes from here HUGO Gene Nomenclature Commitee : 
https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29789

#### Last progress 
- convert AFFIMETRIX probe set ID into gene symbol
- add the 2 multivariate tests used for feature selection in SLATE
- make a similar formater for R_04 ad MDA

- day:



+do the figures, comment, send mail, do the slide and get some bibliography fast

 + repair the marking of tnbc or any response when used at 2nd column



#### From the file "new_in_doc1"

# update the conda packages
- https://stackoverflow.com/questions/51712693/packagenotinstallederror-package-is-not-installed-in-prefix?rq=1
- https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html#updating-packages
- https://stackoverflow.com/questions/38972052/anaconda-update-all-possible-packages
- see here chnages in tensoeflow 2 : https://www.google.com/search?sxsrf=ALeKk01tJK62lDZBCQLI-5VlIZhsZGaGCA%3A1598155825115&ei=MexBX9fMBoWejLsP17qpgAE&q=tensorflow+2+vs+1&oq=tensorflow+2+vs+&gs_lcp=CgZwc3ktYWIQARgAMgIIADIFCAAQywEyBwgAEAoQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBOgQIABBHOgcIABAUEIcCOgQIABAKUIeLMFjgkjBg_5wwaABwAXgAgAE0iAHxAZIBATWYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=psy-ab


To do list :
-  the 3 compared, the R tutorial, the scikit learnet multitask,
- new
- do the tables :
- - a df with fts, resp pCR, and atip3 cluster
- download geo dataset, keep only the best probeset per gene, gives a count of genes remaining, check number of samples,
take the treatment column, the resp pCR col, and later add the atip3 cluster

- to join :
- a df with fts (make for all 8)
- a df of taxanes treated patients's response
- a df with cluster