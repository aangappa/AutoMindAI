from sqlalchemy import (
    select,
)

from models.vehicle import (
    Vehicle,
)

from mvc.database.session import (
    DatabaseSession,
)

from mvc.mapper.vehicle_mapper import (
    VehicleMapper,
)

from mvc.orm.vehicle_record import (
    VehicleRecord,
)

from mvc.repository.vehicle_repository import (
    VehicleRepository,
)


class PostgresVehicleRepository(
    VehicleRepository,
):
    """
    PostgreSQL implementation of
    the Vehicle Repository.
    """

    def save(
        self,
        vehicle: Vehicle,
    ) -> None:

        session = DatabaseSession.create()

        try:

            record = (
                VehicleMapper.to_record(
                    vehicle
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
        vehicle: Vehicle,
    ) -> None:

        session = DatabaseSession.create()

        try:

            record = session.get(

                VehicleRecord,

                vehicle.vehicle_id,

            )

            if record is None:

                return

            updated = (
                VehicleMapper.to_record(
                    vehicle
                )
            )

            for key, value in vars(
                updated
            ).items():

                if key.startswith(
                    "_"
                ):

                    continue

                setattr(

                    record,

                    key,

                    value,

                )

            session.commit()

        finally:

            session.close()

    def delete(
        self,
        vehicle_id: str,
    ) -> None:

        session = DatabaseSession.create()

        try:

            record = session.get(

                VehicleRecord,

                vehicle_id,

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
        vehicle_id: str,
    ) -> Vehicle | None:

        session = DatabaseSession.create()

        try:

            record = session.get(

                VehicleRecord,

                vehicle_id,

            )

            if record is None:

                return None

            return VehicleMapper.to_domain(
                record
            )

        finally:

            session.close()

    def all(
        self,
    ) -> list[Vehicle]:

        session = DatabaseSession.create()

        try:

            records = session.scalars(

                select(
                    VehicleRecord
                )

            ).all()

            return [

                VehicleMapper.to_domain(
                    record
                )

                for record in records

            ]

        finally:

            session.close()

    def exists(
        self,
        vehicle_id: str,
    ) -> bool:

        return (

            self.get(
                vehicle_id
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
                VehicleRecord
            ).delete()

            session.commit()

        finally:

            session.close()