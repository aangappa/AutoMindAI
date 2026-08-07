from akr.knowledge_package import (
    KnowledgePackage,
)
from models.vehicle import (
    Vehicle,
)


class KnowledgePipeline:
    """
    Executes the Automotive Knowledge
    lifecycle.

    Acquire
        ↓
    Validate
        ↓
    Normalize
        ↓
    Enrich
        ↓
    Cache
        ↓
    Vehicle
    """

    def process(
        self,
        package: KnowledgePackage,
    ) -> Vehicle | None:

        if not self.validate(package):

            return None

        return self.normalize(
            package
        )

    # ----------------------------------

    def validate(
        self,
        package: KnowledgePackage,
    ) -> bool:

        package.valid = True

        return True

    # ----------------------------------

    def normalize(
        self,
        package: KnowledgePackage,
    ) -> Vehicle:

        data = package.raw_data

        return Vehicle(

            vehicle_id=str(

                data.get(
                    "id",
                    ""
                )

            ),

            manufacturer=data.get(
                "make",
                ""
            ),

            model=data.get(
                "model",
                ""
            ),

            variant=data.get(
                "trim",
                ""
            ),

            year=data.get(
                "year"
            ),

            body_style=data.get(
                "body_type",
                ""
            ),

            fuel_type=data.get(
                "fuel_type",
                ""
            ),

            transmission=data.get(
                "transmission",
                ""
            ),

            source=package.provider,

            knowledge=data,

        )