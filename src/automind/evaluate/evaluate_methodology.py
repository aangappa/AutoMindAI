from evaluate.vehicle_matcher import (
    VehicleMatcher,
)
from models.customer_dna import (
    CustomerDNA,
)
from models.vehicle_evaluation import (
    VehicleEvaluation,
)


class EvaluateMethodology:
    """
    Implements the ACF Evaluate phase.

    Evaluates the customer's DNA against
    the vehicle catalog and returns the
    highest-ranking vehicles.
    """

    def __init__(self):

        self.matcher = (
            VehicleMatcher()
        )

    def evaluate(
        self,
        customer_dna: CustomerDNA,
        top_n: int = 5,
    ) -> list[VehicleEvaluation]:

        return self.matcher.match(

            customer_dna,

            top_n,

        )