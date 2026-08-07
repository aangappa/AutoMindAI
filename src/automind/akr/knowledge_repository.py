from akr.vehicle_repository import (
    VehicleRepository,
)


class AutomotiveKnowledgeRepository:
    """
    Root of the Automotive Knowledge
    Repository.

    Exposes domain repositories.
    """

    def __init__(self):

        self.vehicles = (
            VehicleRepository()
        )