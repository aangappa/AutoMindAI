from mvc.importer.base_importer import (
    BaseImporter,
)

from mvc.importer.canonical_import_service import (
    CanonicalImportService,
)

from mvc.importer.import_result import (
    ImportResult,
)

from mvc.importer.provider_context import (
    ProviderContext,
)


class ImportPipeline:
    """
    Executes the complete
    AutoMind import pipeline.
    """

    def __init__(
        self,
        importer: BaseImporter,
        canonical_service: CanonicalImportService,
        context: ProviderContext,
    ):

        self.importer = importer

        self.canonical_service = (
            canonical_service
        )

        self.context = context

    def execute(
        self,
    ) -> ImportResult:

        result = ImportResult(

            provider_name=(
                self.context.provider_name
            )

        )

        rows = self.importer.import_data()

        result.total_records = len(
            rows
        )

        for row in rows:

            try:

                self.canonical_service.process(

                    provider_name=(
                        self.context.provider_name
                    ),

                    provider_version=(
                        self.context.provider_version
                    ),

                    row=row,

                )

                result.imported_records += 1

            except Exception as ex:
                result.failed_records += 1

                result.errors.append(
                    str(ex)
                )

        return result