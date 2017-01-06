"""
A single driver file that gives back mysql/sqlite driver object accordingly.
"""

import mysql_driver as m
import sqlite_driver as s

class DBDriver():
    def __init__(self):
        pass

    def init(self, rdbms, **params):
        db = None
        if rdbms.strip().lower() == "mysql":
            db = m.MySql()
        elif rdbms.strip().lower() == "sqlite":
            db = s.Sqlite3()

        err = db.init(**params)

        if err:
            return db, err
        else:
            return db, None


