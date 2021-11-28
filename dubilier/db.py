"""
"""


import os
import sqlite3


class Error(Exception):
    """
    """


class Connection:
    """
    """

    def __init__(self, path: str) -> None:
        """
        """
        super().__init__()
        self._conn = None
        self.path = path

    def connection(self) -> sqlite3.Connection:
        """
        """
        if self._conn is None:
            self._conn = sqlite3.connect(self.path)
        return self._conn


class Mixin:
    """
    """
    SCHEMA = None

    def prepare(self, db: Connection) -> None:
        """
        """
        conn = db.connection()
        try:
            cur = conn.cursor()
            cur.execute(self.SCHEMA)
        except sqlite3.Error as e:
            raise Error(e)