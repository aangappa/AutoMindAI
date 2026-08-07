from abc import (
    ABC,
    abstractmethod,
)

from models.model import (
    Model,
)


class ModelRepository(
    ABC,
):
    """
    Repository contract for
    AutoMind Models.
    """

    @abstractmethod
    def save(
        self,
        model: Model,
    ) -> None:
        pass

    @abstractmethod
    def update(
        self,
        model: Model,
    ) -> None:
        pass

    @abstractmethod
    def delete(
        self,
        model_id: str,
    ) -> None:
        pass

    @abstractmethod
    def get(
        self,
        model_id: str,
    ) -> Model | None:
        pass

    @abstractmethod
    def get_by_name(
        self,
        make_id: str,
        name: str,
    ) -> Model | None:
        pass

    @abstractmethod
    def all(
        self,
    ) -> list[Model]:
        pass

    @abstractmethod
    def get_by_make(
        self,
        make_id: str,
    ) -> list[Model]:
        pass

    @abstractmethod
    def exists(
        self,
        model_id: str,
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