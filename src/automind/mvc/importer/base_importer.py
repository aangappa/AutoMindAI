from abc import (
    ABC,
    abstractmethod,
)


class BaseImporter(
    ABC,
):
    """
    Base contract for all
    AutoMind data importers.

    Examples:

    CSV

    Kaggle

    JATO

    CarsXE

    OEM APIs
    """

    @abstractmethod
    def import_data(
        self,
    ) -> None:
        """
        Imports data into
        AutoMind Canonical MVC.
        """
        pass