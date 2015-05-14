from matplotlib import pyplot as plt
import statsmodels.formula.api as smf
import pandas as pd
import numpy as np

# Generating the data
N = 20
error_scale = 5.0
error = np.random.normal(size=N, loc=0, scale=error_scale)
x = np.linspace(-5,5,N)
y_auxiliar = 1./(1 + np.exp(- (1.5 + 3 * x + error))) 
y_discrete = np.where(y_auxiliar<0.5, 0, 1)

# Generate the pandas dataframe
data = {"x":x, "y_discrete":y_discrete}
df = pd.DataFrame(data)

# Plot the data. What type is it? What should we expect from it?
plt.plot(df["x"], df["y_discrete"], 'sw', label="Measured data")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim([-.1,1.1])
plt.legend(loc="upper left", fontsize=10, numpoints=1)
plt.show()

# Ordinary Least Squares = Linear Regression
model = smf.logit(formula="y_discrete ~ x", data=df)
fitted_model = model.fit()
coeffs = fitted_model.params
print fitted_model.summary()
print "The model obtained is y = 1./(1 + exp(-({0} + {1}*x)))".format(*coeffs)
print coeffs

# Plot the data. What type is it? What should we expect from it?
y_model = fitted_model.predict(df["x"])
y_prediction = np.where(y_model<0.5, 0, 1)
plt.plot(df["x"], df["y_discrete"], 'sw', label="Measured data")
plt.plot(df["x"], y_model, 'o-', label="Obtained prob model")
plt.plot(df["x"], y_prediction, 'xr', label="True predictions")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim([-.1, 1.1])
plt.legend(loc="upper left", fontsize=10, numpoints=1)
plt.show()
