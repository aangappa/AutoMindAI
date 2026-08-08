from dataclasses import (
    dataclass,
)
from datetime import (
    UTC,
    datetime,
)


@dataclass
class ProviderContext:
    """
    Context information for a
    provider import execution.

    Every import into AutoMind
    carries this metadata.
    """

    provider_name: str

    provider_version: str = ""

    source_url: str = ""

    batch_id: str = ""

    canonical_level: str = "variant"

    imported_at: datetime = (
        datetime.now(
            UTC
        )
    )

    imported_by: str = "AutoMind"

    notes: str = ""