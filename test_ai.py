import sys
from pathlib import Path

sys.path.insert(
    0,
    str(
        Path(__file__).parent
        / "src"
        / "automind"
    ),
)

from ai.ai_service import AIService
from prompt.prompt_builder import PromptBuilder


prompt = PromptBuilder.build(
    "discover_prompt.md",
    {
        "discover_context": """
Customer Profile

Marital Status : Married
Children : 2
Budget : 2000000
Body Style : SUV
Transmission : None
Fuel Type : None
Annual Running : None
Ownership Years : None

Latest Customer Message

I want to buy a family SUV.
"""
    },
)

service = AIService()

response = service.chat(prompt)

print(response)