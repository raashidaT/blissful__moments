import streamlit as st
import os

st.title("Blissful Moments Gallery")

image_folder = "blissful images"   # folder where your images are

# Example for logo
logo_path = os.path.join(image_folder, "logo.jpg")
if os.path.exists(logo_path):
    st.image(logo_path, width=150)

# Event gallery
for filename in os.listdir(image_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        st.image(os.path.join(image_folder, filename), caption=filename)
