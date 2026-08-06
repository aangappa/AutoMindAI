from models.customer_dna import CustomerDNA
from models.dna_dimension import DNADimension


class DNAUpdater:
    """
    Evolves the customer's behavioural DNA
    using newly inferred dimensions.
    """

    def apply(
        self,
        customer_dna: CustomerDNA,
        updated_dimensions: list[DNADimension],
    ) -> CustomerDNA:

        for new_dimension in updated_dimensions:

            existing_dimension = (
                customer_dna.get_dimension(
                    new_dimension.name
                )
            )

            if existing_dimension is None:

                customer_dna.add_dimension(
                    new_dimension
                )

                continue

            # -----------------------------
            # Evolve Existing Dimension
            # -----------------------------

            existing_dimension.score = (
                new_dimension.score
            )

            existing_dimension.confidence = max(
                existing_dimension.confidence,
                new_dimension.confidence,
            )

            existing_dimension.knowledge_state = (
                new_dimension.knowledge_state
            )

            existing_dimension.explanation = (
                new_dimension.explanation
            )

            existing_dimension.update_count += 1

        return customer_dna