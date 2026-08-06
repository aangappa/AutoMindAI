from dataclasses import dataclass


@dataclass
class CustomerFact:
    """
    Represents a single structured fact
    extracted from the conversation.
    """

    category: str

    attribute: str

    value: str

    confidence: int = 100

    source: str = "Customer Statement"

    conversation_turn: int = 0