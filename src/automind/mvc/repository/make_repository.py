from abc import (
    ABC,
    abstractmethod,
)

from models.make import (
    Make,
)


class MakeRepository(
    ABC,
):
    """
    Repository contract for
    AutoMind Makes.
    """

    @abstractmethod
    def save(
        self,
        make: Make,
    ) -> None:
        pass

    @abstractmethod
    def update(
        self,
        make: Make,
    ) -> None:
        pass

    @abstractmethod
    def delete(
        self,
        make_id: str,
    ) -> None:
        pass

    @abstractmethod
    def get(
        self,
        make_id: str,
    ) -> Make | None:
        pass

    @abstractmethod
    def get_by_name(
        self,
        name: str,
    ) -> Make | None:
        pass

    @abstractmethod
    def all(
        self,
    ) -> list[Make]:
        pass

    @abstractmethod
    def exists(
        self,
        make_id: str,
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