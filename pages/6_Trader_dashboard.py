import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Trader Dashboard",
    page_icon="🏭",
    layout="wide"
)

# --------------------------------------------------
# LOGIN CHECK
# --------------------------------------------------

if "trader_logged_in" not in st.session_state:
    st.session_state.trader_logged_in = False

if not st.session_state.trader_logged_in:
    st.warning("⚠️ Please login as Trader.")
    st.stop()

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🏭 Trader Dashboard")
st.write("Manage pickup requests and recycling tasks.")
st.divider()

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

waste_file = "data/waste_uploads.csv"

if not os.path.exists(waste_file):
    st.info("No waste requests available.")
    st.stop()

df = pd.read_csv(waste_file)

# Convert numeric columns
if "AI Score" in df.columns:
    df["AI Score"] = pd.to_numeric(df["AI Score"], errors="coerce")

if "EstimatedWeight" in df.columns:
    df["EstimatedWeight"] = pd.to_numeric(df["EstimatedWeight"], errors="coerce")

# --------------------------------------------------
# SORT BY AI SCORE
# --------------------------------------------------

df = df.sort_values(by="AI Score", ascending=False)

# --------------------------------------------------
# DASHBOARD METRICS
# --------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("📦 Total Requests", len(df))

with c2:
    st.metric("⏳ Pending", len(df[df["Status"] == "Pending"]))

with c3:
    st.metric("🚛 Collected", len(df[df["Status"] == "Collected"]))

with c4:
    st.metric("♻️ High Quality", len(df[df["AI Score"].fillna(0) >= 80]))

st.divider()

# --------------------------------------------------
# REQUESTS
# --------------------------------------------------

for index, row in df.iterrows():
    with st.container():
        left, right = st.columns([1, 2])

        with left:
            if os.path.exists(row["Image"]):
                st.image(row["Image"], use_container_width=True)

        with right:
            st.subheader(row["WasteID"])
            st.write(f"👤 **User:** {row['UserName']}")
            st.write(f"📍 **City:** {row['City']}")
            st.write(f"🏠 **Address:** {row['Address']}")
            st.write(f"⚖️ **Weight:** {row['EstimatedWeight']} kg")
            st.write(f"♻️ **Plastic:** {row['PlasticType']}")

            score = pd.to_numeric(row["AI Score"], errors="coerce")
            if pd.isna(score):
                score = 0

            st.write(f"⭐ **AI Score:** {int(score)}/100")
            st.progress(score / 100)
            st.write(f"📦 **Status:** {row['Status']}")

            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"✅ Accept {row['WasteID']}"):
                    df.loc[index, "Status"] = "Accepted"
                    df.to_csv(waste_file, index=False)
                    st.success("Pickup Accepted")
                    st.rerun()

            with col2:
                if st.button(f"🚛 Collected {row['WasteID']}"):
                    df.loc[index, "Status"] = "Collected"
                    df.to_csv(waste_file, index=False)
                    st.success("Marked as Collected")
                    st.rerun()

            with st.expander("🤖 AI Details"):
                st.write(f"Cleanliness: {row['Cleanliness']}")
                st.write(f"Recyclable: {row['Recyclable']}")
                st.write(f"Reuse: {row['Reuse']}")
                st.write(f"Impact: {row['Environmental Impact']}")

        st.divider()
