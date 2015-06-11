import pandas as pd
import data_source #as data_source #SF# no need to rename then!

def load_30_days():
    """
    Load data from the last 30 days from the data source
    :return: json of the last 30 days
    """
    return data_source.load_30_days()


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



def populate_30_days():
    """
    Request weather data for the last 30 days.
    :return: None
    """
    CITIES = {"Atlanta": (33.762909, -84.422675),
              "Austin": (30.303936, -97.754355),
              "Boston": (42.331960, -71.020173),
              "Chicago": (41.837551, -87.681844),
              "Cleveland": (41.478462, -81.679435)
              }

    for days_past in range(0, 30):
        data_source.fetch_weather_data(CITIES['Boston'], days_past)

# * ============= MAIN ======================* #

if __name__ == '__main__':
    # Run the file directly to pull down the data files
    # This happens once, so __main__ is fine.
    print('Populating data...')
    populate_30_days()
