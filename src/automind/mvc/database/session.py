from sqlalchemy.orm import (
    sessionmaker,
)

from mvc.database.engine import (
    DatabaseEngine,
)


class DatabaseSession:
    """
    Factory for creating
    SQLAlchemy sessions.
    """

    _session_factory = sessionmaker(

        bind=DatabaseEngine.engine(),

        autoflush=False,

        autocommit=False,

        expire_on_commit=False,

    )

    @classmethod
    def create(
        cls,
    ):

        return cls._session_factory()