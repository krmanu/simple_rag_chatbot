import os
import streamlit as st
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"

from services.ingest import ingest_docs
from services.rag_pipeline import rag_chat

st.set_page_config(page_title="Simple RAG App")
st.title("📚 Simple RAG Chatbot")

@st.cache_resource
def initialize_rag():

    total_chunks = ingest_docs()
    return total_chunks

total_chunks = initialize_rag()

user_input = st.text_input("Ask your question")

if st.button("Ask"):

    if user_input:

        with st.spinner("Thinking..."):

            answer, sources = rag_chat(user_input)

            st.write(answer)

            st.write("Sources Used:")

            for source in set(sources):
                st.write(f"📄 {source}")