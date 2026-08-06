from dataclasses import dataclass, field


@dataclass
class Vehicle:
    """
    Represents one vehicle in the
    AutoMind vehicle catalog.
    """

    id: str

    brand: str

    model: str

    variant: str

    year: int

    body_style: str

    fuel_type: str

    transmission: str

    ex_showroom_price: float

    dimensions: dict[str, float] = field(
        default_factory=dict
    )

    specifications: dict = field(
        default_factory=dict
    )

    features: dict = field(
        default_factory=dict
    )

    def name(self) -> str:

        return (
            f"{self.brand} "
            f"{self.model} "
            f"{self.variant}"
        )

    def get_dimension_score(
        self,
        dimension: str,
    ) -> float:

        return self.dimensions.get(
            dimension,
            50,
        )