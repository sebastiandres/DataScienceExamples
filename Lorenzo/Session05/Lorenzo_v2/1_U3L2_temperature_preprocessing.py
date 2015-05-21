# Why = Analyzing Temperature data
# Where = https://courses.thinkful.com/data-001v2/project/3.2.4

"""
#SF#
We preprocess everything we need to populate the database
"""
import numpy as np
import datetime
import requests
from pandas.io.json import json_normalize
import sqlite3
import pandas as pd
import collections

# URL format for the API request
# https://api.forecast.io/forecast/APIKEY/LATITUDE,LONGITUDE,TIME

def far2cel(F):
    return (F-32)/1.8

########################### Challenge ###########################
# 1) Build the API call by combining the string elements in Python for your first city''' 
#################################################################

# dictionariy of cities
citta = {"Lugano": '46.0030,8.9513',
         "Lausanne": '46.5196,6.6322',
         "Roma": '41.9031,12.4958',
         "Quebec": '46.8221,-71.2231',
         "Ottawa": '45.4594,-75.5184',
         "Vancouver": '49.2604,-123.1133'}

# Lugano : Switzerland
# Lausanne : Switzerland
# Rome : Italy
# Quebec : East Canada
# Ottawa : East Canada
# Vancouver : Ouest Canada

#SF# Might be a good idea to save this on a file, and then load it dynamically.
#SF# But an overshot for this particular example.
# my API key for foricast.io
API_key = 'bd65082df114cd750f5541445ec7710f'

# base url for the API call
base_url = 'https://api.forecast.io/forecast/'

# SPRING and FALL start time and date in UNIX format
now_spring = datetime.date(2015, 5, 17)
now_fall = datetime.date(2014, 10, 17)

#################################################################
# 2) Test the call for your first city and make sure you have it formatted properly
#################################################################

# API call for the first city
API_call = base_url + API_key + '/' + citta["Lugano"] + ',' + now_spring.strftime('%s')
#SF# Easier just print it and use chrome!
print API_call

#################################################################
# 3a) Once you have the URL formatted properly, issue the request from your code and inspect the result. 
# How many levels does the data have? 
#################################################################

r = requests.get(API_call)

# To check how many levels we have in the data below the root level
#SF# This is not actually the answer. The keys give you the current keys, 
#SF# but not the son's keys.
print 'The level below the root in the API call are {0}'.format(len(r.json().keys()))

#################################################################
# 3b) Which field do we want to save to get the daily maximum temperature?
#################################################################


# The field daily has a keys data and a values that is a list of dictionary
daily = r.json()['daily']['data']

# The list of dictionary contains a keys 'temperatureMax'
for x in daily:
    t_max = far2cel(x["temperatureMax"])
    print "TMax in Lugano:", t_max, " Celsius."

#################################################################
# 4-5) Based on the data sample, create the table in a SQLite database called "weather.db". 
#################################################################

# create and connect to a database
conn = sqlite3.connect('weather.db')

# All interactions with the database are called querys
# And they require to be used through a cursor
c = conn.cursor()

# The queries are applied using the .execute() method
c.execute('DROP TABLE IF EXISTS citta')

# Create a new table called citta (cities in italian) 
c.execute('''CREATE TABLE citta (city_name text, lat_lon float)''')

# Insert the values of citta into the tables
c.executemany("INSERT INTO citta VALUES (?, ?)", citta.items())

# Save (commit) the changes to the database
conn.commit() 

#################################################################
# 5-6) Write a script that takes each city and queries every day for the past 60 days (more interesting) 
# in spring and save the avg temperature values to the table, 
# keyed on the date. 
# L: I will do the same with fall time and compare the results.
#################################################################

# The queries are applied using the .execute() method
# Delete existing table
c.execute('DROP TABLE IF EXISTS daily_avg_spring')
c.execute('DROP TABLE IF EXISTS daily_avg_fall')

# create a new tables to store daily_avg temperature for each citta in SPRING and FALL
#SF# OK, if you already introduce the data, there's no need to make a new table, you
#SF# Could just filter before and after a key date.
#SF# Also, might be a good idea to DRY the code.

c.execute('CREATE TABLE daily_avg_spring (date int, Lugano float, Lausanne float, Roma float, Quebec float, Ottawa float, Vancouver float)''')
c.execute('CREATE TABLE daily_avg_fall (date int, Lugano float, Lausanne float, Roma float, Quebec float, Ottawa float, Vancouver float)''')

# Retrieve data from sql database
df = pd.read_sql_query('SELECT * FROM citta', conn)

# Latitude et Longitude to list
geo = df['lat_lon'].tolist()

# Set the strting date of measurmeents (60 days before now_spring) for SPRING and FALL
date_spring = now_spring - datetime.timedelta(days=60)
date_fall = now_fall - datetime.timedelta(days=60)

#SF# DRY the code, you're repeating yourself.
################# Insert date into the SPRING daily_avg table ##########################
with conn:
    while date_spring <= now_spring:
        c.execute('INSERT INTO daily_avg_spring(date) VALUES (?)', (int(date_spring.strftime('%s')),))
        date_spring += datetime.timedelta(days=1)
    
for k,v in citta.iteritems():
    date_spring = now_spring - datetime.timedelta(days=60)
    while date_spring <= now_spring:
        API = base_url + API_key + '/' + v + ',' + date_spring.strftime('%s')
        s = requests.get(API)
            
        daily = s.json()['daily']['data']
        # The list of dictionary contains a keys 'temperatureMax'
        for x in daily:
            t_max = far2cel(x["temperatureMax"])
        with conn:
            #insert the temperature max to the database
            c.execute('UPDATE daily_avg_spring SET ' + k + ' = ' + str(round(t_max,1)) + ' WHERE date = ' + date_spring.strftime('%s'))
                
        date_spring += datetime.timedelta(days=1)  

################# Insert date into the FALL daily_avg table ##########################
with conn:
    while date_fall <= now_fall:
        c.execute('INSERT INTO daily_avg_fall(date) VALUES (?)', (int(date_fall.strftime('%s')),))
        date_fall += datetime.timedelta(days=1)
    
for k,v in citta.iteritems():
    date_fall = now_fall - datetime.timedelta(days=60)
    while date_fall <= now_fall:
        API = base_url + API_key + '/' + v + ',' + date_fall.strftime('%s')
        f = requests.get(API)
            
        daily = f.json()['daily']['data']
        # The list of dictionary contains a keys 'temperatureMax'
        for x in daily:
            t_max = far2cel(x["temperatureMax"])
        with conn:
            #insert the temperature max to the database
            c.execute('UPDATE daily_avg_fall SET ' + k + ' = ' + str(round(t_max,1)) + ' WHERE date = ' + date_fall.strftime('%s'))
                
        date_fall += datetime.timedelta(days=1)

#SF# Great! 
conn.commit()
conn.close()
