from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):
    """
    Application configuration loaded
    from environment variables.
    """

    # -----------------------------
    # Gemini
    # -----------------------------

    GEMINI_API_KEY: str

    GEMINI_MODEL: str = (
        "gemini-2.5-flash"
    )

    # -----------------------------
    # CarsXE
    # -----------------------------

    CARSXE_API_KEY: str

    # -----------------------------
    # Settings
    # -----------------------------

    model_config = (
        SettingsConfigDict(

            env_file=".env",

            env_file_encoding="utf-8",

            extra="ignore",

        )
    )


settings = Settings()