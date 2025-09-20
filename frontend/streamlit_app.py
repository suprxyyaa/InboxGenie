import streamlit as st
from components import sidebar, dashboard, email_view, settings

st.set_page_config(page_title="InboxGenie", layout="wide")

# Sidebar navigation
page = sidebar.show()

if page == "Dashboard":
    dashboard.show()
elif page == "Emails":
    email_view.show()
elif page == "Settings":
    settings.show()
