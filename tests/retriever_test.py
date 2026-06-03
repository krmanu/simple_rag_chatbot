from utlis.retriever import load_retriever

def test_retriever_loads():
    retriever = load_retriever()
    assert retriever is not None

def test_retriever_returns_documents():
    retriever = load_retriever()
    docs = retriever.invoke("What is LangChain?")
    assert len(docs) > 0

def test_retrieved_doc_contains_content():
    retriever = load_retriever()
    docs = retriever.invoke("What is LangChain?")
    assert docs[0].page_content != ""