from customer.customer_profile import (
    CustomerProfile,
)
from models.vehicle import (
    Vehicle,
)
from mvc.vehicle_catalog import (
    MasterVehicleCatalog,
)


class VehicleDiscovery:
    """
    Discovers candidate vehicles
    from the Master Vehicle Catalog.

    This component performs
    deterministic filtering only.

    AI reasoning belongs to ACF.
    """

    def __init__(
        self,
        catalog: MasterVehicleCatalog,
    ):

        self.catalog = catalog

    def discover(
        self,
        customer_profile: CustomerProfile,
    ) -> list[Vehicle]:

        candidates: list[
            Vehicle
        ] = []

        for vehicle in self.catalog.all():

            if not self._matches(
                vehicle,
                customer_profile,
            ):
                continue

            candidates.append(
                vehicle
            )

        return candidates

    # ----------------------------------

    def _matches(
        self,
        vehicle: Vehicle,
        profile: CustomerProfile,
    ) -> bool:

        if (
            profile.body_style
            and vehicle.body_style
            and vehicle.body_style.lower()
            != profile.body_style.lower()
        ):
            return False

        if (
            profile.fuel_type
            and vehicle.fuel_type
            and vehicle.fuel_type.lower()
            != profile.fuel_type.lower()
        ):
            return False

        if (
            profile.transmission
            and vehicle.transmission
            and vehicle.transmission.lower()
            != profile.transmission.lower()
        ):
            return False

        return True