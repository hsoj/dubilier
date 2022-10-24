# pylint: disable=missing-docstring


import typing
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
        self.assertEqual(conn.path, "")

    def test_formatted_url(self) -> None:
        expected: str = "sqlite://"
        conn: dubilier.db.sqlite.Connection = self.connection()
        self.assertEqual(expected, conn.url)

    @unittest.mock.patch("sqlalchemy.create_engine")
    @unittest.mock.patch("dubilier.db.base.Object.metadata.create_all")
    def test_engine_constructor(self,
                                create_all_mock: unittest.mock.Mock,
                                mock: unittest.mock.Mock) -> None:
        conn: dubilier.db.sqlite.Connection = self.connection()
        create_all_mock.return_value = True
        _: sqlalchemy.engine.Engine = conn.engine
        mock.assert_called_once_with(conn.url, future=True, echo=True)

    @unittest.mock.patch("sqlalchemy.create_engine")
    @unittest.mock.patch("sqlalchemy.orm.sessionmaker")
    @unittest.mock.patch("dubilier.db.base.Object.metadata.create_all")
    def test_session_constructor(self,
                                 create_all_mock: unittest.mock.Mock,
                                 session_mock: unittest.mock.Mock,
                                 engine_mock: unittest.mock.Mock) -> None:
        conn: dubilier.db.sqlite.Connection = self.connection()
        engine_mock.return_value = None
        create_all_mock.return_value = True
        _: sqlalchemy.orm.Session = conn.session
        session_mock.assert_called_once_with(conn.engine)

    def test_session(self) -> None:
        conn: dubilier.db.sqlite.Connection = self.connection()
        expected: list[typing.Any] = [(1,)]
        with conn.session() as session:
            with session.begin():
                session.execute("CREATE TABLE test (id INTEGER NOT NULL)")
            with session.begin():
                session.execute("INSERT INTO test (id) VALUES (1)")
            res = session.execute("SELECT id FROM test")
        self.assertEqual(expected, res.all())
