import streamlit as st

st.set_page_config(
    page_title="GreenTick",
    page_icon="♻️",
    layout="wide"
)

# ==========================
# CUSTOM CSS
# ==========================

st.markdown("""
<style>

html, body, [class*="css"]{
    font-family:Arial,sans-serif;
}

.main{
    background:#F4FFF5;
}

/* Hero */

.hero{
    background:linear-gradient(135deg,#2E7D32,#4CAF50);
    padding:50px;
    border-radius:20px;
    text-align:center;
    color:white;
    box-shadow:0 8px 20px rgba(0,0,0,0.15);
}

.hero h1{
    color:white !important;
    font-size:50px;
}

.hero h3{
    color:white !important;
}

.hero p{
    color:white !important;
    font-size:18px;
}

/* Cards */

.card{
    background:white;
    border-radius:18px;
    padding:25px;
    text-align:center;
    box-shadow:0 5px 15px rgba(0,0,0,.08);
    transition:.3s;
    height:240px;
}

.card:hover{
    transform:translateY(-6px);
    box-shadow:0 12px 25px rgba(0,0,0,.15);
}

.card h2{
    color:#2E7D32 !important;
}

.card p{
    color:#444 !important;
}

/* Steps */

.step{
    background:#E8F5E9;
    border-radius:15px;
    padding:20px;
    text-align:center;
}

.step h1{
    color:#2E7D32 !important;
}

.step h4{
    color:#222 !important;
}

/* Footer */

.footer{
    text-align:center;
    color:gray;
    padding:30px;
}

</style>
""",unsafe_allow_html=True)

# ==========================
# HERO
# ==========================

st.markdown("""
<div class="hero">

<h1>♻️ GreenTick</h1>

<h3>AI Powered Plastic Waste Management Platform</h3>

<p>
Upload Plastic Waste • AI Analysis • Smart Pickup • Rewards • Sustainable Future
</p>

</div>
""",unsafe_allow_html=True)

st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("👤 Register", use_container_width=True):
        st.switch_page("pages/2_User_register.py")

with col2:
    if st.button("🔐 User Login", use_container_width=True):
        st.switch_page("pages/1_User_login.py")

with col3:
    if st.button("🏭 Trader Login", use_container_width=True):
        st.switch_page("pages/5_Trader_login.py")

st.write("")
st.write("")

# ==========================
# HOW IT WORKS
# ==========================

st.header("♻️ How GreenTick Works")

c1,c2,c3,c4,c5,c6=st.columns(6)

steps=[
("📸","Upload"),
("🤖","AI Detects"),
("⭐","Quality"),
("🚛","Pickup"),
("🏭","Recycle"),
("🎁","Rewards")
]

for col,(icon,title) in zip([c1,c2,c3,c4,c5,c6],steps):

    with col:

        st.markdown(f"""
        <div class="step">
        <h1>{icon}</h1>
        <h4>{title}</h4>
        </div>
        """,unsafe_allow_html=True)

st.write("")
st.divider()

# ==========================
# SMART FEATURES
# ==========================

st.header("✨ Smart AI Features")

col1, col2, col3 = st.columns(3)

features = [
    ("🤖 AI Waste Detection",
     "Automatically detects plastic waste from uploaded images using Artificial Intelligence."),

    ("⭐ AI Quality Score",
     "Analyzes cleanliness and recycling quality to help traders make better decisions."),

    ("🚛 Smart Pickup",
     "Optimizes pickup routes to reduce fuel consumption and collection time."),

    ("🛡️ Fraud Detection",
     "Prevents duplicate image uploads and reward abuse using image fingerprinting."),

    ("♻️ Reuse Suggestions",
     "Suggests creative ways to reuse plastic before recycling it."),

    ("🌱 EcoScore",
     "Rewards users with EcoPoints for contributing to a cleaner environment.")
]

cards = [col1, col2, col3]

for i, (title, desc) in enumerate(features):

    with cards[i % 3]:

        st.markdown(f"""
        <div class="card">

        <h2>{title}</h2>

        <br>

        <p>{desc}</p>

        </div>
        """, unsafe_allow_html=True)

        st.write("")

st.divider()

# ==========================
# LIVE IMPACT
# ==========================

st.header("📊 Live Platform Impact")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("👥 Users", "1,258", "+18 Today")

with m2:
    st.metric("♻️ Plastic Collected", "4.8 Tons", "+320 kg")

with m3:
    st.metric("🌍 CO₂ Saved", "2.1 Tons", "+140 kg")

with m4:
    st.metric("🎁 Rewards Distributed", "₹85,000", "+₹2,400")

st.divider()

# ==========================
# WHY GREENTICK?
# ==========================

st.header("💚 Why GreenTick?")

left, right = st.columns([2, 1])

with left:

    st.success("✅ AI-powered waste classification")

    st.success("✅ Quality analysis before pickup")

    st.success("✅ Smart trader connectivity")

    st.success("✅ EcoScore & reward system")

    st.success("✅ Fraud detection using image hashing")

    st.success("✅ Sustainable recycling workflow")

with right:

    st.info("🌱 Every uploaded bottle contributes towards a cleaner and greener future.")

st.divider()

# ==========================
# CALL TO ACTION
# ==========================

st.header("🚀 Join the Green Revolution")

st.markdown("""
<div style="
background:linear-gradient(135deg,#2E7D32,#66BB6A);
padding:35px;
border-radius:20px;
text-align:center;
color:white;
">

<h2 style="color:white;">🌍 Every Plastic Bottle Matters</h2>

<p style="font-size:18px;color:white;">
Upload your plastic waste, let AI analyze it, connect with nearby recyclers,
earn rewards, and help build a cleaner planet.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

c1, c2 = st.columns(2)

with c1:
    st.success("👤 Register as a User")
    st.write("""
- Upload plastic waste
- Track pickup status
- Earn EcoScore
- Get rewards
""")

with c2:
    st.info("🏭 Login as a Trader")
    st.write("""
- Receive pickup requests
- View AI analysis
- Accept collections
- Increase recycling efficiency
""")

st.divider()

# ==========================
# FUTURE ROADMAP
# ==========================

st.header("🛣️ Future Roadmap")

road1, road2, road3 = st.columns(3)

with road1:
    st.markdown("""
### 📍 Phase 1
- ✅ AI Waste Detection
- ✅ Trader Dashboard
- ✅ EcoScore
- ✅ Rewards
""")

with road2:
    st.markdown("""
### 🚀 Phase 2
- 🔄 Live GPS Tracking
- 💳 UPI Reward Redemption
- 📱 Mobile App
- 📊 Analytics Dashboard
""")

with road3:
    st.markdown("""
### 🌎 Phase 3
- 🏙️ Smart City Integration
- 🤝 NGO Partnerships
- 🏭 Recycling Plant Network
- 🌍 Carbon Credit System
""")

st.divider()



st.divider()

# ==========================
# FOOTER
# ==========================

st.markdown("""
<div style="text-align:center;color:gray;padding:20px;">

<h3>♻️ GreenTick</h3>

<p>AI-Powered Plastic Waste Management Platform</p>

<p>Made with ❤️ for a Cleaner, Greener and Smarter Future 🌱</p>

</div>
""", unsafe_allow_html=True)