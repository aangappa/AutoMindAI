from dataclasses import dataclass
from dataclasses import field


@dataclass
class KnowledgeRecord:
    """
    Represents one normalized piece of
    automotive knowledge.

    All AKR repositories return
    KnowledgeRecord objects regardless
    of domain.
    """

    vehicle_id: str

    domain: str

    source: str

    last_updated: str = ""

    confidence: int = 100

    data: dict = field(
        default_factory=dict
    )