from models.evaluation_result import (
    EvaluationResult,
)
from models.recommendation import (
    Recommendation,
)
from models.recommendation_result import (
    RecommendationResult,
)


class RecommendMethodology:
    """
    Implements the ACF Recommend phase.

    Converts Vehicle Evaluations into
    customer-facing recommendations.
    """

    def recommend(
        self,
        evaluation_result: EvaluationResult,
    ) -> RecommendationResult:

        result = RecommendationResult()

        ranked = sorted(

            evaluation_result.evaluations,

            key=lambda vehicle:
                vehicle.overall_score,

            reverse=True,

        )

        for rank, vehicle in enumerate(

            ranked,

            start=1,

        ):

            recommendation = Recommendation(

                rank=rank,

                vehicle=vehicle,

                title=vehicle.vehicle_name,

                summary=(
                    f"{vehicle.recommendation_level} "
                    f"({vehicle.overall_score}/100)"
                ),

                recommendation_level=(
                    vehicle.recommendation_level
                ),

                confidence=int(
                    vehicle.overall_score
                ),

                why_recommended=list(
                    vehicle.strengths
                ),

                trade_offs=list(
                    vehicle.concerns
                ),

                ownership_highlights=[],

                not_recommended_reasons=[],

            )

            result.add(
                recommendation
            )

        result.completed = True

        return result