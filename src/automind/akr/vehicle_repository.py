from akr.knowledge_pipeline import (
    KnowledgePipeline,
)
from akr.knowledge_provider_manager import (
    KnowledgeProviderManager,
)
from akr.provider import (
    AutomotiveKnowledgeProvider,
)
from models.customer_dna import (
    CustomerDNA,
)
from models.vehicle import (
    Vehicle,
)


class VehicleRepository:
    """
    Repository responsible for
    retrieving and enriching
    vehicle information.
    """

    def __init__(self):

        self.providers = (
            KnowledgeProviderManager()
        )

        self.pipeline = (
            KnowledgePipeline()
        )

    def register_provider(
        self,
        provider: AutomotiveKnowledgeProvider,
    ) -> None:

        self.providers.register(
            provider
        )

    def enrich(
        self,
        customer_dna: CustomerDNA,
    ) -> list[Vehicle]:

        packages = (
            self.providers.search_vehicles(
                customer_dna
            )
        )

        vehicles: list[
            Vehicle
        ] = []

        for package in packages:

            vehicle = self.pipeline.process(
                package
            )

            if vehicle is not None:

                vehicles.append(
                    vehicle
                )

        return vehicles