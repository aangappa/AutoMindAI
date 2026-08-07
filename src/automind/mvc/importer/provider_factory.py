from pathlib import (
    Path,
)

from mvc.importer.base_importer import (
    BaseImporter,
)

from mvc.importer.csv_importer import (
    CSVImporter,
)


class ProviderFactory:
    """
    Creates provider importers.

    New providers can be added
    without changing the import
    pipeline.
    """

    @staticmethod
    def create(
        provider_name: str,
        **kwargs,
    ) -> BaseImporter:

        provider = (
            provider_name.lower()
        )

        if provider == "csv":

            csv_path = kwargs.get(
                "csv_path",
            )

            if csv_path is None:

                raise ValueError(
                    "csv_path is required."
                )

            return CSVImporter(
                Path(
                    csv_path
                )
            )

        raise ValueError(

            f"Unsupported provider: "
            f"{provider_name}"

        )