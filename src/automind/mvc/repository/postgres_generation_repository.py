from sqlalchemy import (
    select,
)

from models.generation import (
    Generation,
)

from mvc.database.session import (
    DatabaseSession,
)

from mvc.mapper.generation_mapper import (
    GenerationMapper,
)

from mvc.orm.generation_record import (
    GenerationRecord,
)

from mvc.repository.generation_repository import (
    GenerationRepository,
)


class PostgresGenerationRepository(
    GenerationRepository,
):
    """
    PostgreSQL implementation
    of GenerationRepository.
    """

    def save(
        self,
        generation: Generation,
    ) -> None:

        session = DatabaseSession.create()

        try:

            record = (
                GenerationMapper.to_record(
                    generation
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
        generation: Generation,
    ) -> None:

        session = DatabaseSession.create()

        try:

            record = session.get(

                GenerationRecord,

                generation.id,

            )

            if record is None:

                return

            record.model_id = (
                generation.model_id
            )

            record.generation_code = (
                generation.generation_code
            )

            record.marketing_name = (
                generation.marketing_name
            )

            record.start_year = (
                generation.start_year
            )

            record.end_year = (
                generation.end_year
            )

            record.facelift = (
                generation.facelift
            )

            record.status = (
                generation.status
            )

            record.active = (
                generation.active
            )

            session.commit()

        finally:

            session.close()

    def delete(
        self,
        generation_id: str,
    ) -> None:

        session = DatabaseSession.create()

        try:

            record = session.get(

                GenerationRecord,

                generation_id,

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
        generation_id: str,
    ) -> Generation | None:

        session = DatabaseSession.create()

        try:

            record = session.get(

                GenerationRecord,

                generation_id,

            )

            if record is None:

                return None

            return (
                GenerationMapper.to_domain(
                    record
                )
            )

        finally:

            session.close()

    def get_by_code(
        self,
        model_id: str,
        generation_code: str,
    ) -> Generation | None:

        session = DatabaseSession.create()

        try:

            statement = select(
                GenerationRecord
            ).where(

                GenerationRecord.model_id
                == model_id,

                GenerationRecord.generation_code
                == generation_code,

            )

            record = session.scalar(
                statement
            )

            if record is None:

                return None

            return (
                GenerationMapper.to_domain(
                    record
                )
            )

        finally:

            session.close()

    def all(
        self,
    ) -> list[Generation]:

        session = DatabaseSession.create()

        try:

            records = session.scalars(

                select(
                    GenerationRecord
                )

            ).all()

            return [

                GenerationMapper.to_domain(
                    record
                )

                for record in records

            ]

        finally:

            session.close()

    def get_by_model(
        self,
        model_id: str,
    ) -> list[Generation]:

        session = DatabaseSession.create()

        try:

            statement = select(
                GenerationRecord
            ).where(

                GenerationRecord.model_id
                == model_id

            )

            records = session.scalars(
                statement
            ).all()

            return [

                GenerationMapper.to_domain(
                    record
                )

                for record in records

            ]

        finally:

            session.close()

    def exists(
        self,
        generation_id: str,
    ) -> bool:

        return (

            self.get(
                generation_id
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
                GenerationRecord
            ).delete()

            session.commit()

        finally:

            session.close()