from dataclasses import dataclass


@dataclass
class CustomerProfile:

    marital_status: str | None = None

    children: int | None = None

    budget: int | None = None

    body_style: str | None = None

    transmission: str | None = None

    fuel_type: str | None = None

    annual_running: int | None = None

    ownership_years: int | None = None