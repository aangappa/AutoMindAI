from uuid import (
    uuid4,
)

from models.generation import (
    Generation,
)

from models.make import (
    Make,
)

from models.model import (
    Model,
)

from models.variant import (
    Variant,
)

from mvc.importer.automind_uid_generator import (
    AutoMindUIDGenerator,
)

from mvc.importer.entity_matcher import (
    EntityMatcher,
)

from mvc.importer.provider_cross_reference_service import (
    ProviderCrossReferenceService,
)

from mvc.importer.provider_raw_payload_service import (
    ProviderRawPayloadService,
)

from mvc.repository.postgres_generation_repository import (
    PostgresGenerationRepository,
)

from mvc.repository.postgres_make_repository import (
    PostgresMakeRepository,
)

from mvc.repository.postgres_model_repository import (
    PostgresModelRepository,
)

from mvc.repository.postgres_variant_repository import (
    PostgresVariantRepository,
)


class CanonicalImportService:
    """
    Converts provider records into
    AutoMind canonical entities.

    Provider data is first stored as
    raw payload and then matched
    against the canonical hierarchy.

    The canonical_level controls how
    far the provider data should be
    processed.

    Supported levels:

    make
    model
    generation
    variant
    """

    def __init__(
        self,
        matcher: EntityMatcher,
    ):

        self.matcher = matcher

        self.make_repository = (
            PostgresMakeRepository()
        )

        self.model_repository = (
            PostgresModelRepository()
        )

        self.generation_repository = (
            PostgresGenerationRepository()
        )

        self.variant_repository = (
            PostgresVariantRepository()
        )

        self.raw_payload_service = (
            ProviderRawPayloadService()
        )

        self.cross_reference_service = (
            ProviderCrossReferenceService()
        )

    def process(
        self,
        provider_name: str,
        provider_version: str,
        row: dict,
        canonical_level: str = "variant",
    ) -> None:

        provider_external_id = (
            row.get(
                "provider_external_id",
                row.get(
                    "vehicle_id",
                    "",
                ),
            )
        )

        #
        # Store the original provider
        # payload before canonical processing.
        #

        self.raw_payload_service.save(

            provider_name=provider_name,

            provider_entity_id=(
                provider_external_id
            ),

            payload=row,

        )

        #
        # Make
        #

        make = self.matcher.match_make(
            row
        )

        if make is None:

            make = Make(

                id=str(
                    uuid4()
                ),

                name=row.get(
                    "manufacturer",
                    "",
                ).strip(),

            )

            self.make_repository.save(
                make
            )

        #
        # Make-level provider
        #

        if canonical_level == "make":

            self.cross_reference_service.save(

                canonical_type="make",

                canonical_id=make.id,

                provider_name=provider_name,

                provider_external_id=(
                    provider_external_id
                ),

                provider_version=(
                    provider_version
                ),

            )

            return

        #
        # Model
        #

        model = self.matcher.match_model(
            row,
            make,
        )

        if model is None:

            model = Model(

                id=str(
                    uuid4()
                ),

                make_id=make.id,

                name=row.get(
                    "model",
                    "",
                ).strip(),

                body_style=row.get(
                    "body_style",
                    "",
                ),

            )

            self.model_repository.save(
                model
            )

        #
        # Model-level provider
        #

        if canonical_level == "model":

            self.cross_reference_service.save(

                canonical_type="model",

                canonical_id=model.id,

                provider_name=provider_name,

                provider_external_id=(
                    provider_external_id
                ),

                provider_version=(
                    provider_version
                ),

                provider_metadata=row.get(
                    "provider_metadata"
                ),

            )

            return

        #
        # Generation
        #

        generation = (
            self.matcher.match_generation(
                row,
                model,
            )
        )

        if generation is None:

            generation = Generation(

                id=str(
                    uuid4()
                ),

                model_id=model.id,

                generation_code=row.get(
                    "generation_code",
                    "",
                ),

                start_year=None,

                end_year=None,

            )

            self.generation_repository.save(
                generation
            )

        #
        # Generation-level provider
        #

        if canonical_level == "generation":

            self.cross_reference_service.save(

                canonical_type="generation",

                canonical_id=generation.id,

                provider_name=provider_name,

                provider_external_id=(
                    provider_external_id
                ),

                provider_version=(
                    provider_version
                ),

                provider_metadata=row.get(
                    "provider_metadata"
                ),

            )

            return

        #
        # Generate AutoMind UID
        #

        uid = AutoMindUIDGenerator.generate(

            make=make.name,

            model=model.name,

            generation=(
                generation.generation_code
            ),

            variant=row.get(
                "variant",
                "",
            ),

            model_year=None,

            engine_code=row.get(
                "engine_code",
                "",
            ),

            fuel_type=row.get(
                "fuel_type",
                "",
            ),

        )

        #
        # Look for existing canonical variant
        #

        variant = (
            self.variant_repository
            .get_by_automind_uid(
                uid
            )
        )

        #
        # Already exists
        #

        if variant is not None:

            self.cross_reference_service.save(

                canonical_type="variant",

                canonical_id=variant.id,

                provider_name=provider_name,

                provider_external_id=(
                    provider_external_id
                ),

                provider_version=(
                    provider_version
                ),

                provider_metadata=row.get(
                    "provider_metadata"
                ),

            )

            return

        #
        # Create new canonical variant
        #

        variant = Variant(

            id=str(
                uuid4()
            ),

            generation_id=generation.id,

            automind_uid=uid,

            variant_name=row.get(
                "variant",
                "",
            ),

            model_year=0,

            launch_year=None,

            production_start_year=None,

            production_end_year=None,

            engine_code=row.get(
                "engine_code",
                "",
            ),

            engine_cc=int(
                row.get(
                    "engine_cc",
                    0,
                )
                or 0
            ),

            fuel_type=row.get(
                "fuel_type",
                "",
            ),

            transmission_type=row.get(
                "transmission",
                "",
            ),

            seating_capacity=int(
                row.get(
                    "seating_capacity",
                    0,
                )
                or 0
            ),

        )

        self.variant_repository.save(
            variant
        )

        #
        # Store provider → canonical
        # variant relationship.
        #

        self.cross_reference_service.save(

            canonical_type="variant",

            canonical_id=variant.id,

            provider_name=provider_name,

            provider_external_id=(
                provider_external_id
            ),

            provider_version=(
                provider_version
            ),

            provider_metadata=row.get(
                "provider_metadata"
            ),

        )