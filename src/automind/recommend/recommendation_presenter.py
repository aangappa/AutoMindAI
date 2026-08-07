from models.recommendation_result import (
    RecommendationResult,
)


class RecommendationPresenter:
    """
    Converts RecommendationResult into
    customer-friendly markdown.
    """

    def present(
        self,
        result: RecommendationResult,
    ) -> str:

        lines = [

            "# 🏆 AutoMind Recommendations",

            "",

            "Based on your consultation, here are the vehicles that best match your requirements.",

            "",

        ]

        for recommendation in result.ranked():

            vehicle = recommendation.vehicle

            lines.extend(

                [

                    f"## {recommendation.rank}. {recommendation.title}",

                    f"**Overall Match:** {vehicle.overall_score:.1f}%",

                    f"**Assessment:** {recommendation.recommendation_level}",

                    "",

                    "### Why this vehicle?",

                ]

            )

            if recommendation.why_recommended:

                for item in recommendation.why_recommended:

                    lines.append(

                        f"✅ {item}"

                    )

            else:

                lines.append(

                    "No strengths identified."

                )

            lines.extend(

                [

                    "",

                    "### Trade-offs",

                ]

            )

            if recommendation.trade_offs:

                for item in recommendation.trade_offs:

                    lines.append(

                        f"⚠️ {item}"

                    )

            else:

                lines.append(

                    "No significant trade-offs identified."

                )

            lines.append("")

        return "\n".join(lines)