#Why: User pysql and pandas to create and load a db, and use it.
#Where:  https://courses.thinkful.com/data-001v2/project/1.3.3

#SF# To do, add sys library and accept used input

import sqlite3 as sql
import pandas as pd

cities = (
	('New York City','NY'),
	('Boston','MA'),
	('Chicago','IL'),
	('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA'),
    ('Washington', 'DC'),
    ('Houston', 'TX'),
    ('Las Vegas',' NV'),
    ('Atlanta','GA'))

weather = (
	('New York City','2013','July','January','62'),
	('Boston','2013','July','January','59'),
	('Chicago','2013','July','January','59'),
	('Miami', '2013','August','January','84'),
    ('Dallas', '2013','July','January','77'),
    ('Seattle', '2013','July','January','61'),
    ('Portland', '2013','July','December','63'),
    ('San Francisco', '2013','September','December','64'),
    ('Los Angeles', '2013','September','December','75'),
    ('Washington', '2013','July','January','63'),  #value interpreted
    ('Houston', '2013','July','January','77') ,    #value interpreted
    ('Las Vegas',' 2013','July','December','88'),	  #value interpreted
    ('Atlanta','2013','July','January','82'))		  #value interpreted

#connect to the data base
con = sql.connect('getting_started.db')

with con:
	cur = con.cursor()
        #SF# Try to explain why you're doing this, it'll make easier to reuse your code!
        # Avoid conflict if table cities already exist by deleting it
	cur.execute("DROP TABLE IF EXISTS cities;")
	cur.execute("CREATE TABLE cities (name text, state text);")
        # Avoid conflict if table cities already exist by deleting it
	cur.execute("DROP TABLE IF EXISTS weather;")
	cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer);")
        # Populate the database
	cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
	cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
        #SF# Notice how you can break lines so it can be read
	cur.execute("SELECT name, state, year,warm_month,cold_month,average_high \
                     FROM cities INNNER JOIN weather ON name=city \
                     GROUP BY city HAVING warm_month=='July'" )
	# cur.execute("SELECT name,state")
	rows = cur.fetchall()
	cols = [desc[0] for desc in cur.description]

#SF# Now you're ready with the answer, there's no need to keep in the "with con:" loop
df = pd.DataFrame(rows, columns=cols)

#LP# <- This will always be your comment
#LP# I do not found a solution to print the sentence on one line as the assignement state:
#LP# I think it will be something like :
#LP#		print 'The cities that are warmest in July are: ' + df.name[i] + ", " + df.state[i] for i in range(1)
#LP# but it doesn't work and on the pandas forum i was not able to find the solution:

#LP# This will be my closest solution.

print 'The cities that are warmest in July are: '
print df.name + ", " + 	df.state

#SF# OK, so the answer was something close to
cities_and_states = ""
for city,state in zip(df.name,df.state):
    cities_and_states += city+", "+state+", "
# Now there's an extra ", " at the end
cities_and_states = cities_and_states[:-2]

print('The cities that are warmest in July are: {0}'.format(cities_and_states))

#SF# Now, that is a long and convoluted way. There's a more direct way. Also, the query returns every single city.

#connect to the data base
with sql.connect('getting_started.db') as con:
    cur = con.cursor()
    # Get the cities where the warmest month is July
    cur.execute("SELECT name, state \
                 FROM cities INNNER JOIN weather ON name=city \
                 GROUP BY city HAVING warm_month=='July'" )
    # cur.execute("SELECT name,state")
    cities_and_states = cur.fetchall()

cities_coma_states = [c+" ("+s+")" for (c,s) in cities_and_states]
formated_answer = ", ".join(cities_coma_states[:-1]) + " and " + cities_coma_states[-1]
print('The cities that are warmest in July are: {0}'.format(formated_answer))

#SF# Hope you like the answers. There's some really advanced python there, so don't get disapointed.
#SF# You'll get that in no time. The string.join method is really powerful on strings.
#SF# Also, list comprehensions are one of the coolest features in python.
