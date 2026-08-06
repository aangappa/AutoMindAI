from dataclasses import dataclass


@dataclass
class Evidence:
    """
    Represents one piece of evidence
    supporting behavioural reasoning.

    Evidence is derived from structured
    customer facts and is consumed by
    the ACF reasoning engine.
    """

    # ------------------------------------
    # Identity
    # ------------------------------------

    id: str

    # ------------------------------------
    # Source
    # ------------------------------------

    source: str

    observation: str

    # ------------------------------------
    # Classification
    # ------------------------------------

    dimension: str = "Unknown"

    strength: str = "Medium"

    # ------------------------------------
    # Confidence
    # ------------------------------------

    confidence_impact: int = 0

    # ------------------------------------
    # Traceability
    # ------------------------------------

    conversation_turn: int = 0

    explanation: str = ""

    # ------------------------------------
    # Domain Behaviour
    # ------------------------------------

    def assign_dimension(
        self,
        dimension: str,
    ) -> None:

        self.dimension = dimension

    def increase_confidence(
        self,
        value: int,
    ) -> None:

        self.confidence_impact = min(
            100,
            self.confidence_impact + value,
        )