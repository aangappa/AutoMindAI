import streamlit as st


def show_consultation():

    st.title("🚗 AutoMind")

    st.subheader("Your Automotive Decision Companion")

    st.divider()

    with st.chat_message("assistant"):

        st.markdown(
            """
Welcome to **AutoMind**.

I'm your Automotive Decision Companion.

Rather than asking you to fill out forms,
I'd like to understand your needs through a conversation.

Tell me a little about yourself and the kind of vehicle you're looking for.
"""
        )

    st.chat_input(
        "Tell me about yourself..."
    )