
from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd

# URL with data
url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"

# Getting data from the web and storing for soup analysis
r = requests.get(url)
soup = BeautifulSoup(r.content)

#####################################################################################
############### Grab data from the html table and make a list   #####################
data = []
# I only consider the 7th table 
table = soup.findAll('table')[6]
# I take only the 2nd table within the table where I have data I want
table = table.findAll('table')[1]

rows = table.findAll('tr')
for row in rows:
    # Iterate over column. This script take account for blank space too
    cols = row.find_all('td')
    # This allow me to remove all the tag between <>
    cols = [ele.text.rstrip() for ele in cols]
    data.append([ele for ele in cols]) 

# drop first 6 row
data = data[5::]
# I obtain a list of of list with 12 elements each, blank spaces 
# included.

# Dataframe creation
col = ['country','year','','','total','','','men','','','women','']
df = pd.DataFrame(data,columns=col)
# Drop blank column
df.drop('', axis=1, inplace=True)
# Transform string to int
df.year = df['year'].apply(int)
df.total = df['total'].apply(int)
df.men = df['men'].apply(int)
df.women = df['women'].apply(int)

# Why : Storing the data
# Where : https://courses.thinkful.com/data-001v2/assignment/3.3.3

# I do have a dataframe already, I do not need a sql table creation.
men = df.men.describe()
women = df.women.describe()

print(df.describe())

