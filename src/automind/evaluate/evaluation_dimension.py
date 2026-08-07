from dataclasses import dataclass


@dataclass
class EvaluationDimension:
    """
    Represents the compatibility between
    one Customer DNA dimension and one
    vehicle dimension.
    """

    name: str

    customer_score: float

    vehicle_score: float

    compatibility_score: float = 0.0

    explanation: str = ""

    strength: bool = False

    concern: bool = False

    def calculate_compatibility(
        self,
    ) -> float:

        difference = abs(

            self.customer_score

            -

            self.vehicle_score

        )

        self.compatibility_score = max(

            0,

            100 - difference,

        )

        return self.compatibility_score