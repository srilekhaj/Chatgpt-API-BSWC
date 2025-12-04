from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai 

genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel("gemini-2.5-flash")

chat = model.start_chat(history=[])

def get_model_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialization
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

st.set_page_config(page_title="llm app")
st.header("Gemini application with chat history")

input = st.text_input("Input", key=input)
submit = st.button("Submit")

if submit and input:
    response = get_model_response(input)
    st.session_state['chat_history'].append(( "You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("The Chat history is ")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
#stream=True means
#  without populating  entire response
# llm text data it is going to display it frontend stream
# without waiting for full data to get from llm
    
