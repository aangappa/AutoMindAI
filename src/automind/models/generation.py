from dataclasses import (
    dataclass,
)
from datetime import (
    datetime,
)


@dataclass
class Generation:
    """
    Canonical vehicle
    generation.
    """

    id: str

    model_id: str

    generation_code: str = ""

    marketing_name: str = ""

    start_year: int | None = None

    end_year: int | None = None

    facelift: bool = False

    status: str = "Active"

    active: bool = True

    created_at: datetime | None = None

    updated_at: datetime | None = None