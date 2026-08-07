from abc import (
    ABC,
    abstractmethod,
)

from akr.knowledge_package import (
    KnowledgePackage,
)
from models.vehicle import (
    Vehicle,
)


class AutomotiveKnowledgeProvider(ABC):
    """
    Base interface for all Automotive
    Knowledge providers.

    A provider enriches an already
    identified vehicle.

    Providers DO NOT discover vehicles.
    That responsibility belongs to MVC.
    """

    @abstractmethod
    def enrich(
        self,
        vehicle: Vehicle,
    ) -> KnowledgePackage:
        """
        Returns a KnowledgePackage
        containing raw provider data
        for the supplied vehicle.
        """
        pass