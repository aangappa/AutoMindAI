from ai.ai_gateway import AIGateway
from models.customer_fact import CustomerFact
from prompt.prompt_builder import PromptBuilder


class FactExtractor:
    """
    Extracts structured customer facts
    from the latest conversation.
    """

    def __init__(self):

        self.ai_gateway = AIGateway()

    def extract(
        self,
        conversation_history,
    ) -> list[CustomerFact]:

        prompt = PromptBuilder.build(
            "fact_extractor_prompt.md",
            {
                "conversation_history":
                    conversation_history,
            },
        )

        ai_result = self.ai_gateway.generate_json(
            prompt
        )

        if not ai_result.success:

            return []

        facts = []

        for item in ai_result.data.get(
            "facts",
            [],
        ):

            facts.append(

                CustomerFact(

                    category=item.get(
                        "category",
                        "",
                    ),

                    attribute=item.get(
                        "attribute",
                        "",
                    ),

                    value=str(
                        item.get(
                            "value",
                            "",
                        )
                    ),

                    confidence=item.get(
                        "confidence",
                        100,
                    ),

                    source=item.get(
                        "source",
                        "Customer Statement",
                    ),

                    conversation_turn=item.get(
                        "conversation_turn",
                        0,
                    ),
                )

            )

        return facts