import streamlit as st
from chatbot import get_response
from pdf_generator import generate_pdf
from datetime import datetime
import pandas as pd


# Page configuration
st.set_page_config(
    page_title="AI Public Health Chatbot",
    page_icon="🩺",
    layout="wide"
)


# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    background-color: #4CAF50;
    color: white;
    height: 45px;
    font-size: 16px;
}

.health-card {
    padding: 15px;
    border-radius: 10px;
    background: #c8e6c9;
    color: black;
    margin-bottom: 10px;
    font-size: 16px;
    line-height: 1.8;
}

</style>
""", unsafe_allow_html=True)


# Title
st.title("🩺 AI-Driven Public Health Chatbot")

st.subheader(
    "Disease Awareness and Health Education Assistant"
)


# Session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# Two columns
col1, col2 = st.columns([3, 1])


# Right Side Topics
with col2:

    st.markdown("## Health Topics")

    st.info("Dengue")
    st.info("Malaria")
    st.info("COVID-19")
    st.info("Diabetes")
    st.info("Hypertension")
    st.info("Tuberculosis")
    st.info("Vaccination")
    st.info("Nutrition")


# Left Side Chat Area
with col1:

    st.markdown("""
<div class="health-card">

<b>Ask questions related to:</b>

<ul>
<li>Diseases</li>
<li>Symptoms</li>
<li>Prevention</li>
<li>Vaccination</li>
<li>Health Awareness</li>
</ul>

</div>
""", unsafe_allow_html=True)

    # Input box
    user_query = st.text_input(
        "Enter your health question:"
    )

    # Ask button
    if st.button("Ask Question"):

        if user_query.strip():

            response = get_response(
                user_query
            )

            st.session_state.chat_history.append({

                "time": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

                "question": user_query,

                "response": response
            })

            st.subheader(
                "Chatbot Response"
            )

            st.markdown(f"""
<div class="health-card">

{response}

</div>
""", unsafe_allow_html=True)

        else:

            st.warning(
                "Please enter a question."
            )


# Chat History
if st.session_state.chat_history:

    st.subheader("Chat History")

    for chat in reversed(
        st.session_state.chat_history
    ):

        st.markdown(f"""
<div class="health-card">

<b>Time:</b> {chat['time']}<br><br>

<b>Question:</b> {chat['question']}<br><br>

<b>Response:</b><br>
{chat['response']}

</div>
""", unsafe_allow_html=True)


# Data Table
if st.session_state.chat_history:

    df = pd.DataFrame(
        st.session_state.chat_history
    )

    st.subheader(
        "Conversation Data"
    )

    st.dataframe(df)


# PDF Report
if st.button("Generate PDF Report"):

    pdf_file = generate_pdf(
        st.session_state.chat_history
    )

    st.success(
        "PDF Report Generated Successfully!"
    )

    st.write(
        f"Saved at: {pdf_file}"
    )