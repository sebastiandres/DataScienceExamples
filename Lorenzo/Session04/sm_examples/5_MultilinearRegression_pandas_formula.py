from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import statsmodels.formula.api as smf # This is different #
import pandas as pd
import numpy as np

# Generating the data
N1, N2 = 10, 5
x1 = np.linspace(10,20,N1)
x2 = np.linspace(-5,5,N2)
x1, x2 = np.meshgrid(x1,x2)
y_true = 15 + (3 * x1) + (5 * x2)  # try np.power
error_scale = 8.0
error = np.random.normal(size=x1.shape, loc=0, scale=error_scale)
y_measured = y_true + error

# Generate the pandas dataframe
data = {"x1":x1.flatten(), "x2":x2.flatten(), 
        "y_measured":y_measured.flatten(), "y_true":y_true.flatten()}
df = pd.DataFrame(data)

# Plot the data. What type is it? What should we expect from it?
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['x1'], df['x2'],  df['y_measured'], "y measured")
ax.plot_trisurf(df['x1'], df['x2'],  df['y_true'], label="True relation", color="y", alpha=0.25)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
plt.legend(loc="upper left", fontsize=10, numpoints=1)
plt.show()

# Ordinary Least Squares = Linear Regression
model = smf.ols(formula="y_measured ~ x1 + x2", data=df)
fitted_model = model.fit()
coeffs = fitted_model.params
print fitted_model.summary()
print "The model obtained is y = {0} + {1}*x1 + {1}*x2".format(*coeffs)
print coeffs

# Plot the data. What type is it? What should we expect from it?
y_model = fitted_model.predict(df[["x1","x2"]])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['x1'], df['x2'],  df['y_measured'], "y measured")
ax.plot_trisurf(df['x1'], df['x2'],  df['y_true'], label="True relation", color="y", alpha=0.25)
ax.plot_trisurf(df['x1'], df['x2'],  y_model, label="Model",color="r", alpha=0.25)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
plt.legend(loc="upper left", fontsize=10, numpoints=1)
plt.show()
