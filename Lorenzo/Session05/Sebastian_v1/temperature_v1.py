#What: Getting data from API (forecast.io API)
#Where: https://courses.thinkful.com/DATA-001v2/assignment/3.2.2

import sqlite3 as sql
import requests
import datetime

# Define some parameters
my_api_key = "1c961049c5a9d5fef2e405478a1eadc5"
cities = { "Atlanta": '33.762909,-84.422675',
            "Austin": '30.303936,-97.754355',
            "Boston": '42.331960,-71.020173',
            "Chicago": '41.837551,-87.681844',
            "Cleveland": '41.478462,-81.679435'}

# Get the format for the api
url = "https://api.forecast.io/forecast/{0}/{1},{2}"

# Task: 
# We need to take each city, and query for every day in the past 30 days
# For each returned value, we need to store the data and the temperature on the table

# Create the table
conn = sql.connect("max_daily_temp.db")
c = conn.cursor()

c.execute('''DROP TABLE IF EXISTS max_daily_temp''')
c.execute('''CREATE TABLE max_daily_temp (date text, city text, max_temp float)''')

# Get the values
end_date = datetime.datetime.now()
delta = datetime.timedelta(days=1)
for city in cities.keys():
    for i in range(31):
        # Update the date
        date = end_date - i*delta
        datetime_str = date.strftime('%Y-%m-%dT%H:%M:%S')
        # Get the latlon
        latlon = cities[city]
        # Create the url
        api_link = url.format(my_api_key, latlon, datetime_str)
        # Get the data and transform it to json
        r = requests.get(api_link).json() # Get the info and transform to a dict using the json method
        # Get the max_temp, through the keys and first element of the list, then dict again.
        max_temp = r["daily"]["data"][0]["temperatureMax"]
        # Put it on the database
        date_str = datetime_str.split("T")[0]
        values = (date_str, city, max_temp)
        print values
        c.execute("INSERT INTO max_daily_temp VALUES (?,?,?)",values)

# Now save the database and close it
conn.commit() 
conn.close()

###########################################################################################
# Just to check that everything was saved. Let's open it with pandas dataframe and print it
###########################################################################################
import pandas as pd
conn2 = sql.connect('max_daily_temp.db')
df = pd.read_sql_query("SELECT * FROM max_daily_temp ORDER BY date, city",
                       conn2, index_col=None)
print "Saved database max_daily_temp.db, read with pandas:"
print df
print "Now group, and print the descrition makes all the work for us"
grouped = df.groupby("city")
print(grouped.describe())

###########################################################################################
# Discussion
###########################################################################################
"""
What are the drawbacks of the current implementation? How could we improve it?
# Would it be better to use executemany to include more data at once?
# apikey is exposed.
# Also, the double loop is ugly. What about using some python iterators.
# Also, more stats... what else can we know about this data?
"""
