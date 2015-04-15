import pandas as pd
from scipy import stats



british_data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''



if __name__ == '__main__':
    data = [ line.split(',') for line in british_data.splitlines()]
    header = data.pop(0)
    print(header)

    df = pd.DataFrame(data, columns=header)

    template = "The {function} for {category} is {value}"

    for category in header[1:]:
        frame = df[category] = df[category].astype(float)
        print( template.format( category=category, function='mean', value=frame.mean()) )
        mode_value  = stats.mode(frame)
        print( template.format( category=category, function='mode', value=mode_value[0][0]) )
        print( template.format( category=category, function='median', value=frame.median()) )
        print( template.format( category=category, function='standard deviation', value=frame.std()) )
        print( template.format( category=category, function='variance', value=frame.var()) )
        print( "\n" )
