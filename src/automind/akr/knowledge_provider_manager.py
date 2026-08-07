from akr.knowledge_package import (
    KnowledgePackage,
)
from akr.provider import (
    AutomotiveKnowledgeProvider,
)
from models.customer_dna import (
    CustomerDNA,
)


class KnowledgeProviderManager:
    """
    Coordinates all Automotive
    Knowledge Providers.

    Providers return raw
    Knowledge Packages.

    No validation, normalization
    or caching happens here.
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

    def search_vehicles(
        self,
        customer_dna: CustomerDNA,
    ) -> list[KnowledgePackage]:

        packages: list[
            KnowledgePackage
        ] = []

        for provider in self.providers:

            packages.extend(

                provider.search_vehicles(
                    customer_dna
                )

            )

        return packages