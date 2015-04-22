#https://courses.thinkful.com/data-001v2/project/2.2.1
'''
Challenge
Write a script called "prob.py" that outputs frequencies,
 as well as creates and saves a boxplot, a histogram,
 and a QQ-plot for the data in this lesson.
  Make sure your plots have names that are reasonably descriptive.
  Push your code to GitHub and enter the link below.
'''

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import pdb


def draw_boxplot(dataset):
    plt.boxplot(dataset)
    plt.show()

def draw_histogram(dataset):
    plt.hist(dataset, histtype='bar')
    plt.show()

def draw_qq_plot(dataset):
    plt.figure()
    stats.probplot(dataset, dist="norm", plot=plt)
    plt.show()


test_data = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

draw_histogram(test_data)
draw_boxplot(test_data)
draw_qq_plot(test_data)

# JR: the lesson compared two QQ plots, one normal and one uniform
# Let's see what those look like alongside our test data, for yucks
draw_qq_plot(np.random.normal(size=len(test_data)))
draw_qq_plot(np.random.uniform(size=len(test_data)))

