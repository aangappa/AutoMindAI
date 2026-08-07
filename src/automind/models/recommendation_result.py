from dataclasses import dataclass, field

from models.recommendation import (
    Recommendation,
)


@dataclass
class RecommendationResult:
    """
    Represents the complete output
    of the ACF Recommend phase.
    """

    recommendations: list[
        Recommendation
    ] = field(
        default_factory=list
    )

    completed: bool = False

    def add(
        self,
        recommendation: Recommendation,
    ) -> None:

        self.recommendations.append(
            recommendation
        )

    def ranked(
        self,
    ) -> list[Recommendation]:

        return sorted(

            self.recommendations,

            key=lambda item:
                item.rank,

        )

    def top(
        self,
    ) -> Recommendation | None:

        if not self.recommendations:

            return None

        return self.ranked()[0]

    def count(
        self,
    ) -> int:

        return len(
            self.recommendations
        )