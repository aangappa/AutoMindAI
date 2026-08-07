from dataclasses import dataclass, field


@dataclass
class VehicleEvaluation:
    """
    Represents the evaluation of a
    single vehicle against the
    Customer DNA.
    """

    vehicle_id: str

    vehicle_name: str

    overall_score: float = 0.0

    recommendation_level: str = "Not Evaluated"

    dimension_scores: dict[
        str,
        float,
    ] = field(
        default_factory=dict
    )

    strengths: list[str] = field(
        default_factory=list
    )

    concerns: list[str] = field(
        default_factory=list
    )

    explanation: str = ""

    evaluated_dimensions: int = 0

    def add_dimension_score(
        self,
        dimension: str,
        score: float,
    ) -> None:

        self.dimension_scores[
            dimension
        ] = score

        self.evaluated_dimensions = len(
            self.dimension_scores
        )

    def add_strength(
        self,
        strength: str,
    ) -> None:

        if strength not in self.strengths:

            self.strengths.append(
                strength
            )

    def add_concern(
        self,
        concern: str,
    ) -> None:

        if concern not in self.concerns:

            self.concerns.append(
                concern
            )

    def calculate_overall_score(
        self,
    ) -> float:

        if not self.dimension_scores:

            self.overall_score = 0

            return self.overall_score

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

        return self.overall_score