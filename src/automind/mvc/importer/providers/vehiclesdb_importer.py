import json

import pandas as pd

from mvc.importer.base_importer import (
    BaseImporter,
)


class VehiclesDBImporter(
    BaseImporter,
):
    """
    Provider adapter for the
    VehiclesDB dataset.
    """

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

        for _, record in (
            dataframe.iterrows()
        ):

            kind = self._text(
                record.get(
                    "kind"
                )
            )

            if kind != "car":

                continue

            make_slug = self._text(
                record.get(
                    "make_slug"
                )
            )

            make_name = self._text(
                record.get(
                    "make_name"
                )
            )

            model_slug = self._text(
                record.get(
                    "model_slug"
                )
            )

            model_name = self._text(
                record.get(
                    "model_name"
                )
            )

            provider_external_id = (
                f"{make_slug}/{model_slug}"
            )

            provider_metadata = {

                "make_slug": (
                    make_slug
                ),

                "model_slug": (
                    model_slug
                ),

                "body_types": (
                    self._parse_value(
                        record.get(
                            "body_types"
                        )
                    )
                ),

                "countries": (
                    self._parse_value(
                        record.get(
                            "countries"
                        )
                    )
                ),

                "regions": (
                    self._parse_value(
                        record.get(
                            "regions"
                        )
                    )
                ),

                "global_popularity_decile": (
                    self._integer(
                        record.get(
                            "global_popularity_decile"
                        )
                    )
                ),

                "aliases": (
                    self._parse_value(
                        record.get(
                            "aliases"
                        )
                    )
                ),

                "former_ids": (
                    self._parse_value(
                        record.get(
                            "former_ids"
                        )
                    )
                ),

            }

            rows.append(

                {

                    "provider_name":
                        "vehiclesdb",

                    "provider_external_id":
                        provider_external_id,

                    "manufacturer":
                        make_name,

                    "model":
                        model_name,

                    "body_style":
                        self._body_style(
                            record.get(
                                "body_types"
                            )
                        ),

                    "provider_metadata":
                        provider_metadata,

                    "raw_payload":
                        record.to_dict(),

                }

            )

        return rows

    def _body_style(
        self,
        value,
    ) -> str:

        parsed = self._parse_value(
            value
        )

        if isinstance(
            parsed,
            list,
        ):

            return ", ".join(
                str(item)
                for item in parsed
                if str(item).strip()
            )

        if parsed is None:

            return ""

        return str(
            parsed
        ).strip()

    def _parse_value(
        self,
        value,
    ):

        if pd.isna(
            value
        ):

            return None

        if isinstance(
            value,
            (
                list,
                dict,
            ),
        ):

            return value

        text = str(
            value
        ).strip()

        if not text:

            return None

        try:

            return json.loads(
                text
            )

        except Exception:

            return text

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