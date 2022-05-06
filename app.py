import app1_chatbot

import streamlit as st

PAGES={
    'Self-Checker': app1_chatbot,
}

st.sidebar.title('Dashboard')
selection=st.sidebar.radio('Go to',list(PAGES.keys()))
page=PAGES[selection]
page.app()