from core import weather_utils as wu
import sys

def visualize(city):
    # Read dataset
    content = wu.load_30_days(city)
    
    # Pull out daily and hourly data
    daily = wu.extract_daily_from_json(content)
    max_values = {
        'Highest': daily['temperatureMax'].max(),
        'Lowest': daily['temperatureMax'].min(),
        'Mean': daily['temperatureMax'].mean(),
        'Median': daily['temperatureMax'].median(),
        'Greatest Change': daily['changeMax'].max(),
        'Smallest Change': daily['changeMax'].min(),
    }
    min_values = {
        'Highest': daily['temperatureMax'].max(),
        'Lowest': daily['temperatureMax'].min(),
        'Mean': daily['temperatureMax'].mean(),
        'Median': daily['temperatureMax'].median(),
        'Greatest': daily['changeMax'].max(),
        'Smallest': daily['changeMax'].min(),
    }

    print "%s WEATHER\n" %city.upper()
    print "Daily Highest Temperature"
    for key in max_values.keys():
        print("\t{0:20s}: {1:.1f} [F]".format(key, max_values[key]))
    print "Daily Lowest Temperature"
    for key in min_values.keys():
        print("\t{0:20s}: {1:.1f} [F]".format(key, min_values[key]))
    return sys.exit(0)

def main():
    if len(sys.argv)<2:
        print("Please provide the city")
	return sys.exit(-1)
    elif len(sys.argv)>2:
        print("Please provide only the city")
	return sys.exit(-1)
    else:
	city = sys.argv[1]
        # Do stuff
        visualize(city)

if __name__=="__main__":
    main()
