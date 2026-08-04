import streamlit as st
from customer.profile_extractor import ProfileExtractor
from consultation.consultation_engine import ConsultationEngine

from consultation.consultation_state import (
    initialize_consultation,
)


def show_consultation():

    initialize_consultation()

    st.title("🚗 AutoMind")

    st.subheader("Your Automotive Decision Companion")

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

        # Update customer profile
        engine = ConsultationEngine()

        response = engine.process_message(
        prompt,
        st.session_state.customer_profile,
                                        )

        st.session_state.consultation_messages.append(
          {
             "role": "assistant",
             "content": response,
            }
        )

        st.rerun()