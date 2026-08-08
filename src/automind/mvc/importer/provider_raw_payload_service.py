from datetime import (
    UTC,
    datetime,
)

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

            cleaned_payload = (
                self._clean_payload(
                    payload
                )
            )

            record = (
                ProviderRawPayloadRecord(

                    provider_name=provider_name,

                    provider_entity_id=provider_entity_id,

                    payload=cleaned_payload,

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

    def mark_processed(
        self,
        record_id: str,
        status: str = "Processed",
        notes: str = "",
    ) -> None:

        session = DatabaseSession.create()

        try:

            record = session.get(

                ProviderRawPayloadRecord,

                record_id,

            )

            if record is None:

                return

            record.processed = True

            record.processing_status = (
                status
            )

            record.processing_notes = (
                notes
            )

            record.updated_at = (
                datetime.now(
                    UTC
                )
            )

            session.commit()

        finally:

            session.close()

    def mark_failed(
        self,
        record_id: str,
        notes: str,
    ) -> None:

        session = DatabaseSession.create()

        try:

            record = session.get(

                ProviderRawPayloadRecord,

                record_id,

            )

            if record is None:

                return

            record.processed = False

            record.processing_status = (
                "Failed"
            )

            record.processing_notes = (
                notes
            )

            record.updated_at = (
                datetime.now(
                    UTC
                )
            )

            session.commit()

        finally:

            session.close()

    def _clean_payload(
        self,
        value,
    ):

        import math

        if isinstance(
            value,
            dict,
        ):

            return {

                key: self._clean_payload(
                    item
                )

                for key, item in value.items()

            }

        if isinstance(
            value,
            list,
        ):

            return [

                self._clean_payload(
                    item
                )

                for item in value

            ]

        if isinstance(
            value,
            float,
        ) and math.isnan(
            value
        ):

            return None

        return value