import hashlib


class AutoMindUIDGenerator:
    """
    Generates permanent
    AutoMind UIDs for
    canonical variants.
    """

    @staticmethod
    def generate(
        make: str,
        model: str,
        generation: str,
        variant: str,
        model_year: int | None,
        engine_code: str,
        fuel_type: str,
    ) -> str:

        value = (
            f"{make}|"
            f"{model}|"
            f"{generation}|"
            f"{variant}|"
            f"{model_year}|"
            f"{engine_code}|"
            f"{fuel_type}"
        ).lower().strip()

        digest = hashlib.sha256(

            value.encode(
                "utf-8"
            )

        ).hexdigest()

        return (
            "AM-"
            + digest[:20].upper()
        )