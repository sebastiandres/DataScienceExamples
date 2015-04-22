"""
Utility functions for manipulating the Lending Club data set in Unit 2
"""
import os
import pandas as pd

def fetch_data_frame():
    """
    Loads the Lending Club data with some minimal scrubbing
    :return:a pandas data frame
    """
    # load and scrub data
    data_filepath = os.path.join('data', 'loansData.csv')
    loans_data = pd.read_csv(data_filepath)
    loans_data.dropna(inplace=True)
    return loans_data


def get_low_FICO_score(score):
    """
    :param score: a FICO range, in the format low_num-high_num
    :return: the low number as an int
    """
    (low, high) = score.split('-')
    return int(low)


def scrub_interest_rate(df):
    """
    Converts the interest rate column from "value%" back to floats
    :param df: a pandas data frame
    :return: pandas data frame, Interest.Rate column cleaned up in place
    """
    # JR - took the tutorial's suggestion to round
    df['Interest.Rate'] = map( lambda x: round(float(x.rstrip('%'))/100, 4),
                               df['Interest.Rate'])

def add_FICO_score( df ):
    """
    Adds a FICO score column to the data frame
    :param df: a pandas data frame
    :return:
    """
    df['FICO.Score'] = map( lambda x: get_low_FICO_score(x), df['FICO.Range'])



