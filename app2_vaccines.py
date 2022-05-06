import requests
import streamlit as st
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def app():
    st.title('Vaccination Data Visualisation')
    col1,col2=st.columns(2)
    no_of_days=(col1.text_input('Enter the number of days'))
    
    if st.button('Get Data'):
        response=requests.get('https://disease.sh/v3/covid-19/vaccine/coverage/countries/India?lastdays='+no_of_days+'&fullData=false')
        data=(json.loads(response.text))['timeline']
        cols=list(data.keys())
        rows=list(data.values())
        fig=plt.figure(figsize=(10,5))
        plt.plot(cols,rows,color='red',marker='o')
        plt.xlabel("Dates")
        plt.ylabel('No of Vaccines')
        plt.title('Vaccination Dosed in India')
        st.pyplot(fig)
        