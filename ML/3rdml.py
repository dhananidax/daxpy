import numpy as np
import matplotlib.pyplot as plt

greyhounds = 500
labs = 500

grey_height = 28 + 4 * np.random.randn(greyhounds) # 28 is the mean and 4 is the standard deviation 
lab_height = 24 + 4 * np.random.randn(labs) # 24 is the mean and 4 is the standard deviation

plt.hist([grey_height,lab_height], stacked=True, color=['r','b'])# stacked=True for stacking the histograms in the same graph 
plt.show()# stacked=True for stacking the histograms in the same graph 