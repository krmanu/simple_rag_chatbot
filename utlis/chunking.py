from langchain_community.document_loaders import (PyPDFLoader,CSVLoader,TextLoader,WebBaseLoader)
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_chunk(source, source_path):
    if source == 'pdf':
        loader = PyPDFLoader(source_path)
    elif source == 'csv':
        loader = CSVLoader(source_path)
    elif source == 'text':
        loader = TextLoader(source_path)
    elif source == 'web':
        loader = WebBaseLoader(source_path)
    else:
        raise ValueError("Unsupported source type. Please choose from 'pdf', 'csv', 'text', or 'web'.")

    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)
    
    return chunks