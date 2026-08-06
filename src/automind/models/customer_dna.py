from dataclasses import dataclass, field


@dataclass
class CustomerDNA:
    """
    Represents how a customer makes
    vehicle purchasing decisions.

    Produced by the Define phase.
    """

    # Primary priorities (ordered)
    decision_priorities: list[str] = field(default_factory=list)

    # Lifestyle
    lifestyle: str | None = None

    # Driving pattern
    driving_pattern: str | None = None

    # Ownership behaviour
    ownership_style: str | None = None

    # Technology adoption
    technology_preference: str | None = None

    # Brand behaviour
    brand_preference: str | None = None

    # Purchase behaviour
    budget_flexibility: str | None = None

    # Risk profile
    risk_profile: str | None = None

    # Environmental attitude
    sustainability_preference: str | None = None