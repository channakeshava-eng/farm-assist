import streamlit as st
from PIL import Image
import requests, numpy as np, tempfile
from gtts import gTTS

# ---------------- CAMERA ----------------
try:
    from streamlit_camera_input import camera_input
    CAMERA = True
except:
    CAMERA = False

st.set_page_config(page_title="Farm Assist", layout="centered")

# ---------------- BACK BUTTON STYLE ----------------
st.markdown("""
<style>
.back-btn {
position: fixed;
bottom: 20px;
left: 20px;
z-index: 9999;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "page" not in st.session_state:
    st.session_state.page = 1

# ---------------- WEATHER ----------------
API_KEY = "509887fc92045e1768a7d412cd7c9d1c"

CITIES = [
    "Delhi","Mumbai","Chennai","Kolkata","Hyderabad","Bengaluru","Pune","Nagpur",
    "Warangal","Vijayawada","Guntur","Vizag","Tirupati","Madurai","Coimbatore",
    "Mysuru","Hubli","Belagavi","Nashik","Indore","Bhopal","Jaipur","Udaipur",
    "Jodhpur","Aurangabad","Amravati","Kolhapur","Solapur","Nellore","Kurnool"
]

# ---------------- DISEASES ----------------
DISEASES = {
    "Healthy":"✅","Leaf Blight":"🍂","Rust":"🔴","Brown Spot":"🟤",
    "Root Rot":"🌱","Stem Rot":"🪵","Powdery Mildew":"⚪",
    "Downy Mildew":"💧","Wilt":"🦠","Leaf Curl":"🍃"
}

# ---------------- SOIL ----------------
SOILS = {
    "Alluvial":"Rice, Wheat – Maintain moisture",
    "Black":"Cotton – Improve drainage",
    "Red":"Millets – Add compost",
    "Laterite":"Tea, Coffee – Control pH",
    "Sandy":"Groundnut – Frequent irrigation",
    "Clay":"Paddy – Drain excess water",
    "Loamy":"Vegetables – Balanced nutrients"
}

# ---------------- LANGUAGES ----------------
LANG = {
    "English":{
        "dashboard":"Dashboard","weather":"Weather","soil":"Soil",
        "pest":"Pest Detection","chat":"Farmer Chat","settings":"Settings",
        "solution":"Apply recommended treatment immediately",
        "rain":"Rain Alert","temp":"Temperature","humidity":"Humidity"
    },
    "Hindi":{
        "dashboard":"डैशबोर्ड","weather":"मौसम","soil":"मिट्टी",
        "pest":"कीट पहचान","chat":"किसान चैट","settings":"सेटिंग्स",
        "solution":"तुरंत उपचार करें",
        "rain":"बारिश चेतावनी","temp":"तापमान","humidity":"नमी"
    },
    "Telugu":{
        "dashboard":"డాష్‌బోర్డ్","weather":"వాతావరణం","soil":"మట్టి",
        "pest":"పురుగు గుర్తింపు","chat":"రైతు చాట్","settings":"సెట్టింగ్స్",
        "solution":"తక్షణమే చికిత్స చేయండి",
        "rain":"వర్ష హెచ్చరిక","temp":"ఉష్ణోగ్రత","humidity":"ఆర్ద్రత"
    }
}

# ---------------- FUNCTIONS ----------------
def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

def speak(text):
    tts = gTTS(text)
    f = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(f.name)
    return f.name

def chat_reply(q):
    return (
        "🌾 Fertilizer: Use NPK (19:19:19) every 20 days\n\n"
        "🐛 Pesticides: Neem oil spray weekly\n\n"
        "🦟 Insecticides: Imidacloprid only for heavy infestation\n\n"
        "🌿 Weeds: Manual weeding or Pendimethalin\n\n"
        "💧 Irrigation: Water every 3–4 days in morning\n\n"
        "⚠️ Follow agriculture officer advice"
    )

# ==================================================
# SCREEN 1 – WELCOME
# ==================================================
if st.session_state.page == 1:
    st.markdown("""
    <style>
    .main {background-color:#1565c0;}
    .center {text-align:center;margin-top:120px;}
    .welcome {color:yellow;font-size:36px;}
    .title {color:#00ff00;font-size:42px;}
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="center">
        <div class="welcome">WELCOME</div>
        <div class="title">Farm Assist 🌿🌱</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🟢 Continue"):
        st.session_state.page = 2
        st.rerun()

# ==================================================
# SCREEN 2 – IMAGE
# ==================================================
elif st.session_state.page == 2:
    st.image("images/crop.jpg", use_column_width=True)
    st.title("Farmers Assist")

    if st.button("Continue ➡"):
        st.session_state.page = 3
        st.rerun()

    st.markdown('<div class="back-btn">', unsafe_allow_html=True)
    if st.button("⬅ Back"):
        st.session_state.page = 1
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# SCREEN 3 – HOME
# ==================================================
elif st.session_state.page == 3:
    st.title("🏠 Home")

    c1, c2 = st.columns(2)
    if c1.button("👨‍🌾 Farmer Profile"):
        st.session_state.page = 4
        st.rerun()
    if c2.button("📊 Dashboard"):
        st.session_state.page = 5
        st.rerun()

    st.image("images/crop.jpg")
    st.image("images/soil.jpg")
    st.image("images/tools.jpg")
    st.image("images/weather.jpg")
    st.image("images/pests.jpg")

    st.markdown('<div class="back-btn">', unsafe_allow_html=True)
    if st.button("⬅ Back"):
        st.session_state.page = 2
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# SCREEN 4 – FARMER PROFILE
# ==================================================
elif st.session_state.page == 4:
    st.title("👨‍🌾 Farmer Profile")
    st.text_input("Farmer Name")
    st.text_input("Village / District")
    st.text_input("Land Size (Acres)")
    st.text_input("Crops Grown")

    st.markdown('<div class="back-btn">', unsafe_allow_html=True)
    if st.button("⬅ Back"):
        st.session_state.page = 3
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# SCREEN 5 – DASHBOARD
# ==================================================
elif st.session_state.page == 5:
    lang = st.selectbox("🌐 Select Language", list(LANG.keys()))
    T = LANG[lang]

    st.title("📊 " + T["dashboard"])

    st.subheader("🌥️ " + T["weather"])
    city = st.selectbox("City", CITIES)
    data = get_weather(city)
    if data:
        st.write(f"{T['temp']}: {data['main']['temp']} °C")
        st.write(f"{T['humidity']}: {data['main']['humidity']} %")

    st.subheader("🪰 " + T["pest"])
    upload = st.file_uploader("Upload Crop Image", ["jpg","png"])
    if upload:
        img = Image.open(upload)
        st.image(img, width=220)
        disease = np.random.choice(list(DISEASES.keys()))
        st.success(DISEASES[disease] + " " + disease)
        st.audio(speak(T["solution"]))

    st.subheader("🌱 " + T["soil"])
    soil = st.selectbox("Soil Type", SOILS.keys())
    st.info(SOILS[soil])

    st.subheader("💬 " + T["chat"])
    q = st.text_input("Ask your farming problem")
    if q:
        st.success(chat_reply(q))

    st.subheader("⚙️ " + T["settings"])

    st.markdown('<div class="back-btn">', unsafe_allow_html=True)
    if st.button("⬅ Back"):
        st.session_state.page = 3
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)