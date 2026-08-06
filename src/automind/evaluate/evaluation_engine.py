from evaluate.evaluation_dimension import (
    EvaluationDimension,
)
from models.customer_dna import CustomerDNA
from models.vehicle import Vehicle
from models.vehicle_evaluation import (
    VehicleEvaluation,
)


class EvaluationEngine:
    """
    Evaluates a vehicle against the
    customer's DNA.
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

            if compatibility >= 80:

                evaluation.add_strength(

                    dimension.name

                )

                dimension.strength = True

            elif compatibility <= 50:

                evaluation.add_concern(

                    dimension.name

                )

                dimension.concern = True

        evaluation.calculate_overall_score()

        if evaluation.overall_score >= 90:

            evaluation.recommendation_level = (
                "Excellent Match"
            )

        elif evaluation.overall_score >= 75:

            evaluation.recommendation_level = (
                "Good Match"
            )

        elif evaluation.overall_score >= 60:

            evaluation.recommendation_level = (
                "Possible Match"
            )

        else:

            evaluation.recommendation_level = (
                "Poor Match"
            )

        return evaluation