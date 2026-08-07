import streamlit as st

from consultation.consultation_engine import (
    ConsultationEngine,
)
from consultation.consultation_state import (
    initialize_consultation,
)
from models.evaluation_result import (
    EvaluationResult,
)
from ui.workbench import show_workbench


def show_consultation():

    initialize_consultation()

    st.title("🚗 AutoMind")

    st.subheader(
        "Your Automotive Decision Companion"
    )

    st.divider()

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
            EvaluationResult,
        ):

            lines = [

                "# 🚗 Vehicle Evaluations",

                "",

            ]

            for index, evaluation in enumerate(

                response.ranked(),

                start=1,

            ):

                lines.extend(

                    [

                        f"## {index}. {evaluation.vehicle_name}",

                        f"Overall Score: {evaluation.overall_score}",

                        f"Recommendation: {evaluation.recommendation_level}",

                        "",

                    ]

                )

            response = "\n".join(
                lines
            )

        st.session_state.consultation_messages.append(
            {
                "role": "assistant",
                "content": response,
            }
        )

        st.rerun()

    st.divider()

    show_workbench()