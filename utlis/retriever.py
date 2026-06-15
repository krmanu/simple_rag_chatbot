from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def load_retriever():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore=FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    ## retriever=vectorstore.as_retriever()
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3})
    return retriever