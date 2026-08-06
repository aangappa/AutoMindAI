from ai.ai_service import AIService
from models.ai_result import AIResult


class AIGateway:
    """
    Single entry point for all AI interactions.
    """

    def __init__(self):

        self.ai_service = AIService()

    def generate_text(
        self,
        prompt: str,
    ) -> AIResult:

        try:

            response = self.ai_service.chat(
                prompt
            )

            return AIResult(
                success=True,
                content=response,
                provider="Gemini",
            )

        except Exception as ex:

            return AIResult(
                success=False,
                error=str(ex),
                provider="Gemini",
            )

    def generate_json(
        self,
        prompt: str,
    ) -> AIResult:

        try:

            data = self.ai_service.generate_json(
                prompt
            )

            return AIResult(
                success=True,
                data=data,
                provider="Gemini",
            )

        except Exception as ex:

            return AIResult(
                success=False,
                error=str(ex),
                provider="Gemini",
            )