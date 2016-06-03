#!/bin/python3.5

import sqlite3

uId = 1
uPrice = 62300

con = sqlite3.connect('test.db')
with con:
    cur = con.cursor()

    cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (uPrice, uId))
    con.commit()

    print("Number of rows updated: %d" % cur.rowcount)
