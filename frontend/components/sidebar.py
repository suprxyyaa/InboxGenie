import streamlit as st

def show():
    st.sidebar.title("InboxGenie")
    page = st.sidebar.radio("Navigate", ["Dashboard", "Emails", "Settings"])
    return page
