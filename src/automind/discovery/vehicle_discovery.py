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

        for vehicle in self.catalog.active():

            if not self._matches(

                vehicle,

                customer_profile,

            ):

                continue

            candidates.append(
                vehicle
            )

        candidates.sort(

            key=self._ranking_key

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

        # ------------------------------
        # Budget
        # ------------------------------

        budget = self._budget_value(
            profile.budget
        )

        if (

            budget > 0

            and

            vehicle.price_ex_showroom > budget

        ):

            return False

        # ------------------------------
        # Seating
        # ------------------------------

        if (

            profile.children is not None

            and

            vehicle.seating_capacity > 0

        ):

            required = 2 + profile.children

            if (

                vehicle.seating_capacity

                <

                required

            ):

                return False

        return True

    # ----------------------------------

    @staticmethod
    def _budget_value(
        budget,
    ) -> float:

        if budget is None:

            return 0

        if isinstance(

            budget,

            (

                int,

                float,

            ),

        ):

            return float(
                budget
            )

        text = str(
            budget
        ).lower()

        digits = "".join(

            c

            for c in text

            if c.isdigit()

        )

        if not digits:

            return 0

        value = float(
            digits
        )

        if "lakh" in text:

            value *= 100000

        elif "crore" in text:

            value *= 10000000

        return value

    # ----------------------------------

    @staticmethod
    def _ranking_key(
        vehicle: Vehicle,
    ):

        return (

            vehicle.price_ex_showroom,

            -vehicle.safety_rating,

            vehicle.manufacturer,

            vehicle.model,

        )