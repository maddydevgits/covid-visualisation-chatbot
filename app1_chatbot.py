import streamlit as st
import pickle

model=pickle.load(open('model.pkl','rb'))
def app():
    st.title('Prediction of Severity Level of Covid')

    col1,col2,col3=st.columns(3)
    f1=col1.checkbox('low-grade fever')
    f2=col2.checkbox('dry cough')
    f3=col3.checkbox('fatigue')
    f4=col1.checkbox('digestive issues')
    f5=col2.checkbox('loss of taste and smell')
    f6=col3.checkbox('itchy')
    f7=col1.checkbox('painful skin patches')
    f8=col2.checkbox('high fever')
    f9=col3.checkbox('deeper cough')
    f10=col1.checkbox('body aches')
    f11=col2.checkbox('breating difficulties')
    f12=col3.checkbox('chest discomfort')
    f13=col1.checkbox('confusion')
    f14=col2.checkbox('unresponsiveness')
    f15=col3.checkbox('bluish lips')

    if st.button('Predict'):
        data=([[f1*1,f2*1,f3*1,f4*1,f5*1,f6*1,f7*1,f8*1,f9*1,f10*1,f11*1,f12*1,f13*1,f14*1,f15*1]])
        out=model.predict(data)[0]
        if out=='mild':
            st.success('Type: '+out+' -> Rest, Fluids, Over-the-Counter Pain and Fever Reducer\n, if you have \
            not recovered in 2 weeks take doctor appointment')
        elif out=='moderate':
            st.warning('Type: '+ out+' -> Rest, Fluids, Over-the-Counter Pain and Fever Reducer\n, if you have \
            not recovered in 2 weeks take doctor appointment')
        elif out=='severe':
            st.error('Type: '+out+' -> May need hospitalization for IV fluids, oxygen, antiviral medication\
            dexamethasone, and help with breating. you would recover in 3 to 6 weeks')
