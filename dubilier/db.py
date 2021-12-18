"""
"""


from typing import Any
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

    def get(self, obj: Any, **kwargs: dict) -> Any:
        """
        """
        session_scope = self.session()
        with session_scope() as session:
            results = session.query(obj).filter_by(**kwargs)
            if results.count():
                return results
        return None

    def insert(self, obj: Any) -> None:
        """
        """
        session_scope = self.session()
        with session_scope() as session:
            with session.begin():
                try:
                    session.add(obj)
                except sqlalchemy.ext.InvalidRequestError:
                    cur_sessions = session.object_sessions(obj)
                    cur_sessions.add(obj)
        return obj

    def update(self, obj: Any) -> None:
        """
        """
        session_scope = self.session()
        with session_scope() as session:
            obj_session = session.object_session(obj)
            obj_session.add(obj)
            obj_session.commit()
        return obj

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
