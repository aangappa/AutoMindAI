from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4
from consultation.consultation_state import ConsultationState
from consultation.consultation_message import ConsultationMessage
from customer.customer_profile import CustomerProfile


@dataclass
class Consultation:
    """
    Represents a single automotive consultation session.

    A consultation contains the customer profile, conversation history,
    consultation state, and timestamps. Business logic is intentionally
    kept outside this class.
    """

    consultation_id: str = field(default_factory=lambda: str(uuid4()))

    customer_profile: CustomerProfile = field(default_factory=CustomerProfile)

    state: ConsultationState = ConsultationState.STARTED

    conversation_history: list[ConsultationMessage] = field(default_factory=list)

    created_at: datetime = field(default_factory=datetime.now)

    updated_at: datetime = field(default_factory=datetime.now)