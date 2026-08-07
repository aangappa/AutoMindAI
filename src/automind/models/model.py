from dataclasses import (
    dataclass,
)
from datetime import (
    datetime,
)


@dataclass
class Model:
    """
    Canonical vehicle model.
    """

    id: str

    make_id: str

    name: str

    body_style: str = ""

    segment: str = ""

    start_year: int | None = None

    end_year: int | None = None

    status: str = "Active"

    active: bool = True

    created_at: datetime | None = None

    updated_at: datetime | None = None