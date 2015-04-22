import pandas as pd
from scipy import stats

raw_data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data = raw_data.splitlines()

values = [ raw.split(', ') for raw in data ]

header = values.pop(0)
#print(values)
#print(header)
df = pd.DataFrame(values, columns=header)
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)


print(df['Alcohol'].mean())
print(df['Alcohol'].median())
print(stats.mode(df['Alcohol']))
print(df['Tobacco'].mean())
print(df['Tobacco'].median())
print(stats.mode(df['Tobacco']))
#Why are these the modes? There were no repeated values



