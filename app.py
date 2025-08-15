import streamlit as st
from datetime import date
from PIL import Image, ImageDraw, ImageFont
import os
import time

st.set_page_config(page_title="Blissful Moments", page_icon="🎉", layout="wide")

# --- Custom Page Background ---
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #ffe6f0, #fff5f9);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Display Logo ---
if os.path.exists("logo.jpg"):
    st.image("logo.jpg", width=150)

st.title("🎉 Blissful Moments - Professional Event Management")

# --- Intro Text ---
st.markdown("""
Welcome to **Blissful Moments**, your one-stop destination for unforgettable celebrations!  
We organize:
- 🎂 Birthday Parties
- 💍 Weddings & Receptions
- 👶 Baby Showers
- 📛 Naming Ceremonies
- 🌸 Puberty Functions
- 🧁 Corporate Events

Let us make your special day **blissfully memorable** ✨
""")

# --- Image Gallery ---
st.header("📸 Event Gallery")

gallery = [
    ("img1.jpg", "Outdoor wedding setup"),
    ("img2.jpg", "Reception hall"),
    ("img3.jpg", "Dining hall"),
    ("img4.jpg", "Birthday celebration"),
    ("img5.jpg", "Party hall"),
    ("img6.jpg", "Function Decor"),
    ("img7.jpg", "Couple photoshoot"),
    ("img8.jpg", "Low-cost setup")
]

for i in range(0, len(gallery), 4):
    cols = st.columns(4)
    for j in range(4):
        if i + j < len(gallery):
            img_path, caption = gallery[i + j]
            if os.path.exists(img_path):
                with cols[j]:
                    st.image(Image.open(img_path), use_container_width=True)
                    st.caption(caption)
            else:
                with cols[j]:
                    st.warning(f"Image not found: {img_path}")

# --- Event Booking Form ---
st.markdown("---")
st.header("📅 Plan Your Event")

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
    if submitted and event_title and location and description:
        # Popup-like toast
        st.toast(f"🎉 {event_type} booked successfully!", icon="🥳")
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

        # --- Celebration Popup Style ---
        st.markdown("---")
        with st.container():
            st.markdown("""
                <div style='background-color:#ffe6f0; padding:20px; border-radius:15px; border:2px solid #ff69b4;'>
                    <h3 style='text-align:center;'>🎉 Congratulations! 🎉</h3>
                    <p style='text-align:center;'>Here's your custom event summary image:</p>
                </div>
            """, unsafe_allow_html=True)
            st.image(img_path, caption="🖼️ Your Event Summary")

        # --- Download Button ---
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
st.header("📣 About Us")
st.markdown("""
Blissful Moments is a team of passionate event planners turning dreams into reality.  
From small celebrations to big days, we handle everything — decor, food, music, and memories.

✨ **Your joy is our passion.**
""")

# --- Social Media Links ---
st.markdown("---")
st.header("🔗 Connect With Us")
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
