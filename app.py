import app1_chatbot
import app2_vaccines
import streamlit as st

PAGES={
    'Self-Checker': app1_chatbot,
    'Vaccination' : app2_vaccines,
}

st.sidebar.title('Dashboard')
selection=st.sidebar.radio('Go to',list(PAGES.keys()))
page=PAGES[selection]
page.app()