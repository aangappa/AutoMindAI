import streamlit as st

from customer.customer_profile import CustomerProfile


def initialize_consultation():
    """
    Initialize all consultation-related state.
    This function is called once at the beginning of every session.
    """

    if "consultation_messages" not in st.session_state:

        st.session_state.consultation_messages = [
            {
                "role": "assistant",
                "content": (
                    "Welcome to AutoMind!\n\n"
                    "I'm your Automotive Decision Companion.\n\n"
                    "Rather than asking you to fill out forms, "
                    "I'd like to understand your needs through a conversation.\n\n"
                    "Tell me about yourself and the kind of vehicle you're looking for."
                ),
            }
        ]

    if "customer_profile" not in st.session_state:

        st.session_state.customer_profile = CustomerProfile()