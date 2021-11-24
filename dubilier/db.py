"""
"""

import sqlite3
import logging

#   NOTE: Need a better way to include the DB schema in the event that the
#   contents get too large.
TABLE_SPEC = """
CREATE TABLE IF NOT EXISTS schedule (
    id integer PRIMARY KEY,
    timestamp integer,
    group text
);
"""

class DB:

    def __init__(self, path: str, **kwargs: dict) -> None:
        """
        """
        super().__init__()
        self._conn = None
        self._logger = kwargs.get("logger", None)
        self.path = path

    def create_schema(self) -> None:
        """
        """
        conn = self.connection()
        try:
            cur = conn.cursor()
            cur.execute(TABLE_SPEC)
        except sqlite3.Error as e:
            self.logger().error(e)

    def connection(self) -> sqlite3.Connection:
        """
        """
        if self._conn is None:
            self._conn = sqlite3.connect(self.path)
        return self._conn

    def logger(self) -> logging.Logger:
        """
        """
        if self._logger is None:
            # TODO: This object should not be the facility which manages the
            # logging, but for now it will handle it's own logging until a
            # better solution can be implemented
            self._logger = logging.getLogger(__name__)
        return self._logger