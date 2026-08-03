import streamlit as st
from customer.profile_extractor import ProfileExtractor

from conversation.consultation_state import (
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
        profile = st.session_state.customer_profile

        extractor = ProfileExtractor()

        extractor.extract(prompt, profile)

        st.session_state.consultation_messages.append(
            {
                "role": "assistant",
                "content": (
                    "Thank you! I've started understanding your requirements.\n\n"
                    "We'll continue building your automotive profile before recommending a vehicle."
                ),
            }
        )

        st.rerun()