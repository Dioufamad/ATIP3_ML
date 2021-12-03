# histograms or pCR on high and low cluster

import matplotlib.pyplot as plt
from textwrap import wrap # to wrap plot titles
import numpy as np

# cohort bmshorak
x = np.arange(5)
plt.bar(x, height=[26.32,32.14,25,16.67,11.81], color=['green', 'cyan', 'blue', "red",'black'])
plt.xticks(x, ['low [15]','low-med [9]','med-high [9]','high [1]','total [57]'])
plt.ylim(0,100)
plt.title("\n".join(wrap("Proportion of patients with pCR according to the MTUS1 level in each selected cluster.")))
plt.xlabel('counts across the cohort subdivisions')
plt.ylabel('% of pCR')

# R02
x = np.arange(5)
plt.bar(x, height=[34.15,19.35,14.89,3.95,6.19], color=['green', 'cyan', 'blue', "red",'black'])
plt.xticks(x, ['low [14]','low-med [12]','med-high [7]','high [3]','total [41]'])
plt.ylim(0,100)
plt.title("\n".join(wrap("Proportion of patients with pCR according to the MTUS1 level in each selected cluster.")))
plt.xlabel('counts across the cohort subdivisions')
plt.ylabel('% of pCR')

# osaka (corrected)
x = np.arange(5)
plt.bar(x, height=[33.33,33.33,20.51,12.90,23.48], color=['green', 'cyan', 'blue', "red",'black'])
plt.xticks(x, ['low [6]','low-med [9]','med-high [8]','high [4]','total [27]']) # (values total in each are : 18,27,39,31,115)
plt.ylim(0,100)
plt.title("\n".join(wrap("Proportion of patients with pCR according to the MTUS1 level in each selected cluster.")))
plt.xlabel('counts across the cohort subdivisions')
plt.ylabel('% of pCR')
# mda 1/2
x = np.arange(5)
plt.bar(x, height=[31.25,12.50,22.37,9.80,3.23], color=['green', 'cyan', 'blue', "red",'black'])
plt.xticks(x, ['low [10]','low-med [3]','med-high [34]','high [10]','total [32]'])
plt.ylim(0,100)
plt.title("\n".join(wrap("Proportion of patients with pCR according to the MTUS1 level in each selected cluster.")))
plt.xlabel('counts across the cohort subdivisions')
plt.ylabel('% of pCR')
# fudan
x = np.arange(5)
plt.bar(x, height=[29.63,25,14.29,2.94,6.23], color=['green', 'cyan', 'blue', "red",'black'])
plt.xticks(x, ['low [16]','low-med [23]','med-high [11]','high [1]','total [54]'])
plt.ylim(0,100)
plt.title("\n".join(wrap("Proportion of patients with pCR according to the MTUS1 level in each selected cluster.")))
plt.xlabel('counts across the cohort subdivisions')
plt.ylabel('% of pCR')
# texas_tabchi (corrected)
x = np.arange(5)
plt.bar(x, height=[23.33,12.82,20,35.29,20.88], color=['green', 'cyan', 'blue', "red",'black'])
plt.xticks(x, ['low [7]','low-med [5]','med-high [1]','high [6]','total [19]']) # (values total in each are : 30,39,5,17,91)
plt.ylim(0,100)
plt.title("\n".join(wrap("Proportion of patients with pCR according to the MTUS1 level in each selected cluster.")))
plt.xlabel('counts across the cohort subdivisions')
plt.ylabel('% of pCR')
# iwamoto
x = np.arange(5)
plt.bar(x, height=[50,47.06,37.5,6.25,3.28], color=['green', 'cyan', 'blue', "red",'black'])
plt.xticks(x, ['low [2]','low-med [8]','med-high [9]','high [1]','total [4]'])
plt.ylim(0,100)
plt.title("\n".join(wrap("Proportion of patients with pCR according to the MTUS1 level in each selected cluster.")))
plt.xlabel('counts across the cohort subdivisions')
plt.ylabel('% of pCR')
# R04
x = np.arange(5)
plt.bar(x, height=[48.28,22.73,2.78,0,9.86], color=['green', 'cyan', 'blue', "red",'black'])
plt.xticks(x, ['low [14]','low-med [15]','med-high [1]','high [0]','total [29]'])
plt.ylim(0,100)
plt.title("\n".join(wrap("Proportion of patients with pCR according to the MTUS1 level in each selected cluster.")))
plt.xlabel('counts across the cohort subdivisions')
plt.ylabel('% of pCR')
# mda_508
x = np.arange(5)
plt.bar(x, height=[27.27,24.22,17.03,14.39,3.54], color=['green', 'cyan', 'blue', "red",'black'])
plt.xticks(x, ['low [18]','low-med [31]','med-high [31]','high [19]','total [66]'])
plt.ylim(0,100)
plt.title("\n".join(wrap("Proportion of patients with pCR according to the MTUS1 level in each selected cluster.")))
plt.xlabel('counts across the cohort subdivisions')
plt.ylabel('% of pCR')
#>>>>>>>><<
