# Visualizing Lending Club Data
# https://courses.thinkful.com/data-001v2/project/2.2.2

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import seaborn as sns

filename='dat/loansData.csv'
loansData = pd.read_csv(filename)
loansData.dropna(inplace=True)
colname=['Amount.Requested','Amount.Funded.By.Investors']
data=[loansData[colname[0]],loansData[colname[1]]]

sns.boxplot(data, names=["Amount.Requested", "Amount.Funded.By.Investors"], color='pastel')
plt.savefig("boxplot.pdf", bbox_inches='tight')
plt.title('Boxplot')
plt.show()

# Violinplot, allowing to compare if two different data set have same distribution
sns.violinplot(data, names=["Amount.Requested", "Amount.Funded.By.Investors"], color='pastel')
sns.despine(offset=10, trim=True);
plt.title('Violinplot')
plt.savefig("violinplot.pdf", bbox_inches='tight')
plt.show()


# Histogram
fig, axs = plt.subplots(1,2, figsize=(10,6), facecolor='w', edgecolor='k')
title=['Amount.Requested','Amount.Funded.By.Investors']
for i in range(2):
	sns.distplot(data[i], bins=9,kde=False,fit=stats.norm, ax=axs[i])
	axs[i].set_title(title[i],fontsize=13)
	axs[i].set_xlabel('')
	# axs[i].autoscale(tight='x')
plt.autoscale(tight='x')
plt.savefig("histogram.pdf", bbox_inches='tight')
plt.show()

# QQ-plot
fig = plt.figure(figsize=(10,6), facecolor='w', edgecolor='k')
distribution=['uniform','norm']
for i in range(2):
	fig.add_subplot(1,2,i+1)
	stats.probplot(data[i],dist='norm', plot=plt)
plt.savefig("qqplot.pdf", bbox_inches='tight')
plt.show()


# LP #  comment to data set

# LP #  both distribution are very similar 
# LP #  boxplot and violinplot shows that 1st median and 3rd quartile are the same as 
# LP #  well as the max. The min of Amount.Funded.By.Investors is slightly negative and 
# LP #  for Amount.request is about 1000. The distribution is clearly not uniform as histograms and 
# LP #  qq-plot shows.