import hashlib
import json

from pathlib import (
    Path,
)

import pandas as pd

from mvc.importer.base_importer import (
    BaseImporter,
)


class CarDetailsV4Importer(
    BaseImporter,
):
    """
    Provider adapter for the
    Kaggle Car Details V4 dataset.

    This class converts the
    provider CSV into the
    AutoMind canonical import
    dictionary.

    It DOES NOT perform any
    entity matching or
    database operations.
    """

    def __init__(
        self,
        csv_path: str,
    ):

        self.csv_path = Path(
            csv_path
        )

    def import_data(
        self,
    ) -> list[dict]:

        dataframe = pd.read_csv(
            self.csv_path
        )

        rows: list[dict] = []

        for _, record in (
            dataframe.iterrows()
        ):

            provider_external_id = (
                self._generate_provider_id(
                    record.to_dict()
                )
            )

            rows.append(

                {

                    #
                    # Provider Information
                    #

                    "provider_name":
                        "car_details_v4",

                    "provider_external_id":
                        provider_external_id,

                    #
                    # Canonical Vehicle
                    #

                    "manufacturer":
                        self._text(
                            record.get(
                                "Make"
                            )
                        ),

                    "model":
                        self._text(
                            record.get(
                                "Model"
                            )
                        ),

                    "variant":
                        self._text(
                            record.get(
                                "Model"
                            )
                        ),

                    "generation_code":
                        "",

                    #
                    # Vehicle Specs
                    #

                    "model_year":
                        self._integer(
                            record.get(
                                "Year"
                            )
                        ),

                    "fuel_type":
                        self._text(
                            record.get(
                                "Fuel Type"
                            )
                        ),

                    "transmission":
                        self._text(
                            record.get(
                                "Transmission"
                            )
                        ),

                    "engine_code":
                        "",

                    "engine_cc":
                        self._engine_cc(
                            record.get(
                                "Engine"
                            )
                        ),

                    "power":
                        self._text(
                            record.get(
                                "Max Power"
                            )
                        ),

                    "torque":
                        self._text(
                            record.get(
                                "Max Torque"
                            )
                        ),

                    "drive_type":
                        self._text(
                            record.get(
                                "Drivetrain"
                            )
                        ),

                    "length_mm":
                        self._integer(
                            record.get(
                                "Length"
                            )
                        ),

                    "width_mm":
                        self._integer(
                            record.get(
                                "Width"
                            )
                        ),

                    "height_mm":
                        self._integer(
                            record.get(
                                "Height"
                            )
                        ),

                    "seating_capacity":
                        self._integer(
                            record.get(
                                "Seating Capacity"
                            )
                        ),

                    "fuel_tank_capacity":
                        self._integer(
                            record.get(
                                "Fuel Tank Capacity"
                            )
                        ),

                    #
                    # Raw Provider Row
                    #

                    "raw_payload":
                        record.to_dict(),

                }

            )

        return rows

    def _generate_provider_id(
        self,
        payload: dict,
    ) -> str:

        normalized_payload = (
            self._normalize_for_hash(
                payload
            )
        )

        serialized_payload = json.dumps(

            normalized_payload,

            sort_keys=True,

            separators=(
                ",",
                ":",
            ),

        )

        return hashlib.sha256(
            serialized_payload.encode(
                "utf-8"
            )
        ).hexdigest()

    def _normalize_for_hash(
        self,
        value,
    ):

        if isinstance(
            value,
            dict,
        ):

            return {

                key: self._normalize_for_hash(
                    item
                )

                for key, item in value.items()

            }

        if isinstance(
            value,
            list,
        ):

            return [

                self._normalize_for_hash(
                    item
                )

                for item in value

            ]

        if pd.isna(
            value
        ):

            return None

        if hasattr(
            value,
            "item",
        ):

            return value.item()

        return value

    def _text(
        self,
        value,
    ) -> str:

        if pd.isna(
            value
        ):

            return ""

        return str(
            value
        ).strip()

    def _integer(
        self,
        value,
    ) -> int | None:

        if pd.isna(
            value
        ):

            return None

        try:

            return int(
                float(
                    value
                )
            )

        except Exception:

            return None

    def _engine_cc(
        self,
        value,
    ) -> int | None:

        if pd.isna(
            value
        ):

            return None

        value = (
            str(value)
            .lower()
            .replace(
                "cc",
                "",
            )
            .strip()
        )

        try:

            return int(
                float(
                    value
                )
            )

        except Exception:

            return None