from mvc.importer.import_manager import (
    ImportManager,
)

from mvc.importer.provider_context import (
    ProviderContext,
)

from mvc.importer.provider_factory import (
    ProviderFactory,
)


class ImportRunner:
    """
    Executes provider imports
    into the AutoMind
    Canonical MVC.
    """

    def run_csv(
        self,
        csv_path: str,
    ) -> None:

        importer = (
            ProviderFactory.create(

                provider_name="csv",

                csv_path=csv_path,

            )
        )

        context = ProviderContext(

            provider_name="csv",

            provider_version="1.0",

            source_url=csv_path,

        )

        manager = ImportManager()

        result = manager.run(

            importer=importer,

            context=context,

        )

        print()

        print(
            "========== Import Summary =========="
        )

        print(
            f"Provider : {result.provider_name}"
        )

        print(
            f"Total    : {result.total_records}"
        )

        print(
            f"Imported : {result.imported_records}"
        )

        print(
            f"Updated  : {result.updated_records}"
        )

        print(
            f"Skipped  : {result.skipped_records}"
        )

        print(
            f"Failed   : {result.failed_records}"
        )

        if result.errors:

            print()

            print(
                "Errors"
            )

            print(
                "------"
            )

            for error in result.errors:

                print(
                    error
                )

        print(
            "===================================="
        )


if __name__ == "__main__":

    ImportRunner().run_csv(

        "src/automind/data/vehicles.csv"

    )