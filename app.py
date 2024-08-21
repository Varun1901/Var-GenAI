import streamlit as st 
import google.generativeai as genai
st.title( "Welcome to VARUN-GenAI")
genai.configure(api_key="AIzaSyC-24pSEnb5JyYJe-_xQ4_vj4LHQNijH-g")
text = st.text_input("Enter your prompt!!!")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
if st.button("Click me"):
    response = chat.send_message(text) 
    st.write(response.text)