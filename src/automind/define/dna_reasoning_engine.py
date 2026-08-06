from define.dna_rules import DNARules
from models.customer_dna import CustomerDNA
from models.dna_dimension import DNADimension
from models.evidence import Evidence


class DNAReasoningEngine:
    """
    Evolves CustomerDNA using the
    Automotive Consulting Framework
    reasoning rules.
    """

    def evolve(
        self,
        customer_dna: CustomerDNA,
        classified_evidence: dict[str, list[Evidence]],
    ) -> CustomerDNA:

        for (
            dimension_name,
            evidence_list,
        ) in classified_evidence.items():

            dimension = customer_dna.get_dimension(
                dimension_name
            )

            if dimension is None:

                dimension = DNADimension(
                    name=dimension_name,
                )

                customer_dna.add_dimension(
                    dimension
                )

            # ----------------------------------
            # Attach Evidence
            # ----------------------------------

            for evidence in evidence_list:

                dimension.add_evidence(
                    evidence
                )

            # ----------------------------------
            # Apply Rule
            # ----------------------------------

            rule = DNARules.get(
                dimension_name
            )

            confidence = (
                DNARules.calculate_confidence(
                    dimension_name,
                    dimension.evidence_count(),
                )
            )

            # ----------------------------------
            # Evolve Dimension
            # ----------------------------------

            dimension.evolve(

                score=rule[
                    "base_score"
                ],

                confidence=confidence,

                knowledge_state=rule[
                    "knowledge_state"
                ],

                explanation=(

                    f"{dimension_name} evolved "

                    f"from "

                    f"{dimension.evidence_count()} "

                    f"supporting evidence item(s)."

                ),

            )

        # ----------------------------------
        # Update DNA Metrics
        # ----------------------------------

        customer_dna.calculate_overall_confidence()

        customer_dna.calculate_completeness()

        return customer_dna