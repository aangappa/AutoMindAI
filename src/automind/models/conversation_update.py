from dataclasses import dataclass
from typing import Any


@dataclass
class ConversationUpdate:
    """
    Represents a single customer profile update
    extracted from the conversation.
    """

    field: str
    value: Any