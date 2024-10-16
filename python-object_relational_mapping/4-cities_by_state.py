#!/usr/bin/python3
"""
lists all cities from the database
"""
import MySQLdb
import sys

def list_cities(username, password, database):
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    parameter = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            Join states ON cities.state_id = states.id
            ORDER BY id ASC
            """
    cursor.execute(parameter)
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    db.close()

if __name__ == "__main__":
    list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
