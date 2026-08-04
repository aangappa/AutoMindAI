from google import genai

from automind.config.settings import settings


class AIService:
    """
    Responsible for communicating with the configured AI model.
    """

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def chat(self, prompt: str) -> str:
        """
        Sends a prompt to the configured AI model and
        returns the generated response.
        """

        response = self.client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=prompt,
        )

        return response.text