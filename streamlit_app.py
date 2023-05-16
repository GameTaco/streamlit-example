from collections import namedtuple
import streamlit as st
import langchain as lc
import os
import openai
from dotenv import load_dotenv

load_dotenv()  
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID=os.getenv("GOOGLE_CSE_ID")

st.download_button('Download file', data)
st.text_input('First name')
st.number_input('Pick a number', 0, 10)
st.text_area('Text to translate')

elements = st.container()
with elements:
    st.write('This is inside the container')
    st.button('Submit Message')


col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")