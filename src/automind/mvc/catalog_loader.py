import csv
from pathlib import Path

from models.vehicle import (
    Vehicle,
)
from mvc.vehicle_catalog import (
    MasterVehicleCatalog,
)


class CatalogLoader:
    """
    Loads the Master Vehicle Catalog
    from a CSV file.

    This is the MVP catalog source.

    Later this loader can be replaced
    by a database or commercial
    vehicle catalog provider without
    changing MVC.
    """

    def __init__(
        self,
        catalog: MasterVehicleCatalog,
    ):

        self.catalog = catalog

    def load(
        self,
    ) -> None:

        self.catalog.clear()

        csv_path = (
            Path(__file__)
            .resolve()
            .parent.parent
            / "data"
            / "vehicles.csv"
        )

        with open(
            csv_path,
            newline="",
            encoding="utf-8",
        ) as file:

            reader = csv.DictReader(
                file
            )

            for row in reader:

                vehicle = Vehicle(

                    vehicle_id=row[
                        "vehicle_id"
                    ],

                    manufacturer=row[
                        "manufacturer"
                    ],

                    model=row[
                        "model"
                    ],

                    variant=row[
                        "variant"
                    ],

                    body_style=row[
                        "body_style"
                    ],

                    fuel_type=row[
                        "fuel_type"
                    ],

                    transmission=row[
                        "transmission"
                    ],

                    seating_capacity=int(
                        row[
                            "seating_capacity"
                        ]
                    ),

                )

                self.catalog.add(
                    vehicle
                )