import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from agent.email_agent import EmailAgent

# --- TEMPORARY DEBUG: remove once secrets are confirmed working ---
st.write("EMAIL_ADDRESS loaded:", bool(st.secrets.get("EMAIL_ADDRESS")))
st.write("EMAIL_PASSWORD loaded:", bool(st.secrets.get("EMAIL_PASSWORD")))
# -------------------------------------------------------------------

st.set_page_config(
    page_title="Email Automation Agent",
    page_icon="📧",
    layout="wide"
)

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #1E88E5;
}

.subtitle {
    text-align: center;
    color: gray;
    font-size: 18px;
    margin-bottom: 30px;
}

.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 50px;
    font-size: 18px;
}

.email-card {
    background-color: #f5f7fa;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #ddd;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">📧 Email Automation Agent</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Agentic AI Email Sender using SMTP</div>',
    unsafe_allow_html=True
)

left, right = st.columns([1, 1])

with left:

    st.markdown("### 📨 Email Details")

    receiver = st.text_input(
        "Receiver Email"
    )

    goal = st.selectbox(
        "Email Type",
        [
            "welcome",
            "reminder",
            "internship"
        ]
    )

    send_btn = st.button(
        "🚀 Send Email"
    )

with right:

    st.markdown("### 🤖 Agent Workflow")

    st.info("""
    1. Analyze Goal

    2. Select Template

    3. Prepare Email

    4. Send Email

    5. Save Log
    """)

if send_btn:

    if receiver == "":

        st.error(
            "Please enter receiver email."
        )

    else:

        with st.spinner(
            "Agent Working..."
        ):

            agent = EmailAgent()

            result = agent.run(
                receiver,
                goal
            )

        st.success(
            "Email Sent Successfully"
        )

        st.markdown(
            "### 📄 Generated Email"
        )

        st.text_area(
            "",
            result,
            height=250
        )

st.markdown("---")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Templates",
        "3"
    )

with c2:
    st.metric(
        "Agent Status",
        "Active"
    )

with c3:
    st.metric(
        "SMTP",
        "Connected"
    )

st.markdown("---")

st.caption(
    "Built with Python • Streamlit • SMTP • Agentic AI Workflow"
)
