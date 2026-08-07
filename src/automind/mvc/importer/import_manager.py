from mvc.importer.base_importer import (
    BaseImporter,
)

from mvc.importer.canonical_import_service import (
    CanonicalImportService,
)

from mvc.importer.entity_matcher import (
    EntityMatcher,
)

from mvc.importer.import_pipeline import (
    ImportPipeline,
)

from mvc.importer.import_result import (
    ImportResult,
)

from mvc.importer.provider_context import (
    ProviderContext,
)


class ImportManager:
    """
    Entry point for all
    provider imports.
    """

    def __init__(
        self,
    ):

        matcher = EntityMatcher()

        self.canonical_service = (
            CanonicalImportService(
                matcher
            )
        )

    def run(
        self,
        importer: BaseImporter,
        context: ProviderContext,
    ) -> ImportResult:

        pipeline = ImportPipeline(

            importer=importer,

            canonical_service=(
                self.canonical_service
            ),

            context=context,

        )

        return pipeline.execute()