#!/usr/bin/python3

# Lists all states from the database hbtn_0e_0_usa.

import sys
import MySQLdb

def get_states(user, passwd, dbname):
    """
    Retrieves all states from the specified database.

    Args:
        user (str): The username for connecting to the database.
        passwd (str): The password for connecting to the database.
        dbname (str): The name of the database containing the states.

    Returns:
        list: A list of tuples representing states retrieved from the database.
    """
    # Connect to the database using context manager
    with MySQLdb.connect(user=user, passwd=passwd, db=dbname) as db:
        # Create a cursor object using context manager
        with db.cursor() as cursor:
            # Execute SQL query to select all states
            cursor.execute("SELECT * FROM states")
            # Fetch all rows (states) from the result set
            rows = cursor.fetchall()
            return rows

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]

    # Get command-line arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]

    # Get states from the database
    states = get_states(user, passwd, dbname)

    # Print each state
    for state in states:
        print(state)
