"""Objects for communicating with an sqlite database."""


import typing
import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.engine
import sqlalchemy.ext.declarative
import dubilier.db.base


class Connection:
    """Object to provide functionality for connecting and communicating
    to an sqlite database.
    """
    DEFAULT_PATH: str = ""
    URL_TEMPLATE: str = "sqlite://{path}"

    def __init__(self, **kwargs: str) -> None:
        """Initializes the dubilier.db.sqlite.Connection object."""
        self._engine: typing.Optional[sqlalchemy.engine.Engine] = None
        self._session: typing.Optional[sqlalchemy.orm.sessionmaker] = None
        self.path: str = kwargs.get("path", self.DEFAULT_PATH)

    @property
    def engine(self) -> sqlalchemy.engine.Engine:
        """Property method to construct and provide access to a ready
        to be used sqlite engine.

        Returns:
            sqlalchemy.engine.Engine: sqlite engine ready to use.
        """
        if self._engine is None:
            self._engine = sqlalchemy.create_engine(self.url,
                                                    future=True,
                                                    echo=True)
            dubilier.db.base.Object.metadata.create_all(self._engine)
        return self._engine

    @property
    def session(self) -> sqlalchemy.orm.sessionmaker:
        """Property method to construct an sqlite session.

        Returns:
            sqlalchemy.orm.Session: Session scope to use within calls.
        """
        if self._session is None:
            self._session = sqlalchemy.orm.sessionmaker(self.engine)
        return self._session

    @property
    def url(self) -> str:
        """Property method to format the URL that sqlite expects for
        the connection.

        Returns:
            str: Formatted string of the URL.
        """
        return self.URL_TEMPLATE.format(path=self.path)
