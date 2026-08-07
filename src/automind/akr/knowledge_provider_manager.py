from akr.knowledge_package import (
    KnowledgePackage,
)
from akr.provider import (
    AutomotiveKnowledgeProvider,
)
from models.vehicle import (
    Vehicle,
)


class KnowledgeProviderManager:
    """
    Coordinates Automotive Knowledge
    providers.

    Each registered provider enriches
    the supplied vehicle and returns
    a KnowledgePackage.
    """

    def __init__(self):

        self.providers: list[
            AutomotiveKnowledgeProvider
        ] = []

    def register(
        self,
        provider: AutomotiveKnowledgeProvider,
    ) -> None:

        self.providers.append(
            provider
        )

    def enrich(
        self,
        vehicle: Vehicle,
    ) -> list[KnowledgePackage]:

        packages: list[
            KnowledgePackage
        ] = []

        for provider in self.providers:

            package = provider.enrich(
                vehicle
            )

            if package is not None:

                packages.append(
                    package
                )

        return packages