import os
from utlis.chunking import load_and_chunk
from utlis.embedding_vectorstore import create_vectorstore

def ingest_docs():
    chunks=[]
    """
    source = "pdf"
    source_path = "../data/pdf/genai_principles.pdf"

    chunk = load_and_chunk(source, source_path)

    create_vectorstore(chunk)
    """
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
    return len(chunks)