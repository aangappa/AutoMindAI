from models.vehicle_evaluation import (
    VehicleEvaluation,
)


class RecommendationBuilder:
    """
    Builds the customer-facing
    recommendation from vehicle
    evaluations.
    """

    def build(
        self,
        evaluations: list[VehicleEvaluation],
    ) -> str:

        lines = [

            "# 🚗 AutoMind Recommendation\n",

            "Based on your consultation, the following vehicles are the best matches.\n",

        ]

        for index, evaluation in enumerate(

            evaluations,

            start=1,

        ):

            lines.extend(

                [

                    f"## {index}. {evaluation.vehicle_name}",

                    f"Overall Score : {evaluation.overall_score}",

                    f"Recommendation : {evaluation.recommendation_level}",

                    "",

                    "Strengths",

                ]

            )

            if evaluation.strengths:

                for strength in evaluation.strengths:

                    lines.append(

                        f"- {strength}"

                    )

            else:

                lines.append(

                    "- None"

                )

            lines.append("")

            lines.append("Concerns")

            if evaluation.concerns:

                for concern in evaluation.concerns:

                    lines.append(

                        f"- {concern}"

                    )

            else:

                lines.append(

                    "- None"

                )

            lines.append("")

        return "\n".join(lines)