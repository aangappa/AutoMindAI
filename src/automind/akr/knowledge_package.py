from dataclasses import dataclass, field


@dataclass
class KnowledgePackage:
    """
    Represents automotive knowledge
    acquired from a provider before it
    is validated and normalized.
    """

    provider: str

    knowledge_type: str

    source: str

    acquired_at: str

    raw_data: dict = field(
        default_factory=dict
    )

    metadata: dict = field(
        default_factory=dict
    )

    valid: bool = False

    normalized: bool = False

    enriched: bool = False

    cached: bool = False