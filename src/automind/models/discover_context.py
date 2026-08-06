from dataclasses import dataclass, field


@dataclass
class DiscoverContext:
    """
    Represents the current state of the
    Discover phase.

    This object is produced by the
    Discover Methodology and consumed
    by the Prompt Builder.
    """

    known_information: dict = field(
        default_factory=dict
    )

    missing_information: dict = field(
        default_factory=dict
    )

    valid_fields: str = ""

    completion_percentage: int = 0

    consultation_complete: bool = False