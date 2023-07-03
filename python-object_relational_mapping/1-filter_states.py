#!/usr/bin/python3
""" Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa """


import MySQLdb
import sys


def listNStates():
    """ list all states from database """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()


if __name__ == "__main__":
    listNStates()
