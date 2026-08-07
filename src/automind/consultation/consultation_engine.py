from acf.acf_engine import ACFEngine
from acf.discover import DiscoverMethodology
from ai.ai_gateway import AIGateway
from consultation.consultation_context import (
    ConsultationContext,
)
from prompt.prompt_builder import PromptBuilder


class ConsultationEngine:
    """
    Coordinates the consultation.

    Business logic is delegated to
    the Automotive Consulting Framework.
    """

    def __init__(self):

        self.acf = ACFEngine()

        self.discover = (
            DiscoverMethodology()
        )

        self.ai_gateway = (
            AIGateway()
        )

    def process_message(
        self,
        user_message: str,
        customer_profile,
        customer_dna,
        fact_repository,
        conversation_history,
    ):

        context = ConsultationContext(

            customer_profile=
                customer_profile,

            customer_dna=
                customer_dna,

            conversation_history=
                conversation_history,

        )

        context.latest_user_message = (
            user_message
        )

        evaluation_result = (
            self.acf.process(

                context,

                fact_repository,

            )
        )

        if evaluation_result is not None:

            return (

                evaluation_result,

                context.customer_dna,

            )

        discover_context = (
            self.discover.build_context(

                context.customer_profile,

                user_message,

            )
        )

        prompt = PromptBuilder.build(

            "discover_prompt.md",

            {

                "discover_context":
                    discover_context,

            },

        )

        ai_result = (
            self.ai_gateway.generate_text(
                prompt
            )
        )

        if ai_result.success:

            return (

                ai_result.content,

                context.customer_dna,

            )

        return (

            "⚠️ AutoMind could not contact the AI service.\n\n"
            f"Reason: {ai_result.error}",

            context.customer_dna,

        )