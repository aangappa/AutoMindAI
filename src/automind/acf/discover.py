import yaml
from pathlib import Path

from customer.customer_profile import CustomerProfile


class DiscoverMethodology:
    """
    Implements the ACF Discover phase.
    """

    def __init__(self):

        config_path = (
            Path(__file__).parent
            / "config"
            / "discover.yaml"
        )

        with open(
            config_path,
            "r",
            encoding="utf-8",
        ) as file:

            self.config = yaml.safe_load(file)

    # ---------------------------------------------------------

    def get_known_information(
        self,
        profile: CustomerProfile,
    ) -> dict:

        known = {}

        for category in [
            "critical",
            "important",
            "optional",
        ]:

            for item in self.config["information"][category]:

                field = item["field"]

                value = getattr(profile, field)

                if value is not None:

                    known[field] = value

        return known

    # ---------------------------------------------------------

    def get_missing_information(
        self,
        profile: CustomerProfile,
    ) -> dict:

        missing = {}

        for category in [
            "critical",
            "important",
            "optional",
        ]:

            missing[category] = []

            for item in self.config["information"][category]:

                field = item["field"]

                if getattr(profile, field) is None:

                    missing[category].append(item)

        return missing

    # ---------------------------------------------------------

    def build_context(
        self,
        profile: CustomerProfile,
        latest_message: str,
    ) -> str:

        known = self.get_known_information(profile)

        missing = self.get_missing_information(profile)

        context = "Known Information\n"
        context += "-----------------\n"

        if known:

            for field, value in known.items():

                context += f"✓ {field} : {value}\n"

        else:

            context += "None\n"

        context += "\n"

        context += "Critical Information Still Missing\n"
        context += "----------------------------------\n"

        if missing["critical"]:

            for item in missing["critical"]:

                context += f"- {item['label']}\n"

        else:

            context += "None\n"

        context += "\n"

        context += "Important Information Still Missing\n"
        context += "-----------------------------------\n"

        if missing["important"]:

            for item in missing["important"]:

                context += f"- {item['label']}\n"

        else:

            context += "None\n"

        context += "\n"

        context += "Optional Information Still Missing\n"
        context += "----------------------------------\n"

        if missing["optional"]:

            for item in missing["optional"]:

                context += f"- {item['label']}\n"

        else:

            context += "None\n"

        context += "\n"

        context += "Latest Customer Message\n"
        context += "-----------------------\n"

        context += latest_message

        return context

    def get_valid_fields(self) -> str:
        """
        Returns all valid ACF fields
        for AI prompts.
        """

        lines = []

        information = self.config["information"]

        for category in [
            "critical",
            "important",
            "optional",
        ]:

            items = information.get(category, [])

            for item in items:

                lines.append(
                    f"- {item['field']} : {item['label']}"
                )

        return "\n".join(lines)

    