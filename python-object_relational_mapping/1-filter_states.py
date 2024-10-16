#!/usr/bin/python3
"""
list all states starting with N in mysql database
"""
import MySQLdb
import sys


def list_states_starting_N(username, password, database):
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states_starting__N(sys.argv[1], sys.argv[2], sys.argv[
