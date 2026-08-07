from mvc.database.session import (
    DatabaseSession,
)

from mvc.orm.provider_raw_payload_record import (
    ProviderRawPayloadRecord,
)


class ProviderRawPayloadService:
    """
    Persists raw provider payloads
    before canonical processing.
    """

    def save(
        self,
        provider_name: str,
        provider_entity_id: str,
        payload: dict,
        payload_hash: str = "",
        batch_id: str = "",
        source_url: str = "",
    ) -> ProviderRawPayloadRecord:

        session = DatabaseSession.create()

        try:

            record = (
                ProviderRawPayloadRecord(

                    provider_name=provider_name,

                    provider_entity_id=provider_entity_id,

                    payload=payload,

                    payload_hash=payload_hash,

                    ingestion_batch=batch_id,

                    source_url=source_url,

                )
            )

            session.add(
                record
            )

            session.commit()

            session.refresh(
                record
            )

            return record

        finally:

            session.close()