from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite"
) 

st.title("Q&A Bot")
st.markdown("Ask me anything! Type 'exit', 'quit', or 'bye' to end the chat.")

if "messages" not in st.session_state:
   st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)


query = st.chat_input("Ask your question here...")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    response_text = res.content[0]["text"]

    st.session_state.messages.append({
    "role": "assistant",
    "content": response_text
})
    st.chat_message("assistant").markdown(response_text)
