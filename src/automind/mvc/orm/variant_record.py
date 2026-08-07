from datetime import (
    UTC,
    datetime,
)
from uuid import uuid4

from sqlalchemy import (
    Boolean,
    DateTime,
    Float,
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


class VariantRecord(
    Base,
):
    """
    Canonical vehicle variant.

    This is AutoMind's primary
    vehicle identity.
    """

    __tablename__ = "variants"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(
            uuid4()
        ),
    )

    generation_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey(
            "generations.id",
        ),
        nullable=False,
    )

    automind_uid: Mapped[str] = mapped_column(
        String(120),
        unique=True,
        nullable=False,
    )

    variant_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    model_year: Mapped[int] = mapped_column(
        Integer,
    )

    launch_year: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    production_start_year: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    production_end_year: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    engine_code: Mapped[str] = mapped_column(
        String(50),
        default="",
    )

    engine_cc: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    fuel_type: Mapped[str] = mapped_column(
        String(30),
        default="",
    )

    transmission_type: Mapped[str] = mapped_column(
        String(30),
        default="",
    )

    drive_type: Mapped[str] = mapped_column(
        String(30),
        default="",
    )

    power_bhp: Mapped[float] = mapped_column(
        Float,
        default=0,
    )

    torque_nm: Mapped[float] = mapped_column(
        Float,
        default=0,
    )

    doors: Mapped[int] = mapped_column(
        Integer,
        default=4,
    )

    seating_capacity: Mapped[int] = mapped_column(
        Integer,
        default=5,
    )

    length_mm: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    width_mm: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    height_mm: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    wheelbase_mm: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    ground_clearance_mm: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    boot_space_litres: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    fuel_tank_capacity_litres: Mapped[int] = mapped_column(
        Integer,
        default=0,
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