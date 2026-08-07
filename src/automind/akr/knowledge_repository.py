from akr.vehicle_repository import (
    VehicleRepository,
)


class AutomotiveKnowledgeRepository:
    """
    Root of the Automotive Knowledge
    Repository (AKR).

    Exposes all automotive knowledge
    repositories.

    Additional repositories can be
    added without changing clients.
    """

    def __init__(self):

        self.vehicles = (
            VehicleRepository()
        )

    def initialize(self) -> None:
        """
        Initializes all repositories.

        Reserved for future startup
        logic such as provider
        registration and cache
        initialization.
        """

        pass