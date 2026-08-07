from akr.knowledge_pipeline import (
    KnowledgePipeline,
)
from akr.knowledge_provider_manager import (
    KnowledgeProviderManager,
)
from akr.knowledge_record import (
    KnowledgeRecord,
)
from akr.knowledge_record_repository import (
    KnowledgeRecordRepository,
)
from akr.provider import (
    AutomotiveKnowledgeProvider,
)
from models.vehicle import (
    Vehicle,
)


class VehicleRepository:
    """
    Repository responsible for
    enriching vehicles with
    automotive knowledge.

    Knowledge is persisted inside
    the KnowledgeRecordRepository.
    """

    def __init__(self):

        self.providers = (
            KnowledgeProviderManager()
        )

        self.pipeline = (
            KnowledgePipeline()
        )

        self.records = (
            KnowledgeRecordRepository()
        )

    def register_provider(
        self,
        provider: AutomotiveKnowledgeProvider,
    ) -> None:

        self.providers.register(
            provider
        )

    def enrich(
        self,
        vehicle: Vehicle,
    ) -> None:

        packages = (
            self.providers.enrich(
                vehicle
            )
        )

        for package in packages:

            records = (
                self.pipeline.process(
                    package
                )
            )

            self.records.save(
                records
            )

    def find(
        self,
        vehicle_id: str,
    ) -> list[KnowledgeRecord]:

        return self.records.find(
            vehicle_id
        )