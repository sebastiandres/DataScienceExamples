# Why : QQ-plot, histogram and boxplot for data set
# Where: https://courses.thinkful.com/data-001v2/project/2.2.1
import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt
import random
import collections
import seaborn as sns

""" #SF#
Lorenzo, this is far better than the previous week. Great work.
I would say that you still have to get used to the python "accepted" syntax, 
but overall, you nailed it.
"""

# LP # I would like to make a comprehensive list but the only solution I could found is:
# LP # is something like [x for x in range(m) for y in range(n)] to repeat the n times x that gives a constant
# LP # repetition value.
#data_set1 = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
#SF# Fair enough, this was a hard one to guess if you haven't seen it before.
#SF# You didn't need comprehension lists, but list properties * and +
data_set1 =  [1,]*8 + [2,]*3 + [3,]*1 + [4,]*4 + [5,]*1 + [6,]*3 + [7,]*8 + [8,]*2 + [9,]*2 

# this is to have a larger data_set
# data_set2 = [random.randint(1,9) for num in range(1000)]
data_set2 = [random.normalvariate(0,1) for num in range(1000)]

# list of counter
data = [data_set1, data_set2]
c = [collections.Counter(x) for x in data]

# calculate the number of instances in the list
count_sum = [sum(c[i].values()) for i in range(2)]

# print the outputs

#SF# In python, use four spaces "    " as indentation, it really pays off in terms of readability.
"""
for i in range(2):
	for k,v in c[i].iteritems():
		#print "The frequency of number in first data set: " + str(k) + " is " + str(float(v) / count_sum[i])
"""
for i in range(2):
    for k,v in c[i].iteritems():
        print "The frequency of number %+.2f in first data set is %.5f" %(k, float(v)/count_sum[i])
        print("The frequency of number {0:+.2f} in first data set is {1:.5f}".format(k, float(v)/count_sum[i]))
        print("")

# Plotting Boxplot, Histogram and QQ-plot

# Some layout code for seaborn package (http://stanford.edu/~mwaskom/software/seaborn/index.html)
sns.set_style('dark')
sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8, 4)})

# Classic boxplot
sns.boxplot(data, names=["data set 1", "data set 2"], color='pastel')
plt.savefig("boxplot.pdf", bbox_inches='tight')
plt.title('Boxplot')
plt.show()

# Violinplot, allowing to compare if two different data set have same distribution
sns.violinplot(data, names=["data set 1", "data set 2"], color='pastel')
sns.despine(offset=10, trim=True);
plt.savefig("violinplot.pdf", bbox_inches='tight')
plt.title('Violinplot')
plt.show()

# Histogram
fig, axs = plt.subplots(1,2, figsize=(10,4), facecolor='w', edgecolor='k')
binning=[9,20]
title=['Data set 1','Data set 2']
#SF# 4 space tab again
for i in range(2):
    sns.distplot(data[i], bins=binning[i],kde=False, ax=axs[i])
    axs[i].set_title(title[i], fontsize=13)
plt.suptitle("Bigger title on top") #SF# Use this if you want a title for both plots
plt.savefig("histogram.pdf", bbox_inches='tight')
plt.show()

# QQ-plot
fig = plt.figure(figsize=(10,6), facecolor='w', edgecolor='k')
distribution=['uniform','norm']
for i in range(2):
    fig.add_subplot(1,2,i+1)
    stats.probplot(data[i],dist=distribution[i], plot=plt)
plt.suptitle("Bigger title on top") #SF# Use this if you want a title for both plots
plt.savefig("qq-plot.pdf", bbox_inches='tight')
plt.show()