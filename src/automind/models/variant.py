from dataclasses import (
    dataclass,
)
from datetime import (
    datetime,
)


@dataclass
class Variant:
    """
    Canonical vehicle variant.

    This is the primary vehicle
    identity within AutoMind.
    """

    id: str

    generation_id: str

    automind_uid: str

    variant_name: str

    model_year: int

    launch_year: int | None = None

    production_start_year: int | None = None

    production_end_year: int | None = None

    engine_code: str = ""

    engine_cc: int = 0

    fuel_type: str = ""

    transmission_type: str = ""

    drive_type: str = ""

    power_bhp: float = 0.0

    torque_nm: float = 0.0

    doors: int = 4

    seating_capacity: int = 5

    length_mm: int = 0

    width_mm: int = 0

    height_mm: int = 0

    wheelbase_mm: int = 0

    ground_clearance_mm: int = 0

    boot_space_litres: int = 0

    fuel_tank_capacity_litres: int = 0

    status: str = "Active"

    active: bool = True

    created_at: datetime | None = None

    updated_at: datetime | None = None