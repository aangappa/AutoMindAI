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
    Evaluates one vehicle against the
    current Customer DNA.

    Evaluation is based on the
    customer's known preferences.

    AKR will enrich this engine in
    future without changing its API.
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
                == vehicle.fuel_type.lower()
            ):

                evaluation.add_strength(
                    f"Preferred {vehicle.fuel_type} powertrain."
                )

            else:

                score -= 20

                evaluation.add_tradeoff(
                    f"Uses {vehicle.fuel_type} instead of your preferred {fuel.explanation}."
                )

        # --------------------------
        # Body Style
        # --------------------------

        body = customer_dna.get_dimension(
            "Body Style"
        )

        if (
            body
            and body.knowledge_state != "Unknown"
        ):

            if (
                body.explanation.lower()
                == vehicle.body_style.lower()
            ):

                evaluation.add_strength(
                    f"{vehicle.body_style} matches your preferred body style."
                )

            else:

                score -= 15

                evaluation.add_tradeoff(
                    f"{vehicle.body_style} instead of your preferred {body.explanation}."
                )

        # --------------------------
        # Transmission
        # --------------------------

        transmission = customer_dna.get_dimension(
            "Transmission"
        )

        if (
            transmission
            and transmission.knowledge_state != "Unknown"
        ):

            if (
                transmission.explanation.lower()
                == vehicle.transmission.lower()
            ):

                evaluation.add_strength(
                    f"{vehicle.transmission} transmission matches your preference."
                )

            else:

                score -= 10

                evaluation.add_tradeoff(
                    f"{vehicle.transmission} transmission differs from your preference."
                )

        # --------------------------
        # Seating
        # --------------------------

        if vehicle.seating_capacity >= 5:

            evaluation.add_strength(
                f"Comfortably seats {vehicle.seating_capacity} passengers."
            )

        # --------------------------
        # Overall Score
        # --------------------------

        evaluation.overall_score = max(
            score,
            0,
        )

        evaluation.confidence_score = 90.0

        if evaluation.overall_score >= 90:

            evaluation.recommendation_level = (
                "★★★★★ Excellent Match"
            )

        elif evaluation.overall_score >= 75:

            evaluation.recommendation_level = (
                "★★★★ Good Match"
            )

        elif evaluation.overall_score >= 60:

            evaluation.recommendation_level = (
                "★★★ Possible Match"
            )

        else:

            evaluation.recommendation_level = (
                "★★ Not Recommended"
            )

        evaluation.explanation = (
            "Evaluation completed successfully."
        )

        return evaluation