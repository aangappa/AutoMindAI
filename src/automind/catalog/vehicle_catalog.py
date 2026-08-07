from models.vehicle import Vehicle


class VehicleCatalog:
    """
    Temporary in-memory vehicle catalog.

    This will later be replaced by a
    repository backed by YAML and
    eventually a database/API.
    """

    def get_all(self) -> list[Vehicle]:

        return [

            Vehicle(

                id="car001",

                brand="Toyota",

                model="Hyryder",

                variant="Hybrid G",

                year=2025,

                body_style="SUV",

                fuel_type="Hybrid",

                transmission="Automatic",

                ex_showroom_price=2100000,

                dimensions={

                    "Family Focus": 92,

                    "Budget Sensitivity": 80,

                    "Ownership Horizon": 95,

                    "Running Cost Sensitivity": 95,

                    "Urban Usage": 85,

                    "Highway Usage": 82,

                    "Long Distance Usage": 88,

                },

            ),

            Vehicle(

                id="car002",

                brand="Mahindra",

                model="XUV700",

                variant="AX7",

                year=2025,

                body_style="SUV",

                fuel_type="Petrol",

                transmission="Automatic",

                ex_showroom_price=2450000,

                dimensions={

                    "Family Focus": 96,

                    "Budget Sensitivity": 70,

                    "Ownership Horizon": 90,

                    "Running Cost Sensitivity": 72,

                    "Urban Usage": 76,

                    "Highway Usage": 95,

                    "Long Distance Usage": 94,

                },

            ),

        ]