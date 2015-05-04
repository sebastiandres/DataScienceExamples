
# coding: utf-8

# In[23]:

get_ipython().magic(u'matplotlib inline')


# In[21]:

import pandas as pd
import numpy as np 
from pandas.tools.plotting import autocorrelation_plot
import requests, zipfile, StringIO

r = requests.get('https://resources.lendingclub.com/LoanStats3c.csv.zip')
z = zipfile.ZipFile(StringIO.StringIO(r.content))
filename= 'LoanStats3c.csv'
df = pd.read_csv(z.open(filename),header=1, low_memory=False)

# converts string to datetime object in pandas:
df['issue_d_format'] = pd.to_datetime(df['issue_d']) 
dfts = df.set_index('issue_d_format') 
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']


# #### Test if the time series is stationary
# Here I make an autocorrelation plot of the data. The decay with the lag indicate that the TS is not stationary

# In[24]:

import statsmodels.api as sm
from pandas.tools.plotting import autocorrelation_plot
autocorrelation_plot(loan_count_summary)


# #### Dickey Fuller test
# I can also perform a Dickey Fuller test for presence of unit roots

# In[25]:

test = sm.tsa.adfuller(loan_count_summary.values)
print 'adf: ', test[0] 
print 'p-value: ', test[1]
print 'Critical values: ', test[4]
if test[0] > test[4]['10%']: 
    print 'has unit roots , the series is not stationary'
else:
    print 'has no unit roots , the series is stationary'


# #### Transofrm to a stationary TS
# To transform into a stationary series a can perform a differencing

# In[28]:

loan_count_summary_trans= loan_count_summary.diff()
# loan_count_summary_trans.plot()
autocorrelation_plot(loan_count_summary_trans)
# loan_count_summary_trans.values


# In[29]:

test = sm.tsa.adfuller(loan_count_summary_trans.values)
print 'adf: ', test[0] 
print 'p-value: ', test[1]
print 'Critical values: ', test[4]
if test[0] > test[4]['10%']: 
    print 'has unit roots , the series is not stationary'
else:
    print 'has no unit roots , the series is stationary'

