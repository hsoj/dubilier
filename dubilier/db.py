"""
"""


import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative


Base = sqlalchemy.orm.declarative_base()


class DB:
    """
    """
    DB_URL = "sqlite://{path}"

    def __init__(self, **kwargs: dict) -> None:
        """Initializes the DB object.
        """
        super().__init__()
        self._engine = None
        self._session = None
        self.path = kwargs.get("path", ":memory:")

    def db_url(self) -> str:
        """
        """        
        return self.DB_URL.format(path=self.path)

    def engine(self) -> sqlalchemy.engine.Engine:
        """
        """
        if self._engine is None:
            self._engine = sqlalchemy.create_engine(self.db_url())
            Base.metadata.create_all(self._engine)
        return self._engine

    def session(self) -> sqlalchemy.orm.Session:
        """
        """
        if self._session is None:
            self._session = sqlalchemy.orm.sessionmaker(self.engine())
        return self._session


class Mixin:
    """
    """

    @sqlalchemy.ext.declarative.declared_attr
    def __tablename__(self):
        return self.__name__.lower()

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
