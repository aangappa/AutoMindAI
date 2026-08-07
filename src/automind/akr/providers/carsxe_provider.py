from akr.http_client import (
    HttpClient,
)
from akr.knowledge_package import (
    KnowledgePackage,
)
from akr.provider import (
    AutomotiveKnowledgeProvider,
)
from config.settings import (
    settings,
)
from models.vehicle import (
    Vehicle,
)


class CarsXEProvider(
    AutomotiveKnowledgeProvider,
):
    """
    CarsXE Automotive
    Knowledge Provider.

    Enriches a known vehicle using
    Year-Make-Model lookup.
    """

    BASE_URL = (
        "https://api.carsxe.com/v1/ymm"
    )

    def __init__(self):

        self.client = (
            HttpClient()
        )

    def enrich(
        self,
        vehicle: Vehicle,
    ) -> KnowledgePackage:

        response = self.client.get(

            self.BASE_URL,

            params={

                "key":
                    settings.CARSXE_API_KEY,

                "year":
                    vehicle.year,

                "make":
                    vehicle.manufacturer,

                "model":
                    vehicle.model,

                "trim":
                    vehicle.variant,

            },

        )

        return KnowledgePackage(

            provider="CarsXE",

            raw_data=response,

        )