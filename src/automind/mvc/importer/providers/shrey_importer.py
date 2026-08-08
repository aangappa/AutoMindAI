import pandas as pd

from mvc.importer.base_importer import (
    BaseImporter,
)


class ShreyImporter(
    BaseImporter,
):
    """
    Provider adapter for the
    Shrey Indian Car Dataset.
    """

    PROVIDER_NAME = (
        "shrey_mishra"
    )

    def __init__(
        self,
        csv_path: str,
    ):

        self.csv_path = csv_path

    def import_data(
        self,
    ) -> list[dict]:

        dataframe = pd.read_csv(
            self.csv_path
        )

        rows: list[dict] = []

        for index, record in (
            dataframe.iterrows()
        ):

            make = self._text(
                record.get(
                    "Make"
                )
            )

            model = self._text(
                record.get(
                    "Model"
                )
            )

            variant = self._text(
                record.get(
                    "Variant"
                )
            )

            # ------------------------------------------
            # Ignore unusable rows
            # ------------------------------------------

            if not make:
                continue

            if not model:
                continue

            if not variant:
                continue

            # ------------------------------------------
            # Known source correction
            #
            # Shrey contains these incorrect
            # Mercedes-Benz -> Rolls-Royce records.
            # Do not import them.
            # ------------------------------------------

            normalized_make = (
                self._normalize(
                    make
                )
            )

            normalized_model = (
                self._normalize(
                    model
                )
            )

            if (
                normalized_make
                == "mercedes-benz"
                and normalized_model
                in {
                    "rolls-royce cullinan",
                    "rolls-royce dawn",
                    "rolls-royce drophead coupe",
                    "rolls-royce ghost series ii",
                    "rolls-royce phantom",
                    "rolls-royce phantom coupe",
                    "rolls-royce wraith",
                }
            ):
                continue

            # ------------------------------------------
            # Known source normalization
            # ------------------------------------------

            make = self._normalize_make(
                make
            )

            model = self._normalize_model(
                model
            )

            # ------------------------------------------
            # Stable provider ID
            #
            # The original CSV row number is retained
            # so the source record can always be traced.
            # ------------------------------------------

            provider_external_id = (
                f"row:{index + 2}"
            )

            # ------------------------------------------
            # Shrey metadata
            # ------------------------------------------

            provider_metadata = {

                "source_row": (
                    index + 2
                ),

                "variant": variant,

                "ex_showroom_price": (
                    self._text(
                        record.get(
                            "Ex-Showroom_Price"
                        )
                    )
                ),

                "displacement": (
                    self._number(
                        record.get(
                            "Displacement"
                        )
                    )
                ),

                "cylinders": (
                    self._number(
                        record.get(
                            "Cylinders"
                        )
                    )
                ),

                "fuel_tank_capacity": (
                    self._number(
                        record.get(
                            "Fuel_Tank_Capacity"
                        )
                    )
                ),

                "fuel_type": (
                    self._text(
                        record.get(
                            "Fuel_Type"
                        )
                    )
                ),

                "height": (
                    self._number(
                        record.get(
                            "Height"
                        )
                    )
                ),

                "length": (
                    self._number(
                        record.get(
                            "Length"
                        )
                    )
                ),

                "width": (
                    self._number(
                        record.get(
                            "Width"
                        )
                    )
                ),

                "body_type": (
                    self._text(
                        record.get(
                            "Body_Type"
                        )
                    )
                ),

                "seating_capacity": (
                    self._number(
                        record.get(
                            "Seating_Capacity"
                        )
                    )
                ),

                "transmission_type": (
                    self._text(
                        record.get(
                            "Type"
                        )
                    )
                ),

                "power": (
                    self._text(
                        record.get(
                            "Power.1"
                        )
                    )
                ),

                "torque": (
                    self._text(
                        record.get(
                            "Torque.1"
                        )
                    ),
                ),

            }

            rows.append(
                {

                    "provider_name":
                        self.PROVIDER_NAME,

                    "provider_external_id":
                        provider_external_id,

                    "manufacturer":
                        make,

                    "model":
                        model,

                    "body_style":
                        self._text(
                            record.get(
                                "Body_Type"
                            )
                        ),

                    "provider_metadata":
                        provider_metadata,

                    "raw_payload":
                        record.to_dict(),

                }
            )

        return rows

    # --------------------------------------------------
    # Text helper
    # --------------------------------------------------

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

    # --------------------------------------------------
    # Numeric helper
    # --------------------------------------------------

    def _number(
        self,
        value,
    ):

        if pd.isna(
            value
        ):
            return None

        text = str(
            value
        ).strip()

        if not text:
            return None

        try:

            number = float(
                text
            )

            if number.is_integer():
                return int(
                    number
                )

            return number

        except (
            ValueError,
            TypeError,
        ):

            return None

    # --------------------------------------------------
    # Normalization
    # --------------------------------------------------

    def _normalize(
        self,
        value: str,
    ) -> str:

        value = (
            value
            .strip()
            .lower()
        )

        return " ".join(
            value.split()
        )

    def _normalize_make(
        self,
        value: str,
    ) -> str:

        normalized = self._normalize(
            value
        )

        corrections = {

            "land rover rover":
                "land rover",

            "maruti suzuki r":
                "maruti suzuki",

        }

        return corrections.get(
            normalized,
            normalized,
        )

    def _normalize_model(
        self,
        value: str,
    ) -> str:

        return self._normalize(
            value
        )