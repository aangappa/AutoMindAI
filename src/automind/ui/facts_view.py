import streamlit as st


def show_facts():

    st.subheader(
        "Customer Facts"
    )

    repository = (
        st.session_state.fact_repository
    )

    facts = repository.get_all()

    if not facts:

        st.info(
            "No facts collected yet."
        )

        return

    rows = []

    for fact in facts:

        rows.append(
            {
                "Category": fact.category,
                "Attribute": fact.attribute,
                "Value": fact.value,
            }
        )

    st.table(rows)