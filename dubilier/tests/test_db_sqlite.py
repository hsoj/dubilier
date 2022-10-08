# pylint: disable=missing-docstring


import unittest
import unittest.mock
import sqlalchemy.orm
import sqlalchemy.engine
import dubilier.db.sqlite


class TestConnection(unittest.TestCase):

    def connection(self) -> dubilier.db.sqlite.Connection:
        return dubilier.db.sqlite.Connection()

    def test_default_path(self) -> None:
        conn: dubilier.db.sqlite.Connection = self.connection()
        self.assertEqual(conn.path, ":memory:")

    def test_formatted_url(self) -> None:
        expected: str = "sqlite://:memory:"
        conn: dubilier.db.sqlite.Connection = self.connection()
        self.assertEqual(expected, conn.url)

    @unittest.mock.patch("sqlalchemy.create_engine")
    def test_engine_constructor(self, mock: unittest.mock.Mock) -> None:
        conn: dubilier.db.sqlite.Connection = self.connection()
        _: sqlalchemy.engine.Engine = conn.engine
        mock.assert_called_once_with(conn.url)

    @unittest.mock.patch("sqlalchemy.create_engine")
    @unittest.mock.patch("sqlalchemy.orm.sessionmaker")
    def test_session_constructor(self,
                                 session_mock: unittest.mock.Mock,
                                 engine_mock: unittest.mock.Mock) -> None:
        conn: dubilier.db.sqlite.Connection = self.connection()
        engine_mock.return_value = None
        _: sqlalchemy.orm.Session = conn.session
        session_mock.assert_called_once_with(conn.engine)
