# Where: https://courses.thinkful.com/data-001v2/project/2.2.1
'''
Challenge
Write a script called "prob.py" that outputs frequencies,
 as well as creates and saves a boxplot, a histogram,
 and a QQ-plot for the data in this lesson.
  Make sure your plots have names that are reasonably descriptive.
  Push your code to GitHub and enter the link below.
'''
""" #SF#
This is great and very well written. Congrats.
I would just add some labels and titles, 
as we would in a true stat request.
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import pdb


def draw_boxplot(dataset):
    plt.boxplot(dataset)
    plt.xlabel("xlabel here")
    plt.ylabel("ylabel here")
    plt.show()

def draw_histogram(dataset):
    plt.hist(dataset, histtype='bar')
    plt.xlabel("xlabel here")
    plt.ylabel("ylabel here")
    plt.show()

def draw_qq_plot(dataset, xlabel="", ylabel="", title=""):
    plt.figure()
    stats.probplot(dataset, dist="norm", plot=plt)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


#test_data = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
# If you're lazy like me, you can also use
test_data =  [1,]*8 + [2,]*3 + [3,]*1 + [4,]*4 + [5,]*1 + [6,]*3 + [7,]*8 + [8,]*2 + [9,]*2

draw_histogram(test_data)
draw_boxplot(test_data)
draw_qq_plot(test_data, title="test data")

# JR: the lesson compared two QQ plots, one normal and one uniform
# Let's see what those look like alongside our test data, for yucks
draw_qq_plot(np.random.normal(size=len(test_data)), xlabel="xlabel", title="normal distribution")
draw_qq_plot(np.random.uniform(size=len(test_data)), ylabel="ylabel", title="uniform distribution")

#SF# Notice how in all cases R^2 is very high? Never trust ONLY R^2! It's very misleading...
