from mvc.importer.base_importer import (
    BaseImporter,
)

from mvc.importer.providers.car_details_v4_importer import (
    CarDetailsV4Importer,
)

from mvc.importer.providers.vehiclesdb_importer import (
    VehiclesDBImporter,
)

from mvc.importer.providers.shrey_importer import (
    ShreyImporter,
)


class ProviderFactory:
    """
    Creates provider-specific
    importer implementations.
    """

    @staticmethod
    def create(
        provider_name: str,
        csv_path: str,
    ) -> BaseImporter:

        if provider_name == "car_details_v4":

            return CarDetailsV4Importer(
                csv_path
            )

        if provider_name == "vehiclesdb":

            return VehiclesDBImporter(
                csv_path
            )

        if provider_name == "shrey_mishra":

            return ShreyImporter(
                csv_path
            )

        raise ValueError(
            f"Unsupported provider: "
            f"{provider_name}"
        )