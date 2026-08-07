from mvc.importer.base_importer import (
    BaseImporter,
)


class ProviderRegistry:
    """
    Registers all supported
    AutoMind data providers.

    Every provider implements
    BaseImporter.
    """

    def __init__(
        self,
    ):

        self._providers: dict[
            str,
            BaseImporter,
        ] = {}

    def register(
        self,
        name: str,
        importer: BaseImporter,
    ) -> None:

        self._providers[
            name.lower()
        ] = importer

    def get(
        self,
        name: str,
    ) -> BaseImporter | None:

        return self._providers.get(
            name.lower()
        )

    def exists(
        self,
        name: str,
    ) -> bool:

        return (
            name.lower()
            in self._providers
        )

    def providers(
        self,
    ) -> list[str]:

        return sorted(
            self._providers.keys()
        )

    def clear(
        self,
    ) -> None:

        self._providers.clear()