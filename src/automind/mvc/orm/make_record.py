from datetime import (
    UTC,
    datetime,
)
from uuid import uuid4

from sqlalchemy import (
    Boolean,
    DateTime,
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


class MakeRecord(
    Base,
):
    """
    Canonical manufacturer.

    Examples:

    Toyota
    Honda
    Hyundai
    Mahindra
    """

    __tablename__ = "makes"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(
            uuid4()
        ),
    )

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    country: Mapped[str] = mapped_column(
        String(100),
        default="",
    )

    founded_year: Mapped[int | None] = mapped_column(
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