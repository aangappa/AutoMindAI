from dataclasses import dataclass, field

from models.conversation_update import ConversationUpdate


@dataclass
class InterpretationResult:
    """
    Result returned by the Conversation Interpreter.
    """

    success: bool

    confidence: float

    updates: list[ConversationUpdate] = field(
        default_factory=list
    )

    reason: str = ""