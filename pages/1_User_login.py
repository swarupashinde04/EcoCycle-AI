import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="User Login",
    page_icon="🔐",
    layout="centered"
)

# ----------------------------
# CSS
# ----------------------------

st.markdown("""
<style>

.main{
    background-color:#F5FFF5;
}

.title{
    text-align:center;
    color:#2E7D32;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1 class='title'>🔐 User Login</h1>",
    unsafe_allow_html=True
)

st.write("Welcome back to GreenTick!")

# ----------------------------
# DATA
# ----------------------------

user_file = "data/users.csv"

if not os.path.exists(user_file):
    st.error("No users registered yet.")
    st.stop()

users = pd.read_csv(user_file)
users.columns = users.columns.str.strip()

# ----------------------------
# SESSION
# ----------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if "user_email" not in st.session_state:
    st.session_state.user_email = ""

if "eco_score" not in st.session_state:
    st.session_state.eco_score = 0

if "user_level" not in st.session_state:
    st.session_state.user_level = ""

# ----------------------------
# LOGIN FORM
# ----------------------------

with st.form("login_form"):

    email = st.text_input("📧 Email")

    password = st.text_input(
        "🔒 Password",
        type="password"
    )

    login = st.form_submit_button("🚀 Login")

# ----------------------------
# LOGIN LOGIC
# ----------------------------

if login:

    match = users[
        (users["email"].astype(str).str.strip().str.lower() == email.strip().lower()) &
        (users["Password"].astype(str).str.strip() == password.strip())
    ]

    if match.empty:

        st.error("❌ Invalid Email or Password.")

    else:

        user = match.iloc[0]

        st.session_state.logged_in = True
        st.session_state.user_name = user["Name"]
        st.session_state.user_email = user["email"]
        st.session_state.eco_score = int(user["EcoScore"])
        st.session_state.user_level = user["Level"]

        st.success(f"🎉 Welcome {user['Name']}!")

        st.info("You have logged in successfully.")

# ----------------------------
# LOGIN STATUS
# ----------------------------

if st.session_state.logged_in:

    st.divider()

    st.success(
        f"✅ Logged in as: {st.session_state.user_name}"
    )

    st.write(f"📧 Email : {st.session_state.user_email}")
    st.write(f"🌱 EcoScore : {st.session_state.eco_score}")
    st.write(f"🏅 Level : {st.session_state.user_level}")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button("🏠 Go to Home"):
            st.switch_page("Home.py")

    with col2:

        if st.button("🚪 Logout"):

            st.session_state.logged_in = False
            st.session_state.user_name = ""
            st.session_state.user_email = ""
            st.session_state.eco_score = 0
            st.session_state.user_level = ""

            st.success("Logged out successfully.")

            st.rerun()