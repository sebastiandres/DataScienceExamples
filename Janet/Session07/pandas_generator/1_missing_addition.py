#!/usr/bin/env python
# coding: utf-8
import pandas as pd

df1 = pd.DataFrame([(1,2),(4,5)], columns=['a','b'])
print(df1)
df2 = pd.DataFrame([(10,20,30),(40,50,60),(70,80,90)], columns=['a','b','c'])
print(df2)
df_12 = df1.add(df2, fill_value=0)
print(df_12)
df_21 = df2.add(df1, fill_value=0)
print(df_21)

# Make a iterated sum
df = pd.DataFrame()
print(df)
for i in range(5):
    df = df.add(df1, fill_value=0)
print(df)
