from dataclasses import dataclass, field

from models.customer_dna import CustomerDNA
from customer.customer_profile import CustomerProfile


@dataclass
class ConsultationContext:
    """
    Shared consultation context passed
    between all ACF phases.

    This object represents the current
    state of the consultation.
    """

    # ------------------------------------
    # Conversation
    # ------------------------------------

    conversation_history: list = field(
        default_factory=list
    )

    latest_user_message: str = ""

    latest_assistant_message: str = ""

    # ------------------------------------
    # Knowledge Models
    # ------------------------------------

    customer_profile: CustomerProfile | None = None

    customer_dna: CustomerDNA = field(
        default_factory=CustomerDNA
    )

    # ------------------------------------
    # Consultation State
    # ------------------------------------

    current_phase: str = "Discover"

    consultation_completed: bool = False