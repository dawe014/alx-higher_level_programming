#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys
uname = sys.argv[1]
passwd = sys.argv[2]
dbname = sys.argv[3]
name = sys.argv[4]

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=uname, passwd=passwd, db=dbname, port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cur.close()
    db.close()