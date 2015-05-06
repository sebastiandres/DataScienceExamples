# -*- coding: utf-8 -*-
# Why:
# Where:
"""
Created on Tue Apr 28 14:01:19 2015

@author: lorenzo
"""

import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import seaborn as sns
import numpy as np

filename='dat/loansData_clean.csv'
loansData = pd.read_csv(filename)
loansData['Interest.Score'] = (loansData['Interest.Rate'] <= 0.12)
loansData['Interest.Score'] = pd.get_dummies(loansData['Interest.Score'] <= 0.12, prefix='int')
loansData['Intercept'] = 1

ind_vars=list(loansData)
ind=[0,14,16]
ind_vars=[ind_vars[i] for i in ind]

logit = sm.Logit(loansData['Interest.Score'], loansData[ind_vars])
result = logit.fit()

# LP # 
# Problem set: What is the probability of getting a loan from the 
# Lending Club for $10,000 at an interest rate ≤ 12% with a FICO score of 750?

def logistic_function(fs,la):
    'Calculate the probability to have a given loan with a given fico score\
    at an interest <= 12%'
    cla,cfs,inter=result.params    
    IR = (inter) + (cfs*fs) + (cla*la)
    p = 1/(1+np.exp(IR))
    print 'The probability of getting a loan for {0} at an interest rate of '\
    '12% or less with a FICO score of {1} is {2:.4%}.'.format(la,fs,p)
    print cla
    print cfs
    print inter
    print IR
    return


logistic_function(750,10000)
logistic_function(720,10000)

# LP #
# Graphic one 
rp=sns.lmplot( "Amount.Funded.By.Investors","FICO.Score", loansData, hue="Interest.Score",palette="Set1");
plt.xlim(0,)

# LP # 
# Regression plot showing the Amount funded fonction of the FICO Score. The dots are labelled by the Interest Score,
# i.e., blue dots are for interest <= 12%. This plot clearly shows that:
# 1.   There is a correlation between interest rate, the FICO score and the amount funded. For example, for a loan
#      of 10000$ the recipients that have a FICO score of 700 have an interest rate of <=12% (blue dots). However,
#      For lower FICO  score the interest should be much higher (red dots).
# 2.   The prediction for a 10000$ loan with an interest rate of <= 12% should be > 0.7 for both
#      FICO score of 720 and 750. 


# Graphic two

# I select only 10000$ funded amount
t=loansData.loc[loansData['Amount.Funded.By.Investors'].isin([10000])]

rp=sns.lmplot( "FICO.Score","Interest.Score", t,palette="Set1",logistic=True,y_jitter=.05);

# LP # 
# Regression plot showing the FICO Score in function of the Interest.Rate (binary value 0,1) for loan of 1000$
# This graph show that for FICO Score greater than about 710 and for a loan of 10000$ an interest of <=12 % is given
# 
