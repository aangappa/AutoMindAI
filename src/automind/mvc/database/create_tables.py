from mvc.database.base import (
    Base,
)

from mvc.database.engine import (
    DatabaseEngine,
)

# Import all ORM models

from mvc.orm.make_record import (
    MakeRecord,
)

from mvc.orm.model_record import (
    ModelRecord,
)

from mvc.orm.generation_record import (
    GenerationRecord,
)

from mvc.orm.variant_record import (
    VariantRecord,
)

from mvc.orm.provider_cross_reference_record import (
    ProviderCrossReferenceRecord,
)

from mvc.orm.provider_raw_payload_record import (
    ProviderRawPayloadRecord,
)


def create_tables() -> None:

    Base.metadata.create_all(

        bind=DatabaseEngine.engine()

    )

    print(

        "✅ AutoMind canonical tables created successfully."

    )


if __name__ == "__main__":

    create_tables()