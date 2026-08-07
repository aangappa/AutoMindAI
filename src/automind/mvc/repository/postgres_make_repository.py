from sqlalchemy import (
    select,
)

from models.make import (
    Make,
)

from mvc.database.session import (
    DatabaseSession,
)

from mvc.mapper.make_mapper import (
    MakeMapper,
)

from mvc.orm.make_record import (
    MakeRecord,
)

from mvc.repository.make_repository import (
    MakeRepository,
)


class PostgresMakeRepository(
    MakeRepository,
):
    """
    PostgreSQL implementation
    of MakeRepository.
    """

    def save(
        self,
        make: Make,
    ) -> None:

        session = DatabaseSession.create()

        try:

            record = (
                MakeMapper.to_record(
                    make
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
        make: Make,
    ) -> None:

        session = DatabaseSession.create()

        try:

            record = session.get(

                MakeRecord,

                make.id,

            )

            if record is None:

                return

            record.name = make.name

            record.country = (
                make.country
            )

            record.founded_year = (
                make.founded_year
            )

            record.status = (
                make.status
            )

            record.active = (
                make.active
            )

            session.commit()

        finally:

            session.close()

    def delete(
        self,
        make_id: str,
    ) -> None:

        session = DatabaseSession.create()

        try:

            record = session.get(

                MakeRecord,

                make_id,

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
        make_id: str,
    ) -> Make | None:

        session = DatabaseSession.create()

        try:

            record = session.get(

                MakeRecord,

                make_id,

            )

            if record is None:

                return None

            return (
                MakeMapper.to_domain(
                    record
                )
            )

        finally:

            session.close()

    def get_by_name(
        self,
        name: str,
    ) -> Make | None:

        session = DatabaseSession.create()

        try:

            statement = select(
                MakeRecord
            ).where(

                MakeRecord.name == name

            )

            record = session.scalar(
                statement
            )

            if record is None:

                return None

            return (
                MakeMapper.to_domain(
                    record
                )
            )

        finally:

            session.close()

    def all(
        self,
    ) -> list[Make]:

        session = DatabaseSession.create()

        try:

            records = session.scalars(

                select(
                    MakeRecord
                )

            ).all()

            return [

                MakeMapper.to_domain(
                    record
                )

                for record in records

            ]

        finally:

            session.close()

    def exists(
        self,
        make_id: str,
    ) -> bool:

        return (

            self.get(
                make_id
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
                MakeRecord
            ).delete()

            session.commit()

        finally:

            session.close()