from dataclasses import (
    dataclass,
    field,
)


@dataclass
class KnowledgePackage:
    """
    Represents raw automotive
    knowledge acquired from one
    provider for one vehicle.

    A KnowledgePackage is the input
    to the Knowledge Pipeline.
    """

    # ----------------------------------
    # Vehicle Identity
    # ----------------------------------

    vehicle_id: str

    # ----------------------------------
    # Provider Metadata
    # ----------------------------------

    provider: str

    source: str

    knowledge_type: str

    acquired_at: str

    # ----------------------------------
    # Raw Knowledge
    # ----------------------------------

    raw_data: dict = field(
        default_factory=dict
    )

    metadata: dict = field(
        default_factory=dict
    )

    # ----------------------------------
    # Pipeline Status
    # ----------------------------------

    valid: bool = False

    normalized: bool = False

    enriched: bool = False

    cached: bool = False