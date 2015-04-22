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

import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
import os as os

def draw_boxplot(data_frame, col_name):
    data_frame.boxplot(column=col_name)
    plt.savefig(col_name + '_boxplot.png')
    plt.show()

def draw_histogram(data_frame, col_name):
    # JR: how does it decide interval size?
    data_frame.hist(column=col_name)
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