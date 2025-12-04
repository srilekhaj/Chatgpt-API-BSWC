from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
from llama_index.llms.groq import Groq

#DEFINING API KEY
api_key = os.getenv('GROQ_API_KEY')

#CONFIGURE LLM
llm = Groq(model="llama3-70b-8192", api_key=api_key)

def get_response(query):
    response = llm.complete(query)
    return response.text

st.header('LLAMAINDEX USING GROQ')
input = st.text_input('Enter the question')

if input:
        
    response = get_response(input)
    st.write(response)
