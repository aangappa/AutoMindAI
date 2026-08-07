import streamlit as st


def apply_theme():

    st.set_page_config(

        page_title="AutoMind",

        page_icon="🚗",

        layout="wide",

        initial_sidebar_state="collapsed",

    )

    st.markdown(

        """
<style>

/* ------------------------------------------------ */
/* Page */
/* ------------------------------------------------ */

.block-container{

    padding-top:0.8rem;

    padding-bottom:0.8rem;

    padding-left:1.5rem;

    padding-right:1.5rem;

    max-width:1700px;

}

/* ------------------------------------------------ */
/* Typography */
/* ------------------------------------------------ */

html,
body,
[class*="css"]{

    font-size:14px;

}

h1{

    font-size:30px !important;

    margin-bottom:0.3rem;

}

h2{

    font-size:22px !important;

    margin-bottom:0.25rem;

}

h3{

    font-size:18px !important;

    margin-bottom:0.2rem;

}

h4{

    font-size:16px !important;

}

p{

    font-size:14px;

}

/* ------------------------------------------------ */
/* Chat */
/* ------------------------------------------------ */

.stChatMessage{

    border-radius:14px;

    padding:0.65rem;

    margin-bottom:0.4rem;

}

/* ------------------------------------------------ */
/* Buttons */
/* ------------------------------------------------ */

.stButton button{

    border-radius:10px;

}

/* ------------------------------------------------ */
/* Metrics */
/* ------------------------------------------------ */

div[data-testid="metric-container"]{

    border:1px solid #2b2b2b;

    border-radius:12px;

    padding:0.7rem;

}

/* ------------------------------------------------ */
/* Tables */
/* ------------------------------------------------ */

table{

    font-size:13px;

}

/* ------------------------------------------------ */
/* Expander */
/* ------------------------------------------------ */

.streamlit-expanderHeader{

    font-size:14px;

    font-weight:600;

}

/* ------------------------------------------------ */
/* Progress */
/* ------------------------------------------------ */

.stProgress{

    margin-bottom:0.6rem;

}

/* ------------------------------------------------ */
/* Horizontal Rule */
/* ------------------------------------------------ */

hr{

    margin-top:0.6rem;

    margin-bottom:0.6rem;

}

/* ------------------------------------------------ */
/* Recommendation Cards */
/* (Used later) */
/* ------------------------------------------------ */

.recommendation-card{

    border:1px solid #333333;

    border-radius:14px;

    padding:16px;

    margin-bottom:14px;

    background:#1b1b1b;

}

</style>
""",

        unsafe_allow_html=True,

    )