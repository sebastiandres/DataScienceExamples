from matplotlib import pyplot as plt
import statsmodels.api as sm 
import numpy as np

# Generating the data
N = 20
error_scale = 2.0
x = np.linspace(10,20,N)
y_true = 1.5 + 3 * x 
y_measured = y_true + np.random.normal(size=N, loc=0, scale=error_scale)

# Plot the data. What type is it? What should we expect from it?
plt.plot(x, y_true, '-k', label="True relation")
plt.plot(x, y_measured, 's', label="Measured data")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper left", fontsize=10, numpoints=1)
plt.show()

# Ordinary Least Squares = Linear Regression
X = np.vstack([1+0*x, x]).T   # We need to add the intercept of 1 for the model
#X = np.vstack([x, 1+0*x]).T   # We need to add the intercept of 1 for the model
y = y_measured                # We only have access to the measured quantities
model = sm.OLS(y, X)
fitted_model = model.fit()
coeffs = fitted_model.params
print fitted_model.summary()
print "The model obtained is y = {0} + {1}*x".format(*coeffs)
print coeffs

# Plot the data. What type is it? What should we expect from it?
y_model = coeffs[0]*X[:,0] + coeffs[1]*X[:,1]
plt.plot(x, y_true, '-k', label="True relation")
plt.plot(x, y_measured, 'sw', label="Measured data")
plt.plot(x, y_model, ':r', label="Obtained relationship")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper left", fontsize=10, numpoints=1)
plt.show()

# Prediction: How to use the information
# y(x=15)
fitted_model.predict([1., 15])
# Get all the values
y_prediction = fitted_model.predict(X)
# You can make predictions because you got a model for your data,
# and can now make inferences of values on any point!

# Is it the same?
np.allclose(y_model, y_prediction)
