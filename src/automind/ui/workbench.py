import streamlit as st

from ui.dna_view import show_customer_dna
from ui.evidence_view import show_evidence
from ui.facts_view import show_facts
from ui.metrics_view import show_metrics


def show_workbench():

    with st.expander(
        "🛠️ ACF Workbench",
        expanded=False,
    ):

        # ------------------------------------
        # Customer Profile
        # ------------------------------------

        st.subheader(
            "Customer Profile"
        )

        profile = (
            st.session_state.customer_profile
        )

        profile_data = vars(profile)

        rows = []

        for key, value in profile_data.items():

            if value in [
                None,
                "",
                [],
                {},
            ]:

                continue

            rows.append(
                {
                    "Field": key.replace(
                        "_",
                        " ",
                    ).title(),
                    "Value": value,
                }
            )

        if rows:

            st.table(rows)

        else:

            st.info(
                "No customer information collected yet."
            )

        st.divider()

        # ------------------------------------
        # Customer Facts
        # ------------------------------------

        show_facts()

        st.divider()

        # ------------------------------------
        # Evidence
        # ------------------------------------

        show_evidence()

        st.divider()

        # ------------------------------------
        # Customer DNA
        # ------------------------------------

        show_customer_dna()

        st.divider()

        # ------------------------------------
        # Consultation Metrics
        # ------------------------------------

        show_metrics()