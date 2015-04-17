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
con = sql.connect('getting_satrted.db')

with con:

	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS cities;")
	cur.execute("DROP TABLE IF EXISTS weather;")
	cur.execute("CREATE TABLE cities (name text, state text);")
	cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer);")
	cur.executemany("INSERT INTO cities VALUES(?,?)",cities)
	cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)",weather)
	cur.execute("SELECT name, state, year,warm_month,cold_month,average_high FROM cities INNNER JOIN weather ON name=city GROUP BY city HAVING warm_month=='July'" )
	# cur.execute("SELECT name,state")
	rows = cur.fetchall()
	cols = [desc[0] for desc in cur.description]

	df = pd.DataFrame(rows, columns=cols)

##### Comment LP:
##### I do not found a solution to print the sentence on one line as the assignement state:
##### I think it will be something like :
#####		print 'The cities that are warmest in July are: ' + df.name[i] + ", " + df.state[i] for i in range(1)
##### but it doesn't work and on the pandas forum i was not able to find the solution:

##### This will be my closest solution.

	print 'The cities that are warmest in July are: '
	print df.name + ", " + 	df.state

