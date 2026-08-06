import streamlit as st

from consultation.consultation_engine import ConsultationEngine
from consultation.consultation_state import (
    initialize_consultation,
)


def show_consultation():

    initialize_consultation()

    st.title("🚗 AutoMind")

    st.subheader(
        "Your Automotive Decision Companion"
    )

    st.divider()

    for message in st.session_state.consultation_messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    prompt = st.chat_input(
        "Tell me about yourself..."
    )

    if prompt:

        st.session_state.consultation_messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        engine = ConsultationEngine()

        response = engine.process_message(
            user_message=prompt,
            profile=st.session_state.customer_profile,
            conversation_history=st.session_state.consultation_messages,
        )

        st.session_state.consultation_messages.append(
            {
                "role": "assistant",
                "content": response,
            }
        )

        st.rerun()  