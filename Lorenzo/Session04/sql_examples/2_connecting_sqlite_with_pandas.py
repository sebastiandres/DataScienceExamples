# Quick crash course on sqlite3 and pandas
# See: https://docs.python.org/2/library/sqlite3.html
import sqlite3
import pandas as pd

# Auxiliar function
def print_table(cursor):
    for row in cursor.execute('SELECT * FROM persons ORDER BY name'):
        print row
    return

################################################################################
# Mission:
# Open a pandas dataframe with the content of a given database
################################################################################
conn = sqlite3.connect('persons.db')
c = conn.cursor()
df = pd.read_sql_query("SELECT * FROM persons ORDER BY name",
                       conn, index_col=None)
print "Dataframe created from the database"
print df, "\n"

# OBS: In a larger table, you can (and probably will) select 
# only a few rows
df_small = pd.read_sql_query("SELECT name, age FROM persons WHERE age=28",
                             conn, index_col="name")
print "Small dataframe loaded from the database"
print df_small, "\n"
# OBS: the index_col in the dataframe cannot be modified (?!)

################################################################################
# Using the data is easier in pandas
################################################################################
df["age"] = df["age"] + 1    # Happy birthday, everyone
df["gender"] = "U"            # Unspecified
print "Modified dataframe"
print df, "\n"

# Nevertheless, the database has not been affected by the changes!
print "Original database (Notice the format is completely different)"
conn.commit()
for row in c.execute('SELECT * FROM persons ORDER BY name'):
    print row
print ""

df = pd.read_sql_query("SELECT * FROM persons ORDER BY name",
                       conn, index_col=None)
print "Reloading the dataframe created from the database"
print df, "\n"

print "Takeaway: Dataframes from databases are hardcopied values"
print "          and modifications must be explicitely imposed"
