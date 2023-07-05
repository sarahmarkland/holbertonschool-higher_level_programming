#!/usr/bin/python3
"""
Test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
"""
import MySQLdb
from sys import argv


def safefilterStates():
    """ Test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    safefilterStates()