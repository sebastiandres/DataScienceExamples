# Linear Regression Analysis
# https://courses.thinkful.com/data-001v2/project/2.3.3

import numpy as np
import statsmodels.api as sm
import lending_club_utils as utils


# load and scrub
loans_data = utils.fetch_data_frame()
utils.add_FICO_score(loans_data)
utils.scrub_interest_rate(loans_data)

# Calculate our model
interest_rate = loans_data['Interest.Rate']
loan_amount = loans_data['Amount.Requested']
fico = loans_data['FICO.Score']

y = np.matrix(interest_rate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loan_amount).transpose()

x = np.column_stack([x1, x2])

all_X = sm.add_constant(x)
model = sm.OLS(y, all_X)
f = model.fit()

# JR - interesting - my results came back in a different order
# than the example in the tutorial.
# Googled for the library, and it looks like params() returns a variable, unordered list
# of .. ? ... magic numbers.
# Sent a bug report to Thinkful.


print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared
