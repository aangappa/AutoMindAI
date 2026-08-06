from models.customer_fact import CustomerFact
from models.evidence import Evidence


class EvidenceBuilder:
    """
    Converts structured customer facts
    into behavioural evidence.
    """

    def build(
        self,
        facts: list[CustomerFact],
    ) -> list[Evidence]:

        evidence = []

        for index, fact in enumerate(
            facts,
            start=1,
        ):

            evidence.append(

                Evidence(

                    id=f"E{index}",

                    source=fact.source,

                    observation=(
                        f"{fact.attribute}: "
                        f"{fact.value}"
                    ),

                    dimension="Unknown",

                    strength="Medium",

                    conversation_turn=(
                        fact.conversation_turn
                    ),

                    confidence_impact=(
                        fact.confidence
                    ),

                    explanation=(
                        f"Derived from "
                        f"{fact.attribute}"
                    ),
                )

            )

        return evidence