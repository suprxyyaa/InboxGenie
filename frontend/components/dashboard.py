import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

def show():
    st.title("📊 Dashboard")
    st.write("Quick stats and summary here.")

    if st.button("Check Backend Health"):
        try:
            resp = requests.get(f"{BACKEND_URL}/")
            st.json(resp.json())
        except Exception as e:
            st.error(f"Error connecting to backend: {e}")
