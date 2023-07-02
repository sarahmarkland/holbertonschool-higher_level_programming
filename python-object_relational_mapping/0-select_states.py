#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa idk whats going on"""
import MySQLdb
import sys


def listStates():
    """ Function that lists all states from the database hbtn_0e_0_usa """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    listStates()