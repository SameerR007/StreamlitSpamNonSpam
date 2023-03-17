import streamlit as st
import pickle
cv=pickle.load(open("cv.pkl","rb"))
model=pickle.load(open("model.pkl","rb"))
st.title("Spam-NonSpam Detector")
Input=st.text_input("Input","Write here...")
if st.button("Check"):
    InputDataFeatures=cv.transform([Input])
    prediction=model.predict(InputDataFeatures)
    if prediction==0:
        st.text("Spam")
    else:
        st.text("Ham")

