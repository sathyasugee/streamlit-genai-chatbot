from http.client import responses

from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq


#load the environment variable
load_dotenv(".env")

#streamlit page setup
st.set_page_config(
    page_title="Generative AI Chatbot",
    page_icon="🧑🏻",
    layout="centered"
)
st.title ("💬Generative AI Chatbot")

#initiate chat history
#streamlit everytime reruns the top-to-bottom. cause: it loses the memory immediately.
#so to overcome this, the session_state comes: it persist the memory so the llm come to know what the user talking about.
if "chat_history" not in st.session_state:
    st.session_state.chat_history= []

#show chat history

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


#llm initiate

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temperature=0
)

#input box
user_prompt = st.chat_input("Ask Chatbot")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user","content":user_prompt})

    response= llm.invoke(
        input = [{"role":"system", "content": "you are a helpful assistant"},*st.session_state.chat_history]
    )

    assistant_response = response.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response })

    with st.chat_message("assistant"):
        st.markdown(assistant_response)



