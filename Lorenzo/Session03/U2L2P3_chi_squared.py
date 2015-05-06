# Visualizing Lending Club Data
# https://courses.thinkful.com/data-001v2/project/2.2.3

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import collections
import seaborn as sns

filename='dat/loansData.csv'
loansData = pd.read_csv(filename)
loansData.dropna(inplace=True)
freq = collections.Counter(loansData['Open.CREDIT.Lines'])

# graph the data
ax = sns.barplot(loansData['Open.CREDIT.Lines'], color=".5")
ax.set_xlabel('credit lines')
plt.show()


# Chi-squared test

# LP # The question is: Does the data look evenly distributed
# LP # Why not to test the distribution itself instead of their frequency?

# LP # scipy.stats.chisquare tell me that: 'When just f_obs is given, it is 
# LP # assumed that the expected frequencies are uniform and given by the mean 
# LP # of the observed frequencies'

# LP # So my solution could be simply:
chi, p = stats.chisquare(loansData['Open.CREDIT.Lines'])
print 'The chi-squared is {0:.3f} and the p-value is {1:.3f}'.format(chi,p)

# SF # Then why does it differs from 
chi, p = stats.chisquare(freq.values())
print 'The chi-squared is {0:.3f} and the p-value is {1:.3f}'.format(chi,p)


