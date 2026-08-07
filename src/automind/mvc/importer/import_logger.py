import logging
from pathlib import Path


class ImportLogger:
    """
    Central logger for all
    AutoMind imports.
    """

    def __init__(
        self,
        log_directory: str = "logs",
    ):

        Path(
            log_directory
        ).mkdir(
            parents=True,
            exist_ok=True,
        )

        self._logger = logging.getLogger(
            "automind.importer"
        )

        if self._logger.handlers:
            return

        self._logger.setLevel(
            logging.INFO
        )

        formatter = logging.Formatter(

            "%(asctime)s | "
            "%(levelname)s | "
            "%(message)s"

        )

        file_handler = logging.FileHandler(

            Path(
                log_directory
            )
            / "import.log",

            encoding="utf-8",

        )

        file_handler.setFormatter(
            formatter
        )

        self._logger.addHandler(
            file_handler
        )

    def info(
        self,
        message: str,
    ) -> None:

        self._logger.info(
            message
        )

    def warning(
        self,
        message: str,
    ) -> None:

        self._logger.warning(
            message
        )

    def error(
        self,
        message: str,
    ) -> None:

        self._logger.error(
            message
        )