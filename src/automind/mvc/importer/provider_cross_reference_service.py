from sqlalchemy import (
    select,
)

from mvc.database.session import (
    DatabaseSession,
)

from mvc.orm.provider_cross_reference_record import (
    ProviderCrossReferenceRecord,
)


class ProviderCrossReferenceService:
    """
    Persists provider-to-canonical
    vehicle mappings.
    """

    def save(
        self,
        variant_id: str,
        provider_name: str,
        provider_external_id: str,
        provider_version: str = "",
        provider_metadata: dict | None = None,
        confidence: float = 1.0,
    ) -> ProviderCrossReferenceRecord:

        session = DatabaseSession.create()

        try:

            statement = select(
                ProviderCrossReferenceRecord
            ).where(

                ProviderCrossReferenceRecord.provider_name
                == provider_name,

                ProviderCrossReferenceRecord.provider_external_id
                == provider_external_id,

            )

            record = session.scalar(
                statement
            )

            if record is not None:

                record.variant_id = (
                    variant_id
                )

                record.provider_version = (
                    provider_version
                )

                record.provider_metadata = (
                    provider_metadata
                )

                record.confidence = (
                    confidence
                )

                session.commit()

                session.refresh(
                    record
                )

                return record

            record = (
                ProviderCrossReferenceRecord(

                    variant_id=variant_id,

                    provider_name=provider_name,

                    provider_external_id=provider_external_id,

                    provider_version=provider_version,

                    provider_metadata=provider_metadata,

                    confidence=confidence,

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