from abc import (
    ABC,
    abstractmethod,
)

from models.variant import (
    Variant,
)


class VariantRepository(
    ABC,
):
    """
    Repository contract for
    AutoMind Variants.
    """

    @abstractmethod
    def save(
        self,
        variant: Variant,
    ) -> None:
        pass

    @abstractmethod
    def update(
        self,
        variant: Variant,
    ) -> None:
        pass

    @abstractmethod
    def delete(
        self,
        variant_id: str,
    ) -> None:
        pass

    @abstractmethod
    def get(
        self,
        variant_id: str,
    ) -> Variant | None:
        pass

    @abstractmethod
    def get_by_automind_uid(
        self,
        automind_uid: str,
    ) -> Variant | None:
        pass

    @abstractmethod
    def get_by_generation(
        self,
        generation_id: str,
    ) -> list[Variant]:
        pass

    @abstractmethod
    def all(
        self,
    ) -> list[Variant]:
        pass

    @abstractmethod
    def exists(
        self,
        variant_id: str,
    ) -> bool:
        pass

    @abstractmethod
    def count(
        self,
    ) -> int:
        pass

    @abstractmethod
    def clear(
        self,
    ) -> None:
        pass