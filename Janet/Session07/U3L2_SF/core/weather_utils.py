import pandas as pd
import data_source

import json
import sys
import os

DATA_DIR = "./data"

# Main function in preprocessing
def populate_30_days(city):
    """
    Request weather data for the last 30 days.
    :return: None
    """
    city = city.title()
    print("Updating data...")
    CITIES = {"Atlanta": (33.762909, -84.422675),
              "Austin": (30.303936, -97.754355),
              "Boston": (42.331960, -71.020173),
              "Chicago": (41.837551, -87.681844),
              "Cleveland": (41.478462, -81.679435)
              }

    if city not in CITIES.keys():
	print("Coordinates not found for city %s"%city)
	print("Please try: %s" %(", ".join(CITIES.keys())))
	return sys.exit(-1)
    # Otherwise, we can surely ask for the data
    for days_past in range(0, 30):
        data_source.fetch_weather_data(CITIES[city], days_past, city)
    return

# Most important function in processing


# Most important function in post processing
def load_30_days(city='Boston'):
    """
    load the last 30 days of data.
    The file boston_last_30.json was compiled manually from the daily json files
    From the command line,
       cat 42*json >> boston_last_30.json
    followed by correcting the json in emacs, to wit:
        * separating entries with commas
        * enclosing the json with an opening [ and ending ]
    Possible to script in python, but much faster by hand

    :return: Forecast.io json data for 30 days
    """
    city = city.title()
    datafile = os.path.join(DATA_DIR, city, "last_30.json")
    with open(datafile) as json_src:
        content = json.load(json_src)
        return content

# *============= DATA MUNGING =========* #

def extract_daily_from_json(content):
    """
    Given a Forecast.io json response, pull out all the Daily data
    :param content: json response from Forecast.io
    :return: a data frame containing the json from daily:{...}
    """
    dailies = []
    for item in content:
        dailies.extend(item['daily']['data'])

    df = pd.DataFrame(dailies)
    df.sort(columns='apparentTemperatureMinTime', ascending=True, inplace=True)
    add_temp_deltas(df)
    return df


def extract_hourly_from_json(content):
    """
    Given a Forecast.io json response, pull out all the Hourly data
    :param content: json response from Forecast.io
    :return: a data frame containing the json from hourly:[{...}]
    """
    hourlies = []
    for item in content:
        hourlies.extend(item['hourly']['data'])
    hourly_df = pd.DataFrame(hourlies)
    return hourly_df

def add_temp_deltas(data):
    """
    Calculate the change in max and min temps between days

    :param data: a data frame sorted in ascending date order
    :return: data with changeMax and changeMin columns
    """
    last = None
    deltaMax = []
    deltaMin = []

    for index, item in data.iterrows():
        if last is None:
            deltaMax.append(0)
            deltaMin.append(0)
        else:
            deltaMax.append(abs(item['temperatureMax'] - last['temperatureMax']))
            deltaMin.append(abs(item['temperatureMin'] - last['temperatureMin']))

        last = item

    data['changeMax'] = [x for x in deltaMax]
    data['changeMin'] = [y for y in deltaMin]

