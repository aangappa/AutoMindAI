from dataclasses import dataclass, field


@dataclass
class VehicleEvaluation:
    """
    Represents the evaluation of one vehicle
    against the customer's DNA.
    """

    vehicle_id: str

    vehicle_name: str

    overall_score: float = 0.0

    recommendation_level: str = "Not Evaluated"

    dimension_scores: dict[str, float] = field(
        default_factory=dict
    )

    strengths: list[str] = field(
        default_factory=list
    )

    concerns: list[str] = field(
        default_factory=list
    )

    explanation: str = ""

    def add_dimension_score(
        self,
        dimension: str,
        score: float,
    ):

        self.dimension_scores[
            dimension
        ] = score

    def add_strength(
        self,
        strength: str,
    ):

        if strength not in self.strengths:

            self.strengths.append(
                strength
            )

    def add_concern(
        self,
        concern: str,
    ):

        if concern not in self.concerns:

            self.concerns.append(
                concern
            )

    def calculate_overall_score(
        self,
    ):

        if not self.dimension_scores:

            self.overall_score = 0

            return

        self.overall_score = round(

            sum(
                self.dimension_scores.values()
            )
            /
            len(
                self.dimension_scores
            ),

            1,

        )