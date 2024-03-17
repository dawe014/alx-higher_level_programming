#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys
uname = sys.argv[1]
passwd = sys.argv[2]
dbname = sys.argv[3]


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=uname, passwd=passwd, db=dbname, port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()