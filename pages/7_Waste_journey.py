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

else:

    waste_ids = waste["WasteID"].tolist()

    selected = st.selectbox(
        "Select Waste ID",
        waste_ids
    )

    record = waste[
        waste["WasteID"] == selected
    ].iloc[0]

    st.divider()

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

    st.subheader("🚀 Journey Timeline")

    status = record["Status"]

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

    if os.path.exists(record["Image"]):

        st.subheader("📷 Uploaded Image")

        st.image(
            record["Image"],
            use_container_width=True
        )