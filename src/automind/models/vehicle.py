from dataclasses import dataclass


@dataclass
class Vehicle:
    """
    Canonical Vehicle Identity.

    This object represents the
    permanent identity of a vehicle.

    Dynamic automotive knowledge
    belongs to AKR.
    """

    # ----------------------------------
    # Identity
    # ----------------------------------

    vehicle_id: str

    manufacturer: str

    model: str

    variant: str = ""

    year: int | None = None

    # ----------------------------------
    # Classification
    # ----------------------------------

    body_style: str = ""

    segment: str = ""

    fuel_type: str = ""

    transmission: str = ""

    drivetrain: str = ""

    seating_capacity: int = 0

    # ----------------------------------
    # Metadata
    # ----------------------------------

    source: str = ""

    confidence: int = 100

    active: bool = True

    # ----------------------------------

    @property
    def display_name(
        self,
    ) -> str:

        if self.variant:

            return (
                f"{self.manufacturer} "
                f"{self.model} "
                f"{self.variant}"
            )

        return (
            f"{self.manufacturer} "
            f"{self.model}"
        )