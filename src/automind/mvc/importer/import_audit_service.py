from mvc.database.session import (
    DatabaseSession,
)

from mvc.orm.provider_raw_payload_record import (
    ProviderRawPayloadRecord,
)


class ImportAuditService:
    """
    Provides audit operations
    for provider imports.
    """

    def mark_processed(
        self,
        payload_id: str,
    ) -> None:

        session = DatabaseSession.create()

        try:

            record = session.get(

                ProviderRawPayloadRecord,

                payload_id,

            )

            if record is None:

                return

            record.processed = True

            record.processing_status = (
                "Completed"
            )

            session.commit()

        finally:

            session.close()

    def mark_failed(
        self,
        payload_id: str,
        reason: str,
    ) -> None:

        session = DatabaseSession.create()

        try:

            record = session.get(

                ProviderRawPayloadRecord,

                payload_id,

            )

            if record is None:

                return

            record.processed = False

            record.processing_status = (
                "Failed"
            )

            record.processing_notes = (
                reason
            )

            session.commit()

        finally:

            session.close()