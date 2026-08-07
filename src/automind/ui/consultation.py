import streamlit as st

from consultation.consultation_engine import (
    ConsultationEngine,
)
from consultation.consultation_state import (
    initialize_consultation,
)
from models.recommendation_result import (
    RecommendationResult,
)
from recommend.recommendation_presenter import (
    RecommendationPresenter,
)
from ui.theme import (
    apply_theme,
)
from ui.workbench import (
    show_workbench,
)


def show_consultation():

    apply_theme()

    initialize_consultation()

    st.markdown(
        "# 🚗 AutoMind"
    )

    st.caption(
        "Your Automotive Decision Companion"
    )

    st.divider()

    left, right = st.columns(
        [1, 3],
        gap="large",
    )

    # -------------------------------------------------
    # Left Dashboard
    # -------------------------------------------------

    with left:

        show_workbench()

    # -------------------------------------------------
    # Main Conversation
    # -------------------------------------------------

    with right:

        for message in (
            st.session_state.consultation_messages
        ):

            with st.chat_message(
                message["role"]
            ):

                st.markdown(
                    message["content"]
                )

        prompt = st.chat_input(
            "Tell me about your vehicle requirements..."
        )

        if prompt:

            st.session_state.consultation_messages.append(
                {
                    "role": "user",
                    "content": prompt,
                }
            )

            engine = ConsultationEngine()

            response, customer_dna = (

                engine.process_message(

                    user_message=prompt,

                    customer_profile=(
                        st.session_state.customer_profile
                    ),

                    customer_dna=(
                        st.session_state.customer_dna
                    ),

                    fact_repository=(
                        st.session_state.fact_repository
                    ),

                    conversation_history=(
                        st.session_state.consultation_messages
                    ),

                )

            )

            st.session_state.customer_dna = (
                customer_dna
            )

            if isinstance(
                response,
                RecommendationResult,
            ):

                presenter = (
                    RecommendationPresenter()
                )

                response = presenter.present(
                    response
                )

            st.session_state.consultation_messages.append(
                {
                    "role": "assistant",
                    "content": response,
                }
            )

            st.rerun()