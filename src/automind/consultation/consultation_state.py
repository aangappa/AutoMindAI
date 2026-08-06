import streamlit as st

from customer.customer_profile import CustomerProfile
from define.fact_repository import FactRepository
from models.customer_dna import CustomerDNA


def initialize_consultation():

    if "customer_profile" not in st.session_state:

        st.session_state.customer_profile = (
            CustomerProfile()
        )

    if "customer_dna" not in st.session_state:

        st.session_state.customer_dna = (
            CustomerDNA()
        )

    if "fact_repository" not in st.session_state:

        st.session_state.fact_repository = (
            FactRepository()
        )

    if (
        "consultation_messages"
        not in st.session_state
    ):

        st.session_state.consultation_messages = [

            {
                "role": "assistant",
                "content": (
                    "Hello! I'm AutoMind.\n\n"
                    "I'm here to understand your "
                    "requirements and help you "
                    "find the most suitable vehicle.\n\n"
                    "What kind of vehicle are you "
                    "looking for today?"
                ),
            }

        ]