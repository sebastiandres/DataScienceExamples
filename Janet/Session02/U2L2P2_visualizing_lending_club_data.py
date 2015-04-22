# Visualizing Lending Club Data
# https://courses.thinkful.com/data-001v2/project/2.2.2

'''
Challenge

Write a script called "prob_lending_club.py" that reads in the loan data,
 cleans it, and loads it into a pandas DataFrame. Use the script to generate
 and save a boxplot, histogram, and QQ-plot for the values in the
 "Amount.Requested" column. Be able to describe the result and how it compares
 with the values from the "Amount.Funded.By.Investors".
'''

""" #SF#
This is again very well written.
You're good at coding, so I want you to try go beyond the formal request of the homework.
If you really had to present this information in a meeting, how would you proceed?
In my case, I would present always the two plots side by side, left the amount funded
and right the amount requested, so comparing the two is natural. 
I didn't wanted to do it here because  I would have to do massive 
internal changes.
"""

import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
import os as os

from IPython import embed as ip

def draw_boxplot(data_frame, col_name):
    data_frame.boxplot(column=col_name)
    plt.savefig(col_name + '_boxplot.png')
    plt.show()

def draw_histogram(data_frame, col_name):
    # JR: how does it decide interval size?
    # SF: The number of bins is defaulted to 10,
    # SF: the bins range from min to max,
    # SF: and you can change this using the optional argument!
    # SF: Use IPython library to jump into the functions and ask help on new functions.
    data_frame.hist(column=col_name, bins=20, color="r")
    plt.savefig(col_name + '_histogram.png')
    plt.show()

def draw_qqplot(data_frame, col_name):
    plt.figure()
    stats.probplot(data_frame[col_name], dist="norm", plot=plt)
    plt.savefig(col_name + '_qqplot.png')
    plt.show()

############### MAIN

# load and scrub data
data_filepath = os.path.join('data','loansData.csv')
loansData = pd.read_csv(data_filepath)
loansData.dropna(inplace=True)

# graph amounts funded
amt_funded = 'Amount.Funded.By.Investors'
draw_boxplot(loansData, amt_funded)
draw_histogram(loansData, amt_funded)
draw_qqplot(loansData, amt_funded)

# graph amounts requested
amt_requested = 'Amount.Requested'
draw_boxplot(loansData, amt_requested)
draw_histogram(loansData, amt_requested)
draw_qqplot(loansData, amt_requested)
