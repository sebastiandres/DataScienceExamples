from matplotlib import pyplot as plt
#import statsmodels.api as sm 
import statsmodels.formula.api as smf # This is different #
import pandas as pd
import numpy as np

# Generating the data
N = 20
error_scale = 2.0
x = np.linspace(10,20,N)
y_true = 1.5 + 3 * x 
y_measured = y_true + np.random.normal(size=N, loc=0, scale=error_scale)

# Generate the pandas dataframe
data = {"x":x, "y_measured":y_measured, "y_true":y_true}
df = pd.DataFrame(data)

# Plot the data. What type is it? What should we expect from it?
plt.plot(df["x"], df["y_true"], '-k', label="True relation")
plt.plot(df["x"], df["y_measured"], 's', label="Measured data")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper left", fontsize=10, numpoints=1)
plt.show()

# Ordinary Least Squares = Linear Regression
model = smf.ols(formula="y_measured ~ x", data=df)
fitted_model = model.fit()
coeffs = fitted_model.params
print fitted_model.summary()
print "The model obtained is y = {0} + {1}*x".format(*coeffs)
print coeffs

# Plot the data. What type is it? What should we expect from it?
y_model = fitted_model.predict(df["x"])
plt.plot(df["x"], df["y_true"], '-k', label="True relation")
plt.plot(df["x"], df["y_measured"], 'sw', label="Measured data")
plt.plot(df["x"], y_model, ':r', label="Obtained relationship")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper left", fontsize=10, numpoints=1)
plt.show()
