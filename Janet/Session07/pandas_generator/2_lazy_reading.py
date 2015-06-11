#!/usr/bin/env python
# coding: utf-8

# See http://pandas.pydata.org/pandas-docs/dev/io.html#iterating-through-files-chunk-by-chunk
# Download csv files from http://seanlahman.com/baseball-archive/statistics/
# Or https://support.spatialkey.com/spatialkey-sample-csv-data/

# This requires pandas > 0.13 #
import pandas as pd

filename = 'Fielding.csv'
tag = "POS"

# Mission, we want to find the 3 most common occurrences of tag in the csv file

###############################################################################
# Read whole file in memory
###############################################################################
table_1 = pd.read_table(filename, sep=',')
print(type(table_1))
#print(table_1.head())

subtable_1 = table_1.groupby(tag)[[tag]].count()
print("Most common {0}".format(tag))
print(subtable_1)

###############################################################################
# Read by chunks, version 1
###############################################################################
table_2_reader = pd.read_table(filename, sep=',', chunksize=1024) # Read by 1024 lines at the time
print(type(table_2_reader))
#print(table_2.head())  # This fails, no head as type is a reader-iterator

subtable_2 = None # Empty dataframe
for chunk in table_2_reader:
    if subtable_2 is None:
        subtable_2= chunk.groupby(tag)[[tag]].count()
    else:
	new_subtable = chunk.groupby(tag)[[tag]].count()
        subtable_2 = subtable_2.add(new_subtable, fill_value=0)
print("Most common {0}".format(tag))
print(subtable_2)

###############################################################################
# Read by chunks, version 2
###############################################################################
table_3_reader = pd.read_table(filename, sep=',', iterator=True) # Read by 1024 lines at the time
print(type(table_2_reader))
#print(table_2.head())  # This fails, no head as type is a reader-iterator

subtable_3 = pd.DataFrame() # Empty dataframe
for chunk in table_3_reader:
    new_subtable = chunk.groupby(tag)[[tag]].count()
    subtable_3 = subtable_3.add(new_subtable, fill_value=0)
print("Most common {0}".format(tag))
print(subtable_3)
