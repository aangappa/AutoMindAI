from models.vehicle import (
    Vehicle,
)
from mvc.vehicle_catalog import (
    MasterVehicleCatalog,
)


class CatalogManager:
    """
    Manages the Master Vehicle Catalog.

    MVC never talks directly to
    external providers.

    It receives normalized vehicles
    from AKR and keeps the catalog
    synchronized.
    """

    def __init__(
        self,
        catalog: MasterVehicleCatalog,
    ):

        self.catalog = catalog

    def synchronize(
        self,
        vehicles: list[Vehicle],
    ) -> None:

        for vehicle in vehicles:

            self.catalog.add(
                vehicle
            )

    def clear(
        self,
    ) -> None:

        self.catalog.clear()