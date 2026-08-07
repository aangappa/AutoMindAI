from models.model import (
    Model,
)

from mvc.orm.model_record import (
    ModelRecord,
)


class ModelMapper:
    """
    Converts between the
    AutoMind Model domain model
    and the PostgreSQL ORM model.
    """

    @staticmethod
    def to_record(
        model: Model,
    ) -> ModelRecord:

        return ModelRecord(

            id=model.id,

            make_id=model.make_id,

            name=model.name,

            body_style=model.body_style,

            segment=model.segment,

            start_year=model.start_year,

            end_year=model.end_year,

            status=model.status,

            active=model.active,

            created_at=model.created_at,

            updated_at=model.updated_at,

        )

    @staticmethod
    def to_domain(
        record: ModelRecord,
    ) -> Model:

        return Model(

            id=record.id,

            make_id=record.make_id,

            name=record.name,

            body_style=record.body_style,

            segment=record.segment,

            start_year=record.start_year,

            end_year=record.end_year,

            status=record.status,

            active=record.active,

            created_at=record.created_at,

            updated_at=record.updated_at,

        )