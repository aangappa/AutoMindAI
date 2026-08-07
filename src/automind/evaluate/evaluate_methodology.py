from evaluate.vehicle_matcher import (
    VehicleMatcher,
)
from models.customer_dna import (
    CustomerDNA,
)
from models.evaluation_result import (
    EvaluationResult,
)


class EvaluateMethodology:
    """
    Implements the ACF Evaluate phase.

    Compares the Customer DNA against
    every available vehicle and produces
    an EvaluationResult.

    This phase performs evaluation only.
    It does not make recommendations.
    """

    def __init__(self):

        self.matcher = (
            VehicleMatcher()
        )

    def evaluate(
        self,
        customer_dna: CustomerDNA,
    ) -> EvaluationResult:

        result = EvaluationResult()

        evaluations = self.matcher.match(
            customer_dna
        )

        for evaluation in evaluations:

            result.add(
                evaluation
            )

        result.completed = True

        return result