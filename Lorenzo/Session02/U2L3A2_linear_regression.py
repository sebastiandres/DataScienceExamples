# Clean and plot data
# https://courses.thinkful.com/data-001v2/assignment/2.3.2

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import collections
import seaborn as sns
from sklearn import datasets


filename='dat/loansData.csv'
loansData = pd.read_csv(filename)
loansData.dropna(inplace=True)

# Interest.Rate clean up
loansData['Interest.Rate']=loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%'))/100,4))

# Loan.Length clean up
loansData['Loan.Length']=loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))

#FICO.Range to FICO.Score
step_string=loansData['FICO.Range'].map(lambda x: x.split('-'))
step_int=step_string.map(lambda x: [int(n) for n in x])
loansData['FICO.Score']=step_int.map(lambda x: min(x))

# Histogram

ax=sns.distplot(loansData['FICO.Score'], bins=9,kde=True,fit=stats.norm)
plt.autoscale(tight='x')
plt.savefig("histogram.pdf", bbox_inches='tight')


# Scatter matrix

g = sns.PairGrid(loansData)
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)
plt.savefig('test.pdf')
