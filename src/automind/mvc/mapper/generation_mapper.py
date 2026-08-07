from models.generation import (
    Generation,
)

from mvc.orm.generation_record import (
    GenerationRecord,
)


class GenerationMapper:
    """
    Converts between the
    AutoMind Generation
    domain model and the
    PostgreSQL ORM model.
    """

    @staticmethod
    def to_record(
        generation: Generation,
    ) -> GenerationRecord:

        return GenerationRecord(

            id=generation.id,

            model_id=generation.model_id,

            generation_code=(
                generation.generation_code
            ),

            marketing_name=(
                generation.marketing_name
            ),

            start_year=(
                generation.start_year
            ),

            end_year=(
                generation.end_year
            ),

            facelift=(
                generation.facelift
            ),

            status=(
                generation.status
            ),

            active=(
                generation.active
            ),

            created_at=(
                generation.created_at
            ),

            updated_at=(
                generation.updated_at
            ),

        )

    @staticmethod
    def to_domain(
        record: GenerationRecord,
    ) -> Generation:

        return Generation(

            id=record.id,

            model_id=record.model_id,

            generation_code=(
                record.generation_code
            ),

            marketing_name=(
                record.marketing_name
            ),

            start_year=(
                record.start_year
            ),

            end_year=(
                record.end_year
            ),

            facelift=(
                record.facelift
            ),

            status=(
                record.status
            ),

            active=(
                record.active
            ),

            created_at=(
                record.created_at
            ),

            updated_at=(
                record.updated_at
            ),

        )