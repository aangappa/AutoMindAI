from models.evidence import Evidence


class EvidenceClassifier:
    """
    Classifies evidence into behavioural
    dimensions.

    This class performs only classification.
    It does not contain automotive reasoning.
    """

    DIMENSION_KEYWORDS = {

        "Family Focus": [
            "family",
            "children",
            "child",
            "passenger",
        ],

        "Budget Sensitivity": [
            "budget",
            "lakh",
            "price",
        ],

        "Ownership Horizon": [
            "ownership",
            "year",
        ],

        "Running Cost Sensitivity": [
            "fuel",
            "diesel",
            "petrol",
            "ev",
            "electric",
        ],

        "Urban Usage": [
            "city",
        ],

        "Highway Usage": [
            "highway",
        ],

        "Long Distance Usage": [
            "annual running",
            "kilometre",
            "km",
        ],

    }

    def classify(
        self,
        evidence: list[Evidence],
    ) -> dict[str, list[Evidence]]:

        classified = {}

        for item in evidence:

            observation = item.observation.lower()

            matched = False

            for (
                dimension,
                keywords,
            ) in self.DIMENSION_KEYWORDS.items():

                if any(
                    keyword in observation
                    for keyword in keywords
                ):

                    item.assign_dimension(
                        dimension
                    )

                    classified.setdefault(
                        dimension,
                        []
                    ).append(item)

                    matched = True

            if not matched:

                item.assign_dimension(
                    "General Preference"
                )

                classified.setdefault(
                    "General Preference",
                    []
                ).append(item)

        return classified