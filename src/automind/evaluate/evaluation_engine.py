from models.customer_dna import (
    CustomerDNA,
)
from models.vehicle import (
    Vehicle,
)
from models.vehicle_evaluation import (
    VehicleEvaluation,
)


class EvaluationEngine:
    """
    Evaluates one vehicle against
    the current Customer DNA.

    MVP version.

    Uses only attributes available
    from MVC.

    AKR enrichment will extend this
    engine without changing its API.
    """

    def evaluate(
        self,
        customer_dna: CustomerDNA,
        vehicle: Vehicle,
    ) -> VehicleEvaluation:

        evaluation = VehicleEvaluation(

            vehicle_id=vehicle.vehicle_id,

            vehicle_name=vehicle.display_name,

        )

        score = 100

        # --------------------------
        # Fuel Preference
        # --------------------------

        fuel = customer_dna.get_dimension(
            "Fuel Preference"
        )

        if (
            fuel
            and fuel.knowledge_state != "Unknown"
        ):

            if (
                fuel.explanation.lower()
                != vehicle.fuel_type.lower()
            ):

                score -= 20

                evaluation.add_concern(
                    "Fuel Preference"
                )

            else:

                evaluation.add_strength(
                    "Fuel Preference"
                )

        # --------------------------
        # Seating
        # --------------------------

        seating = customer_dna.get_dimension(
            "Family Size"
        )

        if (
            seating
            and vehicle.seating_capacity >= 5
        ):

            evaluation.add_strength(
                "Family Size"
            )

        # --------------------------

        evaluation.overall_score = max(
            score,
            0,
        )

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