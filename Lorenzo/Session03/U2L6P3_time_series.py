# coding: utf-8
# Why
# Where: 	
import pandas as pd
import numpy as np 
from pandas.tools.plotting import autocorrelation_plot
from matplotlib import pyplot as plt # SF: Important!

# 'LoanStats3c.csv' should be downloaded and unziped from https://resources.lendingclub.com/LoanStats3c.csv.zip 
df = pd.read_csv('LoanStats3c.csv', header=1, low_memory=False)
df=df.dropna(subset = ['issue_d']) #SF#

# converts string to datetime object in pandas:
df['issue_d_format'] = pd.to_datetime(df['issue_d'])
dfts = df.set_index('issue_d_format')
# Why would we want this? Explain...
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()

loan_count_summary = year_month_summary['issue_d']
loan_count_summary.to_csv("LoanStatsGrouped.csv", index=True) # We can read later more rapidly
#loan_count_summary = pd.read_csv('LoanStatsGrouped.csv')

# What do we really care? Just the y values
y = loan_count_summary.values

plt.plot(y)
plt.suptitle("the values")
plt.show()

# Test if the time series is stationary
# Here I make an autocorrelation plot of the data. The decay with the lag indicate that the TS is not stationary
import statsmodels.api as sm
from pandas.tools.plotting import autocorrelation_plot
autocorrelation_plot(y)
plt.suptitle("Original series")
plt.savefig("TS.pdf")
#plt.show()

# #### Dickey Fuller test
# I can also perform a Dickey Fuller test for presence of unit roots
test = sm.tsa.adfuller(y)
print 'adf: ', test[0] 
print 'p-value: ', test[1]
print 'Critical values: ', test[4]
if test[0] > test[4]['10%']: 
    print 'has unit roots , the series is not stationary'
else:
    print 'has no unit roots , the series is stationary'

sm.graphics.tsa.plot_acf(y)
plt.show()

sm.graphics.tsa.plot_pacf(y)
plt.show()

"""
# #### Transofrm to a stationary TS
# To transform into a stationary series a can perform a differencing

loan_count_summary_trans = loan_count_summary.diff()
y2 = loan_count_summary_trans.diff()
# loan_count_summary_trans.plot()
autocorrelation_plot(y2)
# loan_count_summary_trans.values
plt.suptitle("Differenciated series")
plt.savefig("TS_diff.pdf")
#plt.show()

# In[29]:

test = sm.tsa.adfuller(y2)
print 'adf: ', test[0] 
print 'p-value: ', test[1]
print 'Critical values: ', test[4]
if test[0] > test[4]['10%']: 
    print 'has unit roots , the series is not stationary'
else:
    print 'has no unit roots , the series is stationary'
"""
