import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="User Register",
    page_icon="👤",
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
    "<h1 class='title'>👤 User Registration</h1>",
    unsafe_allow_html=True
)

st.write("Create your GreenTick account.")

# ----------------------------
# DATA FILE
# ----------------------------

os.makedirs("data", exist_ok=True)

user_file = "data/users.csv"

# ----------------------------
# LOAD USERS
# ----------------------------

if os.path.exists(user_file):

    users = pd.read_csv(user_file)

    users.columns = users.columns.str.strip()

else:

    users = pd.DataFrame(columns=[
        "Name",
        "email",
        "Mobile",
        "City",
        "Address",
        "Password",
        "EcoScore",
        "Level"
    ])

# ----------------------------
# FORM
# ----------------------------

with st.form("register_form"):

    name = st.text_input("👤 Full Name")

    email = st.text_input("📧 Email")

    mobile = st.text_input("📱 Mobile Number")

    city = st.text_input("🏙 City")

    address = st.text_area("🏠 Address")

    password = st.text_input(
        "🔒 Password",
        type="password"
    )

    confirm = st.text_input(
        "🔒 Confirm Password",
        type="password"
    )

    terms = st.checkbox(
        "I agree to the Terms & Conditions"
    )

    submit = st.form_submit_button("🚀 Register")

# ----------------------------
# REGISTER
# ----------------------------

if submit:

    # Empty fields
    if not all([
        name,
        email,
        mobile,
        city,
        address,
        password,
        confirm
    ]):
        st.error("⚠️ Please fill all fields.")
        st.stop()

    # Terms & Conditions
    if not terms:
        st.error("⚠️ You must accept the Terms & Conditions before registering.")
        st.stop()

    # Password match
    if password != confirm:
        st.error("❌ Passwords do not match.")
        st.stop()

    # Mobile validation
    if not (mobile.isdigit() and len(mobile) == 10):
        st.error("📱 Enter a valid 10-digit mobile number.")
        st.stop()

    # Email validation
    if "@" not in email or "." not in email:
        st.error("📧 Enter a valid email address.")
        st.stop()

    # Duplicate email
    if email.strip().lower() in users["email"].astype(str).str.strip().str.lower().values:
        st.error("⚠️ Email already registered.")
        st.stop()

    # Save User
    new_user = pd.DataFrame([{

        "Name": name.strip(),

        "email": email.strip().lower(),

        "Mobile": mobile.strip(),

        "City": city.strip(),

        "Address": address.strip(),

        "Password": password,

        "EcoScore": 0,

        "Level": "Beginner"

    }])

    users = pd.concat(
        [users, new_user],
        ignore_index=True
    )

    users.to_csv(
        user_file,
        index=False
    )

    st.success("🎉 Registration Successful!")

    st.info("👉 Now login using your Email and Password.")