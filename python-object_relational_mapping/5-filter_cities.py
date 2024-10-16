#!/usr/bin/python3
"""
lists all cities of a state from db
"""
import MySQLdb
import sys

def list_cities_by_state(username, password, database, state_name):
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    parameter = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """
    cursor.execute(parameter, (state_name,))
    cities = cursor.fetchall()
    city_names = [city[0] for city in cities]
    print(", ".join(map(str,city_names)))
    cursor.close()
    db.close()

if __name__ == "__main__":
    list_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
