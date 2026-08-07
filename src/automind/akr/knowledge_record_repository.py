from akr.knowledge_record import (
    KnowledgeRecord,
)


class KnowledgeRecordRepository:
    """
    Stores normalized automotive
    knowledge records.

    Records are grouped by vehicle.

    This repository becomes the
    central knowledge store for AKR.
    """

    def __init__(self):

        self._records: dict[
            str,
            list[KnowledgeRecord]
        ] = {}

    def save(
        self,
        records: list[KnowledgeRecord],
    ) -> None:

        for record in records:

            vehicle_records = (
                self._records.setdefault(
                    record.vehicle_id,
                    []
                )
            )

            vehicle_records.append(
                record
            )

    def find(
        self,
        vehicle_id: str,
    ) -> list[KnowledgeRecord]:

        return self._records.get(
            vehicle_id,
            []
        )

    def clear(
        self,
    ) -> None:

        self._records.clear()