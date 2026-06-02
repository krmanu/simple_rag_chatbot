import os
import streamlit as st
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"

from dotenv import load_dotenv

from utlis.chunking import load_and_chunk
from utlis.embedding_vectorstore import create_vectorstore
from utlis.retriever import load_retriever
from utlis.guardrail import input_guardrail, output_guardrail

from langchain_groq import ChatGroq


load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="Simple RAG App")
st.title("📚 Simple RAG Chatbot")


llm = ChatGroq(model_name="openai/gpt-oss-120b")


@st.cache_resource
def setup_rag():

    chunks = []

    # -------- PDFs --------
    pdf_folder = "data/pdf/"

    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            source_path = os.path.join(pdf_folder, filename)
            chunk = load_and_chunk("pdf", source_path)
            chunks.extend(chunk)

    # -------- CSV --------
    csv_folder = "data/csv/"

    for filename in os.listdir(csv_folder):
        if filename.endswith(".csv"):
            source_path = os.path.join(csv_folder, filename)
            chunk = load_and_chunk("csv", source_path)
            chunks.extend(chunk)

    # -------- Text Files --------
    text_folder = "data/text_files/"

    for filename in os.listdir(text_folder):
        if filename.endswith(".txt"):
            source_path = os.path.join(text_folder, filename)
            chunk = load_and_chunk("text", source_path)
            chunks.extend(chunk)

    # -------- Websites --------
    websites = ["https://python.langchain.com/", "https://docs.groq.com/"]

    for url in websites:
        chunk = load_and_chunk("web", url)
        chunks.extend(chunk)

    create_vectorstore(chunks)

    retriever = load_retriever()

    return retriever

retriever = setup_rag()


def rag_chat(query):

    is_valid, error = input_guardrail(query)
    if not is_valid:
        st.error(error)
        return

    docs = retriever.invoke(query)

    sources = []
    for doc in docs:
        sources.append(doc.metadata["source"])

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    Answer the question based on the context below.

    Context:
    {context}

    Question:
    {query}
    """

    response = llm.invoke(prompt)
    final_response = output_guardrail(
        response.content
    )
    return final_response, sources

user_input = st.text_input("Ask your question")

if st.button("Ask"):

    if user_input:
        with st.spinner("Thinking..."):
            answer, sources = rag_chat(user_input)

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Sources Used")

        for source in set(sources):
            st.write(source)