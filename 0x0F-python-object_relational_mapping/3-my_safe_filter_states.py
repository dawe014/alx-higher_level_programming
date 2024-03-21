#!/usr/bin/python3
"""
Script to display all values in the states table of hbtn_0e_0_usa
where name matches the argument, safely handling MySQL injections.
"""
import sys
import MySQLdb

def main():
    """
    Main function that connects to MySQL database and retrieves data.
    """
    if len(sys.argv) != 5:
        print("Usage: ./safe_script.py <username> <password> <database_name> <state_name>")
        sys.exit(1)

    try:
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        c = db.cursor()
        query = "SELECT * FROM `states` WHERE name=%s"
        c.execute(query, (sys.argv[4],))
        for state in c.fetchall():
            print(state)
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
