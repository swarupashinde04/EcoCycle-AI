import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Rewards",
    page_icon="🎁",
    layout="wide"
)

st.title("🎁 Eco Rewards")
st.write("Earn rewards by recycling plastic responsibly.")

st.divider()

# -------------------------
# LOGIN CHECK
# -------------------------

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("⚠️ Please login first.")
    st.stop()

user_email = st.session_state.user_email

# -------------------------
# LOAD USERS
# -------------------------

users_file = "data/users.csv"

if os.path.exists(users_file):
    users = pd.read_csv(users_file)
else:
    st.error("Users database not found.")
    st.stop()

# Clean column names
users.columns = users.columns.str.strip()

# -------------------------
# FIND CURRENT USER
# -------------------------

user = users[
    users["email"].astype(str).str.strip().str.lower()
    == user_email.strip().lower()
]

if user.empty:
    st.error("User not found.")
    st.stop()

user = user.iloc[0]

# -------------------------
# GET ECOSCORE
# -------------------------

eco_score = user["EcoScore"] if "EcoScore" in users.columns else 0

eco_score = pd.to_numeric(
    eco_score,
    errors="coerce"
)

if pd.isna(eco_score):
    eco_score = 0

eco_score = int(eco_score)

# -------------------------
# GET LEVEL
# -------------------------

if "Level" in users.columns:
    level = user["Level"]
else:
    if eco_score >= 80:
        level = "Gold"
    elif eco_score >= 50:
        level = "Silver"
    else:
        level = "Beginner"

# -------------------------
# REWARD POINTS
# -------------------------

reward_points = eco_score * 10

# -------------------------
# PROFILE
# -------------------------

st.subheader("🌱 Your Eco Profile")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🌱 EcoScore",
        eco_score
    )

with col2:
    st.metric(
        "🏅 Level",
        level
    )

with col3:
    st.metric(
        "🎁 Reward Points",
        reward_points
    )

st.divider()

# -------------------------
# COUPONS
# -------------------------

st.subheader("🎟 Available Coupons")

coupons = [
    {"name": "🛒 ₹100 Amazon Coupon", "cost": 100},
    {"name": "☕ Free Coffee Coupon", "cost": 50},
    {"name": "🍕 20% OFF Food Voucher", "cost": 150},
    {"name": "🛍 ₹200 Shopping Discount", "cost": 200}
]

for coupon in coupons:

    col1, col2 = st.columns([3,1])

    with col1:
        st.write(f"**{coupon['name']}**")
        st.caption(f"Cost : {coupon['cost']} points")

    with col2:

        if reward_points >= coupon["cost"]:

            if st.button(
                "Claim",
                key=coupon["name"]
            ):
                st.success(
                    f"🎉 {coupon['name']} claimed successfully!"
                )

        else:

            st.button(
                "Locked 🔒",
                disabled=True,
                key=coupon["name"]
            )

st.divider()

# -------------------------
# PROGRESS
# -------------------------

st.subheader("🏆 Reward Progress")

st.progress(
    min(eco_score / 100, 1.0)
)

st.write(
    f"Current EcoScore : **{eco_score}/100**"
)

if eco_score < 100:
    st.info(
        "Recycle more plastic to unlock premium rewards!"
    )
else:
    st.success(
        "🎉 Congratulations! You've reached the maximum EcoScore."
    )