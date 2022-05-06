import streamlit as st
import requests
import json

states=['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala***','Ladakh','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']

def app():
    st.title('Current Statistics of India {Covid-19}')
    option=st.selectbox('Select the State', states)
    if st.button('Get Data'):
        response=requests.get('https://disease.sh/v3/covid-19/gov/India/')
        data=json.loads(response.text)
        st.title('Overall India')
        st.write(data['total'])
        st.title(option)
        index=states.index(option)
        st.write(data['states'][index])


