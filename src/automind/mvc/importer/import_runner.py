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

    def run(
        self,
        provider_name: str,
        csv_path: str,
        canonical_level: str = "variant",
    ) -> None:

        importer = (
            ProviderFactory.create(

                provider_name=provider_name,

                csv_path=csv_path,

            )
        )

        context = ProviderContext(

            provider_name=provider_name,

            provider_version="1.0",

            source_url=csv_path,

            canonical_level=canonical_level,

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

    ImportRunner().run(

        provider_name="car_details_v4",

        csv_path=(
            "datasets/"
            "kaggle/"
            "vehicle_dataset/"
            "car details v4.csv"
        ),

        canonical_level="variant",

    )