from models.vehicle import (
    Vehicle,
)


class MasterVehicleCatalog:
    """
    Master Vehicle Catalog (MVC).

    The catalog owns the complete
    collection of vehicles known to
    AutoMind.

    Today the source may be CSV.

    Tomorrow it may be PostgreSQL,
    Elasticsearch or another
    enterprise repository without
    affecting the rest of AutoMind.
    """

    def __init__(self):

        self._vehicles: dict[
            str,
            Vehicle,
        ] = {}

    # ----------------------------------
    # CRUD
    # ----------------------------------

    def add(
        self,
        vehicle: Vehicle,
    ) -> None:

        self._vehicles[
            vehicle.vehicle_id
        ] = vehicle

    def update(
        self,
        vehicle: Vehicle,
    ) -> None:

        self._vehicles[
            vehicle.vehicle_id
        ] = vehicle

    def remove(
        self,
        vehicle_id: str,
    ) -> None:

        self._vehicles.pop(
            vehicle_id,
            None,
        )

    # ----------------------------------
    # Queries
    # ----------------------------------

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

    def exists(
        self,
        vehicle_id: str,
    ) -> bool:

        return (
            vehicle_id
            in self._vehicles
        )

    # ----------------------------------
    # Search
    # ----------------------------------

    def find_by_manufacturer(
        self,
        manufacturer: str,
    ) -> list[Vehicle]:

        manufacturer = (
            manufacturer.lower()
        )

        return [

            vehicle

            for vehicle in self.all()

            if vehicle.manufacturer.lower()
            == manufacturer

        ]

    def find_by_model(
        self,
        model: str,
    ) -> list[Vehicle]:

        model = model.lower()

        return [

            vehicle

            for vehicle in self.all()

            if vehicle.model.lower()
            == model

        ]

    def active(
        self,
    ) -> list[Vehicle]:

        return [

            vehicle

            for vehicle in self.all()

            if vehicle.active

        ]

    # ----------------------------------
    # Maintenance
    # ----------------------------------

    def clear(
        self,
    ) -> None:

        self._vehicles.clear()