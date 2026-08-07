from models.vehicle import (
    Vehicle,
)

from mvc.orm.vehicle_record import (
    VehicleRecord,
)


class VehicleMapper:
    """
    Converts between the
    AutoMind Vehicle domain model
    and the PostgreSQL ORM model.
    """

    @staticmethod
    def to_record(
        vehicle: Vehicle,
    ) -> VehicleRecord:

        return VehicleRecord(

            vehicle_id=vehicle.vehicle_id,

            manufacturer=vehicle.manufacturer,

            model=vehicle.model,

            variant=vehicle.variant,

            variant_code=vehicle.variant_code,

            generation=vehicle.generation,

            year=vehicle.year,

            launch_year=vehicle.launch_year,

            discontinued=vehicle.discontinued,

            body_style=vehicle.body_style,

            segment=vehicle.segment,

            fuel_type=vehicle.fuel_type,

            transmission=vehicle.transmission,

            drivetrain=vehicle.drivetrain,

            seating_capacity=vehicle.seating_capacity,

            doors=vehicle.doors,

            engine_displacement_cc=(
                vehicle.engine_displacement_cc
            ),

            engine_description=(
                vehicle.engine_description
            ),

            horsepower=vehicle.horsepower,

            torque_nm=vehicle.torque_nm,

            price_ex_showroom=(
                vehicle.price_ex_showroom
            ),

            price_on_road=(
                vehicle.price_on_road
            ),

            currency=vehicle.currency,

            safety_rating=(
                vehicle.safety_rating
            ),

            airbags=vehicle.airbags,

            adas_level=vehicle.adas_level,

            market=vehicle.market,

            country=vehicle.country,

            status=vehicle.status,

            source=vehicle.source,

            confidence=vehicle.confidence,

            active=vehicle.active,

        )

    @staticmethod
    def to_domain(
        record: VehicleRecord,
    ) -> Vehicle:

        return Vehicle(

            vehicle_id=record.vehicle_id,

            manufacturer=record.manufacturer,

            model=record.model,

            variant=record.variant,

            variant_code=record.variant_code,

            generation=record.generation,

            year=record.year,

            launch_year=record.launch_year,

            discontinued=record.discontinued,

            body_style=record.body_style,

            segment=record.segment,

            fuel_type=record.fuel_type,

            transmission=record.transmission,

            drivetrain=record.drivetrain,

            seating_capacity=(
                record.seating_capacity
            ),

            doors=record.doors,

            engine_displacement_cc=(
                record.engine_displacement_cc
            ),

            engine_description=(
                record.engine_description
            ),

            horsepower=record.horsepower,

            torque_nm=record.torque_nm,

            price_ex_showroom=(
                record.price_ex_showroom
            ),

            price_on_road=(
                record.price_on_road
            ),

            currency=record.currency,

            safety_rating=(
                record.safety_rating
            ),

            airbags=record.airbags,

            adas_level=record.adas_level,

            market=record.market,

            country=record.country,

            status=record.status,

            source=record.source,

            confidence=record.confidence,

            active=record.active,

        )