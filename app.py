import streamlit as st
from datetime import date
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import time

st.set_page_config(page_title="Blissful Moments", page_icon="🎉", layout="wide")

# --- Custom Page Background ---
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://i.imgur.com/LqR4t5A.jpg"); /* Soft floral background */
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
    """,
    unsafe_allow_html=True
)

# --- Display Logo (Optional) ---
# Uncomment and add your logo path if you have a local logo
# import os
# if os.path.exists("logo.jpg"):
#     st.image("logo.jpg", width=150)

st.title("🎉 Blissful Moments - Professional Event Management")

# --- Intro Text ---
st.markdown("""
Welcome to **Blissful Moments**, your one-stop destination for unforgettable celebrations!  
We organize:
- 🎂 Birthday Parties
- 💍 Weddings & Receptions
- 🤰 Baby Showers
- 🍼 Naming Ceremonies
- 🎉 Puberty Functions
- 🏢 Corporate Events

Let us make your special day **blissfully memorable** ✨
""")

# --- Image Gallery ---
st.header("📸 Event Gallery")

gallery = [
    ("https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=60", "Outdoor wedding setup"),
    ("https://images.unsplash.com/photo-1526779259212-5642cc76e45a?auto=format&fit=crop&w=800&q=60", "Reception hall"),
    ("https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=800&q=60", "Dining hall"),
    ("https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?auto=format&fit=crop&w=800&q=60", "Birthday celebration"),
    ("https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=800&q=60", "Party hall"),
    ("https://images.unsplash.com/photo-1492684223066-81342ee5ff30?auto=format&fit=crop&w=800&q=60", "Function Decor"),
    ("https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?auto=format&fit=crop&w=800&q=60", "Couple photoshoot"),
    ("https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=800&q=60", "Low-cost setup")
]

cols = st.columns(4)
for idx, (url, caption) in enumerate(gallery):
    col = cols[idx % 4]
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        col.image(img, use_container_width=True, caption=caption)
    except Exception:
        col.warning(f"Could not load image: {caption}")

# --- Event Booking Form ---
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
        st.toast(f"🎉 {event_type} booked successfully!", icon="🎈")
        time.sleep(0.8)
        st.balloons()

        st.success(f"🎊 Your {event_type} has been planned successfully! Check below for a celebration summary.")

        # --- Generate Styled Confirmation Image ---
        img = Image.new('RGB', (700, 450), color=(255, 245, 250))
        d = ImageDraw.Draw(img)
        try:
            font_title = ImageFont.truetype("arial.ttf", 24)
            font_body = ImageFont.truetype("arial.ttf", 18)
        except:
            font_title = ImageFont.load_default()
            font_body = ImageFont.load_default()

        d.rectangle([10, 10, 690, 440], outline=(200, 100, 150), width=4)
        d.text((30, 30), "🎉 Event Summary 🎉", font=font_title, fill=(120, 0, 90))

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
            d.text((40, y), line, font=font_body, fill=(0, 0, 0))
            y += 40

        img_path = "confirmation.png"
        img.save(img_path)

        st.markdown("---")
        with st.container():
            st.markdown("""
                <div style='background-color:#ffe6f0; padding:20px; border-radius:15px; border:2px solid #ff69b4;'>
                    <h3 style='text-align:center;'>🎉 Congratulations! 🎉</h3>
                    <p style='text-align:center;'>Here's your custom event summary image:</p>
                </div>
            """, unsafe_allow_html=True)
            st.image(img_path, caption="🎈 Your Event Summary")

        with open(img_path, "rb") as file:
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
st.header("💖 About Us")
st.markdown("""
Blissful Moments is a team of passionate event planners turning dreams into reality.  
From small celebrations to big days, we handle everything — decor, food, music, and memories.

✨ **Your joy is our passion.**
""")

# --- Social Media Links ---
st.markdown("---")
st.header("🌐 Connect With Us")
st.markdown("""
- 📘 [Facebook](https://facebook.com)
- 📸 [Instagram](https://instagram.com)
- 🐦 [Twitter](https://twitter.com)
- 💼 [LinkedIn](https://linkedin.com)
""")

# --- Footer ---
st.markdown(
    "<div style='text-align:center; color:#aaa;'>© 2025 Blissful Moments. All Rights Reserved.</div>",
    unsafe_allow_html=True
)
