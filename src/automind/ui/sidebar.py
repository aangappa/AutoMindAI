import streamlit as st


def value(v):

    return v if v else "Not Known"


def show_sidebar():

    profile = st.session_state.customer_profile

    st.header("🧠 Customer Understanding")

    st.divider()

    st.write("### Budget")

    st.write(value(profile.budget))

    st.write("### Children")

    st.write(value(profile.children))

    st.write("### Transmission")

    st.write(value(profile.transmission))

    st.write("### Fuel")

    st.write(value(profile.fuel_type))

    st.write("### Body Style")

    st.write(value(profile.body_style))