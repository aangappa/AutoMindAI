from dataclasses import dataclass


@dataclass
class ConsultationStep:
    """
    Represents one step in the Automotive
    Consulting Framework (ACF).

    It acts as the contract between the
    consultation methodology and the
    consultation engine.
    """

    # ACF Phase
    phase: str

    # Customer field being collected
    target_field: str

    # Assistant message for this step
    assistant_message: str

    # Whether this phase has completed
    consultation_complete: bool = False