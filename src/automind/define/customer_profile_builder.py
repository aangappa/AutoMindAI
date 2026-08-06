from customer.customer_profile import CustomerProfile
from define.fact_repository import FactRepository


class CustomerProfileBuilder:
    """
    Builds the Customer Profile from the
    accumulated Customer Facts.

    The Fact Repository is the single source
    of truth. The Customer Profile is a
    projection of those facts.
    """

    def build(
        self,
        repository: FactRepository,
        profile: CustomerProfile,
    ) -> CustomerProfile:

        facts = repository.get_all()

        for fact in facts:

            attribute = (
                fact.attribute
                .strip()
                .lower()
                .replace(" ", "_")
            )

            if hasattr(
                profile,
                attribute,
            ):

                setattr(
                    profile,
                    attribute,
                    fact.value,
                )

        return profile