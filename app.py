import streamlit as st

st.set_page_config(page_title="Blissful Moments", page_icon="🎉")

st.title("Blissful Moments — Event Management")
st.write("Hello HOD Mam! This is my Python project running online.")

# Example input and output
event_name = st.text_input("Enter Event Name")
if st.button("Show Event"):
    st.success(f"Event '{event_name or 'Sample Event'}' details loaded successfully, HOD Mam!")
