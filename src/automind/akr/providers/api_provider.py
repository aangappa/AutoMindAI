from akr.knowledge_package import (
    KnowledgePackage,
)
from akr.provider import (
    AutomotiveKnowledgeProvider,
)
from models.customer_dna import (
    CustomerDNA,
)


class ApiProvider(
    AutomotiveKnowledgeProvider
):
    """
    Retrieves automotive knowledge from
    external automotive APIs.

    The underlying API provider is
    intentionally hidden from AKR.
    """

    def search_vehicles(
        self,
        customer_dna: CustomerDNA,
    ) -> list[KnowledgePackage]:

        raise NotImplementedError(
            "API integration has not "
            "been implemented yet."
        )