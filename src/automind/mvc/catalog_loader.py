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
    Loads the Master Vehicle Catalog.

    Current source:
        CSV

    Future sources:
        PostgreSQL
        Commercial datasets
        Enterprise integrations

    The rest of AutoMind should never
    know where the catalog came from.
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

        self._load_from_csv()

    def _load_from_csv(
        self,
    ) -> None:

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

                    # --------------------
                    # Identity
                    # --------------------

                    vehicle_id=row.get(
                        "vehicle_id",
                        "",
                    ),

                    manufacturer=row.get(
                        "manufacturer",
                        "",
                    ),

                    model=row.get(
                        "model",
                        "",
                    ),

                    variant=row.get(
                        "variant",
                        "",
                    ),

                    variant_code=row.get(
                        "variant_code",
                        "",
                    ),

                    generation=row.get(
                        "generation",
                        "",
                    ),

                    year=self._to_int(
                        row.get(
                            "year"
                        )
                    ),

                    launch_year=self._to_int(
                        row.get(
                            "launch_year"
                        )
                    ),

                    # --------------------
                    # Classification
                    # --------------------

                    body_style=row.get(
                        "body_style",
                        "",
                    ),

                    segment=row.get(
                        "segment",
                        "",
                    ),

                    fuel_type=row.get(
                        "fuel_type",
                        "",
                    ),

                    transmission=row.get(
                        "transmission",
                        "",
                    ),

                    drivetrain=row.get(
                        "drivetrain",
                        "",
                    ),

                    seating_capacity=self._to_int(
                        row.get(
                            "seating_capacity"
                        )
                    ),

                    doors=self._to_int(
                        row.get(
                            "doors"
                        ),
                        default=5,
                    ),

                    # --------------------
                    # Powertrain
                    # --------------------

                    engine_displacement_cc=self._to_int(
                        row.get(
                            "engine_displacement_cc"
                        )
                    ),

                    engine_description=row.get(
                        "engine_description",
                        "",
                    ),

                    horsepower=self._to_int(
                        row.get(
                            "horsepower"
                        )
                    ),

                    torque_nm=self._to_int(
                        row.get(
                            "torque_nm"
                        )
                    ),

                    # --------------------
                    # Dimensions
                    # --------------------

                    length_mm=self._to_int(
                        row.get(
                            "length_mm"
                        )
                    ),

                    width_mm=self._to_int(
                        row.get(
                            "width_mm"
                        )
                    ),

                    height_mm=self._to_int(
                        row.get(
                            "height_mm"
                        )
                    ),

                    wheelbase_mm=self._to_int(
                        row.get(
                            "wheelbase_mm"
                        )
                    ),

                    ground_clearance_mm=self._to_int(
                        row.get(
                            "ground_clearance_mm"
                        )
                    ),

                    boot_space_liters=self._to_int(
                        row.get(
                            "boot_space_liters"
                        )
                    ),

                    fuel_tank_capacity_liters=self._to_int(
                        row.get(
                            "fuel_tank_capacity_liters"
                        )
                    ),

                    # --------------------
                    # Efficiency
                    # --------------------

                    mileage_arai=self._to_float(
                        row.get(
                            "mileage_arai"
                        )
                    ),

                    mileage_real_world=self._to_float(
                        row.get(
                            "mileage_real_world"
                        )
                    ),

                    # --------------------
                    # Pricing
                    # --------------------

                    price_ex_showroom=self._to_float(
                        row.get(
                            "price_ex_showroom"
                        )
                    ),

                    price_on_road=self._to_float(
                        row.get(
                            "price_on_road"
                        )
                    ),

                    currency=row.get(
                        "currency",
                        "INR",
                    ),

                    # --------------------
                    # Safety
                    # --------------------

                    safety_rating=self._to_float(
                        row.get(
                            "safety_rating"
                        )
                    ),

                    airbags=self._to_int(
                        row.get(
                            "airbags"
                        )
                    ),

                    adas_level=row.get(
                        "adas_level",
                        "",
                    ),

                    # --------------------
                    # Ownership
                    # --------------------

                    warranty_years=self._to_int(
                        row.get(
                            "warranty_years"
                        )
                    ),

                    warranty_km=self._to_int(
                        row.get(
                            "warranty_km"
                        )
                    ),

                    # --------------------
                    # Media
                    # --------------------

                    image_url=row.get(
                        "image_url",
                        "",
                    ),

                    brochure_url=row.get(
                        "brochure_url",
                        "",
                    ),

                    # --------------------
                    # Market
                    # --------------------

                    market=row.get(
                        "market",
                        "India",
                    ),

                    country=row.get(
                        "country",
                        "India",
                    ),

                    status=row.get(
                        "status",
                        "Active",
                    ),

                    # --------------------
                    # Metadata
                    # --------------------

                    source="CSV",

                )

                self.catalog.add(
                    vehicle
                )

    @staticmethod
    def _to_int(
        value,
        default=0,
    ) -> int:

        try:

            if value in (
                None,
                "",
            ):

                return default

            return int(value)

        except Exception:

            return default

    @staticmethod
    def _to_float(
        value,
        default=0.0,
    ) -> float:

        try:

            if value in (
                None,
                "",
            ):

                return default

            return float(value)

        except Exception:

            return default