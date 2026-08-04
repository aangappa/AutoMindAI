import streamlit as st

from ui.consultation import show_consultation
from ui.sidebar import show_sidebar
from consultation.consultation_state import initialize_consultation


def show_home():

    st.set_page_config(
        page_title="AutoMind",
        page_icon="🚗",
        layout="wide"
    )

    initialize_consultation()

    left, right = st.columns([1, 3])

    with left:
        show_sidebar()

    with right:
        show_consultation()