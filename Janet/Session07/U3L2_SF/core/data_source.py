import forecast_io as forecast

import datetime
import json
import os

# Data_source is responsible for getting the weather data
#
# I saved Forecast.io json responses to file and skipped using a database.
# I'd switch to a database if I were working with more date ranges
# or using SQL for some of the analysis, like min and max.
#
# If the file is present, data_source will load from file.
# If missing, it will fetch from Forecast.io .


DATA_DIR = "./data"

# *============== GENERAL =========* #


def calculate_unix_timestamp(days_offset):
    """
    Calculate a unix timestamp to use in filenames
    :param days_offset: how many days prior to now
    :return:
    """
    when = datetime.datetime.utcnow()
    when = when - datetime.timedelta(days=days_offset,
                                     hours=when.hour,
                                     minutes=when.minute,
                                     seconds=when.second,
                                     microseconds=when.microsecond)
    epoch_seconds = (when - datetime.datetime(1970,1,1)).total_seconds()
    return int(epoch_seconds)


def fetch_weather_data(lat_lon, days_offset, city):
    """
    Read weather data from file cache.
    If missing, fetch from Forecast.io and save to cache.
    :param lat_lon: latitude/longitude of a location
    :param days_offset: how many days prior to today?
    :return: json forecast.io prediciton for day
    """
    timestamp = calculate_unix_timestamp(days_offset)
    obj = get_cached_response(lat_lon, timestamp, city)
    if not obj:
        print "Fetching data the old fashioned way"
        obj = forecast.request_data(lat_lon, timestamp)
        write_to_cache(obj, lat_lon, timestamp, city)
    return obj


# *================ CACHED DATA ========* #

def cache_filepath(lat_lon, timestamp, city):
    return os.path.join(DATA_DIR, city, "%f,%f,%d.json" % (lat_lon[0], lat_lon[1], timestamp))


def get_cached_response(lat_lon, timestamp, city):
    """
    Fetch json from file cache
    :param lat_lon: lat/lon of location
    :param timestamp: time requested
    """
    try:
        with open(cache_filepath(lat_lon, timestamp, city), 'r') as fd:
            return json.load(fd, encoding='utf-8')
    except IOError:
        print "No such file"

def write_to_cache(obj, lat_lon, timestamp, city):
    """
    Save json object to file
    :param obj: a json object
    :param lat_lon: lat/lon of the location it's for
    :param timestamp: timestamp of forecast
    """
    path = os.path.join(DATA_DIR, city)
    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)
    if not os.path.exists(path):
        os.mkdir(path)
    try:
        with open(cache_filepath(lat_lon, timestamp, city), 'w') as fd:
            fd.write( json.dumps(obj, encoding='utf-8'))
    except IOError:
        print "Could not write file"
