from acf.discover import DiscoverMethodology
from ai.ai_gateway import AIGateway
from consultation.consultation_context import ConsultationContext
from conversation.interpreter import ConversationInterpreter
from customer.profile_updater import ProfileUpdater
from define.define_methodology import DefineMethodology
from prompt.prompt_builder import PromptBuilder


class ConsultationEngine:
    """
    Coordinates the Automotive Consultation
    workflow.
    """

    def __init__(self):

        self.interpreter = ConversationInterpreter()

        self.updater = ProfileUpdater()

        self.discover = DiscoverMethodology()

        self.define = DefineMethodology()

        self.ai_gateway = AIGateway()

    def process_message(
        self,
        user_message: str,
        customer_profile,
        customer_dna,
        fact_repository,
        conversation_history,
    ) -> tuple[str, object]:

        # -----------------------------------
        # Create Consultation Context
        # -----------------------------------

        context = ConsultationContext(
            customer_profile=customer_profile,
            customer_dna=customer_dna,
            conversation_history=conversation_history,
        )

        context.latest_user_message = user_message

        # -----------------------------------
        # Step 1
        # Interpret Customer Response
        # -----------------------------------

        result = self.interpreter.interpret(
            context=context,
        )

        # -----------------------------------
        # Step 2
        # Update Customer Profile
        # -----------------------------------

        if result.success:

            self.updater.apply(
                customer_profile,
                result.updates,
            )

        context.customer_profile = (
            customer_profile
        )

        # -----------------------------------
        # Step 3
        # Update Customer DNA
        # -----------------------------------

        context.customer_dna = (
            self.define.update_customer_dna(
                customer_profile=context.customer_profile,
                customer_dna=context.customer_dna,
                fact_repository=fact_repository,
                conversation_history=context.conversation_history,
            )
        )

        # -----------------------------------
        # Step 4
        # Build Discover Context
        # -----------------------------------

        discover_context = (
            self.discover.build_context(
                customer_profile,
                user_message,
            )
        )

        # -----------------------------------
        # Step 5
        # Build Discover Prompt
        # -----------------------------------

        prompt = PromptBuilder.build(
            "discover_prompt.md",
            {
                "discover_context":
                    discover_context,
            },
        )

        # -----------------------------------
        # Step 6
        # Ask AI
        # -----------------------------------

        ai_result = self.ai_gateway.generate_text(
            prompt
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