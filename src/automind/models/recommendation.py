from dataclasses import dataclass, field

from models.vehicle_evaluation import (
    VehicleEvaluation,
)


@dataclass
class Recommendation:
    """
    Represents one customer-facing
    recommendation produced by the
    ACF Recommend phase.
    """

    rank: int

    vehicle: VehicleEvaluation

    title: str = ""

    summary: str = ""

    recommendation_level: str = ""

    confidence: int = 0

    why_recommended: list[str] = field(
        default_factory=list
    )

    trade_offs: list[str] = field(
        default_factory=list
    )

    ownership_highlights: list[str] = field(
        default_factory=list
    )

    not_recommended_reasons: list[str] = field(
        default_factory=list
    )