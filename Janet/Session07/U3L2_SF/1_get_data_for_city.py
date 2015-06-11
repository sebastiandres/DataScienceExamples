from core import weather_utils
import sys

def main():
    if len(sys.argv)<2:
        print("Please provide the city")
	return sys.exit(-1)
    elif len(sys.argv)>2:
        print("Please provide only the city")
	return sys.exit(-1)
    else:
	city = sys.argv[1]
	weather_utils.populate_30_days(city)

if __name__=="__main__":
    main()
