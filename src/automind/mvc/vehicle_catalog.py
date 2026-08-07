from models.vehicle import (
    Vehicle,
)


class MasterVehicleCatalog:
    """
    Master Vehicle Catalog (MVC).

    MVC maintains the universe of
    vehicles known to AutoMind.

    It stores only stable identity
    information.

    Dynamic knowledge belongs to AKR.
    """

    def __init__(self):

        self._vehicles: dict[
            str,
            Vehicle,
        ] = {}

    def add(
        self,
        vehicle: Vehicle,
    ) -> None:

        self._vehicles[
            vehicle.vehicle_id
        ] = vehicle

    def get(
        self,
        vehicle_id: str,
    ) -> Vehicle | None:

        return self._vehicles.get(
            vehicle_id
        )

    def all(
        self,
    ) -> list[Vehicle]:

        return list(
            self._vehicles.values()
        )

    def count(
        self,
    ) -> int:

        return len(
            self._vehicles
        )

    def clear(
        self,
    ) -> None:

        self._vehicles.clear()
        