# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:48:40 2015

@author: lorenzo
"""

import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import seaborn as sns
import numpy as np
import statsmodels.formula.api as smf
import requests, zipfile, StringIO

r = requests.get('https://resources.lendingclub.com/LoanStats3c.csv.zip')
z = zipfile.ZipFile(StringIO.StringIO(r.content))
filename= 'LoanStats3c.csv'
loansData = pd.read_csv(z.open(filename),header=1, low_memory=False)
loansData.dropna(inplace=True)
loansData.int_rate=loansData.int_rate.map(lambda x: round(float(x.rstrip('%'))/100,4))

# LP #
# Plot Annual income versus Interest rate
plt.figure(figsize=(6 * 1.618, 6))
plt.scatter(loansData.annual_inc, loansData.int_rate, s=10, alpha=0.3)
plt.xlabel('Annual Income')
plt.ylabel('Interest rate')
annincome_linspace = np.linspace(loansData.annual_inc.min(), loansData.annual_inc.max(), 100)
y=loansData.int_rate
## fit a OLS model with intercept on Annua Income
x=loansData.annual_inc
X = sm.add_constant(x)
est = sm.OLS(y, X).fit()
# LP # Using formulaic predictor
# formula: response ~ predictor + predictor
est = smf.ols(formula='int_rate ~ annual_inc', data=loansData).fit()
plt.plot(annincome_linspace, est.params[0] + est.params[1]*annincome_linspace, 'r')
plt.show()

# LP # Added home_ownership without interaction
plt.figure(figsize=(10, 6))
plt.scatter(loansData.annual_inc, loansData.int_rate, s=10, alpha=0.3)
plt.xlabel('Annual Income')
plt.ylabel('Interest rate')
mod = smf.ols("int_rate ~ annual_inc + C(home_ownership)", data=loansData)
est_b=mod.fit()
plt.plot(annincome_linspace, est_b.params[0] + est_b.params[3]*annincome_linspace + est_b.params[1] * 0, 'r')
plt.plot(annincome_linspace, est_b.params[0] + est_b.params[3]*annincome_linspace + est_b.params[1] * 1, 'g')
plt.plot(annincome_linspace, est_b.params[0] + est_b.params[3]*annincome_linspace + est_b.params[2] * 1, 'y')
plt.show()

# LP # Added home_ownership with interaction
plt.figure(figsize=(10, 6))
plt.scatter(loansData.annual_inc, loansData.int_rate, s=10, alpha=0.3)
plt.xlabel('Annual Income')
plt.ylabel('Interest rate')
mod2 = smf.ols("int_rate ~ annual_inc * C(home_ownership)", data=loansData)
est_c=mod2.fit()
plt.plot(annincome_linspace, est_c.params[0] + est_c.params[3]*annincome_linspace + est_c.params[1] * 0 + est_c.params[4]*0*annincome_linspace, 'r')
plt.plot(annincome_linspace, est_c.params[0] + est_c.params[3]*annincome_linspace + est_c.params[1] * 1 + est_c.params[4]*1*annincome_linspace, 'g')
plt.plot(annincome_linspace, est_c.params[0] + est_c.params[3]*annincome_linspace + est_c.params[2] * 1 + est_c.params[5]*1*annincome_linspace, 'y')
plt.show()