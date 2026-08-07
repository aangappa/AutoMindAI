from datetime import (
    UTC,
    datetime,
)
from uuid import uuid4

from sqlalchemy import (
    Boolean,
    DateTime,
    JSON,
    String,
    Text,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from mvc.database.base import (
    Base,
)


class ProviderRawPayloadRecord(
    Base,
):
    """
    Stores the original payload
    received from external
    providers before any
    normalization or mapping.

    This allows AutoMind to
    reprocess provider data
    without calling the provider
    again.
    """

    __tablename__ = (
        "provider_raw_payloads"
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

    provider_entity_id: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    payload: Mapped[dict] = mapped_column(
        JSON,
        nullable=False,
    )

    payload_hash: Mapped[str] = mapped_column(
        String(128),
        default="",
    )

    ingestion_batch: Mapped[str] = mapped_column(
        String(100),
        default="",
    )

    source_url: Mapped[str] = mapped_column(
        Text,
        default="",
    )

    processed: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    processing_status: Mapped[str] = mapped_column(
        String(30),
        default="Pending",
    )

    processing_notes: Mapped[str] = mapped_column(
        Text,
        default="",
    )

    received_at: Mapped[datetime] = mapped_column(
        DateTime(
            timezone=True,
        ),
        default=lambda: datetime.now(
            UTC
        ),
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