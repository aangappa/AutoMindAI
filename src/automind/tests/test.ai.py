import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from automind.ai.ai_service import AIService


service = AIService()

response = service.chat(
    "I want to buy a family SUV."
)

print(response)