import pandas as pd
from scipy import stats

df=pd.read_csv('dat/alcohol_tobacco_uk.csv')

mean = [round(df.Alcohol.mean(),2),round(df.Tobacco.mean(),2)]
median = [round(df.Alcohol.median(),2),round(df.Tobacco.median(),2)]
mode = [stats.mode(df.Alcohol)[0][0],stats.mode(df.Tobacco)[0][0]]
range1 = [round((df.Alcohol.max()-df.Alcohol.min()),2),round((df.Tobacco.max()-df.Tobacco.min()),2)]
variance = [round(df.Alcohol.var(),2),round(df.Tobacco.var(),2)]
std = [round(df.Alcohol.std(),2),round(df.Tobacco.std(),2)]

desc_stat=[mean,median,mode,range1,variance,std]
text= ['mean','median','mode','range1','variance','standard deviation']
for i in range(len(text)):
	print('The {0} for the Alcohol and Tobacco dataset is {1} and {2}'.format(text[i],desc_stat[i][0],desc_stat[i][1]))