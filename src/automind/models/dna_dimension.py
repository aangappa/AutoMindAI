from dataclasses import dataclass, field

from models.evidence import Evidence


@dataclass
class DNADimension:
    """
    Represents one behavioural dimension
    within Customer DNA.
    """

    # ------------------------------------
    # Identity
    # ------------------------------------

    name: str

    # ------------------------------------
    # Behaviour Assessment
    # ------------------------------------

    score: int = 0

    confidence: int = 0

    knowledge_state: str = "Unknown"

    explanation: str = ""

    # ------------------------------------
    # Evolution
    # ------------------------------------

    update_count: int = 0

    evidence: list[Evidence] = field(
        default_factory=list
    )

    # ------------------------------------
    # Domain Behaviour
    # ------------------------------------

    def add_evidence(
        self,
        evidence: Evidence,
    ) -> None:

        self.evidence.append(
            evidence
        )

    def evolve(
        self,
        score: int,
        confidence: int,
        knowledge_state: str,
        explanation: str,
    ) -> None:
        """
        Evolves this behavioural dimension
        using new reasoning results.
        """

        self.update_count += 1

        self.score = score

        self.confidence = confidence

        self.knowledge_state = (
            knowledge_state
        )

        self.explanation = (
            explanation
        )

    # ------------------------------------
    # Query Operations
    # ------------------------------------

    def evidence_count(
        self,
    ) -> int:

        return len(
            self.evidence
        )

    def has_evidence(
        self,
    ) -> bool:

        return len(
            self.evidence
        ) > 0