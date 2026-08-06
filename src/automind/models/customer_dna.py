from dataclasses import dataclass, field

from models.dna_dimension import DNADimension


@dataclass
class CustomerDNA:
    """
    Represents the consultant's behavioural
    understanding of the customer.

    CustomerDNA is the aggregate root of the
    behavioural knowledge model.
    """

    # ------------------------------------
    # Behavioural Dimensions
    # ------------------------------------

    dimensions: dict[str, DNADimension] = field(
        default_factory=dict
    )

    # ------------------------------------
    # Consultation Metrics
    # ------------------------------------

    overall_confidence: int = 0

    completeness: int = 0

    created_at: str | None = None

    last_updated: str | None = None

    framework_version: str = "1.0"

    # ------------------------------------
    # Dimension Operations
    # ------------------------------------

    def get_dimension(
        self,
        name: str,
    ) -> DNADimension | None:

        return self.dimensions.get(
            name
        )

    def add_dimension(
        self,
        dimension: DNADimension,
    ) -> None:

        self.dimensions[
            dimension.name
        ] = dimension

    def has_dimension(
        self,
        name: str,
    ) -> bool:

        return (
            name in self.dimensions
        )

    # ------------------------------------
    # DNA Metrics
    # ------------------------------------

    def calculate_overall_confidence(
        self,
    ) -> int:

        if not self.dimensions:

            return 0

        total = sum(

            dimension.confidence

            for dimension in self.dimensions.values()

        )

        self.overall_confidence = int(

            total / len(self.dimensions)

        )

        return self.overall_confidence

    def calculate_completeness(
        self,
    ) -> int:

        if not self.dimensions:

            return 0

        confirmed = 0

        for dimension in self.dimensions.values():

            if dimension.knowledge_state in [

                "Emerging",

                "Confirmed",

                "Stable",

            ]:

                confirmed += 1

        self.completeness = int(

            confirmed
            / len(self.dimensions)
            * 100

        )

        return self.completeness

    # ------------------------------------
    # Reporting
    # ------------------------------------

    def summary(
        self,
    ) -> dict:

        self.calculate_overall_confidence()

        self.calculate_completeness()

        return {

            "dimensions": len(
                self.dimensions
            ),

            "overall_confidence":
                self.overall_confidence,

            "completeness":
                self.completeness,

        }