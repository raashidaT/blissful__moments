import streamlit as st
from datetime import date
from PIL import Image, ImageDraw, ImageFont
import time
import requests
from io import BytesIO

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

st.title("🎉 Blissful Moments - Professional Event Management")

# --- Intro Text ---
st.markdown("""
Welcome to **Blissful Moments**, your one-stop destination for unforgettable celebrations!  
We organize:
- 🎂 Birthday Parties
- 💍 Weddings & Receptions
- 👶 Baby Showers
- 🙏 Naming Ceremonies
- 🌸 Puberty Functions
- 🏢 Corporate Events

Let us make your special day **blissfully memorable** 🎈
""")

# --- Image Gallery ---
st.header("📸 Event Gallery")

gallery = [
    ("https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=60", "Outdoor wedding setup"),
    ("https://images.unsplash.com/photo-1526779259212-5642cc76e45a?auto=format&fit=crop&w=800&q=60", "Reception hall"),
    ("https://images.unsplash.com/photo-1512917774080-9
