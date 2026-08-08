from datetime import (
    UTC,
    datetime,
)
from uuid import uuid4

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    Float,
    JSON,
    String,
    UniqueConstraint,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from mvc.database.base import (
    Base,
)


class ProviderCrossReferenceRecord(
    Base,
):
    """
    Maps provider identifiers to
    AutoMind canonical entities.

    The canonical entity may be:

    make
    model
    generation
    variant
    """

    __tablename__ = (
        "provider_cross_references"
    )

    __table_args__ = (

        UniqueConstraint(

            "provider_name",

            "provider_external_id",

            name=(
                "uq_provider_external_id"
            ),

        ),

        CheckConstraint(

            """
            canonical_type IN (
                'make',
                'model',
                'generation',
                'variant'
            )
            """,

            name=(
                "ck_canonical_type"
            ),

        ),

    )

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(
            uuid4()
        ),
    )

    provider_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    provider_external_id: Mapped[
        str
    ] = mapped_column(
        String(255),
        nullable=False,
    )

    canonical_type: Mapped[
        str
    ] = mapped_column(
        String(20),
        nullable=False,
    )

    canonical_id: Mapped[
        str
    ] = mapped_column(
        String(36),
        nullable=False,
    )

    provider_version: Mapped[
        str
    ] = mapped_column(
        String(50),
        default="",
    )

    provider_metadata: Mapped[
        dict | None
    ] = mapped_column(
        JSON,
        nullable=True,
    )

    confidence: Mapped[
        float
    ] = mapped_column(
        Float,
        default=1.0,
    )

    last_synced_at: Mapped[
        datetime
    ] = mapped_column(
        DateTime(
            timezone=True,
        ),
        default=lambda: datetime.now(
            UTC
        ),
    )

    created_at: Mapped[
        datetime
    ] = mapped_column(
        DateTime(
            timezone=True,
        ),
        default=lambda: datetime.now(
            UTC
        ),
    )

    updated_at: Mapped[
        datetime
    ] = mapped_column(
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