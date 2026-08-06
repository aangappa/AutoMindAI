class DNARules:
    """
    Automotive Consulting Framework (ACF)
    behavioural reasoning rules.

    This class represents the behavioural
    knowledge base of the framework.
    """

    RULES = {

        "Family Focus": {
            "base_score": 90,
            "knowledge_state": "Confirmed",
            "confidence_per_evidence": 12,
        },

        "Budget Sensitivity": {
            "base_score": 75,
            "knowledge_state": "Emerging",
            "confidence_per_evidence": 10,
        },

        "Ownership Horizon": {
            "base_score": 90,
            "knowledge_state": "Confirmed",
            "confidence_per_evidence": 12,
        },

        "Running Cost Sensitivity": {
            "base_score": 85,
            "knowledge_state": "Confirmed",
            "confidence_per_evidence": 10,
        },

        "Urban Usage": {
            "base_score": 80,
            "knowledge_state": "Emerging",
            "confidence_per_evidence": 8,
        },

        "Highway Usage": {
            "base_score": 80,
            "knowledge_state": "Emerging",
            "confidence_per_evidence": 8,
        },

        "Long Distance Usage": {
            "base_score": 85,
            "knowledge_state": "Confirmed",
            "confidence_per_evidence": 10,
        },

        "General Preference": {
            "base_score": 50,
            "knowledge_state": "Hypothesis",
            "confidence_per_evidence": 5,
        },

    }

    @classmethod
    def get(
        cls,
        dimension_name: str,
    ) -> dict:

        return cls.RULES.get(
            dimension_name,
            {
                "base_score": 50,
                "knowledge_state": "Unknown",
                "confidence_per_evidence": 5,
            },
        )

    @classmethod
    def calculate_confidence(
        cls,
        dimension_name: str,
        evidence_count: int,
    ) -> int:

        rule = cls.get(
            dimension_name
        )

        confidence = (
            rule["base_score"]
            +
            (
                evidence_count
                * rule["confidence_per_evidence"]
            )
        )

        return min(
            100,
            confidence,
        )   