import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Waste Journey",
    page_icon="♻️",
    layout="wide"
)

st.title("♻️ Waste Journey Tracker")
st.write("Track the complete lifecycle of your uploaded plastic waste.")

st.divider()

# -------------------------
# LOGIN CHECK
# -------------------------

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("⚠️ Please login first.")
    st.stop()

user_email = st.session_state.user_email.strip().lower()

# -------------------------
# LOAD DATA
# -------------------------

waste_file = "data/waste_uploads.csv"

if os.path.exists(waste_file):
    waste = pd.read_csv(waste_file)
else:
    waste = pd.DataFrame()

# -------------------------
# NO DATA
# -------------------------

if waste.empty:
    st.info("No waste uploads found.")
    st.stop()

# -------------------------
# CLEAN COLUMNS
# -------------------------

waste.columns = waste.columns.str.strip()

# -------------------------
# CHECK USEREMAIL COLUMN
# -------------------------

if "UserEmail" not in waste.columns:
    st.error("❌ UserEmail column not found in waste_uploads.csv")
    st.info("Please update Upload Waste page to save UserEmail.")
    st.stop()

# -------------------------
# SHOW ONLY CURRENT USER DATA
# -------------------------

waste = waste[
    waste["UserEmail"].astype(str).str.strip().str.lower()
    == user_email
]

if waste.empty:
    st.info("📭 You haven't uploaded any waste yet.")
    st.stop()

# -------------------------
# SELECT WASTE ID
# -------------------------

waste_ids = waste["WasteID"].tolist()

selected = st.selectbox(
    "Select Waste ID",
    waste_ids
)

record = waste[
    waste["WasteID"] == selected
].iloc[0]

st.divider()

# -------------------------
# WASTE DETAILS
# -------------------------

st.subheader("📦 Waste Details")

col1, col2 = st.columns(2)

with col1:

    st.write(f"**Waste ID:** {record['WasteID']}")
    st.write(f"**User:** {record['UserName']}")
    st.write(f"**Plastic Type:** {record['PlasticType']}")
    st.write(f"**Weight:** {record['EstimatedWeight']} kg")

with col2:

    st.write(f"**City:** {record['City']}")
    st.write(f"**Date:** {record['Date']}")
    st.write(f"**Current Status:** {record['Status']}")

st.divider()

# -------------------------
# JOURNEY TIMELINE
# -------------------------

st.subheader("🚀 Journey Timeline")

status = str(record["Status"])

stages = [
    ("📸 Uploaded", True),
    ("🤖 AI Verified", status in ["Accepted", "Completed"]),
    ("🏭 Trader Accepted", status in ["Accepted", "Completed"]),
    ("🚛 Pickup Scheduled", status == "Completed"),
    ("♻️ Recycling Center", status == "Completed"),
    ("🎁 Reward Credited", status == "Completed")
]

for stage, done in stages:

    if done:
        st.success(stage)
    else:
        st.info(stage)

st.divider()

# -------------------------
# IMAGE
# -------------------------

if os.path.exists(record["Image"]):

    st.subheader("📷 Uploaded Image")

    st.image(
        record["Image"],
        use_container_width=True
    )

else:
    st.warning("Uploaded image not found.")