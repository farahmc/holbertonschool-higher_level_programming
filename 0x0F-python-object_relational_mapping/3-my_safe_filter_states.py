#!/usr/bin/python3
""" script safe from MySQL injections that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa where name matches the
argument """


import sys
import MySQLdb

if __name__ == "__main__":
    match = sys.argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states \
                    WHERE name = %(match)s \
                    ORDER BY id ASC", {'match': match})
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
