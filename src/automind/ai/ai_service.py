import json
from google import genai

from config.settings import settings


class AIService:
    """
    Responsible only for communicating
    with the configured AI model.
    """

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def chat(
        self,
        prompt: str,
    ) -> str:
        """
        Sends a prompt to the configured AI model
        and returns the response text.
        """

        response = self.client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=prompt,
        )

        return response.text

    def generate_json(
    self,
    prompt: str,
    ) -> dict:
        """
        Sends a prompt expecting JSON and
        returns a Python dictionary.
        """

        response = self.chat(prompt)

        response = (
            response
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return json.loads(response)