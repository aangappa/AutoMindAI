from evaluate.evaluation_engine import (
    EvaluationEngine,
)
from models.customer_dna import (
    CustomerDNA,
)
from models.vehicle import (
    Vehicle,
)
from models.vehicle_evaluation import (
    VehicleEvaluation,
)


class VehicleMatcher:
    """
    Evaluates candidate vehicles
    supplied by Vehicle Discovery.

    VehicleMatcher no longer owns
    a vehicle catalog.
    """

    def __init__(self):

        self.engine = (
            EvaluationEngine()
        )

    def match(
        self,
        customer_dna: CustomerDNA,
        vehicles: list[Vehicle],
        top_n: int = 5,
    ) -> list[VehicleEvaluation]:

        evaluations: list[
            VehicleEvaluation
        ] = []

        for vehicle in vehicles:

            evaluation = (
                self.engine.evaluate(

                    customer_dna,

                    vehicle,

                )
            )

            evaluations.append(
                evaluation
            )

        evaluations.sort(

            key=lambda item:
                item.overall_score,

            reverse=True,

        )

        return evaluations[
            :top_n
        ]