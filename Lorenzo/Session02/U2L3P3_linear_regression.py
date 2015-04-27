# Clean and plot data + regression analysis
# https://courses.thinkful.com/data-001v2/assignment/2.3.2 and
# https://courses.thinkful.com/data-001v2/assignment/2.3.3

import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import seaborn as sns
import numpy as np


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
# Since the whole matrix have some problem to be plotted on mac os x I'll plot only 
# the 3 variables

g = sns.PairGrid(loansData,vars=["Amount.Requested", "Interest.Rate","FICO.Score"])
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)
plt.savefig('scatter_matrix.pdf')


# LP # Regression plot as the graph in notes. The results is slightly different 
# LP # as i only consider values for 10k and 30k
t=loansData.loc[loansData['Amount.Requested'].isin([10000,30000])]
sns.lmplot("FICO.Score", "Interest.Rate", t, hue="Amount.Requested");
plt.ylim(0,)
plt.savefig('regression_plot.pdf')



intrate = np.matrix(loansData['Interest.Rate']).transpose()
loanamt = np.matrix(loansData['Amount.Requested']).transpose()
fico = np.matrix(loansData['FICO.Score']).transpose()

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
#x1 = np.matrix(fico).transpose()
#x2 = np.matrix(loanamt).transpose()

x = np.column_stack([fico,loanamt])

X = sm.add_constant(x)
model = sm.OLS(intrate,X)
f = model.fit()


# LP #  Coefficient and intercepts differs from those of the data, 
# LP #  maybe caused by the choice of the FICO.Score ?!?!
print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared