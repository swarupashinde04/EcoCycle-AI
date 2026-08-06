import streamlit as st
import pandas as pd
from PIL import Image
import os

st.set_page_config(
    page_title="My Uploads",
    page_icon="📂",
    layout="wide"
)

st.title("📂 My Uploads")

# -------------------------
# LOGIN CHECK
# -------------------------

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("⚠️ Please login first.")
    st.stop()

user_email = st.session_state.user_email

# -------------------------
# LOAD CSV
# -------------------------

waste_file = "data/waste_uploads.csv"

if not os.path.exists(waste_file):
    st.info("No uploads yet.")
    st.stop()

waste = pd.read_csv(waste_file)

if waste.empty:
    st.info("No uploads yet.")
    st.stop()

# -------------------------
# FIX COLUMN NAMES
# -------------------------

waste.columns = waste.columns.str.strip()

if "UserEmail" not in waste.columns:
    st.error("UserEmail column not found in waste_uploads.csv")
    st.stop()

# -------------------------
# FILTER CURRENT USER
# -------------------------

my_uploads = waste[
    waste["UserEmail"].astype(str).str.strip().str.lower()
    ==
    user_email.strip().lower()
]

if my_uploads.empty:
    st.info("You haven't uploaded any waste yet.")
    st.stop()

# -------------------------
# SHOW LATEST UPLOAD
# -------------------------

latest = my_uploads.iloc[-1]

st.success("✅ Latest Upload")

if os.path.exists(latest["Image"]):
    st.image(
        latest["Image"],
        caption="Uploaded Waste",
        use_container_width=True
    )

st.divider()

st.subheader("🤖 AI Analysis")

c1, c2 = st.columns(2)

with c1:

    st.metric(
        "♻ Plastic Type",
        latest["PlasticType"]
    )

    st.metric(
        "⭐ AI Score",
        latest["AI Score"]
    )

    st.metric(
        "🧼 Cleanliness",
        latest["Cleanliness"]
    )

with c2:

    st.metric(
        "♻ Recyclable",
        latest["Recyclable"]
    )

    st.metric(
        "🏅 Grade",
        latest["Grade"]
    )

    st.metric(
        "📍 Pickup Status",
        latest["Status"]
    )

st.divider()

st.subheader("💡 Reuse Suggestion")
st.info(latest["Reuse"])

st.subheader("🌍 Environmental Impact")
st.success(latest["Environmental Impact"])

st.divider()

st.subheader("📄 Upload Summary")

summary = pd.DataFrame({

    "Field":[
        "Waste ID",
        "Weight",
        "City",
        "Address",
        "Status",
        "Upload Time"
    ],

    "Value":[
        latest["WasteID"],
        f'{latest["EstimatedWeight"]} kg',
        latest["City"],
        latest["Address"],
        latest["Status"],
        latest["Date"]
    ]

})

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.subheader("📜 Upload History")

history = my_uploads[[
    "WasteID",
    "PlasticType",
    "EstimatedWeight",
    "AI Score",
    "Status",
    "Date"
]]

st.dataframe(
    history.iloc[::-1],
    use_container_width=True,
    hide_index=True
)