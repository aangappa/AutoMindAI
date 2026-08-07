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


class ModelRecord(
    Base,
):
    """
    Canonical vehicle model.

    Examples:

    Toyota -> Innova

    Hyundai -> Creta

    Honda -> City
    """

    __tablename__ = "models"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(
            uuid4()
        ),
    )

    make_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey(
            "makes.id",
        ),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    body_style: Mapped[str] = mapped_column(
        String(50),
        default="",
    )

    segment: Mapped[str] = mapped_column(
        String(50),
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