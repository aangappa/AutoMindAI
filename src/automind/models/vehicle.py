from dataclasses import dataclass
from datetime import datetime


@dataclass
class Vehicle:
    """
    Canonical Vehicle Entity.

    This represents the permanent
    identity of a vehicle inside
    AutoMind's Master Vehicle Catalog
    (MVC).

    Dynamic knowledge such as
    maintenance, recalls, reviews,
    ownership experience and market
    intelligence belongs to AKR.
    """

    # ----------------------------------
    # Identity
    # ----------------------------------

    vehicle_id: str

    manufacturer: str

    model: str

    variant: str = ""

    variant_code: str = ""

    generation: str = ""

    year: int | None = None

    launch_year: int | None = None

    discontinued: bool = False

    # ----------------------------------
    # Classification
    # ----------------------------------

    body_style: str = ""

    segment: str = ""

    fuel_type: str = ""

    transmission: str = ""

    drivetrain: str = ""

    seating_capacity: int = 0

    doors: int = 5

    # ----------------------------------
    # Powertrain
    # ----------------------------------

    engine_displacement_cc: int = 0

    engine_description: str = ""

    horsepower: int = 0

    torque_nm: int = 0

    # ----------------------------------
    # Dimensions
    # ----------------------------------

    length_mm: int = 0

    width_mm: int = 0

    height_mm: int = 0

    wheelbase_mm: int = 0

    ground_clearance_mm: int = 0

    boot_space_liters: int = 0

    fuel_tank_capacity_liters: int = 0

    # ----------------------------------
    # Efficiency
    # ----------------------------------

    mileage_arai: float = 0.0

    mileage_real_world: float = 0.0

    # ----------------------------------
    # Pricing
    # ----------------------------------

    price_ex_showroom: float = 0.0

    price_on_road: float = 0.0

    currency: str = "INR"

    # ----------------------------------
    # Safety
    # ----------------------------------

    safety_rating: float = 0.0

    airbags: int = 0

    adas_level: str = ""

    # ----------------------------------
    # Ownership
    # ----------------------------------

    warranty_years: int = 0

    warranty_km: int = 0

    # ----------------------------------
    # Media
    # ----------------------------------

    image_url: str = ""

    brochure_url: str = ""

    # ----------------------------------
    # Market
    # ----------------------------------

    market: str = "India"

    country: str = "India"

    status: str = "Active"

    # ----------------------------------
    # Metadata
    # ----------------------------------

    source: str = ""

    confidence: int = 100

    active: bool = True

    created_at: datetime | None = None

    updated_at: datetime | None = None

    # ----------------------------------

    @property
    def display_name(
        self,
    ) -> str:

        parts = [

            self.manufacturer,

            self.model,

        ]

        if self.variant:

            parts.append(
                self.variant
            )

        return " ".join(parts)

    @property
    def short_name(
        self,
    ) -> str:

        return self.display_name

    @property
    def full_name(
        self,
    ) -> str:

        parts = [

            self.manufacturer,

            self.model,

        ]

        if self.generation:

            parts.append(
                self.generation
            )

        if self.variant:

            parts.append(
                self.variant
            )

        if self.year:

            parts.append(
                str(self.year)
            )

        return " ".join(parts)