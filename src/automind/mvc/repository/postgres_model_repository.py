from sqlalchemy import (
    select,
)

from models.model import (
    Model,
)

from mvc.database.session import (
    DatabaseSession,
)

from mvc.mapper.model_mapper import (
    ModelMapper,
)

from mvc.orm.model_record import (
    ModelRecord,
)

from mvc.repository.model_repository import (
    ModelRepository,
)


class PostgresModelRepository(
    ModelRepository,
):
    """
    PostgreSQL implementation
    of ModelRepository.
    """

    def save(
        self,
        model: Model,
    ) -> None:

        session = DatabaseSession.create()

        try:

            record = (
                ModelMapper.to_record(
                    model
                )
            )

            session.add(
                record
            )

            session.commit()

        finally:

            session.close()

    def update(
        self,
        model: Model,
    ) -> None:

        session = DatabaseSession.create()

        try:

            record = session.get(

                ModelRecord,

                model.id,

            )

            if record is None:

                return

            record.make_id = (
                model.make_id
            )

            record.name = (
                model.name
            )

            record.body_style = (
                model.body_style
            )

            record.segment = (
                model.segment
            )

            record.start_year = (
                model.start_year
            )

            record.end_year = (
                model.end_year
            )

            record.status = (
                model.status
            )

            record.active = (
                model.active
            )

            session.commit()

        finally:

            session.close()

    def delete(
        self,
        model_id: str,
    ) -> None:

        session = DatabaseSession.create()

        try:

            record = session.get(

                ModelRecord,

                model_id,

            )

            if record:

                session.delete(
                    record
                )

                session.commit()

        finally:

            session.close()

    def get(
        self,
        model_id: str,
    ) -> Model | None:

        session = DatabaseSession.create()

        try:

            record = session.get(

                ModelRecord,

                model_id,

            )

            if record is None:

                return None

            return (
                ModelMapper.to_domain(
                    record
                )
            )

        finally:

            session.close()

    def get_by_name(
        self,
        make_id: str,
        name: str,
    ) -> Model | None:

        session = DatabaseSession.create()

        try:

            statement = select(
                ModelRecord
            ).where(

                ModelRecord.make_id
                == make_id,

                ModelRecord.name
                == name,

            )

            record = session.scalar(
                statement
            )

            if record is None:

                return None

            return (
                ModelMapper.to_domain(
                    record
                )
            )

        finally:

            session.close()

    def all(
        self,
    ) -> list[Model]:

        session = DatabaseSession.create()

        try:

            records = session.scalars(

                select(
                    ModelRecord
                )

            ).all()

            return [

                ModelMapper.to_domain(
                    record
                )

                for record in records

            ]

        finally:

            session.close()

    def get_by_make(
        self,
        make_id: str,
    ) -> list[Model]:

        session = DatabaseSession.create()

        try:

            statement = select(
                ModelRecord
            ).where(

                ModelRecord.make_id
                == make_id

            )

            records = session.scalars(
                statement
            ).all()

            return [

                ModelMapper.to_domain(
                    record
                )

                for record in records

            ]

        finally:

            session.close()

    def exists(
        self,
        model_id: str,
    ) -> bool:

        return (

            self.get(
                model_id
            )

            is not None

        )

    def count(
        self,
    ) -> int:

        return len(
            self.all()
        )

    def clear(
        self,
    ) -> None:

        session = DatabaseSession.create()

        try:

            session.query(
                ModelRecord
            ).delete()

            session.commit()

        finally:

            session.close()