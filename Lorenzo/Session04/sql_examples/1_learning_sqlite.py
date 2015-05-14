# Quick crash course on sqlite3
# See: https://docs.python.org/2/library/sqlite3.html
import sqlite3

def print_table(cursor):
    for row in cursor.execute('SELECT * FROM persons ORDER BY name'):
        print row
    return

################################################################################
# Connect to a database
################################################################################
# We call it conn because it's a connection, it's not the database itself
conn = sqlite3.connect('persons.db')
# All interactions with the database are called querys
# And they require to be used through a cursor
c = conn.cursor()

################################################################################
# Querys "posting" info
################################################################################
# Querys that "put" information in the table.
# They are applied using the .execute() method. They are immediately accesible
# from the pysql library, but the changes only affect the database (persons.db)
# If you commit the changes before closing the connection.

# Example: Delete a table
# This completely destroys the table, so be careful before dropping tables
c.execute('''DROP TABLE IF EXISTS persons''')

# Example: Create table
c.execute('''CREATE TABLE persons (name text, gender text, age int)''')

# Example: Insert one row of data
c.execute("INSERT INTO persons VALUES ('Sebastian Flores','M','32')")

# Example: Insert several rows of data
data = [('Maria Jose', 'F', 32), ('Lorenzo','M','28'), ('Janet','F','28')]
c.executemany("INSERT INTO persons VALUES (?, ?, ?)", data)

# Save (commit) the changes to the database
conn.commit() 

################################################################################
# Querys "delivering" info
################################################################################
# Querys that "get" information from the table.
# They are applied using the .execute() method.
# The retrieved values can be accessed:
# using .fetchone(): Gives you only the first row from the query
# using .fetchall(): Gives you all the rows from the query, at once
# using a iterator: Gives you all the rows from the query, one by one

# Examples using .fetchone()
print "Examples using fetchone()"
c.execute('SELECT * FROM persons WHERE age=28')
print c.fetchone()
target_age = (28,)
c.execute('SELECT * FROM persons WHERE age=?',target_age)
print c.fetchone()

# Examples using .fetchall()
print "Examples using fetchall()"
c.execute('SELECT * FROM persons WHERE age=32')
print c.fetchall()
target_age = (32,)
c.execute('SELECT * FROM persons WHERE age=?',target_age)
print c.fetchall()

# Examples using an iterator
print "Examples using iterator()"
for row in c.execute('SELECT * FROM persons WHERE age=28'):
    print row
target_age = (28,)
for row in c.execute('SELECT * FROM persons WHERE age=?',target_age):
    print row

################################################################################
# Disconnect to a database
################################################################################
# Beware of loosing data, be sure to commit your changes
conn.close()
