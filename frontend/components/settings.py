import streamlit as st

def show():
    st.title("⚙️ Settings")
    st.text_input("API Key", type="password")
    st.text_input("Gmail OAuth Token", type="password")
    st.button("Save")
