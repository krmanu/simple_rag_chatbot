import os
from dotenv import load_dotenv
from utlis.chunking import load_and_chunk
from utlis.embedding_vectorstore import create_vectorstore
from utlis.retriever import load_retriever
from langchain_groq import ChatGroq

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

"""
source = "pdf"
source_path = "../data/pdf/genai_principles.pdf"

chunk = load_and_chunk(source, source_path)

create_vectorstore(chunk)
"""
chunks=[]

pdf_folder ="data/pdf/"

for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        source_path = os.path.join(pdf_folder, filename)
        chunk = load_and_chunk("pdf", source_path)
        chunks.extend(chunk)

csv_folder ="data/csv/"

for filename in os.listdir(csv_folder):
    if filename.endswith(".csv"):
        source_path = os.path.join(csv_folder, filename)
        chunk = load_and_chunk("csv", source_path)
        chunks.extend(chunk)

text_folder ="data/text_files/"

for filename in os.listdir(text_folder):
    if filename.endswith(".txt"):
        source_path = os.path.join(text_folder, filename)
        chunk = load_and_chunk("text", source_path)
        chunks.extend(chunk)

websites = ["https://python.langchain.com/","https://docs.groq.com/"]

for url in websites:
    chunk =load_and_chunk("web", url)
    chunks.extend(chunk)

create_vectorstore(chunks)

retriever = load_retriever()

llm = ChatGroq(model_name="openai/gpt-oss-120b")

def rag_chat(query):

    docs = retriever.invoke(query)
    print("\nSources Used:")

    for doc in docs:
        print(doc.metadata['source'])
        
    context ="\n\n".join([doc.page_content for doc in docs])
    prompt = f"Answer the question based on the following context:\n\n{context}\n\nQuestion: {query}"
    response = llm.invoke(prompt)
    return response.content

while True:
    user_input = input("\n Ask a question (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    answer =rag_chat(user_input)
    print(f"Response: {answer}")