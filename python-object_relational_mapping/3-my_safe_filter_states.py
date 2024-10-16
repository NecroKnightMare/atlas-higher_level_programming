#!/usr/bin/python3
"""
display values of states, 4 arguments, copied 2 into 3
"""
import MySQLdb
import sys


def list_states_starting_with_N(username, password, database, state_name):
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    display_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
