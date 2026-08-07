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

            "Based on your consultation, AutoMind evaluated the available vehicles and ranked them according to your preferences.",

            "",

        ]

        for recommendation in result.ranked():

            vehicle = recommendation.vehicle

            lines.extend(

                [

                    f"## {recommendation.rank}. {recommendation.title}",

                    f"### {recommendation.recommendation_level}",

                    "",

                    f"**Overall Match:** **{vehicle.overall_score:.1f}%**",

                    f"**Confidence:** **{recommendation.confidence}%**",

                    "",

                    "---",

                    "",

                    "### ✅ Why AutoMind recommends this vehicle",

                ]

            )

            if recommendation.why_recommended:

                for item in recommendation.why_recommended:

                    lines.append(

                        f"- ✅ {item}"

                    )

            else:

                lines.append(

                    "- No specific strengths identified yet."

                )

            lines.extend(

                [

                    "",

                    "### ⚠️ Trade-offs",

                ]

            )

            if recommendation.trade_offs:

                for item in recommendation.trade_offs:

                    lines.append(

                        f"- ⚠️ {item}"

                    )

            else:

                lines.append(

                    "- No significant trade-offs identified."

                )

            if recommendation.ownership_highlights:

                lines.extend(

                    [

                        "",

                        "### 🚘 Ownership Highlights",

                    ]

                )

                for item in recommendation.ownership_highlights:

                    lines.append(

                        f"- {item}"

                    )

            if recommendation.not_recommended_reasons:

                lines.extend(

                    [

                        "",

                        "### ❌ Consider Before Buying",

                    ]

                )

                for item in recommendation.not_recommended_reasons:

                    lines.append(

                        f"- {item}"

                    )

            lines.extend(

                [

                    "",

                    "---",

                    "",

                ]

            )

        return "\n".join(lines)