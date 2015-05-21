# -*- coding: utf-8 -*-
# Why: Logistic Regression
# Where: 

import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
import numpy as np
from IPython import embed as ip

# U2L5P2
df = pd.read_csv('loansData_clean.csv')
df['IR_TF'] = 0 + (df['Interest.Rate'] <= 0.12)
df['Intercept'] = 1
ind_vars = ['Intercept', 'FICO.Score', 'Amount.Requested']
#ind_vars = ['Intercept', 'FICO.Score', 'Amount.Funded.By.Investors']
# Spot checks
df["IR_TF"][df['Interest.Rate'] < 0.10].head() # should all be True
df["IR_TF"][df['Interest.Rate'] > 0.13].head() # should all be False

# U2L5P3
logit = sm.Logit(df['IR_TF'], df[ind_vars])
result = logit.fit()
coeffs = result.params
print coeffs

"""
Write a function called logistic_function that will take a FICO Score and a Loan Amount of this linear predictor, and return p. (Try not to hardcode any values if you can! Hint: pass the coefficients object to the function as an argument.)
"""
def logistic_function(fico_score, loan_amount, coefficients):
    'Calculate the probability to have a given loan with a given fico score\
    at an interest <= 12%'
    b, a1, a2 = coefficients   
    x = b + a1*fico_score + a2*loan_amount
    p = 1./(1.+np.exp(-x))
    return p

# or simply and more general #
def logistic_function2(fico_score, loan_amount, result):
    return result.predict([1., fico_score, loan_amount])

"""
Determine the probability that we can obtain a loan at ≤12% Interest for $10,000 with a FICO score of 720 using this function.
"""
p1 = logistic_function(720, 10000, coeffs)
p2 = logistic_function2(720, 10000, result)

print "Probability that we can obtain a loan at ≤12% Interest for $10,000 with a FICO score of 720"
print "p = ", p1
print "p = ", p2

"""
Is p above or below 0.70? Do you predict that we will or won't obtain the loan?
"""
print "p > 0.70?"
print p1 > 0.70

"""
If you're feeling really adventurous, you can create a new function pred to predict whether or not we'll get the loan automatically.
"""
def prep(fico_score, loan_amount, coefficients):
    return logistic_function(fico_score, loan_amount, coefficients) > 0.70

print "Are we getting a loan at ≤12% Interest for $100,000 with a FICO score of 400"
print prep(400, 100000, coeffs)


"""
Now think critically, does your prediction make sense given the data? Try plotting the data to see if you can see the prediction visually.
 If you cannot find the correlation visually, you might have to re-evaluate your logistic function. 
An example plot can be seen here, created by one of our data science mentors, 
which compares two different equations for the logistic regression. Which one makes more sense?
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Plot your data
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
colors = ["r" if bool(ib12) else "b" for ib12 in df['IR_TF'] ]
ax.scatter(df['FICO.Score'], df['Amount.Requested'],  df['IR_TF'], 
           c=colors)
ax.set_xlabel('FICO SCORE')
ax.set_ylabel('Amount Requested')
ax.set_zlabel('Interest Below 0.12?')
plt.show()

# Plot your data and the surface
xmin = df['FICO.Score'].min()
xmax = df['FICO.Score'].max()
ymin = df['Amount.Requested'].min()
ymax = df['Amount.Requested'].max()
N = 10
x = np.linspace(xmin, xmax, 20)
y = np.linspace(ymin, ymax, 20)
X, Y = np.meshgrid(x,y)
Z = logistic_function(X,Y,coeffs)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
colors = ["r" if bool(ib12) else "b" for ib12 in df['IR_TF'] ]
ax.scatter(df['FICO.Score'], df['Amount.Requested'],  df['IR_TF'], 
           c=colors)
preds = result.predict(df[ind_vars])
ax.scatter(df['FICO.Score'], df['Amount.Requested'],  preds, c="y")
ax.plot_wireframe(X,Y,Z,alpha=0.5)
ax.set_xlabel('FICO SCORE')
ax.set_ylabel('Amount Requested')
ax.set_zlabel('Interest Below 0.12?')
plt.show()
