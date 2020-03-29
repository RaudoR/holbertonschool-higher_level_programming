#!/usr/bin/python3
# this script will display the state matching the argument
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE "%s" ORDER BY id'
                .format(argv[4]))
    for state in cur.fetchall():
            print(state)

    cur.close()
    db.close()
