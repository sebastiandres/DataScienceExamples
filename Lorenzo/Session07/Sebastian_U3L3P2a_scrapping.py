# utf-8
from bs4 import BeautifulSoup
import requests

# The url to be scrapped
url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"
# Get the content
r = requests.get(url)
# Read it with BeautifulSoup
soup = BeautifulSoup(r.content)

"""
#Data for "School life expectancy (in years), primary to tertiary education" 
is provided in the format: 
Line 0: Zambia (name)
Line 1: 2000 (year)
Line 2:  
Line 3: a (additional info)
Line 4: 7 (total)
Line 5: 
Line 6: 
Line 7: 8 (men)
Line 8: 
Line 9: 
Line 10: 7 (women)
Line 11: 
"""
# Scrap the content

# All the possibly interesting tags
all_td = list(soup.findAll("td"))
# Numbers obtained through exploration
useful_td = all_td[37:-29] 
# We know what we need to store.
country = []
year = []
total = []
men = []
women = []
# There are 13 lines for each country
for i, td in enumerate(useful_td):
    if (i%12)==0:
        country.append(td.text)
    if (i%12)==1:
        year.append(td.text)
    if (i%12)==4:
        total.append(td.text)
    if (i%12)==7:
        men.append(td.text)
    if (i%12)==10:
        women.append(td.text)

# Don't do format conversion, we'll only be saving the data for now

# What is the easiest way to save the data?
# Probably a csv file, to open it later with dataframes.
# a database is also possible, but too much for this simple example.

with open("SchoolLifeExpectancy.csv","w") as fh:
    fh.write("country,men,women,total,year\n")
    for c,m,w,t,y in zip(country, men, women,total,year):
        # Will have trouble with some utf-8 names
        c = c.encode("ASCII","replace") # Other options: "ignore" and "xmlcharrefreplace"
        # Will have trouble if data already has a comma
        c = c.replace(","," ")
        # Now create the line to be written
        line = ",".join([c,m,w,t,y])
        fh.write(line + "\n")
