# Simple RAG Chatbot

## Overview

This project is a Retrieval-Augmented Generation (RAG) chatbot built using LangChain, FAISS, Hugging Face Embeddings, Groq LLM, and Streamlit. It allows users to ask questions based on content from PDFs, CSV files, text files, and websites.

## Features

* Load data from multiple sources:
    * PDF documents
    * CSV files
    * Text files
    * Web pages
* Automatic document chunking using Recursive Character Text Splitter
* Generate embeddings using Sentence Transformers (`all-MiniLM-L6-v2`)
* Store embeddings in a FAISS vector database
* Retrieve the most relevant chunks using semantic search
* Generate context-aware answers using Groq LLM
* Display source documents used for answering

## Tech Stack

* LangChain
* FAISS
* Hugging Face Embeddings
* Groq LLM
* Streamlit
* PyPDF
* BeautifulSoup

## Workflow

1. Load documents from PDFs, CSVs, text files, and websites.
2. Split documents into smaller chunks.
3. Generate vector embeddings for each chunk.
4. Store embeddings in FAISS.
5. Retrieve relevant chunks based on user queries.
6. Pass retrieved context to the LLM.
7. Generate and display answers with source references.

## Project Structure

data/
 ├── pdf/
 ├── csv/
 └── text_files/

utils/
 ├── chunking.py
 ├── embedding_vectorstore.py
 └── retriever.py

app.py

## Installation

uv add -r requirements.txt

## Run Application

streamlit run app.py

