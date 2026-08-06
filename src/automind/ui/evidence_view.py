import streamlit as st

from define.evidence_builder import EvidenceBuilder


def show_evidence():

    st.subheader(
        "Evidence"
    )

    repository = (
        st.session_state.fact_repository
    )

    facts = repository.get_all()

    if not facts:

        st.info(
            "No evidence generated yet."
        )

        return

    builder = EvidenceBuilder()

    evidence = builder.build(
        facts
    )

    rows = []

    for item in evidence:

        rows.append(
            {
                "Source": item.source,
                "Observation": item.observation,
                "Dimension": item.dimension,
                "Strength": item.strength,
            }
        )

    st.table(rows)