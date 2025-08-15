import streamlit as st
from datetime import date
from PIL import Image, ImageDraw, ImageFont
import os
import time
from pathlib import Path

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

# Updated gallery list
gallery = [
    ("img1.jpg", "Outdoor wedding setup"),
    ("img1.jpeg", "Reception hall"),  # Your uploaded image
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
