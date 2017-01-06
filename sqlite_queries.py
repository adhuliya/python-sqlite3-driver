"""
To add new queries add them here.

This module contains the queries specifically designed for sqlite which 
may not run on other databases. This module is tied with the sqlite_driver.py
module that refers this module for each query name supplied to it.

"""

import re
"""
This is the only entity present in the file.

Don't add any other entity.
"""
_queries = {
        "1":
        """
        CREATE TABLE IF NOT EXISTS task (
            id INT PRIMARY KEY,
            task TEXT,
            status TEXT,
            bornon TEXT,
            wakeupat TEXT,
            naptill TEXT
        )

        """,

        "2":
        """
        INSERT INTO task (task, status, bornon)
        VALUES(?, ?, ?)
        """,

        "3":
        """
        SELECT * FROM task
        """
        }

def removewhitespace(query):
    return " ".join(query.split())

def compressqueries():
    queries = dict()
    for queryid,query in _queries.items():
        queries[queryid] = removewhitespace(query)

    return queries


queries = compressqueries()


