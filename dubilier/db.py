"""
"""


import sqlalchemy
import sqlalchemy.orm


DBBase = sqlalchemy.orm.declarative_base()


class DB:
    """
    """
    DB_URL = "sqlite://{path}"

    def __init__(self, **kwargs: dict) -> None:
        """Initializes the DB object.
        """
        super().__init__()
        self._engine = None
        self.path = kwargs.get("path", ":memory:")

    def db_url(self) -> str:
        """
        """        
        return self.DB_URL.format(path=self.path)

    def engine(self) -> sqlalchemy.engine.Engine:
        """
        """
        if self._engine is None:
            self._engine = sqlalchemy.create_engine(self.db_url)
        return self._engine
