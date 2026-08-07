from abc import (
    ABC,
    abstractmethod,
)

from models.vehicle import (
    Vehicle,
)


class VehicleRepository(
    ABC,
):
    """
    Contract for all AutoMind
    Vehicle repositories.

    Implementations may use:

    - PostgreSQL
    - CSV (migration only)
    - Commercial APIs
    - Cloud databases
    """

    @abstractmethod
    def save(
        self,
        vehicle: Vehicle,
    ) -> None:
        pass

    @abstractmethod
    def update(
        self,
        vehicle: Vehicle,
    ) -> None:
        pass

    @abstractmethod
    def delete(
        self,
        vehicle_id: str,
    ) -> None:
        pass

    @abstractmethod
    def get(
        self,
        vehicle_id: str,
    ) -> Vehicle | None:
        pass

    @abstractmethod
    def all(
        self,
    ) -> list[Vehicle]:
        pass

    @abstractmethod
    def exists(
        self,
        vehicle_id: str,
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