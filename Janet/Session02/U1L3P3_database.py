import sqlite3 as lite
import pandas as pd


def load_data(cursor):
    for line in read_migration_file():
        cursor.execute(line)

def read_migration_file():
    with open('cities_and_weather.sql') as dump:
        for line in dump:
            yield line

def fetch_data(cursor, month):
    query = "SELECT c.* FROM cities c" \
            " INNER JOIN weather w ON name = city" \
            " WHERE w.warm_month='%s'" \
            " ORDER BY c.name, c.state;" % month

    cursor.execute(query)
    return cursor.fetchall()


if __name__ == '__main__':

    month = raw_input("What month would you like data for?") or 'July'

    conn = lite.connect('challenge.db')
    with conn:
        cur = conn.cursor()
        load_data(cur)

        print( "The cities that are warmest in %s are:" % (month))

        for row in fetch_data(cur, month):
            print("%s, %s" % (row[0], row[1]))

