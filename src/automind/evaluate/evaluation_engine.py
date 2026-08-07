from evaluate.evaluation_dimension import (
    EvaluationDimension,
)
from evaluate.evaluation_rules import (
    EvaluationRules,
)
from models.customer_dna import CustomerDNA
from models.vehicle import Vehicle
from models.vehicle_evaluation import (
    VehicleEvaluation,
)


class EvaluationEngine:
    """
    Evaluates one vehicle against the
    Customer DNA.
    """

    def evaluate(
        self,
        customer_dna: CustomerDNA,
        vehicle: Vehicle,
    ) -> VehicleEvaluation:

        evaluation = VehicleEvaluation(

            vehicle_id=vehicle.id,

            vehicle_name=vehicle.name(),

        )

        for dna_dimension in (
            customer_dna.dimensions.values()
        ):

            vehicle_score = (
                vehicle.get_dimension_score(
                    dna_dimension.name
                )
            )

            dimension = (
                EvaluationDimension(

                    name=dna_dimension.name,

                    customer_score=dna_dimension.score,

                    vehicle_score=vehicle_score,

                )
            )

            compatibility = (
                dimension.calculate_compatibility()
            )

            evaluation.add_dimension_score(

                dimension.name,

                compatibility,

            )

            if EvaluationRules.is_strength(
                compatibility
            ):

                evaluation.add_strength(
                    dimension.name
                )

                dimension.strength = True

            elif EvaluationRules.is_concern(
                compatibility
            ):

                evaluation.add_concern(
                    dimension.name
                )

                dimension.concern = True

        evaluation.calculate_overall_score()

        evaluation.recommendation_level = (
            EvaluationRules.recommendation_level(
                evaluation.overall_score
            )
        )

        return evaluation