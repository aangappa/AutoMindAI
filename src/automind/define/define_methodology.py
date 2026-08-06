from customer.customer_profile import CustomerProfile
from define.customer_profile_builder import (
    CustomerProfileBuilder,
)
from define.dna_reasoning_engine import (
    DNAReasoningEngine,
)
from define.evidence_builder import (
    EvidenceBuilder,
)
from define.evidence_classifier import (
    EvidenceClassifier,
)
from define.fact_extractor import (
    FactExtractor,
)
from define.fact_repository import (
    FactRepository,
)
from models.customer_dna import CustomerDNA


class DefineMethodology:
    """
    Implements the ACF Define phase.

    Customer knowledge evolves continuously
    throughout the consultation.
    """

    def __init__(self):

        self.fact_extractor = (
            FactExtractor()
        )

        self.profile_builder = (
            CustomerProfileBuilder()
        )

        self.evidence_builder = (
            EvidenceBuilder()
        )

        self.evidence_classifier = (
            EvidenceClassifier()
        )

        self.reasoning_engine = (
            DNAReasoningEngine()
        )

    def update_customer_dna(
        self,
        customer_profile: CustomerProfile,
        customer_dna: CustomerDNA,
        fact_repository: FactRepository,
        conversation_history,
    ) -> CustomerDNA:

        # -----------------------------------
        # Step 1
        # Extract Facts
        # -----------------------------------

        new_facts = self.fact_extractor.extract(
            conversation_history
        )

        # -----------------------------------
        # Step 2
        # Update Fact Repository
        # -----------------------------------

        fact_repository.add(
            new_facts
        )

        # -----------------------------------
        # Step 3
        # Build Customer Profile
        # -----------------------------------

        self.profile_builder.build(
            repository=fact_repository,
            profile=customer_profile,
        )

        # -----------------------------------
        # Step 4
        # Build Evidence
        # -----------------------------------

        facts = fact_repository.get_all()

        evidence = self.evidence_builder.build(
            facts
        )

        # -----------------------------------
        # Step 5
        # Classify Evidence
        # -----------------------------------

        classified_evidence = (
            self.evidence_classifier.classify(
                evidence
            )
        )

        # -----------------------------------
        # Step 6
        # Evolve Customer DNA
        # -----------------------------------

        customer_dna = (
            self.reasoning_engine.evolve(
                customer_dna,
                classified_evidence,
            )
        )

        return customer_dna