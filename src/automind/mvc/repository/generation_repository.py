from abc import (
    ABC,
    abstractmethod,
)

from models.generation import (
    Generation,
)


class GenerationRepository(
    ABC,
):
    """
    Repository contract for
    AutoMind Generations.
    """

    @abstractmethod
    def save(
        self,
        generation: Generation,
    ) -> None:
        pass

    @abstractmethod
    def update(
        self,
        generation: Generation,
    ) -> None:
        pass

    @abstractmethod
    def delete(
        self,
        generation_id: str,
    ) -> None:
        pass

    @abstractmethod
    def get(
        self,
        generation_id: str,
    ) -> Generation | None:
        pass

    @abstractmethod
    def get_by_code(
        self,
        model_id: str,
        generation_code: str,
    ) -> Generation | None:
        pass

    @abstractmethod
    def all(
        self,
    ) -> list[Generation]:
        pass

    @abstractmethod
    def get_by_model(
        self,
        model_id: str,
    ) -> list[Generation]:
        pass

    @abstractmethod
    def exists(
        self,
        generation_id: str,
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