
#SF# Don't forget the headers, if possible
# Why: Required code, mix pandas, formatting and lists.
# Where: https://courses.thinkful.com/data-001v2/project/2.1.1

#SF# I think that overall this is great, it accomplish the required task
#SF# There are some small "eficiency" tips I would like to introduce.
#SF# They took me a while to learn, but I want to share them asap,
#SF$ So you can be more efficient

import pandas as pd
from scipy import stats

#SF# Great, I like importing too
#df=pd.read_csv('dat/alcohol_tobacco_uk.csv')
#SF# But it would be better to have the flexibility to copy and paste code, so better use two lines. 
#SF# This is really optional. 
filename = "dat/alcohol_tobacco_uk.csv"
df=pd.read_csv(filename)

#SF# I would advice to save the rounding to the end. It's actually the printing of the number
#SF# You want to control, not the number itself.
#SF# Also, comprehension list can save lots of space!!!
tables = [df.Alcohol, df.Tobacco]
mean = [x.mean() for x in tables]
median = [x.median() for x in tables]
mode = [stats.mode(x)[0][0] for x in tables]
range1 = [x.max() for x in tables]
variance = [x.var() for x in tables]
std = [x.std() for x in tables] # or [(x)**.5 for x in variance] # As str**2 = var
desc_stat = [mean, median, mode, range1, variance, std]
text= ['mean', 'median', 'mode', 'range1', 'variance', 'standard deviation']

# This works, and it's ok. We can control the precision on the formatting
print "Almost correct"
for i in range(len(text)):
    # Control value directly on print
    print('The {0} for the Alcohol and Tobacco dataset is {1:.2f} and {2:.2f}'.format(text[i], desc_stat[i][0], desc_stat[i][1]))


# Iterate directly over the values, this is a huge gain in clarity but can be hard to understand
# This might be too advanced, but we can see the details next session.
print "A little better"
for function_name, (value_alcohol, value_tobacco) in zip(text, desc_stat):
    # Control value before passing on print
    all_values = ( function_name, round(value_alcohol,2), round(value_tobacco,2) )
    print('The {0} for the Alcohol and Tobacco dataset is {1} and {2}'.format(*all_values))
    #OBS# print wont't work if the * is not present in *all_values
    # this is called unpacking a list
    #print('The {0} for the Alcohol and Tobacco dataset is {1} and {2}'.format(all_values)) # NOT WORKING
