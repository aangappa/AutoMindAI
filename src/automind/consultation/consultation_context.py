from dataclasses import dataclass, field

from customer.customer_profile import CustomerProfile


@dataclass
class ConsultationContext:
    """
    Represents the complete state of
    an ongoing customer consultation.
    """

    # Customer
    customer_profile: CustomerProfile

    # Conversation
    conversation_history: list = field(
        default_factory=list
    )

    # Current ACF Phase
    current_phase: str = "Discover"

    # ACF Context
    known_information: dict = field(
        default_factory=dict
    )

    missing_information: dict = field(
        default_factory=dict
    )

    valid_fields: str = ""

    # Interpreter

    latest_user_message: str = ""

    previous_assistant_message: str = ""

    # Future

    target_field: str = ""

    consultation_complete: bool = False