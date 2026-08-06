import streamlit as st

st.set_page_config(
    page_title="Trader Login",
    page_icon="🏭",
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

st.markdown("<h1 class='title'>🏭 Trader Login</h1>", unsafe_allow_html=True)

st.write("Login to manage waste pickup requests.")

# ----------------------------
# SESSION
# ----------------------------

if "trader_logged_in" not in st.session_state:
    st.session_state.trader_logged_in = False

if "trader_name" not in st.session_state:
    st.session_state.trader_name = ""

# ----------------------------
# LOGIN FORM
# ----------------------------

with st.form("trader_login"):

    trader_id = st.text_input("🏭 Trader ID")

    password = st.text_input(
        "🔒 Password",
        type="password"
    )

    login = st.form_submit_button("🚀 Login")

# ----------------------------
# DEMO LOGIN
# ----------------------------

DEMO_ID = "trader"
DEMO_PASS = "1234"

if login:

    if trader_id == DEMO_ID and password == DEMO_PASS:

        st.session_state.trader_logged_in = True
        st.session_state.trader_name = "Green Recycling Center"

        st.success("✅ Login Successful!")

        st.info(
            f"Welcome {st.session_state.trader_name}"
        )

    else:

        st.error("❌ Invalid Trader ID or Password")

# ----------------------------
# STATUS
# ----------------------------

if st.session_state.trader_logged_in:

    st.divider()

    st.success(
        f"🏭 Logged in as: {st.session_state.trader_name}"
    )

    c1, c2 = st.columns(2)

    with c1:

        if st.button("📦 Open Trader Dashboard"):

            st.switch_page("pages/6_Trader_dashboard.py")

    with c2:

        if st.button("🚪 Logout"):

            st.session_state.trader_logged_in = False
            st.session_state.trader_name = ""

            st.success("Logged Out Successfully")

            st.rerun()

st.divider()

st.info("""
### Demo Credentials

**Trader ID:** trader

**Password:** 1234
""")