from dataclasses import dataclass, field

from models.vehicle_evaluation import (
    VehicleEvaluation,
)


@dataclass
class EvaluationResult:
    """
    Represents the complete output
    of the ACF Evaluate phase.
    """

    evaluations: list[
        VehicleEvaluation
    ] = field(
        default_factory=list
    )

    evaluated_vehicle_count: int = 0

    completed: bool = False

    def add(
        self,
        evaluation: VehicleEvaluation,
    ) -> None:

        self.evaluations.append(
            evaluation
        )

        self.evaluated_vehicle_count = len(
            self.evaluations
        )

    def ranked(
        self,
    ) -> list[VehicleEvaluation]:

        return sorted(

            self.evaluations,

            key=lambda item:
                item.overall_score,

            reverse=True,

        )