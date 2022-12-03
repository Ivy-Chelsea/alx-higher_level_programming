#!/usr/bin/python3

"""
lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv


def get_states(username, password, dbname):
    """lists all states from the database hbtn_0e_0_usa"""
    db = MySQLdb.connect(host="localhost", port=3306, user=str(username),
                         passwd=str(password), db=str(dbname), charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    get_states(argv[1], argv[2], argv[3])
