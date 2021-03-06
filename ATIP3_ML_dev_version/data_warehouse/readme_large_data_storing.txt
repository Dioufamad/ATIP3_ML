# Content of the former versions of our gitignore file was the following line and was due to managing large size files
# simply ignoring them and create a google drive folder where they will be put
#/ATIP3_ML_dev_version/data_warehouse/inputs/atip3_material

# The latest choices in managing the large size files is to use "git lfs" instead of the previous method
# ie such files will be tracked but only a pointer to the large file will be in github and the true large file will
# be stored in another location

# What we really want to put away as large size files is :
# - data_warehouse/*.gz (1 files)
# - data_warehouse/*.npz (2 files)
# - data_warehouse/*.tsv (some...)
# - data_warehouse/*.csv (a whole bunch)
# - data_acquisition/*.RData (some...)
# but due to syntax of git lfs issues, we can write the 1st 4 lines

# Solution : we choose to track using "git lfs"
#- the whole data_warehouse folder and all its content
#- all the files with *.RData

# multiples attempting to push, the LFS has been deactivated for our account due to size limit exceeded
# this error has been thrown :
#batch response: This repository is over its data quota. Account responsible for LFS bandwidth should purchase more data packs to restore access.
#batch response: This repository is over its data quota. Account responsible for LFS bandwidth should purchase more data packs to restore access.
#error: failed to push some refs to 'https://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@github.com/Dioufamad/ATIP3_ML.git'

# Instead, we decide to use the gitignore for this :
#- the whole data_warehouse contents are ignored (by ignoring subfolders of inputs and outputs)
#- all the files with *.RData are ignored

# activate the following in the .gitignore file
ATIP3_ML_dev_version/data_warehouse/inputs/**
ATIP3_ML_dev_version/data_warehouse/outputs/**
*.RData