#!/usr/bin/python3
# this script will display all states in the database starting with N
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE "N%" ORDER BY id')
    for state_starting_with_N in cur.fetchall():
        if state_starting_with_N[1][0] == "N":
            print(state_starting_with_N)

    cur.close()
    db.close()
