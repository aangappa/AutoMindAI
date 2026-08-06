from models.customer_fact import CustomerFact


class FactRepository:
    """
    Maintains all customer facts collected
    throughout the consultation.

    Facts accumulate over time and represent
    the customer's evolving knowledge base.
    """

    def __init__(self):

        self._facts: list[CustomerFact] = []

    def add(
        self,
        facts: list[CustomerFact],
    ) -> None:

        for fact in facts:

            exists = any(

                existing.category == fact.category
                and
                existing.attribute == fact.attribute
                and
                existing.value == fact.value

                for existing in self._facts

            )

            if not exists:

                self._facts.append(
                    fact
                )

    def get_all(
        self,
    ) -> list[CustomerFact]:

        return list(
            self._facts
        )

    def clear(
        self,
    ) -> None:

        self._facts.clear()