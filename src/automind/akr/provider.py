from abc import ABC
from abc import abstractmethod

from akr.knowledge_package import (
    KnowledgePackage,
)
from models.customer_dna import (
    CustomerDNA,
)


class AutomotiveKnowledgeProvider(
    ABC
):
    """
    Base class for every Automotive
    Knowledge Provider.

    Providers acquire raw automotive
    knowledge only.

    They never normalize, enrich,
    validate or cache knowledge.
    """

    @abstractmethod
    def search_vehicles(
        self,
        customer_dna: CustomerDNA,
    ) -> list[KnowledgePackage]:
        """
        Acquires candidate vehicle
        knowledge from the underlying
        source.
        """
        pass