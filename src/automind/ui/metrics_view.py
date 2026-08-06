import streamlit as st

from acf.discover import DiscoverMethodology


def show_metrics():

    st.subheader(
        "Consultation Metrics"
    )

    discover = DiscoverMethodology()

    profile = (
        st.session_state.customer_profile
    )

    fact_repository = (
        st.session_state.fact_repository
    )

    dna = (
        st.session_state.customer_dna
    )

    information = discover.config["information"]

    critical = information["critical"]
    important = information["important"]
    optional = information["optional"]

    def completed(items):

        count = 0

        for item in items:

            value = getattr(
                profile,
                item["field"],
                None,
            )

            if value not in (
                None,
                "",
                [],
                {},
            ):

                count += 1

        return count

    critical_complete = completed(
        critical
    )

    important_complete = completed(
        important
    )

    optional_complete = completed(
        optional
    )

    total_fields = (
        len(critical)
        + len(important)
        + len(optional)
    )

    completed_fields = (
        critical_complete
        + important_complete
        + optional_complete
    )

    completion = (
        completed_fields
        / total_fields
        * 100
        if total_fields
        else 0
    )

    metrics = [

        {
            "Metric": "Current Phase",
            "Value": "Discover",
        },

        {
            "Metric": "Profile Completion",
            "Value": f"{completion:.0f}%",
        },

        {
            "Metric": "Critical Fields",
            "Value": (
                f"{critical_complete}"
                f" / {len(critical)}"
            ),
        },

        {
            "Metric": "Important Fields",
            "Value": (
                f"{important_complete}"
                f" / {len(important)}"
            ),
        },

        {
            "Metric": "Optional Fields",
            "Value": (
                f"{optional_complete}"
                f" / {len(optional)}"
            ),
        },

        {
            "Metric": "Facts Collected",
            "Value": len(
                fact_repository.get_all()
            ),
        },

        {
            "Metric": "DNA Dimensions",
            "Value": len(
                dna.dimensions
            ),
        },

        {
            "Metric": "Ready For Evaluate",
            "Value": (
                "Yes"
                if critical_complete
                == len(critical)
                else "No"
            ),
        },

    ]

    st.table(metrics)