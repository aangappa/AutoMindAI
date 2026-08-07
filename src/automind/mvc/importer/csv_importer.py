import csv
from pathlib import Path

from mvc.importer.base_importer import (
    BaseImporter,
)


class CSVImporter(
    BaseImporter,
):
    """
    Imports vehicle data from
    CSV into AutoMind's
    canonical data platform.

    This importer performs only
    data ingestion.

    Entity matching and
    canonical mapping are
    handled separately.
    """

    def __init__(
        self,
        csv_path: str | Path,
    ):

        self.csv_path = Path(
            csv_path
        )

    def import_data(
        self,
    ) -> list[dict]:

        rows: list[
            dict
        ] = []

        with open(

            self.csv_path,

            newline="",

            encoding="utf-8",

        ) as file:

            reader = csv.DictReader(
                file
            )

            for row in reader:

                rows.append(
                    row
                )

        return rows