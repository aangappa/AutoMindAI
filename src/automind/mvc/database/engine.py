from sqlalchemy import (
    create_engine,
)

from mvc.database.config import (
    DatabaseConfig,
)


class DatabaseEngine:
    """
    Creates the SQLAlchemy engine
    used by MVC.
    """

    _engine = None

    @classmethod
    def engine(
        cls,
    ):

        if cls._engine is None:

            cls._engine = create_engine(

                DatabaseConfig.url(),

                echo=False,

                pool_pre_ping=True,

                future=True,

            )

        return cls._engine

    @classmethod
    def test_connection(
        cls,
    ) -> bool:

        try:

            with cls.engine().connect():

                return True

        except Exception as ex:

            print(
                ex
            )

            return False