from catalog.vehicle_catalog import (
    VehicleCatalog,
)
from evaluate.evaluation_engine import (
    EvaluationEngine,
)
from models.customer_dna import CustomerDNA
from models.vehicle_evaluation import (
    VehicleEvaluation,
)


class VehicleMatcher:
    """
    Evaluates every vehicle in the catalog
    and returns the best matches.
    """

    def __init__(self):

        self.catalog = VehicleCatalog()

        self.engine = EvaluationEngine()

    def match(
        self,
        customer_dna: CustomerDNA,
        top_n: int = 5,
    ) -> list[VehicleEvaluation]:

        evaluations = []

        vehicles = self.catalog.get_all()

        for vehicle in vehicles:

            evaluation = self.engine.evaluate(

                customer_dna,

                vehicle,

            )

            evaluations.append(
                evaluation
            )

        evaluations.sort(

            key=lambda x: x.overall_score,

            reverse=True,

        )

        return evaluations[:top_n]