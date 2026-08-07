import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 GreenTick Dashboard")
st.write("Overview of the complete recycling ecosystem.")

st.divider()

# -------------------------
# LOAD DATA
# -------------------------

users_file = "data/users.csv"
waste_file = "data/waste_uploads.csv"

if os.path.exists(users_file):
    users = pd.read_csv(users_file)
else:
    users = pd.DataFrame()

if os.path.exists(waste_file):
    waste = pd.read_csv(waste_file)
else:
    waste = pd.DataFrame()

# -------------------------
# METRICS
# -------------------------

total_users = len(users)
total_uploads = len(waste)

pending = 0
accepted = 0
completed = 0
total_weight = 0
avg_score = 0
recyclable = 0

if not waste.empty:
    # Convert numeric columns

    if "EstimatedWeight" in waste.columns:
        waste["EstimatedWeight"] = pd.to_numeric(
          waste["EstimatedWeight"],
          errors="coerce"
        )

    if "AI Score" in waste.columns:
        waste["AI Score"] = pd.to_numeric(
          waste["AI Score"],
          errors="coerce"
        )

    pending = len(
        waste[waste["Status"] == "Pending"]
    )

    accepted = len(
        waste[waste["Status"] == "Accepted"]
    )

    completed = len(
        waste[waste["Status"] == "Completed"]
    )

    total_weight = waste["EstimatedWeight"].fillna(0).sum()


    if "AI Score" in waste.columns:

        avg = waste["AI Score"].dropna().mean()

    if pd.isna(avg):
        avg_score = 0
    else:
        avg_score = round(avg, 1)
    if "Recyclable" in waste.columns:

        recyclable = len(
            waste[
                waste["Recyclable"]=="Yes"
            ]
        )

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric(
        "👤 Registered Users",
        total_users
    )

with c2:
    st.metric(
        "♻ Waste Uploads",
        total_uploads
    )

with c3:
    st.metric(
        "⚖ Plastic (gms)",
        round(total_weight,2)
    )

with c4:
    st.metric(
        "⭐ Avg AI Score",
        avg_score
    )

st.divider()

c5,c6,c7,c8 = st.columns(4)

with c5:
    st.metric(
        "🟡 Pending",
        pending
    )

with c6:
    st.metric(
        "✅ Accepted",
        accepted
    )

with c7:
    st.metric(
        "🏭 Recycled",
        completed
    )

with c8:
    st.metric(
        "♻ Recyclable",
        recyclable
    )

st.divider()

# -------------------------
# COLLECTION PROGRESS
# -------------------------

st.subheader("📦 Collection Progress")

if total_uploads > 0:

    completed_percent = round(
        (completed / total_uploads) * 100,
        1
    )

    accepted_percent = round(
        (accepted / total_uploads) * 100,
        1
    )

    pending_percent = round(
        (pending / total_uploads) * 100,
        1
    )

else:

    completed_percent = 0
    accepted_percent = 0
    pending_percent = 0

st.write(f"🟢 Recycled : {completed_percent}%")
st.progress(completed_percent / 100)

st.write(f"🟡 Accepted : {accepted_percent}%")
st.progress(accepted_percent / 100)

st.write(f"🔴 Pending : {pending_percent}%")
st.progress(pending_percent / 100)

st.divider()

# -------------------------
# PROJECT FEATURES
# -------------------------

st.subheader("🚀 GreenTick AI Features")

f1, f2, f3 = st.columns(3)

with f1:

    st.success("""
🤖 AI Waste Detection

⭐ AI Quality Score

🛡 Fraud Detection
""")

with f2:

    st.success("""
🚛 Route Optimization

📦 Smart Pickup

♻ Waste Tracking
""")

with f3:

    st.success("""
🌍 Environmental Impact

🎁 Reward System

🌱 Sustainable Recycling
""")

st.divider()

# -------------------------
# FOOTER
# -------------------------

st.success(
    "🌍 Every upload helps build a cleaner, smarter and more sustainable future."
)