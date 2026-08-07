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


class EntityMatcher:
    """
    Matches provider entities
    to AutoMind canonical
    entities.
    """

    def __init__(
        self,
    ):

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

    def match_make(
        self,
        row: dict,
    ) -> Make | None:

        make_name = row.get(
            "manufacturer",
            "",
        ).strip()

        if not make_name:

            return None

        return self.make_repository.get_by_name(
            make_name
        )

    def match_model(
        self,
        row: dict,
        make: Make | None,
    ) -> Model | None:

        if make is None:

            return None

        model_name = row.get(
            "model",
            "",
        ).strip()

        if not model_name:

            return None

        return self.model_repository.get_by_name(

            make.id,

            model_name,

        )

    def match_generation(
        self,
        row: dict,
        model: Model | None,
    ) -> Generation | None:

        if model is None:

            return None

        generation_code = row.get(
            "generation_code",
            "",
        ).strip()

        return self.generation_repository.get_by_code(

            model.id,

            generation_code,

        )

    def match_variant(
        self,
        row: dict,
        generation: Generation | None,
    ) -> Variant | None:

        if generation is None:

            return None

        automind_uid = row.get(
            "automind_uid",
            "",
        ).strip()

        if automind_uid:

            return self.variant_repository.get_by_automind_uid(
                automind_uid
            )

        return None