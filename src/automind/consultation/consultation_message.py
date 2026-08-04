from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4


class MessageRole(Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


@dataclass
class ConsultationMessage:
    """
    Represents a single message exchanged during a consultation.
    """

    message_id: str = field(default_factory=lambda: str(uuid4()))

    role: MessageRole = MessageRole.USER

    content: str = ""

    timestamp: datetime = field(default_factory=datetime.now)