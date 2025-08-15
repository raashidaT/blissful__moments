import streamlit as st
from datetime import date
from PIL import Image, ImageDraw, ImageFont
import time
import tempfile
import requests
from io import BytesIO

st.set_page_config(page_title="Blissful Moments", page_icon="✨", layout="wide")

# --- Custom Page Background ---
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://i.imgur.com/LqR4t5A.jpg");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
    }
    .stMa
