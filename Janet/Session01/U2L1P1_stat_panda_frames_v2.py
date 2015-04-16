# New version of the homework, more appropiate to a general use
# https://courses.thinkful.com/data-001v2/project/2.1.1

import pandas as pd
from scipy import stats

filename = "U2L1P1_stat_panda_frames_v2.csv"
df = pd.read_csv(filename, header=0)
header = list(df)
template = "The {function} for {category} is {value}"
for category in header[1:]:
    frame = df[category] = df[category].astype(float)
    print( template.format( function='mean', category=category, value=frame.mean()) )
    print( template.format( function='mode', category=category, value=stats.mode(frame)[0][0]) )
    print( template.format( function='median', category=category, value=frame.median()) )
    print( template.format( function='standard deviation', category=category, value=frame.std()) )
    print( template.format( function='variance', category=category, value=frame.var()) )
