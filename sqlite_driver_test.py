#!/usr/bin/env python3

import unittest
import sqlite_driver as sqld
import logging as log
import sqlite3
from datetime import datetime as dt



class TestClass(unittest.TestCase):
    def test_create_db(self):
        db = None
        try:
            db = sqld.Sqlite3()
        except sqlite3.Error as e:
            log.error(e)
            self.assertTrue(False)


        rowcount, err = db.modify('00001')
        if err: log.error(err); self.assertTrue(False)

        rowcount, err = db.modify('00002', ("Finish testing", "asleep",
            str(dt.now())))
        if err: log.error(err); self.assertTrue(False)

        rowcount, err = db.modify('00002', ("Packup and go home", "asleep",
            str(dt.now())))
        if err: log.error(err); self.assertTrue(False)



        rows, err = db.select('00003')
        if err: log.error(err); self.assertTrue(False)

        log.debug(rows)




if __name__ == "__main__":
    log.basicConfig(filename="log.txt", level=log.DEBUG,
            format=("[%(asctime)s:%(levelname)8s:%(filename)s:%(lineno)3s"
            " - %(funcName)20s() ]\n %(message)s\n"))

    unittest.main()
