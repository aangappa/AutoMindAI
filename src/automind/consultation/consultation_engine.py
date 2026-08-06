from acf.discover import DiscoverMethodology
from ai.ai_gateway import AIGateway
from consultation.consultation_context import ConsultationContext
from conversation.interpreter import ConversationInterpreter
from customer.profile_updater import ProfileUpdater
from prompt.prompt_builder import PromptBuilder


class ConsultationEngine:
    """
    Coordinates the Automotive Consultation
    workflow.

    This class contains no business logic.
    It orchestrates the consultation
    components.
    """

    def __init__(self):

        self.interpreter = ConversationInterpreter()

        self.updater = ProfileUpdater()

        self.discover = DiscoverMethodology()

        self.ai_gateway = AIGateway()

    def process_message(
        self,
        user_message: str,
        profile,
        conversation_history,
    ) -> str:

        # -----------------------------------
        # Create Consultation Context
        # -----------------------------------

        context = ConsultationContext(
            customer_profile=profile,
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
        # Apply Updates
        # -----------------------------------

        if result.success:

            self.updater.apply(
                profile,
                result.updates,
            )

        context.customer_profile = profile

        # -----------------------------------
        # Step 3
        # Build Discover Context
        # -----------------------------------

        discover_context = self.discover.build_context(
            profile,
            user_message,
        )

        # -----------------------------------
        # Step 4
        # Build AI Prompt
        # -----------------------------------

        prompt = PromptBuilder.build(
            "discover_prompt.md",
            {
                "discover_context": discover_context,
            },
        )

        # -----------------------------------
        # Step 5
        # Ask AI
        # -----------------------------------

        ai_result = self.ai_gateway.generate_text(
            prompt
        )

        if ai_result.success:

            return ai_result.content

        return (
            "⚠️ AutoMind could not contact the AI service.\n\n"
            f"Reason: {ai_result.error}"
        )