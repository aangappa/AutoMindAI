from mvc.importer.base_importer import (
    BaseImporter,
)

from mvc.importer.csv_importer import (
    CSVImporter,
)

from mvc.importer.providers.car_details_v4_importer import (
    CarDetailsV4Importer,
)


class ProviderFactory:
    """
    Factory responsible for
    creating provider-specific
    importers.
    """

    @staticmethod
    def create(
        provider_name: str,
        **kwargs,
    ) -> BaseImporter:

        provider_name = (
            provider_name
            .lower()
            .strip()
        )

        if provider_name == "csv":

            return CSVImporter(

                csv_path=kwargs[
                    "csv_path"
                ],

            )

        if provider_name == "car_details_v4":

            return CarDetailsV4Importer(

                csv_path=kwargs[
                    "csv_path"
                ],

            )

        raise ValueError(

            f"Unsupported provider: "
            f"{provider_name}"

        )