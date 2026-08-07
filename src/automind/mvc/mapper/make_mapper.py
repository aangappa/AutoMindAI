from models.make import (
    Make,
)

from mvc.orm.make_record import (
    MakeRecord,
)


class MakeMapper:
    """
    Converts between the
    AutoMind Make domain model
    and the PostgreSQL ORM model.
    """

    @staticmethod
    def to_record(
        make: Make,
    ) -> MakeRecord:

        return MakeRecord(

            id=make.id,

            name=make.name,

            country=make.country,

            founded_year=make.founded_year,

            status=make.status,

            active=make.active,

            created_at=make.created_at,

            updated_at=make.updated_at,

        )

    @staticmethod
    def to_domain(
        record: MakeRecord,
    ) -> Make:

        return Make(

            id=record.id,

            name=record.name,

            country=record.country,

            founded_year=record.founded_year,

            status=record.status,

            active=record.active,

            created_at=record.created_at,

            updated_at=record.updated_at,

        )