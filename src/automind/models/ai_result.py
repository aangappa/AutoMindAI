from dataclasses import dataclass


@dataclass
class AIResult:
    """
    Standard response returned by
    every AI interaction.
    """

    success: bool

    content: str = ""

    data: dict | None = None

    error: str = ""

    provider: str = ""

    latency_ms: float = 0

    input_tokens: int = 0

    output_tokens: int = 0