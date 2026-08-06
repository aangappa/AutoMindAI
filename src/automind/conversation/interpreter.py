from acf.discover import DiscoverMethodology
from ai.ai_gateway import AIGateway
from consultation.consultation_context import ConsultationContext
from models.conversation_update import ConversationUpdate
from models.interpretation_result import InterpretationResult
from prompt.prompt_builder import PromptBuilder


class ConversationInterpreter:
    """
    Uses AI to understand customer responses
    in the context of the conversation.
    """

    def __init__(self):

        self.ai_gateway = AIGateway()

        self.discover = DiscoverMethodology()

    def interpret(
        self,
        conversation_history=None,
        customer_profile=None,
        context: ConsultationContext | None = None,
    ) -> InterpretationResult:
        """
        Backward compatible.

        Supports both:

        interpret(conversation_history, profile)

        and

        interpret(context=context)
        """

        # -----------------------------------
        # V2 Path
        # -----------------------------------

        if context is not None:

            conversation_history = (
                context.conversation_history
            )

            customer_profile = (
                context.customer_profile
            )

        previous_assistant_message = ""
        latest_user_message = ""

        for message in reversed(conversation_history):

            if (
                not latest_user_message
                and message["role"] == "user"
            ):
                latest_user_message = message["content"]

            elif (
                not previous_assistant_message
                and message["role"] == "assistant"
            ):
                previous_assistant_message = message["content"]

            if (
                previous_assistant_message
                and latest_user_message
            ):
                break

        valid_fields = self.discover.get_valid_fields()

        known_information = (
            self.discover.get_known_information(
                customer_profile
            )
        )

        prompt = PromptBuilder.build(
            "interpreter_prompt.md",
            {
                "previous_assistant_message":
                    previous_assistant_message,

                "latest_user_message":
                    latest_user_message,

                "valid_customer_fields":
                    valid_fields,

                "known_information":
                    str(known_information),
            },
        )

        ai_result = self.ai_gateway.generate_json(
            prompt
        )

        if not ai_result.success:

            return InterpretationResult(
                success=False,
                confidence=0,
                updates=[],
                reason=ai_result.error,
            )

        data = ai_result.data

        updates = []

        for item in data.get(
            "updates",
            [],
        ):

            updates.append(
                ConversationUpdate(
                    field=item["field"],
                    value=item["value"],
                )
            )

        return InterpretationResult(
            success=data.get(
                "success",
                False,
            ),
            confidence=data.get(
                "confidence",
                0,
            ),
            updates=updates,
            reason=data.get(
                "reason",
                "",
            ),
        )