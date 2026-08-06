import streamlit as st


def show_customer_dna():

    st.subheader(
        "Customer DNA"
    )

    dna = st.session_state.customer_dna

    if not dna.dimensions:

        st.info(
            "Customer DNA has not been generated yet."
        )

        return

    rows = []

    for dimension in dna.dimensions.values():

        rows.append(
            {
                "Dimension": dimension.name,
                "Score": dimension.score,
                "Confidence": dimension.confidence,
                "Knowledge": dimension.knowledge_state,
                "Evidence": dimension.evidence_count(),
            }
        )

    st.table(rows)