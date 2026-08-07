from models.variant import (
    Variant,
)

from mvc.orm.variant_record import (
    VariantRecord,
)


class VariantMapper:
    """
    Converts between the
    AutoMind Variant domain model
    and the PostgreSQL ORM model.
    """

    @staticmethod
    def to_record(
        variant: Variant,
    ) -> VariantRecord:

        return VariantRecord(

            id=variant.id,

            generation_id=(
                variant.generation_id
            ),

            automind_uid=(
                variant.automind_uid
            ),

            variant_name=(
                variant.variant_name
            ),

            model_year=(
                variant.model_year
            ),

            launch_year=(
                variant.launch_year
            ),

            production_start_year=(
                variant.production_start_year
            ),

            production_end_year=(
                variant.production_end_year
            ),

            engine_code=(
                variant.engine_code
            ),

            engine_cc=(
                variant.engine_cc
            ),

            fuel_type=(
                variant.fuel_type
            ),

            transmission_type=(
                variant.transmission_type
            ),

            drive_type=(
                variant.drive_type
            ),

            power_bhp=(
                variant.power_bhp
            ),

            torque_nm=(
                variant.torque_nm
            ),

            doors=(
                variant.doors
            ),

            seating_capacity=(
                variant.seating_capacity
            ),

            length_mm=(
                variant.length_mm
            ),

            width_mm=(
                variant.width_mm
            ),

            height_mm=(
                variant.height_mm
            ),

            wheelbase_mm=(
                variant.wheelbase_mm
            ),

            ground_clearance_mm=(
                variant.ground_clearance_mm
            ),

            boot_space_litres=(
                variant.boot_space_litres
            ),

            fuel_tank_capacity_litres=(
                variant.fuel_tank_capacity_litres
            ),

            status=(
                variant.status
            ),

            active=(
                variant.active
            ),

            created_at=(
                variant.created_at
            ),

            updated_at=(
                variant.updated_at
            ),

        )

    @staticmethod
    def to_domain(
        record: VariantRecord,
    ) -> Variant:

        return Variant(

            id=record.id,

            generation_id=(
                record.generation_id
            ),

            automind_uid=(
                record.automind_uid
            ),

            variant_name=(
                record.variant_name
            ),

            model_year=(
                record.model_year
            ),

            launch_year=(
                record.launch_year
            ),

            production_start_year=(
                record.production_start_year
            ),

            production_end_year=(
                record.production_end_year
            ),

            engine_code=(
                record.engine_code
            ),

            engine_cc=(
                record.engine_cc
            ),

            fuel_type=(
                record.fuel_type
            ),

            transmission_type=(
                record.transmission_type
            ),

            drive_type=(
                record.drive_type
            ),

            power_bhp=(
                record.power_bhp
            ),

            torque_nm=(
                record.torque_nm
            ),

            doors=(
                record.doors
            ),

            seating_capacity=(
                record.seating_capacity
            ),

            length_mm=(
                record.length_mm
            ),

            width_mm=(
                record.width_mm
            ),

            height_mm=(
                record.height_mm
            ),

            wheelbase_mm=(
                record.wheelbase_mm
            ),

            ground_clearance_mm=(
                record.ground_clearance_mm
            ),

            boot_space_litres=(
                record.boot_space_litres
            ),

            fuel_tank_capacity_litres=(
                record.fuel_tank_capacity_litres
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