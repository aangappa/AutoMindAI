from akr.knowledge_package import (
    KnowledgePackage,
)
from akr.knowledge_record import (
    KnowledgeRecord,
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
    KnowledgeRecord
    """

    def process(
        self,
        package: KnowledgePackage,
    ) -> list[KnowledgeRecord]:

        if not self.validate(
            package
        ):
            return []

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
    ) -> list[KnowledgeRecord]:

        records: list[
            KnowledgeRecord
        ] = []

        raw = package.raw_data

        if isinstance(raw, dict):

            records.append(

                KnowledgeRecord(

                    vehicle_id=package.vehicle_id,

                    domain="vehicle",

                    source=package.provider,

                    confidence=100,

                    data=raw,

                )

            )

        return records