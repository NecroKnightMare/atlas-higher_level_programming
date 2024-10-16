#!/usr/bin/python3
"""
list all states with values from states table
"""
import MySQLdb
import sys


def display_states(username, password, database):
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    parameters = "SELECT * FROM states WHERE name = LIKE '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(parameters)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    display_states(sys.argv[1], sys.argv[2], sys.argv[3])
