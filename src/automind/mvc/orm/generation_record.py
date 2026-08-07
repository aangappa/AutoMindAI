from datetime import (
    UTC,
    datetime,
)
from uuid import uuid4

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from mvc.database.base import (
    Base,
)


class GenerationRecord(
    Base,
):
    """
    Canonical vehicle generation.

    Examples:

    Honda City
        5th Generation

    Hyundai Creta
        2nd Generation

    Toyota Fortuner
        AN160
    """

    __tablename__ = "generations"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(
            uuid4()
        ),
    )

    model_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey(
            "models.id",
        ),
        nullable=False,
    )

    generation_code: Mapped[str] = mapped_column(
        String(50),
        default="",
    )

    marketing_name: Mapped[str] = mapped_column(
        String(100),
        default="",
    )

    start_year: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    end_year: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    facelift: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="Active",
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(
            timezone=True,
        ),
        default=lambda: datetime.now(
            UTC
        ),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(
            timezone=True,
        ),
        default=lambda: datetime.now(
            UTC
        ),
        onupdate=lambda: datetime.now(
            UTC
        ),
    )