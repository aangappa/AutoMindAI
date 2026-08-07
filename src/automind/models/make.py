from dataclasses import (
    dataclass,
)
from datetime import (
    datetime,
)


@dataclass
class Make:
    """
    Canonical vehicle
    manufacturer.
    """

    id: str

    name: str

    country: str = ""

    founded_year: int | None = None

    status: str = "Active"

    active: bool = True

    created_at: datetime | None = None

    updated_at: datetime | None = None