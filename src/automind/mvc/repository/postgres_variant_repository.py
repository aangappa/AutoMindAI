from sqlalchemy import (
    select,
)

from models.variant import (
    Variant,
)

from mvc.database.session import (
    DatabaseSession,
)

from mvc.mapper.variant_mapper import (
    VariantMapper,
)

from mvc.orm.variant_record import (
    VariantRecord,
)

from mvc.repository.variant_repository import (
    VariantRepository,
)


class PostgresVariantRepository(
    VariantRepository,
):
    """
    PostgreSQL implementation
    of VariantRepository.
    """

    def save(
        self,
        variant: Variant,
    ) -> None:

        session = DatabaseSession.create()

        try:

            record = (
                VariantMapper.to_record(
                    variant
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
        variant: Variant,
    ) -> None:

        session = DatabaseSession.create()

        try:

            record = session.get(

                VariantRecord,

                variant.id,

            )

            if record is None:

                return

            record.generation_id = (
                variant.generation_id
            )

            record.automind_uid = (
                variant.automind_uid
            )

            record.variant_name = (
                variant.variant_name
            )

            record.model_year = (
                variant.model_year
            )

            record.launch_year = (
                variant.launch_year
            )

            record.production_start_year = (
                variant.production_start_year
            )

            record.production_end_year = (
                variant.production_end_year
            )

            record.engine_code = (
                variant.engine_code
            )

            record.engine_cc = (
                variant.engine_cc
            )

            record.fuel_type = (
                variant.fuel_type
            )

            record.transmission_type = (
                variant.transmission_type
            )

            record.drive_type = (
                variant.drive_type
            )

            record.power_bhp = (
                variant.power_bhp
            )

            record.torque_nm = (
                variant.torque_nm
            )

            record.doors = (
                variant.doors
            )

            record.seating_capacity = (
                variant.seating_capacity
            )

            record.length_mm = (
                variant.length_mm
            )

            record.width_mm = (
                variant.width_mm
            )

            record.height_mm = (
                variant.height_mm
            )

            record.wheelbase_mm = (
                variant.wheelbase_mm
            )

            record.ground_clearance_mm = (
                variant.ground_clearance_mm
            )

            record.boot_space_litres = (
                variant.boot_space_litres
            )

            record.fuel_tank_capacity_litres = (
                variant.fuel_tank_capacity_litres
            )

            record.status = (
                variant.status
            )

            record.active = (
                variant.active
            )

            session.commit()

        finally:

            session.close()

    def delete(
        self,
        variant_id: str,
    ) -> None:

        session = DatabaseSession.create()

        try:

            record = session.get(

                VariantRecord,

                variant_id,

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
        variant_id: str,
    ) -> Variant | None:

        session = DatabaseSession.create()

        try:

            record = session.get(

                VariantRecord,

                variant_id,

            )

            if record is None:

                return None

            return (
                VariantMapper.to_domain(
                    record
                )
            )

        finally:

            session.close()

    def get_by_automind_uid(
        self,
        automind_uid: str,
    ) -> Variant | None:

        session = DatabaseSession.create()

        try:

            statement = select(
                VariantRecord
            ).where(

                VariantRecord.automind_uid
                == automind_uid

            )

            record = session.scalar(
                statement
            )

            if record is None:

                return None

            return (
                VariantMapper.to_domain(
                    record
                )
            )

        finally:

            session.close()

    def get_by_generation(
        self,
        generation_id: str,
    ) -> list[Variant]:

        session = DatabaseSession.create()

        try:

            statement = select(
                VariantRecord
            ).where(

                VariantRecord.generation_id
                == generation_id

            )

            records = session.scalars(
                statement
            ).all()

            return [

                VariantMapper.to_domain(
                    record
                )

                for record in records

            ]

        finally:

            session.close()

    def all(
        self,
    ) -> list[Variant]:

        session = DatabaseSession.create()

        try:

            records = session.scalars(

                select(
                    VariantRecord
                )

            ).all()

            return [

                VariantMapper.to_domain(
                    record
                )

                for record in records

            ]

        finally:

            session.close()

    def exists(
        self,
        variant_id: str,
    ) -> bool:

        return (

            self.get(
                variant_id
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
                VariantRecord
            ).delete()

            session.commit()

        finally:

            session.close()