import app1_chatbot
import app2_vaccines
import app3_current
import app4
import streamlit as st

PAGES={
    'Self-Checker': app1_chatbot,
    'Vaccination' : app2_vaccines,
    'Indiawide'   : app3_current,
    'Worldwide'   : app4,
}

st.sidebar.title('Dashboard')
selection=st.sidebar.radio('Go to',list(PAGES.keys()))
page=PAGES[selection]
page.app()