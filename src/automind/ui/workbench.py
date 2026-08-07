import streamlit as st

from ui.dna_view import show_customer_dna
from ui.evidence_view import show_evidence
from ui.facts_view import show_facts
from ui.metrics_view import show_metrics


def show_workbench():

    profile = (
        st.session_state.customer_profile
    )

    profile_data = vars(profile)

    known = 0
    total = len(profile_data)

    for value in profile_data.values():

        if value not in (
            None,
            "",
            [],
            {},
        ):

            known += 1

    understanding = 0

    if total > 0:

        understanding = int(

            (known / total) * 100

        )

    confidence = min(

        100,

        understanding + 10,

    )

    st.markdown(
        "## 🧠 Customer Understanding"
    )

    st.progress(
        understanding / 100
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(

            "Understanding",

            f"{understanding}%",

        )

    with col2:

        st.metric(

            "AI Confidence",

            f"{confidence}%",

        )

    st.markdown(
        "### ✅ Known"
    )

    for key, value in profile_data.items():

        if value in (

            None,

            "",

            [],

            {},

        ):

            continue

        st.write(

            f"✅ **{key.replace('_',' ').title()}** : {value}"

        )

    st.markdown(
        "### ⭕ Still Learning"
    )

    for key, value in profile_data.items():

        if value not in (

            None,

            "",

            [],

            {},

        ):

            continue

        st.write(

            f"⭕ {key.replace('_',' ').title()}"

        )

    st.divider()

    with st.expander(

        "🛠️ ACF Workbench",

        expanded=False,

    ):

        st.subheader(
            "Customer Profile"
        )

        rows = []

        for key, value in profile_data.items():

            if value in (

                None,

                "",

                [],

                {},

            ):

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

            st.table(

                rows

            )

        else:

            st.info(

                "No customer information collected yet."

            )

        st.divider()

        show_facts()

        st.divider()

        show_evidence()

        st.divider()

        show_customer_dna()

        st.divider()

        show_metrics()