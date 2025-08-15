import streamlit as st
from datetime import date
from PIL import Image, ImageDraw, ImageFont
import time
import tempfile
import requests
from io import BytesIO

st.set_page_config(page_title="Blissful Moments", page_icon="✨", layout="wide")

# --- Custom Page Background ---
st.markdown("""
<style>
.stApp {
    background-image: url("https://i.imgur.com/LqR4t5A.jpg");
    background-size: cover;
    background-attachment: fixed;
    background-repeat: no-repeat;
    background-position: center;
}
.stMarkdown, .stTextInput > div > input, .stSelectbox, .stTextArea, .stNumberInput > div > input {
    background-color: rgba(255, 255, 255, 0.85) !important;
    border-radius: 10px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# --- Logo ---
logo_url = "https://i.imgur.com/1XZGZ9A.png"  # Replace with your actual logo URL
st.image(logo_url, width=150)

st.title("✨ Blissful Moments - Professional Event Management")

# --- Intro Text ---
st.markdown("""
Welcome to **Blissful Moments**, your one-stop destination for unforgettable celebrations!  
We organize:
- 🎂 Birthday Parties  
- 💍 Weddings & Receptions  
- 👶 Baby Showers  
- 🍼 Naming Ceremonies  
- 🌸 Puberty Functions  
- 🏢 Corporate Events

Let us make your special day **blissfully memorable** 💖
""")

# --- Image Gallery ---
st.header("📸 Event Gallery")

gallery = [
    ("https://i.imgur.com/sV0SBRp.jpg", "Outdoor wedding setup"),
    ("https://i.imgur.com/L6e3LFn.jpg", "Reception hall"),
    ("https://i.imgur.com/9RyzNRx.jpg", "Dining hall"),
    ("https://i.imgur.com/sNLhEVW.jpg", "Birthday celebration"),
    ("https://i.imgur.com/M3GFSTl.jpg", "Party hall"),
    ("https://i.imgur.com/kJrOzEJ.jpg", "Function Decor"),
    ("https://i.imgur.com/TdbG3Vr.jpg", "Couple photoshoot"),
    ("https://i.imgur.com/eAokE2L.jpg", "Low-cost setup")
]

for i in range(0, len(gallery), 4):
    cols = st.columns(4)
    for j in range(4):
        if i + j < len(gallery):
            url, caption = gallery[i + j]
            try:
                response = requests.get(url)
                img = Image.open(BytesIO(response.content))
                with cols[j]:
                    st.image(img, use_container_width=True)
                    st.caption(caption)
            except:
                with cols[j]:
                    st.warning(f"Could not load image: {caption}")

# --- Booking Form ---
st.markdown("---")
st.header("📝 Plan Your Event")

with st.form("event_form"):
    col1, col2 = st.columns(2)
    with col1:
        event_type = st.selectbox("Event Type", [
            "Birthday", "Marriage", "Reception", "Baby Shower",
            "Naming Ceremony", "Puberty Function", "Other"])
        event_title = st.text_input("Event Title")
        event_date = st.date_input("Event Date", min_value=date.today())
    with col2:
        guest_count = st.number_input("Expected Guests", min_value=10, max_value=1000, step=10)
        location = st.text_input("Event Location")
        description = st.text_area("Event Description")

    submitted = st.form_submit_button("Submit")
    if submitted and all([event_title.strip(), location.strip(), description.strip()]):
        st.toast(f"🎉 {event_type} booked successfully!", icon="🎊")
        time.sleep(0.8)
        st.balloons()

        st.success(f"✅ Your {event_type} has been planned successfully! Here's your celebration summary.")

        # Create confirmation image
        img = Image.new('RGB', (700, 450), color=(255, 245, 250))
        draw = ImageDraw.Draw(img)

        try:
            font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
            font_body = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
        except:
            font_title = ImageFont.load_default()
            font_body = ImageFont.load_default()

        draw.rectangle([10, 10, 690, 440], outline=(200, 100, 150), width=4)
        draw.text((30, 30), "🎊 Event Summary 🎊", font=font_title, fill=(120, 0, 90))

        details = [
            f"Event Type: {event_type}",
            f"Title: {event_title}",
            f"Date: {event_date.strftime('%Y-%m-%d')}",
            f"Guests: {int(guest_count)}",
            f"Location: {location}",
            f"Description: {description[:80]}..."
        ]

        y = 80
        for line in details:
            draw.text((40, y), line, font=font_body, fill=(0, 0, 0))
            y += 40

        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
            img.save(tmp.name)
            st.markdown("---")
            st.markdown("""
                <div style='background-color:#ffe6f0; padding:20px; border-radius:15px; border:2px solid #ff69b4;'>
                    <h3 style='text-align:center;'>🎉 Congratulations! 🎉</h3>
                    <p style='text-align:center;'>Here's your custom event summary image:</p>
                </div>
            """, unsafe_allow_html=True)
            st.image(tmp.name, caption="🎊 Your Event Summary")
            with open(tmp.name, "rb") as file:
                st.download_button(
                    label="📥 Download Event Summary",
                    data=file,
                    file_name="Event_Summary.png",
                    mime="image/png"
                )
    elif submitted:
        st.error("Please fill in all fields.")

# --- About Us ---
st.markdown("---")
st.header("🌟 About Us")
st.markdown("""
Blissful Moments is a team of passionate event planners turning dreams into reality.  
From small celebrations to big days, we handle everything — decor, food, music, and memories.

💖 **Your joy is our passion.**
""")

# --- Social Media Links ---
st.markdown("---")
st.header("📱 Connect With Us")
st.markdown("""
- 🌐 [Facebook](https://facebook.com)  
- 📸 [Instagram](https://instagram.com)  
- 🐦 [Twitter](https://twitter.com)  
- 💼 [LinkedIn](https://linkedin.com)
""")

# --- Footer ---
st.markdown(
    "<div style='text-align:center; color:#aaa;'>© 2025 Blissful Moments. All Rights Reserved.</div>",
    unsafe_allow_html=True
)
