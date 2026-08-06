from ai.ai_gateway import AIGateway
from models.customer_dna import CustomerDNA
from prompt.prompt_builder import PromptBuilder


class DefineMethodology:
    """
    Implements the ACF Define phase.

    The Define phase analyzes the discovered
    customer profile and produces a
    CustomerDNA.
    """

    def __init__(self):

        self.ai_gateway = AIGateway()

    def build_customer_dna(
        self,
        customer_profile,
    ) -> CustomerDNA:

        prompt = PromptBuilder.build(
            "define_prompt.md",
            {
                "customer_profile": customer_profile,
            },
        )

        ai_result = self.ai_gateway.generate_json(
            prompt
        )

        if not ai_result.success:

            return CustomerDNA()

        data = ai_result.data

        return CustomerDNA(

            decision_priorities=data.get(
                "decision_priorities",
                [],
            ),

            lifestyle=data.get(
                "lifestyle",
            ),

            driving_pattern=data.get(
                "driving_pattern",
            ),

            ownership_style=data.get(
                "ownership_style",
            ),

            technology_preference=data.get(
                "technology_preference",
            ),

            brand_preference=data.get(
                "brand_preference",
            ),

            budget_flexibility=data.get(
                "budget_flexibility",
            ),

            risk_profile=data.get(
                "risk_profile",
            ),

            sustainability_preference=data.get(
                "sustainability_preference",
            ),
        )