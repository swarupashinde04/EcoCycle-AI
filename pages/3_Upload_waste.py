import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime

from utils.gemini_ai import analyze_waste
from utils.fraud_detection import get_image_hash

st.set_page_config(
    page_title="Upload Waste",
    page_icon="♻️",
    layout="wide"
)

# --------------------------------------------------
# LOGIN CHECK
# --------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("⚠️ Please login first.")
    st.stop()

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("♻️ Upload Plastic Waste")

st.write(
    f"Welcome **{st.session_state.user_name}** "
)

st.divider()

# --------------------------------------------------
# CREATE FOLDERS
# --------------------------------------------------

os.makedirs("data", exist_ok=True)
os.makedirs("uploads", exist_ok=True)

# --------------------------------------------------
# CSV FILE
# --------------------------------------------------

waste_file = "data/waste_uploads.csv"

columns = [

    "WasteID",

    "UserName",

    "UserEmail",

    "PlasticType",

    "EstimatedWeight",

    "City",

    "Address",

    "Image",

    "ImageHash",

    "AI Score",

    "Grade",

    "Recyclable",

    "Cleanliness",

    "Reuse",

    "Environmental Impact",

    "Status",

    "Date"

]

if os.path.exists(waste_file):

    waste = pd.read_csv(waste_file)

    # Future compatibility
    for col in columns:

        if col not in waste.columns:

            waste[col] = ""

else:

    waste = pd.DataFrame(columns=columns)

# --------------------------------------------------
# GENERATE WASTE ID
# --------------------------------------------------

def generate_waste_id():

    if waste.empty:
        return "WST001"

    last = waste.iloc[-1]["WasteID"]

    number = int(last.replace("WST","")) + 1

    return f"WST{number:03d}"

# --------------------------------------------------
# FORM
# --------------------------------------------------

with st.form("upload_form"):

    st.subheader("📦 Waste Details")

    user = st.session_state.user_name
    user_email = st.session_state.user_email  
    weight = st.number_input(

        "Estimated Weight (kg)",

        min_value=0.1,

        value=1.0,

        step=0.1

    )

    city = st.text_input("City")

    address = st.text_area("Pickup Address")

    image = st.file_uploader(

        "Upload Plastic Waste Image",

        type=["jpg","jpeg","png"]

    )

    submit = st.form_submit_button(

        "🚀 Analyze & Upload"

    )
# --------------------------------------------------
# PROCESS
# --------------------------------------------------

if submit:

    # ---------- Validation ----------

    if city.strip() == "" or address.strip() == "" or image is None:

        st.error("⚠️ Please fill all fields and upload an image.")
        st.stop()

    # ---------- Save Image ----------

    image_name = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{image.name}"

    image_path = os.path.join(
        "uploads",
        image_name
    )

    with open(image_path, "wb") as f:
        f.write(image.getbuffer())

    # ---------- Image Hash ----------

    image_hash = get_image_hash(image_path)

    # ---------- Duplicate Detection ----------

    if (
        not waste.empty
        and "ImageHash" in waste.columns
        and image_hash in waste["ImageHash"].astype(str).values
    ):

        st.error("⚠️ Duplicate Image Detected!")
        st.warning("This image has already been uploaded.")

        os.remove(image_path)

        st.stop()

    # ---------- AI Analysis ----------

    with st.spinner("🤖 AI is analyzing your waste..."):

        try:

            response = analyze_waste(image_path)

            result = json.loads(response)

        except Exception as e:

            st.warning("⚠️ Gemini unavailable. Using Demo AI.")

            result = {

                "plastic_type": "PET Bottle",

                "recyclable": "Yes",

                "quality_score": 84,

                "cleanliness": "Medium",

                "reuse_suggestion": "Reuse as a plant pot or storage bottle.",

                "environmental_impact":
                "Recycling this plastic helps reduce landfill waste."

            }

    # ---------- Extract Values ----------

    plastic = result.get("plastic_type", "Unknown")

    recyclable = result.get("recyclable", "Unknown")

    score = int(result.get("quality_score", 50))

    cleanliness = result.get("cleanliness", "Medium")

    reuse = result.get(
        "reuse_suggestion",
        "Reuse whenever possible."
    )

    impact = result.get(
        "environmental_impact",
        "Proper recycling protects the environment."
    )

    # ---------- Grade ----------

    if score >= 90:
        grade = "Excellent"

    elif score >= 75:
        grade = "Good"

    elif score >= 60:
        grade = "Average"

    else:
        grade = "Poor"

    # ---------- Save Data ----------

    new_row = {

        "WasteID": generate_waste_id(),

        "UserName": user,

        "UserEmail": user_email,

        "PlasticType": plastic,

        "EstimatedWeight": weight,

        "City": city,

        "Address": address,

        "Image": image_path,

        "ImageHash": image_hash,

        "AI Score": score,

        "Grade": grade,

        "Recyclable": recyclable,

        "Cleanliness": cleanliness,

        "Reuse": reuse,

        "Environmental Impact": impact,

        "Status": "Pending",

        "Date": datetime.now().strftime("%d-%m-%Y %H:%M")

    }

    waste = pd.concat(
        [waste, pd.DataFrame([new_row])],
        ignore_index=True
    )

    waste.to_csv(
        waste_file,
        index=False
    )
    st.session_state["current_waste_id"] = new_row["WasteID"]
    # --------------------------------------------------
    # SUCCESS MESSAGE
    # --------------------------------------------------

    st.success("✅ Waste Uploaded Successfully!")

    st.balloons()

    st.divider()

    # --------------------------------------------------
    # IMAGE PREVIEW
    # --------------------------------------------------

    st.image(
        image,
        caption="Uploaded Plastic Waste",
        use_container_width=True
    )

    st.divider()

    # --------------------------------------------------
    # AI ANALYSIS
    # --------------------------------------------------

    st.subheader("🤖 AI Waste Analysis")

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "♻️ Plastic Type",
            plastic
        )

        st.metric(
            "⭐ Quality Score",
            f"{score}/100"
        )

        st.metric(
            "🧼 Cleanliness",
            cleanliness
        )

    with c2:

        st.metric(
            "♻️ Recyclable",
            recyclable
        )

        st.metric(
            "🏅 Grade",
            grade
        )

        st.metric(
            "📍 Pickup Status",
            "Pending"
        )

    st.divider()

    # --------------------------------------------------
    # REUSE SUGGESTION
    # --------------------------------------------------

    st.subheader("💡 AI Reuse Suggestion")

    st.info(reuse)

    # --------------------------------------------------
    # ENVIRONMENTAL IMPACT
    # --------------------------------------------------

    st.subheader("🌍 Environmental Impact")

    st.success(impact)

    # --------------------------------------------------
    # UPLOAD SUMMARY
    # --------------------------------------------------

    st.divider()

    st.subheader("📄 Upload Summary")

    summary = pd.DataFrame({

        "Field": [

            "Waste ID",

            "User",

            "Weight",

            "City",

            "Status",

            "Upload Time"

        ],

        "Value": [

            generate_waste_id(),

            user,

            f"{weight} kg",

            city,

            "Pending Pickup",

            datetime.now().strftime("%d-%m-%Y %H:%M")

        ]

    })

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # NEXT STEPS
    # --------------------------------------------------

    st.divider()

    st.subheader("📦 What Happens Next?")

    st.markdown("""
✅ Your waste request has been sent to the nearest recycling partner.

🚛 Pickup will be scheduled within **24 hours**.

♻️ After successful collection, your **EcoScore** will increase.

🎁 Reward points will be credited to your account.

🌍 You can track the complete recycling journey from the **Waste Journey Tracker**.
    """)

    st.success("🎉 Thank you for making our planet greener!")