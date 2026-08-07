class EvaluationRules:
    """
    Encapsulates all vehicle evaluation
    rules used by the Evaluate phase.

    This class will evolve into the
    automotive decision engine.
    """

    STRONG_MATCH = 80

    POSSIBLE_MATCH = 60

    CONCERN = 50

    @staticmethod
    def recommendation_level(
        overall_score: float,
    ) -> str:

        if overall_score >= 90:

            return "Excellent Match"

        if overall_score >= 75:

            return "Good Match"

        if overall_score >= 60:

            return "Possible Match"

        return "Poor Match"

    @staticmethod
    def is_strength(
        compatibility: float,
    ) -> bool:

        return (
            compatibility
            >= EvaluationRules.STRONG_MATCH
        )

    @staticmethod
    def is_concern(
        compatibility: float,
    ) -> bool:

        return (
            compatibility
            <= EvaluationRules.CONCERN
        )