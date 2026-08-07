import os
from urllib.parse import quote_plus

from dotenv import load_dotenv


load_dotenv()


class DatabaseConfig:
    """
    PostgreSQL configuration
    for AutoMind MVC.
    """

    HOST = os.getenv(
        "DB_HOST",
        "localhost",
    )

    PORT = int(
        os.getenv(
            "DB_PORT",
            "5432",
        )
    )

    DATABASE = os.getenv(
        "DB_NAME",
        "automind",
    )

    USERNAME = os.getenv(
        "DB_USER",
        "postgres",
    )

    PASSWORD = os.getenv(
        "DB_PASSWORD",
        "",
    )

    @classmethod
    def url(
        cls,
    ) -> str:

        username = quote_plus(
            cls.USERNAME
        )

        password = quote_plus(
            cls.PASSWORD
        )

        return (

            f"postgresql+psycopg://"

            f"{username}:"

            f"{password}@"

            f"{cls.HOST}:"

            f"{cls.PORT}/"

            f"{cls.DATABASE}"

        )