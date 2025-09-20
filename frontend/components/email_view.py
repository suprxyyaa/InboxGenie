import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

def show():
    st.title("📧 Emails")
    
    if st.button("Fetch Emails"):
        try:
            resp = requests.get(f"{BACKEND_URL}/gmail/")
            data = resp.json()
            for email in data.get("emails", []):
                with st.expander(email["subject"]):
                    st.write(email["snippet"])
        except Exception as e:
            st.error(f"Failed to fetch emails: {e}")
